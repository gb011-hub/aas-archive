# 🧩 PhotolithographyTrackEquipment_AAS_v0.0.1.aasx

[← 장비 페이지](../README.md) · [⤓ AASX 다운로드](../AASX/PhotolithographyTrackEquipment_AAS_v0.0.1.aasx) · 2.4 MB

> 🤖 AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.

<img src="PhotolithographyTrackEquipment_AAS_v0.0.1_thumbnail.jpg" alt="썸네일" height="180" align="right">

| 항목 | 내용 |
|---|---|
| AAS idShort | `PhotolithographyTrackEquipment` |
| AAS id | <sub>https://www.smart-factory.kr/ids/aas/PhotolithographyTrackEquipment/0/1</sub> |
| 자산 종류 (assetKind) | Type |
| globalAssetId | <sub>https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0</sub> |
| 설명 | 300 mm 반도체 포토리소그래피 트랙기 Type 참조모델 |
| 서브모델 | 7개 |
| 전체 요소 | 616개 |

## 서브모델 한눈에 보기

| # | 서브모델 | 요소 수 | semanticId |
|:-:|---|--:|---|
| 1 | [Nameplate](#sm-1) | 38 | <sub>https://admin-shell.io/idta/nameplate/3/0/Nameplate</sub> |
| 2 | [HandoverDocumentation](#sm-2) | 178 | <sub>0173-1#01-AHF578#003</sub> |
| 3 | [TechnicalData](#sm-3) | 108 | <sub>0173-1#01-AHX837#002</sub> |
| 4 | [OperationalData](#sm-4) | 54 | <sub>https://www.smart-factory.kr/ids/sm/PhotolithographyTrackEquipment/OperationalData/1/0</sub> |
| 5 | [TimeSeries](#sm-5) | 100 | <sub>https://admin-shell.io/idta/TimeSeries/1/1</sub> |
| 6 | [ProcessParameters](#sm-6) | 56 | <sub>https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0</sub> |
| 7 | [PredictiveMaintenance](#sm-7) | 82 | <sub>https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0</sub> |

## 서브모델 상세

각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.

<a id="sm-1"></a>
<details>
<summary><b>1. Nameplate</b> — 요소 38개</summary>

> Contains the nameplate information attached to the product

semanticId: `https://admin-shell.io/idta/nameplate/3/0/Nameplate`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| URIOfTheProduct | 속성 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrack/PT-SN-2026-0001 | <sub>0112/2///61987#ABN590#002</sub> |
| ManufacturerName | 다국어 속성 | ExampleCompany | <sub>0112/2///61987#ABA565#009</sub> |
| ManufacturerProductDesignation | 다국어 속성 | 300 mm 포토리소그래피 트랙 시스템 | <sub>0112/2///61987#ABA567#009</sub> |
| **AddressInformation** | 묶음 (4) |  | <sub>https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/Address…</sub> |
| &nbsp;&nbsp;&nbsp;└ Street | 다국어 속성 | 예시로 1 | <sub>0173-1#02-AAO128#002</sub> |
| &nbsp;&nbsp;&nbsp;└ Zipcode | 다국어 속성 | 00000 | <sub>0173-1#02-AAO129#002</sub> |
| &nbsp;&nbsp;&nbsp;└ CityTown | 다국어 속성 | 예시시 | <sub>0173-1#02-AAO132#002</sub> |
| &nbsp;&nbsp;&nbsp;└ NationalCode | 다국어 속성 | KR | <sub>0173-1#02-AAO134#002</sub> |
| ManufacturerProductRoot | 다국어 속성 | 트랙기 | <sub>0112/2///61360_7#AAS011#001</sub> |
| ManufacturerProductFamily | 다국어 속성 | PT-3000 제품군 | <sub>0112/2///61987#ABP464#002</sub> |
| ManufacturerProductType | 속성 | PT-3000 | <sub>0112/2///61987#ABA300#008</sub> |
| OrderCodeOfManufacturer | 속성 | PT3000-193I-CD | <sub>0112/2///61987#ABA950#008</sub> |
| ProductArticleNumberOfManufacturer | 속성 | PT-3000-ART | <sub>0112/2///61987#ABA581#007</sub> |
| SerialNumber | 속성 | PT-SN-2026-0001 | <sub>0112/2///61987#ABA951#009</sub> |
| YearOfConstruction | 속성 | 2026 | <sub>0112/2///61987#ABP000#002</sub> |
| DateOfManufacture | 속성 | 2026-06-17 | <sub>0112/2///61987#ABB757#007</sub> |
| HardwareVersion | 속성 | HW-1.0 | <sub>0112/2///61987#ABA926#008</sub> |
| FirmwareVersion | 속성 | FW-2.3.1 | <sub>0112/2///61987#ABA302#006</sub> |
| SoftwareVersion | 속성 | SW-4.2.0 | <sub>0112/2///61987#ABA601#008</sub> |
| CountryOfOrigin | 속성 | KR | <sub>0112/2///61987#ABP462#001</sub> |
| UniqueFacilityIdentifier | 속성 | PT-SN-2026-0001 | <sub>https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier</sub> |
| CompanyLogo | 파일 | /aasx/files/logo/CompanyLogo.png | <sub>0112/2///61987#ABP463#001</sub> |
| **Markings** | 목록 (1) |  | <sub>0112/2///61360_7#AAS006#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (6) |  | <sub>0112/2///61360_7#AAS009#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingName | 속성 | CE (example) | <sub>0112/2///61987#ABA231#009</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DesignationOfCertificateOrApproval | 속성 | Example declaration PT-CE-001 | <sub>0112/2///61987#ABH783#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IssueDate | 속성 | 2026-06-17 | <sub>0112/2///61987#ABO097#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExpiryDate | 속성 | 2031-06-16 | <sub>0112/2///61987#ABH830#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingFile | 파일 | /aasx/files/documents/PT-CE-001.pdf | <sub>0112/2///61987#ABO100#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingAdditionalText | 속성 | Synthetic example only | <sub>0112/2///61987#ABB146#007</sub> |
| **AssetSpecificProperties** | 묶음 (4) |  | <sub>0173-1#02-ABI218#003/0173-1#01-AGZ672#004</sub> |
| &nbsp;&nbsp;&nbsp;└ TrackType | 속성 | Inline coater/developer track | <sub>https://www.smart-factory.kr/ids/cd/TrackType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ WaferSize | 속성 | 300 | <sub>https://www.smart-factory.kr/ids/cd/WaferSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ NumberOfLoadPorts | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfLoadPorts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **GuidelineSpecificProperties** | 목록 (1) |  | <sub>0173-1#02-ABI219#003/0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuidelineForConformityDeclaration | 속성 | SEMI S2 safety assessment guideline (synthetic example) | <sub>0173-1#02-AAO856#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SafetyAssessmentReportId | 속성 | PT-S2-ASSESSMENT-EXAMPLE-001 | <sub>https://www.smart-factory.kr/ids/cd/SafetyAssessmentReportId/1/0</sub> |

</details>

<a id="sm-2"></a>
<details>
<summary><b>2. HandoverDocumentation</b> — 요소 178개</summary>

> The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment

semanticId: `0173-1#01-AHF578#003`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Documents** | 목록 (5) |  | <sub>0173-1#02-ABI500#003</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | VDI2770 | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | PT-OM-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 03-02 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Operation manual | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Operation manual | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 트랙기 예시 문서 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Photo track operation, recipe selection, wafer recovery and alarm response. | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 트랙기, 포토리소그래피, 코팅, 현상 | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany Semiconductor Equipment | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/PT-OM-001.pdf | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 | /aasx/files/documents/PT-OM-001.pdf | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | VDI2770 | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | PT-CM-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | false | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 03-01 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Installation and commissioning guide | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Installation and commissioning guide | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 트랙기 예시 문서 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Cleanroom installation, utilities, exhaust, chemical supply and acceptance chec… | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 트랙기, 포토리소그래피, 코팅, 현상 | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany Semiconductor Equipment | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/PT-CM-001.pdf | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 | /aasx/files/documents/PT-CM-001.pdf | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | VDI2770 | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | PT-SF-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | false | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 03-03 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Chemical and safety instructions | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Chemical and safety instructions | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 트랙기 예시 문서 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Photoresist, solvent, TMAH, hot plate, robot and interlock safety. | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 트랙기, 포토리소그래피, 코팅, 현상 | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany Semiconductor Equipment | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/PT-SF-001.pdf | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 | /aasx/files/documents/PT-SF-001.pdf | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | VDI2770 | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | PT-MT-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | false | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 03-04 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Maintenance and inspection guide | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Maintenance and inspection guide | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 트랙기 예시 문서 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Nozzle, dispense pump, spin chuck, hot plate and transfer robot maintenance. | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 트랙기, 포토리소그래피, 코팅, 현상 | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany Semiconductor Equipment | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/PT-MT-001.pdf | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 | /aasx/files/documents/PT-MT-001.pdf | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | VDI2770 | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | PT-CE-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | false | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 02-04 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Example declaration of conformity | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Example declaration of conformity | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 트랙기 예시 문서 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Illustrative conformity record only; not a real approval. | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 트랙기, 포토리소그래피, 코팅, 현상 | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-06-17 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany Semiconductor Equipment | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/PT-CE-001.pdf | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 | /aasx/files/documents/PT-CE-001.pdf | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/asset/PhotolithographyTrackEquipment/1/0 | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| **Entities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntitiesForDocumentation</sub> |
| &nbsp;&nbsp;&nbsp;└  | 엔티티 |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation</sub> |

</details>

<a id="sm-3"></a>
<details>
<summary><b>3. TechnicalData</b> — 요소 108개</summary>

> Submodel containing technical data of the asset and associated product classificatons

semanticId: `0173-1#01-AHX837#002`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **GeneralInformation** | 묶음 (6) |  | <sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerName | 속성 | ExampleCompany | <sub>0173-1#02-AAO677#004</sub> |
| &nbsp;&nbsp;&nbsp;└ CompanyLogo | 파일 | /aasx/files/logo/CompanyLogo.png | <sub>0173-1#02-ABI776#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerProductDesignation | 다국어 속성 | 300 mm 포토리소그래피 트랙 시스템 | <sub>0173-1#02-AAW338#003</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerArticleNumber | 속성 | PT-3000-ART | <sub>0173-1#02-AAO676#005</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerOrderCode | 속성 | PT3000-193I-CD | <sub>0173-1#02-AAO227#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductImages** | 목록 (1) |  | <sub>0173-1#02-ABM220#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageFile | 파일 | /aasx/files/images/PhotolithographyTrackEquipment.png | <sub>0173-1#02-ABK291#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageNote | 다국어 속성 | 트랙기 예시 제품 이미지 | <sub>0173-1#02-ABL423#001</sub> |
| **ProductClassifications** | 목록 (1) |  | <sub>0173-1#02-ABK162#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (7) |  | <sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | ECLASS | <sub>0173-1#02-ABL424#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemVersion | 속성 | 16.0 | <sub>0173-1#02-AAR710#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemUrl | 속성 | https://eclass.eu/en/eclass-standard/search-content/show?tx_eclasssearch_ecsear… | <sub>https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/Prod…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassId | 속성 | 0173-1#01-AKL119#021 | <sub>0173-1#02-ABG776#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassCodedName | 속성 | 33-15-13-90 | <sub>0173-1#02-ABK128#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassName | 다국어 속성 | 코팅 설비(전체, 상세 유형 미지정) | <sub>0173-1#02-ABK273#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ReferenceToTechnicalPropertyArea | 참조 | https://www.smart-factory.kr/ids/sm/PhotolithographyTrackEquipment/TechnicalDat… | <sub>0173-1#02-ABL358#002</sub> |
| **TechnicalPropertyAreas** | 목록 (6) |  | <sub>0173-1#02-ABK163#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PhotoTrackCommonSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/PhotoTrackCommonSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PhotoTrackCommonSpecifications** | 묶음 (10) |  | <sub>https://www.smart-factory.kr/ids/cd/PhotoTrackCommonSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TrackType | 속성 | Inline coater/developer track (litho cell) | <sub>https://www.smart-factory.kr/ids/cd/TrackType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModuleArrangement | 속성 | Stacked coat/bake/develop modules with central transfer robot | <sub>https://www.smart-factory.kr/ids/cd/ModuleArrangement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ScannerInterfaceType | 속성 | Inline interface to immersion/DUV exposure scanner | <sub>https://www.smart-factory.kr/ids/cd/ScannerInterfaceType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferSize | 속성 | 300 | <sub>https://www.smart-factory.kr/ids/cd/WaferSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferTransferRobotType | 속성 | Dual-arm wafer transfer robot | <sub>https://www.smart-factory.kr/ids/cd/WaferTransferRobotType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LoadPortType | 속성 | FOUP load port (SEMI E15.1) | <sub>https://www.smart-factory.kr/ids/cd/LoadPortType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfLoadPorts | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfLoadPorts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SystemConfiguration | 속성 | Multi-module coat/bake/develop track with FOUP load ports | <sub>https://www.smart-factory.kr/ids/cd/SystemConfiguration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ InstallationType | 속성 | Cleanroom floor-mounted modular track | <sub>https://www.smart-factory.kr/ids/cd/InstallationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NetWeight | 속성 | 8500 | <sub>0173-1#02-AAS707#005</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CoatingAndDispenseSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/CoatingAndDispenseSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CoatingAndDispenseSpecifications** | 묶음 (11) |  | <sub>https://www.smart-factory.kr/ids/cd/CoatingAndDispenseSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatingMethod | 속성 | Spin coating | <sub>https://www.smart-factory.kr/ids/cd/CoatingMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfCoatingModules | 속성 | 2 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfCoatingModules/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxSpinSpeed | 속성 | 6000 | <sub>https://www.smart-factory.kr/ids/cd/MaxSpinSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinSpeedRange | 범위 | 300 ~ 6000 | <sub>https://www.smart-factory.kr/ids/cd/SpinSpeedRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinChuckType | 속성 | Vacuum wafer spin chuck | <sub>https://www.smart-factory.kr/ids/cd/SpinChuckType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistDispenseType | 속성 | Programmable syringe-pump dispense | <sub>https://www.smart-factory.kr/ids/cd/ResistDispenseType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistDispenseVolumeRange | 범위 | 0.3 ~ 3.0 | <sub>https://www.smart-factory.kr/ids/cd/ResistDispenseVolumeRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfDispenseNozzles | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfDispenseNozzles/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EdgeBeadRemovalSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/EdgeBeadRemovalSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AdhesionPrimingType | 속성 | HMDS vapor prime | <sub>https://www.smart-factory.kr/ids/cd/AdhesionPrimingType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ThroughputCapacity | 속성 | 250 | <sub>https://www.smart-factory.kr/ids/cd/ThroughputCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BakeAndChillThermalSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/BakeAndChillThermalSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BakeAndChillThermalSpecifications** | 묶음 (11) |  | <sub>https://www.smart-factory.kr/ids/cd/BakeAndChillThermalSpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateType | 속성 | Proximity hot plate | <sub>https://www.smart-factory.kr/ids/cd/BakePlateType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfBakePlates | 속성 | 8 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfBakePlates/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakeTemperatureRange | 범위 | 70 ~ 250 | <sub>https://www.smart-factory.kr/ids/cd/BakeTemperatureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakeTemperatureUniformity | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/BakeTemperatureUniformity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoftBakeSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/SoftBakeSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PostExposureBakeSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/PostExposureBakeSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChillPlateType | 속성 | Water-cooled chill plate | <sub>https://www.smart-factory.kr/ids/cd/ChillPlateType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfChillPlates | 속성 | 8 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfChillPlates/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChillPlateTemperature | 속성 | 23 | <sub>https://www.smart-factory.kr/ids/cd/ChillPlateTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperatureControlAccuracy | 속성 | 0.1 | <sub>https://www.smart-factory.kr/ids/cd/TemperatureControlAccuracy/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakeAtmosphere | 속성 | Nitrogen purge / clean dry air | <sub>https://www.smart-factory.kr/ids/cd/BakeAtmosphere/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DevelopAndDimensionSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/DevelopAndDimensionSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DevelopAndDimensionSpecifications** | 묶음 (11) |  | <sub>https://www.smart-factory.kr/ids/cd/DevelopAndDimensionSpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopMethod | 속성 | Spin/puddle development | <sub>https://www.smart-factory.kr/ids/cd/DevelopMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperType | 속성 | TMAH 2.38% (metal-ion-free) | <sub>https://www.smart-factory.kr/ids/cd/DeveloperType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfDevelopModules | 속성 | 2 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfDevelopModules/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperDispenseType | 속성 | Slit-scan developer nozzle | <sub>https://www.smart-factory.kr/ids/cd/DeveloperDispenseType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RinseMethod | 속성 | DI water rinse and spin dry | <sub>https://www.smart-factory.kr/ids/cd/RinseMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfDevelopCups | 속성 | 2 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfDevelopCups/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleanroomClassRequirement | 속성 | ISO Class 4 mini-environment | <sub>https://www.smart-factory.kr/ids/cd/CleanroomClassRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsLength | 속성 | 4200 | <sub>0173-1#02-BAA018#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsWidth | 속성 | 2600 | <sub>0173-1#02-BAA019#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsHeight | 속성 | 2300 | <sub>0173-1#02-BAA020#007</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoundPowerLevel | 속성 | 72 | <sub>0173-1#02-AAZ122#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DrainageAndExhaustSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/DrainageAndExhaustSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DrainageAndExhaustSpecifications** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/DrainageAndExhaustSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SolventExhaustType | 속성 | Dedicated solvent fume exhaust with damper control | <sub>https://www.smart-factory.kr/ids/cd/SolventExhaustType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SolventExhaustConnectionSize | 속성 | 150 | <sub>https://www.smart-factory.kr/ids/cd/SolventExhaustConnectionSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AlkalineExhaustSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/AlkalineExhaustSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChemicalDrainType | 속성 | Segregated solvent / developer / DI drain | <sub>https://www.smart-factory.kr/ids/cd/ChemicalDrainType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DrainConnectionSize | 속성 | 50 | <sub>https://www.smart-factory.kr/ids/cd/DrainConnectionSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExhaustAirflowRate | 속성 | 1200 | <sub>https://www.smart-factory.kr/ids/cd/ExhaustAirflowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DrainNeutralizationSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/DrainNeutralizationSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetySystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetySystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetySpecifications** | 묶음 (13) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetySpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedVoltage | 범위 | 200 ~ 240 | <sub>https://www.smart-factory.kr/ids/cd/RatedVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupplyPhase | 속성 | 3-phase | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplyPhase/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupplyFrequency | 속성 | 50/60 | <sub>0173-1#02-ABG814#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedPower | 속성 | 45000 | <sub>0173-1#02-AAC970#010</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxRunningCurrent | 속성 | 130000 | <sub>0173-1#02-ABE741#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LeakageBreakerCapacity | 속성 | 150 | <sub>https://www.smart-factory.kr/ids/cd/LeakageBreakerCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SupportedSafetyFunctions | 속성 | Emergency stop, door interlock, solvent leak detection, exhaust flow interlock | <sub>https://www.smart-factory.kr/ids/cd/SupportedSafetyFunctions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SolventLeakDetectionSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/SolventLeakDetectionSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExhaustFlowInterlockSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/ExhaustFlowInterlockSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DoorInterlockSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/DoorInterlockSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FireSuppressionInterfaceSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/FireSuppressionInterfaceSupported…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IPRating | 속성 | IP40 | <sub>https://www.smart-factory.kr/ids/cd/IPRating/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GroundingRequired | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/GroundingRequired/1/0</sub> |
| **FurtherInformation** | 묶음 (2) |  | <sub>0173-1#02-ABK164#002</sub> |
| &nbsp;&nbsp;&nbsp;└ TextStatement | 다국어 속성 | AAS 자산 경계는 300 mm 코터/디벨로퍼 트랙 본체와 통합 반송 모듈이다. | <sub>0173-1#02-ABK134#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ValidDate | 속성 | 2026-09-20 | <sub>0173-1#02-ABL775#001</sub> |
| **SpecificDescriptions** | 목록 (1) |  | <sub>0173-1#02-ABM221#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABM221#001/0173-1#01-AHY912#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PhotoTrackBoundaryDescription** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/PhotoTrackBoundaryDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AssetBoundaryDescription | 속성 | Coat, bake, chill, develop, FOUP load-port and transfer modules included; expos… | <sub>https://www.smart-factory.kr/ids/cd/AssetBoundaryDescription/1/0</sub> |

</details>

<a id="sm-4"></a>
<details>
<summary><b>4. OperationalData</b> — 요소 54개</summary>

> 포토리소그래피 트랙기의 현재 운전값과 상태값

semanticId: `https://www.smart-factory.kr/ids/sm/PhotolithographyTrackEquipment/OperationalData/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **DeviceOperationSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/DeviceOperationSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **DeviceOperationMonitoring** | 묶음 (10) |  | <sub>https://www.smart-factory.kr/ids/cd/DeviceOperationMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Coat-develop track processing | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ActiveProcessId | 속성 | PT-P-001 | <sub>https://www.smart-factory.kr/ids/cd/ActiveProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ActiveRecipeId | 속성 | RECIPE-PT-193i-01 | <sub>https://www.smart-factory.kr/ids/cd/ActiveRecipeId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentLotId | 속성 | LOT-2026-0617-03 | <sub>https://www.smart-factory.kr/ids/cd/CurrentLotId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentWaferId | 속성 | W-25-03 | <sub>https://www.smart-factory.kr/ids/cd/CurrentWaferId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferThroughputActual | 속성 | 242 | <sub>https://www.smart-factory.kr/ids/cd/WaferThroughputActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativeWaferCount | 속성 | 185300 | <sub>https://www.smart-factory.kr/ids/cd/CumulativeWaferCount/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationStartTimestamp | 속성 | 2026-06-17T08:00:00Z | <sub>https://www.smart-factory.kr/ids/cd/OperationStartTimestamp/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdateTimestamp | 속성 | 2026-06-17T08:20:30Z | <sub>https://www.smart-factory.kr/ids/cd/LastUpdateTimestamp/1/0</sub> |
| **CoatAndBakeProcessSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/CoatAndBakeProcessSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **CoatAndBakeProcessMonitoring** | 묶음 (12) |  | <sub>https://www.smart-factory.kr/ids/cd/CoatAndBakeProcessMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatModuleRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/CoatModuleRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinSpeedActual | 속성 | 2500 | <sub>https://www.smart-factory.kr/ids/cd/SpinSpeedActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistDispenseVolumeActual | 속성 | 1.2 | <sub>https://www.smart-factory.kr/ids/cd/ResistDispenseVolumeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/ResistTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatFilmThicknessActual | 속성 | 120 | <sub>https://www.smart-factory.kr/ids/cd/CoatFilmThicknessActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateTemperatureActual | 속성 | 110 | <sub>https://www.smart-factory.kr/ids/cd/BakePlateTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateTempDeviation | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/BakePlateTempDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChillPlateTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/ChillPlateTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HMDSPrimeStatus | 속성 | Completed | <sub>https://www.smart-factory.kr/ids/cd/HMDSPrimeStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferThroughputRate | 속성 | 242 | <sub>https://www.smart-factory.kr/ids/cd/WaferThroughputRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatingUniformityIndex | 속성 | 0.97 | <sub>https://www.smart-factory.kr/ids/cd/CoatingUniformityIndex/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ReworkWaferRate | 속성 | 0.6 | <sub>https://www.smart-factory.kr/ids/cd/ReworkWaferRate/1/0</sub> |
| **DevelopAndDispenseSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/DevelopAndDispenseSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **DevelopAndDispenseMonitoring** | 묶음 (9) |  | <sub>https://www.smart-factory.kr/ids/cd/DevelopAndDispenseMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopModuleRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DevelopModuleRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperDispenseVolumeActual | 속성 | 45 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperDispenseVolumeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopTimeActual | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/DevelopTimeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RinseFlowActual | 속성 | 1.5 | <sub>https://www.smart-factory.kr/ids/cd/RinseFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DIWaterTemperatureActual | 속성 | 22.5 | <sub>https://www.smart-factory.kr/ids/cd/DIWaterTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChemicalLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ChemicalLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NozzleClogStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/NozzleClogStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DispenseVolumeDriftIndex | 속성 | 0.35 | <sub>https://www.smart-factory.kr/ids/cd/DispenseVolumeDriftIndex/1/0</sub> |
| **ProtectionAndSafetyStateSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectionAndSafetyStateSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProtectionAndSafetyStateMonitoring** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectionAndSafetyStateMonitorin…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SolventLeakDetectionStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/SolventLeakDetectionStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExhaustFlowStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ExhaustFlowStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExhaustFlowInterlockStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ExhaustFlowInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DoorInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/DoorInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PhotoTrackAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/PhotoTrackAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferTransferErrorStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/WaferTransferErrorStatus/1/0</sub> |
| **ElectricalAndSafetyConditionSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetyConditionSyste…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetyConditionMonitoring** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetyConditionMonit…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SafetyCoverState | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/SafetyCoverState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |

</details>

<a id="sm-5"></a>
<details>
<summary><b>5. TimeSeries</b> — 요소 100개</summary>

> Contains time series data and references to time series data to discover and semantically describe them along the asset lifecycle.

semanticId: `https://admin-shell.io/idta/TimeSeries/1/1`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Metadata** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | 포토트랙 운전 시계열 | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 트랙기 코팅·베이크·현상 운전값 시계열 | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **Record** | 묶음 (28) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ UtcTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Coat-develop track processing | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatModuleRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/CoatModuleRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinSpeedActual | 속성 | 2500 | <sub>https://www.smart-factory.kr/ids/cd/SpinSpeedActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistDispenseVolumeActual | 속성 | 1.2 | <sub>https://www.smart-factory.kr/ids/cd/ResistDispenseVolumeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/ResistTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatFilmThicknessActual | 속성 | 120 | <sub>https://www.smart-factory.kr/ids/cd/CoatFilmThicknessActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateTemperatureActual | 속성 | 110 | <sub>https://www.smart-factory.kr/ids/cd/BakePlateTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateTempDeviation | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/BakePlateTempDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChillPlateTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/ChillPlateTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopModuleRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DevelopModuleRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperDispenseVolumeActual | 속성 | 45 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperDispenseVolumeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopTimeActual | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/DevelopTimeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RinseFlowActual | 속성 | 1.5 | <sub>https://www.smart-factory.kr/ids/cd/RinseFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DIWaterTemperatureActual | 속성 | 22.5 | <sub>https://www.smart-factory.kr/ids/cd/DIWaterTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferThroughputActual | 속성 | 242 | <sub>https://www.smart-factory.kr/ids/cd/WaferThroughputActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SolventLeakDetectionStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/SolventLeakDetectionStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExhaustFlowStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ExhaustFlowStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PhotoTrackAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/PhotoTrackAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 0 | <sub>https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1</sub> |
| **Segments** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **ExternalSegment** | 묶음 (12) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/ExternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Photo track historian file data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 합성 예시 기록 1건. 수집 주기는 1초이며 시작·종료 시각은 이 기록의 관측시각이다. 외부 연결은 실제 서비스가 아닌 예시이다. | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT0S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-18T00:00:05Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ File | 파일 | /aasx/files/timeseries/PT_TS_20260617.csv | <sub>https://admin-shell.io/idta/TimeSeries/File/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Blob | 바이너리 | application/gzip | <sub>https://admin-shell.io/idta/TimeSeries/Blob/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **LinkedSegment** | 묶음 (12) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/LinkedSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Photo track historian API data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 합성 예시 기록 1건. 수집 주기는 1초이며 시작·종료 시각은 이 기록의 관측시각이다. 외부 연결은 실제 서비스가 아닌 예시이다. | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT0S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-18T00:00:05Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Endpoint | 속성 | https://historian.example.com/api/timeseries | <sub>https://admin-shell.io/idta/TimeSeries/Endpoint/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Query | 속성 | assetId=PT-SN-2026-0001&from=2026-06-17T00:00:00Z&to=2026-06-18T00:00:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Query/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **InternalSegment** | 묶음 (11) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/InternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Recent photo track operation data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 합성 예시 기록 1건. 수집 주기는 1초이며 시작·종료 시각은 이 기록의 관측시각이다. 외부 연결은 실제 서비스가 아닌 예시이다. | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT0S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-18T00:00:05Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Records** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/TimeSeries/Records/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record0001** | 묶음 (28) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ UtcTime | 속성 | 2026-06-17T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Coat-develop track processing | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatModuleRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/CoatModuleRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinSpeedActual | 속성 | 2500 | <sub>https://www.smart-factory.kr/ids/cd/SpinSpeedActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistDispenseVolumeActual | 속성 | 1.2 | <sub>https://www.smart-factory.kr/ids/cd/ResistDispenseVolumeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/ResistTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CoatFilmThicknessActual | 속성 | 120 | <sub>https://www.smart-factory.kr/ids/cd/CoatFilmThicknessActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateTemperatureActual | 속성 | 110 | <sub>https://www.smart-factory.kr/ids/cd/BakePlateTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BakePlateTempDeviation | 속성 | 0.2 | <sub>https://www.smart-factory.kr/ids/cd/BakePlateTempDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChillPlateTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/ChillPlateTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopModuleRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DevelopModuleRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperDispenseVolumeActual | 속성 | 45 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperDispenseVolumeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperTemperatureActual | 속성 | 23.0 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopTimeActual | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/DevelopTimeActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RinseFlowActual | 속성 | 1.5 | <sub>https://www.smart-factory.kr/ids/cd/RinseFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DIWaterTemperatureActual | 속성 | 22.5 | <sub>https://www.smart-factory.kr/ids/cd/DIWaterTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WaferThroughputActual | 속성 | 242 | <sub>https://www.smart-factory.kr/ids/cd/WaferThroughputActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 38 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SolventLeakDetectionStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/SolventLeakDetectionStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExhaustFlowStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ExhaustFlowStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PhotoTrackAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/PhotoTrackAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 0 | <sub>https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1</sub> |

</details>

<a id="sm-6"></a>
<details>
<summary><b>6. ProcessParameters</b> — 요소 56개</summary>

> The Submodel provides all the necessary parameters in a structured form that are required for the manufacture of any product

semanticId: `https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Processes** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Processes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **Process__00__** | 묶음 (8) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Process/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessId | 속성 | PT-P-001 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessName | 속성 | Photolithography coat-develop | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessDescription | 다국어 속성 | 300 mm 웨이퍼 포토레지스트 코팅·베이크·현상 공정 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlannedProcessTime | 속성 | PT6M | <sub>https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TrackProductSpecification** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/TrackProductSpecification/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MaterialAndQualityTargets** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/MaterialAndQualityTargets/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PhotoresistType | 속성 | ArF 193 nm positive resist | <sub>https://www.smart-factory.kr/ids/cd/PhotoresistType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetFilmThickness | 속성 | 120 | <sub>https://www.smart-factory.kr/ids/cd/TargetFilmThickness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetCriticalDimension | 속성 | 38 | <sub>https://www.smart-factory.kr/ids/cd/TargetCriticalDimension/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductionTargets** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ProductionTargets/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LotSize | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/LotSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetThroughput | 속성 | 250 | <sub>https://www.smart-factory.kr/ids/cd/TargetThroughput/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TrackRecipeConfiguration** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/TrackRecipeConfiguration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecipeIdentification** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/RecipeIdentification/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationRecipeId | 속성 | RECIPE-PT-193i-01 | <sub>https://www.smart-factory.kr/ids/cd/OperationRecipeId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Coat-develop track processing | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessStepSequence | 속성 | HMDS-Coat-SoftBake-Chill-(Expose)-PEB-Chill-Develop-Rinse-Dry | <sub>https://www.smart-factory.kr/ids/cd/ProcessStepSequence/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CoatingSettings** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/CoatingSettings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinSpeedSetpoint | 속성 | 2500 | <sub>https://www.smart-factory.kr/ids/cd/SpinSpeedSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SpinTimeSetpoint | 속성 | 30 | <sub>https://www.smart-factory.kr/ids/cd/SpinTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ResistDispenseVolumeSetpoint | 속성 | 1.2 | <sub>https://www.smart-factory.kr/ids/cd/ResistDispenseVolumeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EdgeBeadRemovalWidthSetpoint | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/EdgeBeadRemovalWidthSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BakeAndChillSettings** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/BakeAndChillSettings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoftBakeTemperatureSetpoint | 속성 | 110 | <sub>https://www.smart-factory.kr/ids/cd/SoftBakeTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoftBakeTimeSetpoint | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/SoftBakeTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PostExposureBakeTemperatureSetpoint | 속성 | 105 | <sub>https://www.smart-factory.kr/ids/cd/PostExposureBakeTemperatureSetpoi…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PostExposureBakeTimeSetpoint | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/PostExposureBakeTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChillPlateTemperatureSetpoint | 속성 | 23 | <sub>https://www.smart-factory.kr/ids/cd/ChillPlateTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DevelopmentSettings** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/DevelopmentSettings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperDispenseVolumeSetpoint | 속성 | 45 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperDispenseVolumeSetpoint/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DevelopTimeSetpoint | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/DevelopTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ResourceParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TrackResourceRequirements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/TrackResourceRequirements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **EquipmentResources** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/EquipmentResources/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredSpinCoater | 속성 | SpinCoater01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredSpinCoater/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredBakePlate | 속성 | HotPlate01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredBakePlate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredChillPlate | 속성 | ChillPlate01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredChillPlate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredDeveloperModule | 속성 | DevelopModule01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredDeveloperModule/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredResistDispensePump | 속성 | ResistPump01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredResistDispensePump/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredWaferTransferRobot | 속성 | WaferRobot01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredWaferTransferRobot/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredFilmThicknessSensor | 속성 | ThicknessSensor01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredFilmThicknessSensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessConsumables** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/ProcessConsumables/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PhotoresistConsumable | 속성 | RESIST-ARF193i-001 | <sub>https://www.smart-factory.kr/ids/cd/PhotoresistConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeveloperConsumable | 속성 | TMAH-238-001 | <sub>https://www.smart-factory.kr/ids/cd/DeveloperConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EdgeBeadRemoverSolvent | 속성 | EBR-THINNER-001 | <sub>https://www.smart-factory.kr/ids/cd/EdgeBeadRemoverSolvent/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HMDSConsumable | 속성 | HMDS-001 | <sub>https://www.smart-factory.kr/ids/cd/HMDSConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DIWaterConsumable | 속성 | DIWATER-001 | <sub>https://www.smart-factory.kr/ids/cd/DIWaterConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessBoM** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TrackWorkpieces** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/TrackWorkpieces/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WaferProducts** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/WaferProducts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ InputWaferProduct | 속성 | W-25-03 | <sub>https://www.smart-factory.kr/ids/cd/InputWaferProduct/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessedWaferProduct | 속성 | W-25-03-TRACK | <sub>https://www.smart-factory.kr/ids/cd/ProcessedWaferProduct/1/0</sub> |

</details>

<a id="sm-7"></a>
<details>
<summary><b>7. PredictiveMaintenance</b> — 요소 82개</summary>

> The Submodel Predictive Maintenance is a collection of properties to provide information for predictive maintenance use cases. It is intended to use this submodel in sub-systems of production lines to describe predictive maintenance relevant topics for the sub-system, as well as to use this submode…

semanticId: `https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **RemainingUsefulLifePrediction** | 묶음 (7) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;└ **RemainingUsefulLifetime** | 엔티티 (6) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IndicationType | 속성 | operating hours | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IndicationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DurationValue | 속성 | 9000 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DurationValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EngineeringUnit | 속성 | h | <sub>https://admin-shell.io/idta/PredictiveMaintenance/EngineeringUnit/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartValue | 속성 | 9000 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartDateTime | 속성 | 2026-06-26T09:00:00+09:00 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartDateTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 속성 | Spin-chuck drive motor bearing RUL estimated from motor current, vibration and … | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Description/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ RemainingUsfulLifeDateTime | 속성 | 2027-07-06T09:00:00+09:00 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsfulLifeD…</sub> |
| &nbsp;&nbsp;&nbsp;└ ConfidenceInterval | 범위 | 7800 ~ 10200 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConfidenceInterval/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListRULBoundaryConditions** | 목록 (6) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListRULBoundaryCond…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | SpinMotorCurrentActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 9.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | A | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0 ~ 0.15 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 5.2 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.8 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.4 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Synthetic applicability interval: 3.0 to 9.0. BoundaryValueRange stores the upp… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | SpinMotorBearingVibrationRMS | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 6.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | mm/s | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0 ~ 0.15 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 2.3 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.6 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.85 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Synthetic applicability interval: 0.8 to 6.5. BoundaryValueRange stores the upp… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | DispensePumpPressureActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 350 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | kPa | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0 ~ 0.15 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 240 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 25 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | -0.4 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Synthetic applicability interval: 150 to 350. BoundaryValueRange stores the upp… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | BearingTemperatureActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 70 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | °C | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0 ~ 0.15 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 42 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 5.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.7 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Synthetic applicability interval: 20 to 70. BoundaryValueRange stores the upper… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | SpinMotorImbalanceFactor | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0 ~ 0.15 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 1.12 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.08 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.2 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Synthetic applicability interval: 1.0 to 1.5. BoundaryValueRange stores the upp… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | CoatingLoadCorrectionFactor | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0 ~ 0.15 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 1.05 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.05 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Synthetic applicability interval: 1.0 to 1.5. BoundaryValueRange stores the upp… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;└ **PredictionModelInformation** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PredictionModelInfo…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelType | 속성 | ModelTypeHybrid | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelDescription | 속성 | Synthetic hybrid RUL example for the spin-chuck drive bearing. No trained model… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SMAIModelNamePlate | 참조 |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/SMAIModelNamePlate/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListPreAlerts** | 목록 (1) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListPreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertMessage | 속성 | Pre-alert: photo track spin-chuck drive RUL is below 1200 h; schedule bearing i… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertValue | 속성 | 1200 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AlertAfterExceedingRemainingUsableLife** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertAfterExceeding…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AlertMessage | 속성 | Stop the photo track and replace the affected spin-chuck bearing or dispense pu… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaintenanceRequired | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MaintenanceRequired…</sub> |

</details>
