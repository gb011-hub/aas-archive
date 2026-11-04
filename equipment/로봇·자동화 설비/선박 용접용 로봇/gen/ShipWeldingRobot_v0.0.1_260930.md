# 🧩 ShipWeldingRobot_v0.0.1_260930.aasx

[← 장비 페이지](../README.md) · [⤓ AASX 다운로드](../AASX/ShipWeldingRobot_v0.0.1_260930.aasx) · 485 KB

> 🤖 AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.

<img src="ShipWeldingRobot_v0.0.1_260930_thumbnail.jpg" alt="썸네일" height="180" align="right">

| 항목 | 내용 |
|---|---|
| AAS idShort | `ShipWeldingRobot` |
| AAS id | <sub>https://www.smart-factory.kr/ids/aas/ShipWeldingRobot/1/0</sub> |
| 자산 종류 (assetKind) | Type |
| globalAssetId | <sub>https://www.smart-factory.kr/ids/asset/ShipWeldingRobot/1/0</sub> |
| 설명 | 선박 용접용 로봇(Ship Welding Robot) 참조 모델 - 자산관리쉘(AAS) Type 수준 표준 모델. |
| 서브모델 | 8개 |
| 전체 요소 | 260개 |

## 서브모델 한눈에 보기

| # | 서브모델 | 요소 수 | semanticId |
|:-:|---|--:|---|
| 1 | [DigitalNameplate](#sm-1) | 30 | <sub>https://admin-shell.io/idta/nameplate/3/0/Nameplate</sub> |
| 2 | [HandoverDocumentation](#sm-2) | 38 | <sub>0173-1#01-AHF578#003</sub> |
| 3 | [TechnicalData](#sm-3) | 55 | <sub>0173-1#01-AHX837#002</sub> |
| 4 | [OperationalData](#sm-4) | 25 | <sub>https://www.smart-factory.kr/ids/sm/ShipWeldingRobot/OperationalData/1/0</sub> |
| 5 | [FunctionalSafety](#sm-5) | 31 | <sub>https://admin-shell.io/idta/iec62683/1/0/FunctionalSafety</sub> |
| 6 | [ProcessParameters](#sm-6) | 25 | <sub>https://admin-shell.io/idta/SubmodelTemplate/ProcessParameters/1/0</sub> |
| 7 | [TimeSeries](#sm-7) | 24 | <sub>https://admin-shell.io/idta/TimeSeries/1/1</sub> |
| 8 | [PredictiveMaintenance](#sm-8) | 32 | <sub>https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0</sub> |

## 서브모델 상세

각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.

<a id="sm-1"></a>
<details>
<summary><b>1. DigitalNameplate</b> — 요소 30개</summary>

> 디지털 명판 서브모델 - 제조사-모델-식별번호-제조일-인증 등 제품의 신분 정보를 표준 구조로 담는다(IDTA 공식 템플릿).

semanticId: `https://admin-shell.io/idta/nameplate/3/0/Nameplate`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| URIOfTheProduct | 속성 | https://www.domain-abc.com/Model-Nr-1234/Serial-Nr-5678 | <sub>0112/2///61987#ABN590#002</sub> |
| ManufacturerName | 다국어 속성 | "Muster AG" | <sub>0112/2///61987#ABA565#009</sub> |
| ManufacturerProductDesignation | 다국어 속성 | "ABC-123" | <sub>0112/2///61987#ABA567#009</sub> |
| AddressInformation | 묶음 |  | <sub>https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/Address…</sub> |
| ManufacturerProductRoot | 다국어 속성 | "flow meter" | <sub>0112/2///61360_7#AAS011#001</sub> |
| ManufacturerProductFamily | 다국어 속성 | "Type ABC" | <sub>0112/2///61987#ABP464#002</sub> |
| ManufacturerProductType | 속성 | FM-ABC-1234 | <sub>0112/2///61987#ABA300#008</sub> |
| OrderCodeOfManufacturer | 속성 | FMABC1234 | <sub>0112/2///61987#ABA950#008</sub> |
| ProductArticleNumberOfManufacturer | 속성 | FM11-ABC22-123456 | <sub>0112/2///61987#ABA581#007</sub> |
| SerialNumber | 속성 | 12345678 | <sub>0112/2///61987#ABA951#009</sub> |
| YearOfConstruction | 속성 | 2022 | <sub>0112/2///61987#ABP000#002</sub> |
| DateOfManufacture | 속성 | 2022-01-01 | <sub>0112/2///61987#ABB757#007</sub> |
| HardwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA926#008</sub> |
| FirmwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA302#006</sub> |
| SoftwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA601#008</sub> |
| CountryOfOrigin | 속성 | DE | <sub>0112/2///61987#ABP462#001</sub> |
| UniqueFacilityIdentifier | 속성 | 987654321 | <sub>https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier</sub> |
| CompanyLogo | 파일 |  | <sub>0112/2///61987#ABP463#001</sub> |
| **Markings** | 목록 (1) |  | <sub>0112/2///61360_7#AAS006#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (6) |  | <sub>0112/2///61360_7#AAS009#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingName | 속성 | 0173-1#07-DAA603#004 | <sub>0112/2///61987#ABA231#009</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DesignationOfCertificateOrApproval | 속성 | KEMA99IECEX1105/128 | <sub>0112/2///61987#ABH783#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IssueDate | 속성 | 2022-01-01 | <sub>0112/2///61987#ABO097#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExpiryDate | 속성 | 2022-01-01 | <sub>0112/2///61987#ABH830#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingFile | 파일 |  | <sub>0112/2///61987#ABO100#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingAdditionalText | 속성 | 0044 | <sub>0112/2///61987#ABB146#007</sub> |
| **AssetSpecificProperties** | 묶음 (1) |  | <sub>0173-1#02-ABI218#003/0173-1#01-AGZ672#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **GuidelineSpecificProperties** | 목록 (1) |  | <sub>0173-1#02-ABI219#003/0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuidelineForConformityDeclaration | 속성 | EXAMPLE-GuidelineForConformityDeclaration | <sub>0173-1#02-AAO856#002</sub> |

</details>

<a id="sm-2"></a>
<details>
<summary><b>2. HandoverDocumentation</b> — 요소 38개</summary>

> 인계 문서 서브모델 - 사용 매뉴얼-도면-인증서 등 인계 문서를 VDI 2770 기반 표준 구조로 관리한다(IDTA 공식 템플릿).

semanticId: `0173-1#01-AHF578#003`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Documents** | 목록 (1) |  | <sub>0173-1#02-ABI500#003</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | IODA-HYU | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | MAN-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | false | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 03-02 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | 운영 | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI2770 Blatt1:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | en | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1.0 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | 선박 용접 로봇 운영 매뉴얼 | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 설치 및 운전 안내 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 운영·정비 매뉴얼 | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | 매뉴얼, 운영, 정비 | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-01-01 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Released | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | IODA | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | IODA Lab, Hanyang University | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 |  | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| **Entities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntitiesForDocumentation</sub> |
| &nbsp;&nbsp;&nbsp;└  | 엔티티 |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation</sub> |

</details>

<a id="sm-3"></a>
<details>
<summary><b>3. TechnicalData</b> — 요소 55개</summary>

> 기술 데이터 서브모델 - 기구-성능-제어-전기 등 정적(변하지 않는) 기술 사양을 도메인 영역별 계층으로 담는다.

semanticId: `0173-1#01-AHX837#002`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **GeneralInformation** | 묶음 (6) |  | <sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerName | 속성 | ExampleCompany Co., Ltd. | <sub>0173-1#02-AAO677#004</sub> |
| &nbsp;&nbsp;&nbsp;└ CompanyLogo | 파일 |  | <sub>0173-1#02-ABI776#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerProductDesignation | 다국어 속성 | Articulated Arc Welding Robot | <sub>0173-1#02-AAW338#003</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerArticleNumber | 속성 | ART-WR-2000 | <sub>0173-1#02-AAO676#005</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerOrderCode | 속성 | WR-2000-STD | <sub>0173-1#02-AAO227#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductImages** | 묶음 (2) |  | <sub>0173-1#02-ABM220#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageFile | 파일 | /aasx/files/shipweldingrobot/productimage.png | <sub>0173-1#02-ABK291#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageNote | 다국어 속성 | View of ship welding robot manipulator | <sub>0173-1#02-ABL423#001</sub> |
| **ProductClassifications** | 목록 (1) |  | <sub>0173-1#02-ABK162#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (6) |  | <sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | ECLASS | <sub>0173-1#02-ABL424#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemVersion | 속성 | 16.0 | <sub>0173-1#02-AAR710#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemUrl | 속성 | https://eclass.eu | <sub>https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/Prod…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassId | 속성 | 0173-1#01-AAZ344#021 | <sub>0173-1#02-ABG776#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassCodedName | 속성 | 27-38-01-01 | <sub>0173-1#02-ABK128#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassName | 다국어 속성 | Articulated robot | <sub>0173-1#02-ABK273#002</sub> |
| **TechnicalPropertyAreas** | 목록 (1) |  | <sub>0173-1#02-ABK163#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (4) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RobotCharacteristics** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RobotCharacteristics/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MechanicalStructure** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/MechanicalStructure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RobotType | 속성 | 6-axis articulated arc welding robot | <sub>https://www.smart-factory.kr/ids/cd/RobotType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriveType | 속성 | AC servo motor drive | <sub>https://www.smart-factory.kr/ids/cd/DriveType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ControlSystemType | 속성 | Robot controller (teach/playback) | <sub>https://www.smart-factory.kr/ids/cd/ControlSystemType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SystemConfiguration | 속성 | Manipulator + welding torch + wire feeder + power source + controller | <sub>https://www.smart-factory.kr/ids/cd/SystemConfiguration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ InstallationType | 속성 | Indoor floor/rail-mounted | <sub>https://www.smart-factory.kr/ids/cd/InstallationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MachineWeight | 속성 | 224.0 | <sub>https://www.smart-factory.kr/ids/cd/MachineWeight/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfAxes | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/NumberOfAxes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MotionPerformance** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/MotionPerformance/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxPayload | 속성 | 6.0 | <sub>https://www.smart-factory.kr/ids/cd/MaxPayload/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Reach | 속성 | 1994.0 | <sub>https://www.smart-factory.kr/ids/cd/Reach/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PositioningRepeatability | 속성 | 0.08 | <sub>https://www.smart-factory.kr/ids/cd/PositioningRepeatability/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxTravelSpeed | 속성 | 150.0 | <sub>https://www.smart-factory.kr/ids/cd/MaxTravelSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WeldingCharacteristics** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/WeldingCharacteristics/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WeldingProcessCapability** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/WeldingProcessCapability/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingTarget | 속성 | Ship hull block (steel) | <sub>https://www.smart-factory.kr/ids/cd/WeldingTarget/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingMethod | 속성 | GMAW (CO2/MAG) | <sub>https://www.smart-factory.kr/ids/cd/WeldingMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingCurrentRange | 범위 | 30.0 ~ 350.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingCurrentRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingVoltageRange | 범위 | 12.0 ~ 36.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingVoltageRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WireDiameterRange | 범위 | 0.9 ~ 1.6 | <sub>https://www.smart-factory.kr/ids/cd/WireDiameterRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WireFeedSpeedRange | 범위 | 1.0 ~ 20.0 | <sub>https://www.smart-factory.kr/ids/cd/WireFeedSpeedRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ControlAndInterface** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/ControlAndInterface/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ControlSystem** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ControlSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ControllerModel | 속성 | WR-RC-2000 | <sub>https://www.smart-factory.kr/ids/cd/ControllerModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TeachingMethod | 속성 | Teach pendant / offline | <sub>https://www.smart-factory.kr/ids/cd/TeachingMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CommunicationInterface | 속성 | EtherCAT / DeviceNet | <sub>https://www.smart-factory.kr/ids/cd/CommunicationInterface/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PositionFeedback | 속성 | Absolute encoder | <sub>https://www.smart-factory.kr/ids/cd/PositionFeedback/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndEnvironment** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndEnvironment/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalRatings** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalRatings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedVoltage | 속성 | 380.0 | <sub>0173-1#02-ABM190#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ControllerRatedPower | 속성 | 20.0 | <sub>https://www.smart-factory.kr/ids/cd/ControllerRatedPower/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionClassIP | 속성 | IP54 | <sub>https://www.smart-factory.kr/ids/cd/ProtectionClassIP/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **EnvironmentalConditions** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/EnvironmentalConditions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperatingTemperatureRange | 범위 | 0.0 ~ 45.0 | <sub>https://www.smart-factory.kr/ids/cd/OperatingTemperatureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MachineDimensions | 속성 | 600.0 | <sub>https://www.smart-factory.kr/ids/cd/MachineDimensions/1/0</sub> |

</details>

<a id="sm-4"></a>
<details>
<summary><b>4. OperationalData</b> — 요소 25개</summary>

> 운영 데이터 서브모델 - 운전 상태-측정값-알람-누적 카운터 등 동적(운전 중 변하는) 데이터를 담는다.

semanticId: `https://www.smart-factory.kr/ids/sm/ShipWeldingRobot/OperationalData/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **OperationStatus** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/OperationStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **CurrentState** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/CurrentState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingOperationState | 속성 | Run | <sub>https://www.smart-factory.kr/ids/cd/WeldingOperationState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingOperationMode | 속성 | Auto (teach/playback) | <sub>https://www.smart-factory.kr/ids/cd/WeldingOperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ArcStatus | 속성 | ArcOff | <sub>https://www.smart-factory.kr/ids/cd/ArcStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentWPSId | 속성 | WR-WPS-012 | <sub>https://www.smart-factory.kr/ids/cd/CurrentWPSId/1/0</sub> |
| **MeasuredValues** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/MeasuredValues/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **WeldingMeasurements** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/WeldingMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeasuredWeldingCurrent | 속성 | 258.0 | <sub>https://www.smart-factory.kr/ids/cd/MeasuredWeldingCurrent/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeasuredWeldingVoltage | 속성 | 27.6 | <sub>https://www.smart-factory.kr/ids/cd/MeasuredWeldingVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeasuredWireFeedSpeed | 속성 | 9.4 m/min | <sub>https://www.smart-factory.kr/ids/cd/MeasuredWireFeedSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeasuredTravelSpeed | 속성 | 41.0 | <sub>https://www.smart-factory.kr/ids/cd/MeasuredTravelSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeasuredShieldingGasFlow | 속성 | 20 L/min | <sub>https://www.smart-factory.kr/ids/cd/MeasuredShieldingGasFlow/1/0</sub> |
| **AlarmInformation** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/AlarmInformation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **CurrentAlarm** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/CurrentAlarm/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingAlarmCode | 속성 | E-ARC-START-FAIL | <sub>0173-1#02-ABI766#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingAlarmText | 다국어 속성 | 아크 스타트 실패 알람@ko | <sub>https://www.smart-factory.kr/ids/cd/WeldingAlarmText/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingAlarmSeverity | 속성 | Critical | <sub>https://www.smart-factory.kr/ids/cd/WeldingAlarmSeverity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastAlarmTimestamp | 속성 | 2026-01-22T10:14:22+00:00 | <sub>https://www.smart-factory.kr/ids/cd/LastAlarmTimestamp/1/0</sub> |
| **CumulativeCounters** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/CumulativeCounters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **OperationCounters** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/OperationCounters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativeOperatingHours | 속성 | 9800.0 | <sub>https://www.smart-factory.kr/ids/cd/CumulativeOperatingHours/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativeArcOnHours | 속성 | 4200.0 | <sub>https://www.smart-factory.kr/ids/cd/CumulativeArcOnHours/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativeWeldLength | 속성 | 152000 m | <sub>https://www.smart-factory.kr/ids/cd/CumulativeWeldLength/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaintenanceCycleCount | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/MaintenanceCycleCount/1/0</sub> |

</details>

<a id="sm-5"></a>
<details>
<summary><b>5. FunctionalSafety</b> — 요소 31개</summary>

> 기능 안전 서브모델 - 안전 기능의 SIL-PL-Category 등 기능 안전 특성을 표준 구조로 담는다(IDTA 공식 템플릿).

semanticId: `https://admin-shell.io/idta/iec62683/1/0/FunctionalSafety`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| NumberOfFunctionalSafetySetsOfCharacteristics | 속성 | 1 | <sub>0112/2///62683#ACE005#001</sub> |
| **OperatingConditionsOfFunctionalSafetyCharacteristics** | 묶음 (9) |  | <sub>0112/2///62683#ACG057#001</sub> |
| &nbsp;&nbsp;&nbsp;└ TypeOfVoltage | 속성 | DC | <sub>0112/2///61987#ABA969#007</sub> |
| &nbsp;&nbsp;&nbsp;└ RatedVoltage | 속성 | 1.0 | <sub>0112/2///61987#ABA588#004</sub> |
| &nbsp;&nbsp;&nbsp;└ MinimumRatedVoltage | 속성 | 1.0 | <sub>0112/2///61987#ABD461#004</sub> |
| &nbsp;&nbsp;&nbsp;└ MaximumRatedVoltage | 속성 | 1.0 | <sub>0112/2///61987#ABD462#004</sub> |
| &nbsp;&nbsp;&nbsp;└ RatedOperationalCurrent | 속성 | 1.0 | <sub>https://admin-shell.io/idta/FunctionalSafety/RatedOperationalCurrent/…</sub> |
| &nbsp;&nbsp;&nbsp;└ TypeOfInterlockingDevice | 속성 | Safety door interlock switch | <sub>0112/2///62683#ACE053#001</sub> |
| &nbsp;&nbsp;&nbsp;└ OtherOperatingConditions | 속성 | Ambient 0-40 C, protection IP54 | <sub>0112/2///62683#ACE070#001</sub> |
| &nbsp;&nbsp;&nbsp;└ UsefulLifeInNumberOfOperations | 속성 | 1.0 | <sub>0112/2///62683#ACE055#001</sub> |
| &nbsp;&nbsp;&nbsp;└ UsefulLifeInTimeInterval | 속성 | 1.0 | <sub>0112/2///62683#ACE054#001</sub> |
| **SafetyDeviceTypes** | 묶음 (5) |  | <sub>0112/2///62683#ACG070#001</sub> |
| &nbsp;&nbsp;&nbsp;└ FunctionalSafetyDeviceType | 속성 | Safety controller | <sub>0112/2///62683#ACE071#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **SafetySubsystem** | 묶음 (5) |  | <sub>0112/2///62683#ACG065#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SIL | 속성 | SIL2 | <sub>0112/2///62683#ACE051#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PFH | 속성 | 1.0 | <sub>0112/2///62683#ACE052#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProofTestInterval | 속성 | 1.0 | <sub>0112/2///62683#ACE058#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PL | 속성 | d | <sub>0112/2///62683#ACE060#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Category | 속성 | 3 | <sub>0112/2///62683#ACE063#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **ElectronicElement** | 묶음 (3) |  | <sub>0112/2///62683#ACG066#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MTTFD | 속성 | 1 | <sub>0112/2///62683#ACE057#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RDF | 속성 | 1 | <sub>https://admin-shell.io/idta/FunctionalSafety/RDF/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProofTestInterval | 속성 | 1.0 | <sub>0112/2///62683#ACE058#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **ElectromechanicalElement** | 묶음 (2) |  | <sub>0112/2///62683#ACG067#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ B10D | 속성 | 1.0 | <sub>0112/2///62683#ACE056#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProofTestInterval | 속성 | 1.0 | <sub>0112/2///62683#ACE058#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **InherentlySafeSubsystem** | 묶음 (4) |  | <sub>0112/2///62683#ACG069#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SIL | 속성 | SIL2 | <sub>0112/2///62683#ACE051#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProofTestInterval | 속성 | 1.0 | <sub>0112/2///62683#ACE058#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PL | 속성 | d | <sub>0112/2///62683#ACE060#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Category | 속성 | 3 | <sub>0112/2///62683#ACE063#001</sub> |

</details>

<a id="sm-6"></a>
<details>
<summary><b>6. ProcessParameters</b> — 요소 25개</summary>

> 공정 파라미터 서브모델 - 작업 절차(예: 용접 WPS)의 설정 파라미터를 공정(Process) 단위로 담는다(IDTA 공식 템플릿).

semanticId: `https://admin-shell.io/idta/SubmodelTemplate/ProcessParameters/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Processes** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Processes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **Process** | 묶음 (8) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Process/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessId | 속성 | WR-WELD-001 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessName | 속성 | Arc Welding | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessDescription | 다국어 속성 | GMAW arc welding of ship hull block | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlannedProcessTime | 속성 | PT25S | <sub>https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductParameters** | 묶음 (5) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BaseMetalMaterial | 속성 | AH36 (조선용 강재) | <sub>https://www.smart-factory.kr/ids/cd/BaseMetalMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BaseMetalThickness | 속성 | 12.0 | <sub>https://www.smart-factory.kr/ids/cd/BaseMetalThickness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ JointType | 속성 | Fillet weld | <sub>https://www.smart-factory.kr/ids/cd/JointType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GrooveAngle | 속성 | 45° | <sub>https://www.smart-factory.kr/ids/cd/GrooveAngle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingPosition | 속성 | PB (수평 필릿) | <sub>https://www.smart-factory.kr/ids/cd/WeldingPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessParameters** | 묶음 (4) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingCurrentSetpoint | 속성 | 260.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingCurrentSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingVoltageSetpoint | 속성 | 28.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingVoltageSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TravelSpeedSetpoint | 속성 | 40.0 | <sub>https://www.smart-factory.kr/ids/cd/TravelSpeedSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WireFeedSpeedSetpoint | 속성 | 9 m/min | <sub>https://www.smart-factory.kr/ids/cd/WireFeedSpeedSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ResourceParameters** | 묶음 (4) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TorchWorkAngle | 속성 | 45° | <sub>https://www.smart-factory.kr/ids/cd/TorchWorkAngle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ContactTipToWorkDistance | 속성 | 15.0 | <sub>https://www.smart-factory.kr/ids/cd/ContactTipToWorkDistance/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ShieldingGasType | 속성 | 80% Ar + 20% CO2 | <sub>https://www.smart-factory.kr/ids/cd/ShieldingGasType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ShieldingGasFlowRate | 속성 | 20 L/min | <sub>https://www.smart-factory.kr/ids/cd/ShieldingGasFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessBoM** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingWire | 속성 | 70.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingWire/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ShieldingGas | 속성 | Ar/CO2 혼합가스 | <sub>https://www.smart-factory.kr/ids/cd/ShieldingGas/1/0</sub> |

</details>

<a id="sm-7"></a>
<details>
<summary><b>7. TimeSeries</b> — 요소 24개</summary>

> 시계열 데이터 서브모델 - 운전 중 측정되는 값들을 시간 축으로 기록하는 구조(메타데이터-세그먼트-레코드)를 담는다(IDTA 공식 템플릿).

semanticId: `https://admin-shell.io/idta/TimeSeries/1/1`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Metadata** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | 용접 사이클 #1@ko | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 시계열 측정 변수 설명 | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **Record** | 묶음 (5) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 0 | <sub>https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingCurrent | 속성 | 258.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingCurrent/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingVoltage | 속성 | 27.6 | <sub>https://www.smart-factory.kr/ids/cd/WeldingVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WireFeedSpeed | 속성 | 9.4 | <sub>https://www.smart-factory.kr/ids/cd/WireFeedSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TravelSpeed | 속성 | 41.0 | <sub>https://www.smart-factory.kr/ids/cd/TravelSpeed/1/0</sub> |
| **Segments** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **InternalSegment** | 묶음 (7) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/InternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | 용접 사이클 #1@ko | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 1000 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-01-01T00:00:00+09:00 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-01-01T00:01:40+09:00 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 10 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Records** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/TimeSeries/Records/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record** | 묶음 (5) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 0 | <sub>https://admin-shell.io/idta/TimeSeries/RelativePointInTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingCurrent | 속성 | 258.0 | <sub>https://www.smart-factory.kr/ids/cd/WeldingCurrent/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WeldingVoltage | 속성 | 27.6 | <sub>https://www.smart-factory.kr/ids/cd/WeldingVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WireFeedSpeed | 속성 | 9.4 | <sub>https://www.smart-factory.kr/ids/cd/WireFeedSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TravelSpeed | 속성 | 41.0 | <sub>https://www.smart-factory.kr/ids/cd/TravelSpeed/1/0</sub> |

</details>

<a id="sm-8"></a>
<details>
<summary><b>8. PredictiveMaintenance</b> — 요소 32개</summary>

> 예지보전 서브모델 - 잔여수명(RUL) 예측-경계조건-예측모델-경보 등 예지보전 정보를 표준 구조로 담는다(IDTA 공식 템플릿).

semanticId: `https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **RemainingUsefulLifePrediction** | 묶음 (7) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;└ **RemainingUsefulLifetime** | 엔티티 (6) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IndicationType | 속성 | RemainingUsefulLife | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IndicationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DurationValue | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DurationValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EngineeringUnit | 속성 | h | <sub>https://admin-shell.io/idta/PredictiveMaintenance/EngineeringUnit/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartValue | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartDateTime | 속성 | 2026-01-01T00:00:00+09:00 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartDateTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 속성 | 용접 소모품·구동부 마모 기반 잔여수명 예측 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Description/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ RemainingUsfulLifeDateTime | 속성 | 2026-01-01T00:00:00+09:00 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsfulLifeD…</sub> |
| &nbsp;&nbsp;&nbsp;└ ConfidenceInterval | 범위 | 0.0 ~ 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConfidenceInterval/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListRULBoundaryConditions** | 목록 (1) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListRULBoundaryCond…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | AccumulatedArcTime | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | h | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.0 ~ 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 컨택트팁 교체 권고 경계 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;└ **PredictionModelInformation** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PredictionModelInfo…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelType | 속성 | Statistical | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelDescription | 속성 | 누적 아크가동시간 기반 통계 예측 모델 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SMAIModelNamePlate | 참조 |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/SMAIModelNamePlate/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListPreAlerts** | 목록 (1) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListPreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertMessage | 속성 | 소모품 교체 사전 경보 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertValue | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AlertAfterExceedingRemainingUsableLife** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertAfterExceeding…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AlertMessage | 속성 | 소모품 교체 경보 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaintenanceRequired | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MaintenanceRequired…</sub> |

</details>
