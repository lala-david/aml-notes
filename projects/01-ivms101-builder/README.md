# Project 01 — IVMS101 메시지 빌더 + 검증

> Travel Rule 메시지 표준을 손으로 만들면서 체화. (D28 미니 프로젝트)

## 🏗 아키텍처

```mermaid
flowchart LR
    I["📥 Input<br/>송수신 정보 + VASP"] --> B["🔨 build_ivms101_message()"]
    B --> J["📝 IVMS101 JSON"]
    J --> V["🔍 validate_ivms101()"]
    V --> OK["✅ 성공"]
    V --> ERR["⚠️ 에러 리스트<br/>• 필드 누락<br/>• 타입 오류<br/>• 포맷 오류"]
    OK --> S["💾 sample_messages/<br/>5 JSON files"]
    style B fill:#1a2e4a,color:#fff,stroke:#1a2e4a
    style OK fill:#d1fae5,stroke:#10b981
    style ERR fill:#fee2e2,stroke:#dc2626
```

## 왜 이걸 만드나

Travel Rule 이론을 여러 문서로 읽어도 **실제 IVMS101 메시지가 어떻게 생겼는지** 한 번도 만져보지 않으면 이해가 겉핥기로 남습니다. 이 프로젝트는 **한국 100만원 시나리오**를 중심으로 Originator·Beneficiary·VASP 정보를 JSON으로 직접 생성하고 검증합니다. 필수 필드·타입·길이 제약을 손으로 처리해보면 **D22·D23에서 배운 내용**이 정확히 어디에 쓰이는지 몸에 새겨집니다.

## 학습 목표

1. IVMS101 JSON 스키마 구조 이해
2. 필수 vs 선택 필드 구분
3. 한국 100만원 시나리오 메시지 생성
4. 기본 검증 (필드 누락, 타입 오류) 함수

## 사양

### 입력
- 송신인 정보 (이름, 주소, 지갑주소, DOB)
- 수신인 정보 (이름, 지갑주소)
- VASP 정보 (송수신측 LEI 또는 ID)
- 금액, 자산 종류

### 출력
- IVMS101 호환 JSON
- 검증 결과 (성공/실패 + 에러 리스트)

## 인터페이스

```python
def build_ivms101_message(
    originator: dict,
    beneficiary: dict,
    originating_vasp: dict,
    beneficiary_vasp: dict,
    amount: float,
    asset: str,
) -> dict:
    """IVMS101 호환 JSON 빌드"""

def validate_ivms101(msg: dict) -> tuple[bool, list[str]]:
    """필수 필드 + 타입 검증"""
```

## 테스트 케이스

1. **정상 한국 100만원** — 필드 모두 채움
2. **송신인 이름 누락** — 검증 실패
3. **잘못된 wallet 형식** — 0x...가 아닌 ETH 주소
4. **비표준 통화 코드** — "BTCC" 같은 오타
5. **EU TFR 호환** — 200만원, 임계 없는 EU 시나리오

## 산출물

```
01_ivms101_builder/
├── README.md (이 파일)
├── main.py
├── test.py
├── requirements.txt
├── sample_messages/
│   ├── 01_korea_normal.json
│   ├── 02_originator_missing.json
│   ├── 03_invalid_wallet.json
│   ├── 04_invalid_currency.json
│   └── 05_eu_tfr.json
└── .env.example  # 사용 안 함, 빈 파일
```

## IVMS101 핵심 스키마 (빌더가 반드시 다뤄야 할 경로)

```
originator
 └─ originatorPersons[]
     └─ naturalPerson  (또는 legalPerson — 택일 discriminator)
         ├─ name
         │   └─ nameIdentifier[]
         │       ├─ primaryIdentifier      (성)
         │       ├─ secondaryIdentifier    (이름)
         │       └─ nameIdentifierType     (LEGL / BIRT / ALIA ...)
         ├─ geographicAddress[]
         │   ├─ addressType                (HOME / BIZZ ...)
         │   ├─ country                    (ISO 3166-1 alpha-2)
         │   └─ addressLine[]              (또는 streetName + buildingNumber)
         ├─ nationalIdentification
         │   ├─ nationalIdentifier
         │   ├─ nationalIdentifierType     (ARNU / DRLC / PASS ...)
         │   └─ countryOfIssue
         ├─ dateAndPlaceOfBirth
         │   ├─ dateOfBirth                (YYYY-MM-DD)
         │   ├─ placeOfBirth
         │   └─ countryOfBirth
         └─ countryOfResidence
 └─ accountNumber[]                         (보통 지갑주소)

beneficiary: originator와 동일 구조 (최소 필드는 완화 가능)

originatingVASP  / beneficiaryVASP
 └─ legalPerson
     ├─ name.nameIdentifier (LEGL)
     ├─ nationalIdentification  (LEI 권장, countryOfIssue 필수)
     └─ geographicAddress
```

### 검증 수준 (validate_ivms101이 잡아야 할 것)
1. **Discriminator**: `naturalPerson` XOR `legalPerson` (둘 다 있거나 없으면 오류)
2. **필수 필드**: `primaryIdentifier`, `country`(ISO-2), `accountNumber`, VASP `name` 존재
3. **포맷**: `dateOfBirth` ISO 8601, `country` ISO 3166-1 alpha-2, LEI 20자 영숫자
4. **문자열 길이**: IVMS101은 대부분 길이 제한 있음 (이름 100자, 주소 필드 35자 등)

JSON Schema로 검증하려면 `jsonschema` 라이브러리 + [공식 IVMS101 스키마 JSON 파일](https://intervasp.org) 또는 Notabene 샘플 스키마를 내려받아 사용.

## 학습 자료

- [`../../notes/4-technology/travel-rule-protocols.md`](../../notes/4-technology/travel-rule-protocols.md) — IVMS101 deep
- [`../../notes/3-crypto-aml/travel-rule.md`](../../notes/3-crypto-aml/travel-rule.md) — Travel Rule 운영
- [Notabene IVMS101 분석](https://notabene.id/travel-rule-messaging-protocols/ivms-101)
- [VerifyVASP IVMS101 docs](https://www.verifyvasp.com/)

## 한계 / 주의

- **이 코드는 학습용**. 실제 Travel Rule 운영에는 인증서 + 전송 프로토콜 + 카운터파티 식별 등이 더 필요
- IVMS101 정식 스키마는 InterVASP에서 라이센스 (이 프로젝트는 단순화 버전)
- 프로덕션 환경에서는 Notabene/VerifyVASP/CODE 같은 검증된 솔루션 사용

## 보너스 챌린지

- IVMS101 → ISO 20022 메시지 변환 (전통 금융 호환)
- 카운터파티 VASP Discovery (Mock)
- PII 암호화 (송신 전)
