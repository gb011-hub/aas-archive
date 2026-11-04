# 🧩 UltrafiltrationUnit_AAS_V0.0.1.aasx

[← 장비 페이지](../README.md) · [⤓ AASX 다운로드](../AASX/UltrafiltrationUnit_AAS_V0.0.1.aasx) · 3.6 MB

> 🤖 AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.

<img src="UltrafiltrationUnit_AAS_V0.0.1_thumbnail.png" alt="썸네일" height="180" align="right">

| 항목 | 내용 |
|---|---|
| AAS idShort | `UltrafiltrationUnit` |
| AAS id | <sub>https://www.smart-factory.kr/ids/aas/UltrafiltrationUnit/1/0</sub> |
| 자산 종류 (assetKind) | Type |
| globalAssetId | <sub>https://www.smart-factory.kr/ids/asset/UltrafiltrationUnit/1/0</sub> |
| 설명 | 크로스플로우 한외여과 유닛 참조모델. 모든 운전·제조사·인증 값은 비식별 예시이며 현장 운전 지침이 아닙니다. |
| 서브모델 | 7개 |
| 전체 요소 | 533개 |

## 서브모델 한눈에 보기

| # | 서브모델 | 요소 수 | semanticId |
|:-:|---|--:|---|
| 1 | [Nameplate](#sm-1) | 40 | <sub>https://admin-shell.io/idta/nameplate/3/0/Nameplate</sub> |
| 2 | [HandoverDocumentation](#sm-2) | 38 | <sub>0173-1#01-AHF578#003</sub> |
| 3 | [TechnicalData](#sm-3) | 116 | <sub>0173-1#01-AHX837#002</sub> |
| 4 | [OperationalData](#sm-4) | 57 | <sub>https://www.smart-factory.kr/ids/sm/UltrafiltrationUnit/OperationalData/1/0</sub> |
| 5 | [TimeSeries](#sm-5) | 138 | <sub>https://admin-shell.io/idta/TimeSeries/1/1</sub> |
| 6 | [ProcessParameters](#sm-6) | 52 | <sub>https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0</sub> |
| 7 | [PredictiveMaintenance](#sm-7) | 92 | <sub>https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0</sub> |

## 서브모델 상세

각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.

<a id="sm-1"></a>
<details>
<summary><b>1. Nameplate</b> — 요소 40개</summary>

> Contains the nameplate information attached to the product

semanticId: `https://admin-shell.io/idta/nameplate/3/0/Nameplate`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| URIOfTheProduct | 속성 | https://www.smart-factory.kr/ids/asset/UltrafiltrationUnit/1/0 | <sub>0112/2///61987#ABN590#002</sub> |
| ManufacturerName | 다국어 속성 | ExampleCompany | <sub>0112/2///61987#ABA565#009</sub> |
| ManufacturerProductDesignation | 다국어 속성 | Cross-flow Ultrafiltration Unit | <sub>0112/2///61987#ABA567#009</sub> |
| **AddressInformation** | 묶음 (4) |  | <sub>https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/Address…</sub> |
| &nbsp;&nbsp;&nbsp;└ Street | 다국어 속성 | 예시로 1 | <sub>0173-1#02-AAO128#002</sub> |
| &nbsp;&nbsp;&nbsp;└ Zipcode | 다국어 속성 | 00000 | <sub>0173-1#02-AAO129#002</sub> |
| &nbsp;&nbsp;&nbsp;└ CityTown | 다국어 속성 | 예시시 | <sub>0173-1#02-AAO132#002</sub> |
| &nbsp;&nbsp;&nbsp;└ NationalCode | 다국어 속성 | KR | <sub>0173-1#02-AAO134#002</sub> |
| ManufacturerProductRoot | 다국어 속성 | Membrane separation equipment | <sub>0112/2///61360_7#AAS011#001</sub> |
| ManufacturerProductFamily | 다국어 속성 | UF industrial unit | <sub>0112/2///61987#ABP464#002</sub> |
| ManufacturerProductType | 속성 | UF-3000 | <sub>0112/2///61987#ABA300#008</sub> |
| OrderCodeOfManufacturer | 속성 | UF-3000-ORD | <sub>0112/2///61987#ABA950#008</sub> |
| ProductArticleNumberOfManufacturer | 속성 | UF-3000-ART | <sub>0112/2///61987#ABA581#007</sub> |
| SerialNumber | 속성 | UF-SN-2026-0001 | <sub>0112/2///61987#ABA951#009</sub> |
| YearOfConstruction | 속성 | 2026 | <sub>0112/2///61987#ABP000#002</sub> |
| DateOfManufacture | 속성 | 2026-06-01 | <sub>0112/2///61987#ABB757#007</sub> |
| HardwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA926#008</sub> |
| FirmwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA302#006</sub> |
| SoftwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA601#008</sub> |
| CountryOfOrigin | 속성 | KR | <sub>0112/2///61987#ABP462#001</sub> |
| UniqueFacilityIdentifier | 속성 | EXAMPLE-UF-FACTORY-001 | <sub>https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier</sub> |
| CompanyLogo | 파일 | /aasx/files/logo/CompanyLogo.png | <sub>0112/2///61987#ABP463#001</sub> |
| **Markings** | 목록 (1) |  | <sub>0112/2///61360_7#AAS006#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (6) |  | <sub>0112/2///61360_7#AAS009#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingName | 속성 | EXAMPLE-NOT-CERTIFIED | <sub>0112/2///61987#ABA231#009</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DesignationOfCertificateOrApproval | 속성 | EXAMPLE-UF-CERT-001 | <sub>0112/2///61987#ABH783#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IssueDate | 속성 | 2026-06-01 | <sub>0112/2///61987#ABO097#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExpiryDate | 속성 | 2027-06-01 | <sub>0112/2///61987#ABH830#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingFile | 파일 | /aasx/files/markings/ExampleMarking.png | <sub>0112/2///61987#ABO100#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingAdditionalText | 속성 | 가상 예시이며 실제 인증 또는 승인 사실을 의미하지 않음 | <sub>0112/2///61987#ABB146#007</sub> |
| **AssetSpecificProperties** | 묶음 (4) |  | <sub>0173-1#02-ABI218#003/0173-1#01-AGZ672#004</sub> |
| &nbsp;&nbsp;&nbsp;└ EquipmentFunction | 속성 | Cross-flow ultrafiltration | <sub>https://www.smart-factory.kr/ids/cd/EquipmentFunction/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ ApplicationDescription | 다국어 속성 | Industrial liquid separation | <sub>https://www.smart-factory.kr/ids/cd/ApplicationDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ EquipmentSpecificationFile | 파일 | /aasx/files/docs/UF-SPEC-001.pdf | <sub>https://www.smart-factory.kr/ids/cd/EquipmentSpecificationFile/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **GuidelineSpecificProperties** | 목록 (1) |  | <sub>0173-1#02-ABI219#003/0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuidelineForConformityDeclaration | 속성 | EXAMPLE-UF-SAFETY-GUIDELINE-001 | <sub>0173-1#02-AAO856#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EquipmentFunction | 속성 | Cross-flow ultrafiltration | <sub>https://www.smart-factory.kr/ids/cd/EquipmentFunction/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EquipmentSpecificationFile | 파일 | /aasx/files/docs/UF-SPEC-001.pdf | <sub>https://www.smart-factory.kr/ids/cd/EquipmentSpecificationFile/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ApplicationDescription | 다국어 속성 | Industrial liquid separation | <sub>https://www.smart-factory.kr/ids/cd/ApplicationDescription/1/0</sub> |

</details>

<a id="sm-2"></a>
<details>
<summary><b>2. HandoverDocumentation</b> — 요소 38개</summary>

> The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment

semanticId: `0173-1#01-AHF578#003`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Documents** | 목록 (1) |  | <sub>0173-1#02-ABI500#003</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | example.com/UF | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | UF-OM-001-KO | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 03-02 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Operation | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | 울트라필트레이션 운전 매뉴얼 | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | UF-3000 설치 및 운전 예시 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 공급·여과·역세·세정 절차와 안전 확인 항목 | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 한외여과, UF, 역세, CIP | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/sm/UltrafiltrationUnit/HandoverDocumentation/1… | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://example.com/uf/UF-SPEC-001 | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://example.com/uf/UF-OM-001-EN | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/docs/UF-OM-001-KO.pdf | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 | /aasx/files/docs/UF-OM-001-KO.png | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/sm/UltrafiltrationUnit/HandoverDocumentation/1… | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| **Entities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntitiesForDocumentation</sub> |
| &nbsp;&nbsp;&nbsp;└  | 엔티티 |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation</sub> |

</details>

<a id="sm-3"></a>
<details>
<summary><b>3. TechnicalData</b> — 요소 116개</summary>

> Submodel containing technical data of the asset and associated product classificatons

semanticId: `0173-1#01-AHX837#002`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **GeneralInformation** | 묶음 (6) |  | <sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerName | 속성 | ExampleCompany | <sub>0173-1#02-AAO677#004</sub> |
| &nbsp;&nbsp;&nbsp;└ CompanyLogo | 파일 | /aasx/files/logo/CompanyLogo.png | <sub>0173-1#02-ABI776#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerProductDesignation | 다국어 속성 | ExampleCompany Cross-flow Ultrafiltration Unit | <sub>0173-1#02-AAW338#003</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerArticleNumber | 속성 | UF-3000-ART | <sub>0173-1#02-AAO676#005</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerOrderCode | 속성 | UF-3000-ORD | <sub>0173-1#02-AAO227#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductImages** | 목록 (1) |  | <sub>0173-1#02-ABM220#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageFile | 파일 | /aasx/files/images/ULTRAFILTRATION_ProductImage.jpg | <sub>0173-1#02-ABK291#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageNote | 다국어 속성 | Side view of ExampleCompany ultrafiltration unit | <sub>0173-1#02-ABL423#001</sub> |
| **ProductClassifications** | 목록 (1) |  | <sub>0173-1#02-ABK162#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (7) |  | <sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | ECLASS | <sub>0173-1#02-ABL424#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemVersion | 속성 | 16.0 | <sub>0173-1#02-AAR710#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassId | 속성 | 0173-1#01-ACJ349#020 | <sub>0173-1#02-ABG776#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassCodedName | 속성 | 32-11-02-03 | <sub>0173-1#02-ABK128#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassName | 다국어 속성 | Membrane filter (lab) | <sub>0173-1#02-ABK273#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemUrl | 속성 | https://eclass.eu/ | <sub>https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/Prod…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ReferenceToTechnicalPropertyArea | 참조 | https://www.smart-factory.kr/ids/sm/UltrafiltrationUnit/TechnicalData/1/0 / Tec… | <sub>0173-1#02-ABL358#002</sub> |
| **TechnicalPropertyAreas** | 목록 (6) |  | <sub>0173-1#02-ABK163#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **UltrafiltrationCommonSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/UltrafiltrationCommonSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FiltrationPrincipleSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/FiltrationPrincipleSpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationProcessType | 속성 | Cross-flow ultrafiltration | <sub>https://www.smart-factory.kr/ids/cd/FiltrationProcessType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneModuleType | 속성 | Outside-in hollow fiber membrane module | <sub>https://www.smart-factory.kr/ids/cd/MembraneModuleType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationType | 속성 | Continuous cross-flow with periodic backwash | <sub>https://www.smart-factory.kr/ids/cd/OperationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedSolutionType | 속성 | Macromolecule/colloid-laden industrial process solution | <sub>https://www.smart-factory.kr/ids/cd/FeedSolutionType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **InstallationSpecifications** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/InstallationSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SystemConfiguration | 속성 | Skid-mounted multi-module UF system with feed pump, recirculation pump, backwas… | <sub>https://www.smart-factory.kr/ids/cd/SystemConfiguration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ InstallationType | 속성 | Floor-mounted stainless steel skid frame | <sub>https://www.smart-factory.kr/ids/cd/InstallationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NetWeight | 속성 | 1800 | <sub>https://www.smart-factory.kr/ids/cd/NetWeight/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FiltrationCapacityAndFluxSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/FiltrationCapacityAndFluxSystem/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ThroughputAndFluxSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/ThroughputAndFluxSpecifications/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateCapacity | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PermeateCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxPermeateCapacity | 속성 | 32 | <sub>https://www.smart-factory.kr/ids/cd/MaxPermeateCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedFlowRate | 속성 | 30 | <sub>https://www.smart-factory.kr/ids/cd/FeedFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DesignFlux | 속성 | 50 | <sub>https://www.smart-factory.kr/ids/cd/DesignFlux/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FluxRange | 범위 | 40 ~ 90 | <sub>https://www.smart-factory.kr/ids/cd/FluxRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **SeparationPerformanceSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/SeparationPerformanceSpecificatio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecoveryRate | 속성 | 83.333333 | <sub>https://www.smart-factory.kr/ids/cd/RecoveryRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ VolumeConcentrationFactor | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/VolumeConcentrationFactor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CrossFlowVelocity | 속성 | 3.5 | <sub>https://www.smart-factory.kr/ids/cd/CrossFlowVelocity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RejectionRate | 속성 | 99 | <sub>https://www.smart-factory.kr/ids/cd/RejectionRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MembraneAndPressureSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/MembraneAndPressureSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MembraneElementSpecifications** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/MembraneElementSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneMaterial | 속성 | PVDF (polyvinylidene fluoride) | <sub>https://www.smart-factory.kr/ids/cd/MembraneMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneConfiguration | 속성 | Outside-in hollow fiber | <sub>https://www.smart-factory.kr/ids/cd/MembraneConfiguration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MolecularWeightCutOff | 속성 | 100 | <sub>https://www.smart-factory.kr/ids/cd/MolecularWeightCutOff/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NominalPoreSize | 속성 | 0.02 | <sub>https://www.smart-factory.kr/ids/cd/NominalPoreSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneArea | 속성 | 500 | <sub>https://www.smart-factory.kr/ids/cd/MembraneArea/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModuleCount | 속성 | 12 | <sub>https://www.smart-factory.kr/ids/cd/ModuleCount/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **OperatingEnvelopeSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/OperatingEnvelopeSpecifications/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedTransmembranePressure | 속성 | 1.5 | <sub>https://www.smart-factory.kr/ids/cd/RatedTransmembranePressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TransmembranePressureRange | 범위 | 0.5 ~ 3.0 | <sub>https://www.smart-factory.kr/ids/cd/TransmembranePressureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperatingTemperatureRange | 범위 | 5 ~ 40 | <sub>https://www.smart-factory.kr/ids/cd/OperatingTemperatureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPHRange | 범위 | 2 ~ 11 | <sub>https://www.smart-factory.kr/ids/cd/FeedPHRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxOperatingPressure | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/MaxOperatingPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ModuleAndDimensionSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ModuleAndDimensionSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ModuleConstructionSpecifications** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/ModuleConstructionSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FrameType | 속성 | Stainless steel skid frame | <sub>https://www.smart-factory.kr/ids/cd/FrameType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HousingMaterial | 속성 | SUS316L membrane housing | <sub>https://www.smart-factory.kr/ids/cd/HousingMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModuleArrangement | 속성 | 12 parallel modules on one skid | <sub>https://www.smart-factory.kr/ids/cd/ModuleArrangement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModuleLength | 속성 | 1800 | <sub>https://www.smart-factory.kr/ids/cd/ModuleLength/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModuleDiameter | 속성 | 225 | <sub>https://www.smart-factory.kr/ids/cd/ModuleDiameter/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PipingConnectionSize | 속성 | DN100 | <sub>https://www.smart-factory.kr/ids/cd/PipingConnectionSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WettedPartsMaterial | 속성 | SUS316L / EPDM | <sub>https://www.smart-factory.kr/ids/cd/WettedPartsMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **InstallationEnvelopeSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/InstallationEnvelopeSpecification…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsLength | 속성 | 3500 | <sub>0173-1#02-BAA018#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsWidth | 속성 | 1500 | <sub>0173-1#02-BAA019#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsHeight | 속성 | 2200 | <sub>0173-1#02-BAA020#007</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoundPowerLevel | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/SoundPowerLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CirculationAndBackwashSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/CirculationAndBackwashSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PumpAndCirculationSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/PumpAndCirculationSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpType | 속성 | Multistage centrifugal feed pump | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpRatedPower | 속성 | 15 | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpRatedPower/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpType | 속성 | Centrifugal recirculation pump | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpRatedPower | 속성 | 22 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpRatedPower/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFlowRate | 속성 | 180 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CleaningSystemSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/CleaningSystemSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BackwashMethod | 속성 | Permeate backwash with air scour | <sub>https://www.smart-factory.kr/ids/cd/BackwashMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BackwashInterval | 속성 | PT30M | <sub>https://www.smart-factory.kr/ids/cd/BackwashInterval/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CIPSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/CIPSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CIPChemicalType | 속성 | Alkaline (NaOH) and acidic (citric acid) cleaning | <sub>https://www.smart-factory.kr/ids/cd/CIPChemicalType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AirScourSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/AirScourSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetySystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetySystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalSupplySpecifications** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplySpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedVoltage | 범위 | 380 ~ 415 | <sub>https://www.smart-factory.kr/ids/cd/RatedVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupplyPhase | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplyPhase/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupplyFrequency | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplyFrequency/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedPower | 속성 | 45 | <sub>https://www.smart-factory.kr/ids/cd/RatedPower/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxRunningCurrent | 속성 | 82 | <sub>https://www.smart-factory.kr/ids/cd/MaxRunningCurrent/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LeakageBreakerCapacity | 속성 | 125 | <sub>https://www.smart-factory.kr/ids/cd/LeakageBreakerCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProtectiveFunctionSpecifications** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectiveFunctionSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SupportedSafetyFunctions | 속성 | Emergency stop, high-TMP cutout, low-flow protection, membrane integrity (turbi… | <sub>https://www.smart-factory.kr/ids/cd/SupportedSafetyFunctions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighPressureProtectionSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/HighPressureProtectionSupported/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneIntegrityMonitoringSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/MembraneIntegrityMonitoringSuppor…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DryRunProtectionSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/DryRunProtectionSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IPRating | 속성 | IP54 | <sub>https://www.smart-factory.kr/ids/cd/IPRating/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GroundingRequired | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/GroundingRequired/1/0</sub> |
| **FurtherInformation** | 묶음 (2) |  | <sub>0173-1#02-ABK164#002</sub> |
| &nbsp;&nbsp;&nbsp;└ TextStatement | 다국어 속성 | Representative UF-3000 data at 25 degC | <sub>0173-1#02-ABK134#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ValidDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABL775#001</sub> |
| **SpecificDescriptions** | 목록 (1) |  | <sub>0173-1#02-ABM221#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABM221#001/0173-1#01-AHY912#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ApplicationConditions** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ApplicationConditions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FeedAndCleaningNotes** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/FeedAndCleaningNotes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ApplicationNote | 다국어 속성 | Cross-flow UF of industrial aqueous feed; use compatible cleaning chemicals | <sub>https://www.smart-factory.kr/ids/cd/ApplicationNote/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ReferenceFeedTemperature | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/ReferenceFeedTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecommendedPHRange | 범위 | 2 ~ 11 | <sub>https://www.smart-factory.kr/ids/cd/RecommendedPHRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **SupportingDocumentFiles** | 목록 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/SupportingDocumentFiles/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/docs/UF-SPEC-001.pdf | <sub>https://www.smart-factory.kr/ids/cd/SupportingDocumentFile/1/0</sub> |

</details>

<a id="sm-4"></a>
<details>
<summary><b>4. OperationalData</b> — 요소 57개</summary>

> 한외여과 장비의 현재 운전 상태와 센서 측정값

semanticId: `https://www.smart-factory.kr/ids/sm/UltrafiltrationUnit/OperationalData/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **DeviceOperationSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/DeviceOperationSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **OperatingState** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/OperatingState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Concentration mode | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ActiveProcessId | 속성 | UF-P-001 | <sub>https://www.smart-factory.kr/ids/cd/ActiveProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/FiltrationRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductionMeasurements** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/ProductionMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateFlowActual | 속성 | 24.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedFlowActual | 속성 | 28.5 | <sub>https://www.smart-factory.kr/ids/cd/FeedFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecoveryRateActual | 속성 | 84.912281 | <sub>https://www.smart-factory.kr/ids/cd/RecoveryRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativePermeateVolume | 속성 | 185000 | <sub>https://www.smart-factory.kr/ids/cd/CumulativePermeateVolume/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationStartTimestamp | 속성 | 2026-06-17T08:00:00Z | <sub>https://www.smart-factory.kr/ids/cd/OperationStartTimestamp/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdateTimestamp | 속성 | 2026-06-17T08:15:30Z | <sub>https://www.smart-factory.kr/ids/cd/LastUpdateTimestamp/1/0</sub> |
| **FiltrationProcessSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/FiltrationProcessSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **HydraulicMeasurements** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/HydraulicMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TransmembranePressureActual | 속성 | 1.6 | <sub>https://www.smart-factory.kr/ids/cd/TransmembranePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPressureActual | 속성 | 2.1 | <sub>https://www.smart-factory.kr/ids/cd/FeedPressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RetentatePressureActual | 속성 | 1.9 | <sub>https://www.smart-factory.kr/ids/cd/RetentatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeatePressureActual | 속성 | 0.4 | <sub>https://www.smart-factory.kr/ids/cd/PermeatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FluxActual | 속성 | 48.4 | <sub>https://www.smart-factory.kr/ids/cd/FluxActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CrossFlowVelocityActual | 속성 | 3.4 | <sub>https://www.smart-factory.kr/ids/cd/CrossFlowVelocityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConcentrationFactorActual | 속성 | 6.627907 | <sub>https://www.smart-factory.kr/ids/cd/ConcentrationFactorActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **LiquidQualityMeasurements** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/LiquidQualityMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateTurbidityActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateTurbidityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedTemperatureActual | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/FeedTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPHActual | 속성 | 7.2 | <sub>https://www.smart-factory.kr/ids/cd/FeedPHActual/1/0</sub> |
| **MembraneAndCirculationSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/MembraneAndCirculationSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PumpMeasurements** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/PumpMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpCurrentActual | 속성 | 26 | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpCurrentActual | 속성 | 40 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFlowActual | 속성 | 172 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **MembraneAndCleaningMeasurements** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/MembraneAndCleaningMeasurements/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneDifferentialPressureActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/MembraneDifferentialPressureActua…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneFoulingIndexActual | 속성 | 0.18 | <sub>https://www.smart-factory.kr/ids/cd/MembraneFoulingIndexActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NormalizedPermeabilityActual | 속성 | 92 | <sub>https://www.smart-factory.kr/ids/cd/NormalizedPermeabilityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TimeSinceLastBackwash | 속성 | PT18M | <sub>https://www.smart-factory.kr/ids/cd/TimeSinceLastBackwash/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TimeSinceLastCIP | 속성 | PT72H | <sub>https://www.smart-factory.kr/ids/cd/TimeSinceLastCIP/1/0</sub> |
| **ProtectionAndSafetyStateSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectionAndSafetyStateSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **FiltrationProtectionStates** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/FiltrationProtectionStates/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighTMPAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/HighTMPAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LowFlowAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/LowFlowAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneIntegrityStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/MembraneIntegrityStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateTurbidityAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PermeateTurbidityAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProtectionResponseStates** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectionResponseStates/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FiltrationAlarmStatus/1/0</sub> |
| **ElectricalAndSafetyConditionSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetyConditionSyste…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ElectricalMeasurements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **SafetyInterlockStates** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/SafetyInterlockStates/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SafetyCoverState | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/SafetyCoverState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |

</details>

<a id="sm-5"></a>
<details>
<summary><b>5. TimeSeries</b> — 요소 138개</summary>

> Contains time series data and references to time series data to discover and semantically describe them along the asset lifecycle.

semanticId: `https://admin-shell.io/idta/TimeSeries/1/1`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Metadata** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Ultrafiltration unit operation time series | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Time series data for ultrafiltration unit (cross-flow membrane filtration) oper… | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **Record** | 묶음 (31) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Concentration mode | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/FiltrationRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TransmembranePressureActual | 속성 | 1.6 | <sub>https://www.smart-factory.kr/ids/cd/TransmembranePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPressureActual | 속성 | 2.1 | <sub>https://www.smart-factory.kr/ids/cd/FeedPressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RetentatePressureActual | 속성 | 1.9 | <sub>https://www.smart-factory.kr/ids/cd/RetentatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeatePressureActual | 속성 | 0.4 | <sub>https://www.smart-factory.kr/ids/cd/PermeatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FluxActual | 속성 | 48.4 | <sub>https://www.smart-factory.kr/ids/cd/FluxActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateFlowActual | 속성 | 24.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedFlowActual | 속성 | 28.5 | <sub>https://www.smart-factory.kr/ids/cd/FeedFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecoveryRateActual | 속성 | 84.912281 | <sub>https://www.smart-factory.kr/ids/cd/RecoveryRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CrossFlowVelocityActual | 속성 | 3.4 | <sub>https://www.smart-factory.kr/ids/cd/CrossFlowVelocityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConcentrationFactorActual | 속성 | 6.627907 | <sub>https://www.smart-factory.kr/ids/cd/ConcentrationFactorActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateTurbidityActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateTurbidityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedTemperatureActual | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/FeedTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPHActual | 속성 | 7.2 | <sub>https://www.smart-factory.kr/ids/cd/FeedPHActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpCurrentActual | 속성 | 26 | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpCurrentActual | 속성 | 40 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFlowActual | 속성 | 172 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneDifferentialPressureActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/MembraneDifferentialPressureActua…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NormalizedPermeabilityActual | 속성 | 92 | <sub>https://www.smart-factory.kr/ids/cd/NormalizedPermeabilityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighTMPAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/HighTMPAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneIntegrityStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/MembraneIntegrityStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FiltrationAlarmStatus/1/0</sub> |
| **Segments** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **ExternalSegment** | 묶음 (12) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/ExternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Ultrafiltration unit historian file data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Ultrafiltration unit time series data stored in external CSV file | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 2 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:31Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT1S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-17T08:15:32Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ File | 파일 | /aasx/files/timeseries/UF_TS_20260617.csv | <sub>https://admin-shell.io/idta/TimeSeries/File/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Blob | 바이너리 | application/gzip | <sub>https://admin-shell.io/idta/TimeSeries/Blob/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **LinkedSegment** | 묶음 (12) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/LinkedSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Ultrafiltration unit historian API data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Ultrafiltration unit time series data queried from external historian API | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 2 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:31Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT1S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-17T08:15:32Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Endpoint | 속성 | https://historian.example.com/api/timeseries | <sub>https://admin-shell.io/idta/TimeSeries/Endpoint/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Query | 속성 | assetId=UF-SN-2026-0001&from=2026-06-17T08:15:30Z&to=2026-06-17T08:15:32Z | <sub>https://admin-shell.io/idta/TimeSeries/Query/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **InternalSegment** | 묶음 (11) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/InternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Recent ultrafiltration unit operation data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Recent ultrafiltration unit operation records stored directly in AAS | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 2 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:31Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT1S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-17T08:15:32Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Records** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/TimeSeries/Records/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record** | 묶음 (31) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Concentration mode | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/FiltrationRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TransmembranePressureActual | 속성 | 1.6 | <sub>https://www.smart-factory.kr/ids/cd/TransmembranePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPressureActual | 속성 | 2.1 | <sub>https://www.smart-factory.kr/ids/cd/FeedPressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RetentatePressureActual | 속성 | 1.9 | <sub>https://www.smart-factory.kr/ids/cd/RetentatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeatePressureActual | 속성 | 0.4 | <sub>https://www.smart-factory.kr/ids/cd/PermeatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FluxActual | 속성 | 48.4 | <sub>https://www.smart-factory.kr/ids/cd/FluxActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateFlowActual | 속성 | 24.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedFlowActual | 속성 | 28.5 | <sub>https://www.smart-factory.kr/ids/cd/FeedFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecoveryRateActual | 속성 | 84.912281 | <sub>https://www.smart-factory.kr/ids/cd/RecoveryRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CrossFlowVelocityActual | 속성 | 3.4 | <sub>https://www.smart-factory.kr/ids/cd/CrossFlowVelocityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConcentrationFactorActual | 속성 | 6.627907 | <sub>https://www.smart-factory.kr/ids/cd/ConcentrationFactorActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateTurbidityActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateTurbidityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedTemperatureActual | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/FeedTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPHActual | 속성 | 7.2 | <sub>https://www.smart-factory.kr/ids/cd/FeedPHActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpCurrentActual | 속성 | 26 | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpCurrentActual | 속성 | 40 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFlowActual | 속성 | 172 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneDifferentialPressureActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/MembraneDifferentialPressureActua…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NormalizedPermeabilityActual | 속성 | 92 | <sub>https://www.smart-factory.kr/ids/cd/NormalizedPermeabilityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighTMPAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/HighTMPAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneIntegrityStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/MembraneIntegrityStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FiltrationAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record2** | 묶음 (31) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-17T08:15:31Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Concentration mode | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/FiltrationRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TransmembranePressureActual | 속성 | 1.6 | <sub>https://www.smart-factory.kr/ids/cd/TransmembranePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPressureActual | 속성 | 2.1 | <sub>https://www.smart-factory.kr/ids/cd/FeedPressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RetentatePressureActual | 속성 | 1.9 | <sub>https://www.smart-factory.kr/ids/cd/RetentatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeatePressureActual | 속성 | 0.4 | <sub>https://www.smart-factory.kr/ids/cd/PermeatePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FluxActual | 속성 | 48.4 | <sub>https://www.smart-factory.kr/ids/cd/FluxActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateFlowActual | 속성 | 24.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedFlowActual | 속성 | 28.5 | <sub>https://www.smart-factory.kr/ids/cd/FeedFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecoveryRateActual | 속성 | 84.912281 | <sub>https://www.smart-factory.kr/ids/cd/RecoveryRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CrossFlowVelocityActual | 속성 | 3.4 | <sub>https://www.smart-factory.kr/ids/cd/CrossFlowVelocityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConcentrationFactorActual | 속성 | 6.627907 | <sub>https://www.smart-factory.kr/ids/cd/ConcentrationFactorActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PermeateTurbidityActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/PermeateTurbidityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedTemperatureActual | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/FeedTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPHActual | 속성 | 7.2 | <sub>https://www.smart-factory.kr/ids/cd/FeedPHActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedPumpCurrentActual | 속성 | 26 | <sub>https://www.smart-factory.kr/ids/cd/FeedPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationPumpCurrentActual | 속성 | 40 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationPumpCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFlowActual | 속성 | 172 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneDifferentialPressureActual | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/MembraneDifferentialPressureActua…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NormalizedPermeabilityActual | 속성 | 92 | <sub>https://www.smart-factory.kr/ids/cd/NormalizedPermeabilityActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighTMPAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/HighTMPAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneIntegrityStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/MembraneIntegrityStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FiltrationAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FiltrationAlarmStatus/1/0</sub> |

</details>

<a id="sm-6"></a>
<details>
<summary><b>6. ProcessParameters</b> — 요소 52개</summary>

> The Submodel provides all the necessary parameters in a structured form that are required for the manufacture of any product

semanticId: `https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Processes** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Processes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **Process__00__** | 묶음 (8) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Process/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessId | 속성 | UF-P-001 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessName | 속성 | Cross-flow ultrafiltration / concentration | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessDescription | 다국어 속성 | Process parameters for ultrafiltration concentration and diafiltration operation | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlannedProcessTime | 속성 | PT8H | <sub>https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductParameters** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FeedMaterialConditions** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/FeedMaterialConditions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaterialType | 속성 | Macromolecule/colloid-laden process solution | <sub>https://www.smart-factory.kr/ids/cd/MaterialType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedSolidsConcentration | 속성 | 2 | <sub>https://www.smart-factory.kr/ids/cd/FeedSolidsConcentration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedViscosity | 속성 | 5 | <sub>https://www.smart-factory.kr/ids/cd/FeedViscosity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedTurbidity | 속성 | 120 | <sub>https://www.smart-factory.kr/ids/cd/FeedTurbidity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetMoleculeSize | 속성 | 100 | <sub>https://www.smart-factory.kr/ids/cd/TargetMoleculeSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **SeparationTargets** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/SeparationTargets/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetConcentrationFactor | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/TargetConcentrationFactor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetRecoveryRate | 속성 | 83.333333 | <sub>https://www.smart-factory.kr/ids/cd/TargetRecoveryRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessParameters** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **OperatingRecipe** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/OperatingRecipe/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationRecipeId | 속성 | RECIPE-UF-001 | <sub>https://www.smart-factory.kr/ids/cd/OperationRecipeId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Concentration mode | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessStepSequence | 속성 | Startup-Concentration-Diafiltration-Backwash | <sub>https://www.smart-factory.kr/ids/cd/ProcessStepSequence/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FiltrationSetpoints** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/FiltrationSetpoints/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPermeateFlux | 속성 | 50 | <sub>https://www.smart-factory.kr/ids/cd/TargetPermeateFlux/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TransmembranePressureSetpoint | 속성 | 1.5 | <sub>https://www.smart-factory.kr/ids/cd/TransmembranePressureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxTransmembranePressureLimit | 속성 | 3.0 | <sub>https://www.smart-factory.kr/ids/cd/MaxTransmembranePressureLimit/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CrossFlowVelocitySetpoint | 속성 | 3.5 | <sub>https://www.smart-factory.kr/ids/cd/CrossFlowVelocitySetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFlowSetpoint | 속성 | 180 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFlowSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FeedTemperatureSetpoint | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/FeedTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CleaningAndAlarmSettings** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/CleaningAndAlarmSettings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BackwashInterval | 속성 | PT30M | <sub>https://www.smart-factory.kr/ids/cd/BackwashInterval/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BackwashDuration | 속성 | PT30S | <sub>https://www.smart-factory.kr/ids/cd/BackwashDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CIPTriggerTMPThreshold | 속성 | 2.5 | <sub>https://www.smart-factory.kr/ids/cd/CIPTriggerTMPThreshold/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighTMPAlarmThreshold | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/HighTMPAlarmThreshold/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LowFluxAlarmThreshold | 속성 | 35 | <sub>https://www.smart-factory.kr/ids/cd/LowFluxAlarmThreshold/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ResourceParameters** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RequiredInstrumentation** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/RequiredInstrumentation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredFeedPressureSensor | 속성 | FeedPressureSensor01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredFeedPressureSensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredTMPSensor | 속성 | TMPSensor01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredTMPSensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredPermeateFlowSensor | 속성 | PermeateFlowSensor01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredPermeateFlowSensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredTurbiditySensor | 속성 | TurbiditySensor01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredTurbiditySensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RequiredActuationResources** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/RequiredActuationResources/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredFeedPump | 속성 | FeedPump01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredFeedPump/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredRecirculationPump | 속성 | RecirculationPump01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredRecirculationPump/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredBackwashValve | 속성 | BackwashValve01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredBackwashValve/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredCIPUnit | 속성 | CIPUnit01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredCIPUnit/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessBoM** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MembraneConsumables** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/MembraneConsumables/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MembraneModuleConsumable | 속성 | UF-MODULE-PVDF-001 | <sub>https://www.smart-factory.kr/ids/cd/MembraneModuleConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CleaningConsumables** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/CleaningConsumables/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CIPChemicalAlkaline | 속성 | CIP-NAOH-001 | <sub>https://www.smart-factory.kr/ids/cd/CIPChemicalAlkaline/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CIPChemicalAcid | 속성 | CIP-CITRIC-001 | <sub>https://www.smart-factory.kr/ids/cd/CIPChemicalAcid/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AntiscalantConsumable | 속성 | ANTISCALANT-001 | <sub>https://www.smart-factory.kr/ids/cd/AntiscalantConsumable/1/0</sub> |

</details>

<a id="sm-7"></a>
<details>
<summary><b>7. PredictiveMaintenance</b> — 요소 92개</summary>

> The Submodel Predictive Maintenance is a collection of properties to provide information for predictive maintenance use cases. It is intended to use this submodel in sub-systems of production lines to describe predictive maintenance relevant topics for the sub-system, as well as to use this submode…

semanticId: `https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **RemainingUsefulLifePrediction** | 묶음 (7) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;└ **RemainingUsefulLifetime** | 엔티티 (6) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IndicationType | 속성 | operating hours | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IndicationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DurationValue | 속성 | 11000 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DurationValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EngineeringUnit | 속성 | h | <sub>https://admin-shell.io/idta/PredictiveMaintenance/EngineeringUnit/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartValue | 속성 | 0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartDateTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartDateTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 속성 | UF 막모듈의 가상 잔여수명. 기준시점 이후 11,000시간 연속 운전을 가정한 예시이며 실제 진단 결과가 아님. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Description/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ RemainingUsfulLifeDateTime | 속성 | 2027-09-18T16:15:30Z | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsfulLifeD…</sub> |
| &nbsp;&nbsp;&nbsp;└ ConfidenceInterval | 범위 | 9600 ~ 12400 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConfidenceInterval/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListRULBoundaryConditions** | 목록 (7) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListRULBoundaryCond…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | RecirculationPumpCurrentActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 40 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | A | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.05 ~ 0.09 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 40.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 3.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.4 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 30~55 A. 전류 변화를 운전 부하·펌프 상태 판단에 사용하는 가상 조건. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | PumpBearingVibrationRMS | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 2.6 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | mm/s | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.08 ~ 0.14 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 2.6 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.7 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.9 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 1.0~7.1 mm/s. 베어링 진동을 수명 예측에 사용하는 가상 조건. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | NormalizedPermeabilityActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 92 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | % | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.06 ~ 0.12 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 88.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 5.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | -0.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 60~100%. 초기 대비 투과도 감소를 막의 오염·노화 판단에 사용하는 가상 조건. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | BearingTemperatureActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 56 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | °C | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.04 ~ 0.08 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 56.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 6.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.7 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 30~85 °C. 예측 모델 입력에서는 제외하고 온도 경보에 사용하는 가상 조건. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | MembraneFoulingLoadIndex | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 0.58 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.02 ~ 0.06 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 0.55 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.08 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.3 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 0~1. 막의 누적 오염 부하를 나타내는 예시 지수. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | PumpErosionFactor | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.12 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.01 ~ 0.05 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 1.10 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.04 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.2 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 1~1.5. 펌프 마모와 부하 변동을 반영하는 예시 보정계수. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | FiltrationLoadCorrectionFactor | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.07 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.01 ~ 0.04 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 1.05 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.03 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 유효 범위 1~1.5. 여과 운전 부하 변동을 반영하는 예시 보정계수. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;└ **PredictionModelInformation** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PredictionModelInfo…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelType | 속성 | ModelTypeHybrid | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelDescription | 속성 | 막 투과도와 운전 부하를 사용하는 가상 복합 예측모델 UF-RUL-001. 실제 학습 성능을 뜻하지 않음. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SMAIModelNamePlate | 참조 | https://example.com/models/UF-RUL-001/nameplate | <sub>https://admin-shell.io/idta/PredictiveMaintenance/SMAIModelNamePlate/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListPreAlerts** | 목록 (1) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListPreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertMessage | 속성 | 잔여수명이 1,500 h 미만이면 세정·누설 점검과 다음 정지 시 막 교체를 계획하세요. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertValue | 속성 | 1500 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AlertAfterExceedingRemainingUsableLife** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertAfterExceeding…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AlertMessage | 속성 | 잔여수명이 소진되면 장비를 정지하고 막모듈·순환펌프를 점검한 뒤 정비 절차에 따라 재가동하세요. | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaintenanceRequired | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MaintenanceRequired…</sub> |

</details>
