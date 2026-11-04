# HydraulicFormingPress_v0.0.3_261013.aasx

[장비 페이지](../README.md) · [AASX 다운로드](../AASX/HydraulicFormingPress_v0.0.3_261013.aasx) · 13.1 MB

> AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.

<img src="HydraulicFormingPress_v0.0.3_261013_thumbnail.jpg" alt="썸네일" height="180" align="right">

| 항목 | 내용 |
|---|---|
| AAS idShort | `HydraulicFormingPress` |
| AAS id | <sub>https://www.smart-factory.kr/ids/aas/HydraulicFormingPress/1/0</sub> |
| 자산 종류 (assetKind) | Type |
| globalAssetId | <sub>https://www.smart-factory.kr/ids/asset/HydraulicFormingPress/PR2000H/1/0</sub> |
| 설명 | 냉간 금속 판재 성형용 4주식 유압 프레스의 Type1 참조모델입니다. ExampleCompany·PR-2000H와 장비·운전·레시피 값은 비식별 합성 예시입니다. 공개 제조사 문서와 실린더·램 사진은 참고 자료이며 장비 채택 사양의 근거가 아닙니다. 썸네일은 4주식·주 가압 실린더 2개 장비 전경의 실사진이며 구성 참고용임. 출처: https://chi… |
| 서브모델 | 6개 |
| 전체 요소 | 1,600개 |

## 서브모델 한눈에 보기

| # | 서브모델 | 요소 수 | semanticId |
|:-:|---|--:|---|
| 1 | [Nameplate](#sm-1) | 21 | <sub>https://admin-shell.io/idta/nameplate/3/0/Nameplate</sub> |
| 2 | [HandoverDocumentation](#sm-2) | 25 | <sub>0173-1#01-AHF578#003</sub> |
| 3 | [TechnicalData](#sm-3) | 63 | <sub>0173-1#01-AHX837#002</sub> |
| 4 | [OperationalData](#sm-4) | 34 | <sub>https://www.smart-factory.kr/ids/sm/HydraulicFormingPress/OperationalData/1/0</sub> |
| 5 | [TimeSeries](#sm-5) | 1,431 | <sub>https://admin-shell.io/idta/TimeSeries/1/1</sub> |
| 6 | [ProcessParameters](#sm-6) | 26 | <sub>https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0</sub> |

## 서브모델 상세

각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.

<a id="sm-1"></a>
<details>
<summary><b>1. Nameplate</b> — 요소 21개</summary>

> 4주식 유압 성형 프레스의 식별 정보이며 제품·주소 값은 비식별 합성 예시입니다.

semanticId: `https://admin-shell.io/idta/nameplate/3/0/Nameplate`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| URIOfTheProduct | 속성 | https://www.smart-factory.kr/ids/asset/HydraulicFormingPress/PR2000H/1/0 | <sub>0112/2///61987#ABN590#002</sub> |
| ManufacturerName | 다국어&nbsp;속성 | ExampleCompany | <sub>0112/2///61987#ABA565#009</sub> |
| ManufacturerProductDesignation | 다국어&nbsp;속성 | ExampleCompany Hydraulic Forming Press | <sub>0112/2///61987#ABA567#009</sub> |
| **AddressInformation** | 묶음&nbsp;(4) |  | <sub>https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/Address…</sub> |
| &nbsp;&nbsp;&nbsp;└ Street | 다국어&nbsp;속성 | 1 Example-ro | <sub>0173-1#02-AAO128#002</sub> |
| &nbsp;&nbsp;&nbsp;└ Zipcode | 다국어&nbsp;속성 | 12345 | <sub>0173-1#02-AAO129#002</sub> |
| &nbsp;&nbsp;&nbsp;└ CityTown | 다국어&nbsp;속성 | ExampleCity | <sub>0173-1#02-AAO132#002</sub> |
| &nbsp;&nbsp;&nbsp;└ NationalCode | 다국어&nbsp;속성 | KR | <sub>0173-1#02-AAO134#002</sub> |
| ManufacturerProductRoot | 다국어&nbsp;속성 | Hydraulic press | <sub>0112/2///61360_7#AAS011#001</sub> |
| ManufacturerProductFamily | 다국어&nbsp;속성 | Hydraulic forming press | <sub>0112/2///61987#ABP464#002</sub> |
| ManufacturerProductType | 속성 | PR-2000H | <sub>0112/2///61987#ABA300#008</sub> |
| OrderCodeOfManufacturer | 속성 | PR-2000H-ORD | <sub>0112/2///61987#ABA950#008</sub> |
| ProductArticleNumberOfManufacturer | 속성 | PR-2000H-ART | <sub>0112/2///61987#ABA581#007</sub> |
| SerialNumber | 속성 | SYN-PR2000H-0001 | <sub>0112/2///61987#ABA951#009</sub> |
| YearOfConstruction | 속성 | 2026 | <sub>0112/2///61987#ABP000#002</sub> |
| DateOfManufacture | 속성 | 2026-06-01 | <sub>0112/2///61987#ABB757#007</sub> |
| HardwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA926#008</sub> |
| FirmwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA302#006</sub> |
| SoftwareVersion | 속성 | 1.0.0 | <sub>0112/2///61987#ABA601#008</sub> |
| CountryOfOrigin | 속성 | KR | <sub>0112/2///61987#ABP462#001</sub> |
| UniqueFacilityIdentifier | 속성 | SYN-FACILITY-001 | <sub>https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier</sub> |

</details>

<a id="sm-2"></a>
<details>
<summary><b>2. HandoverDocumentation</b> — 요소 25개</summary>

> 공개 제조사 카탈로그를 참고 문서로 연결하며, 장비 운전매뉴얼 또는 PDF/A 적합성이 확인된 인수문서와 구분합니다.

semanticId: `0173-1#01-AHF578#003`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Documents** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABI500#003</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(3) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | multipress.com | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | 11-002-V0320-MP-4-Post-Presses-Single.pdf | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 02-01 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어&nbsp;속성 | Technical specification | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770 Blatt 1:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(9) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록&nbsp;(1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | en | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | sha256-ac3439e1ac12 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어&nbsp;속성 | 4-Post Presses | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어&nbsp;속성 | Public MULTIPRESS four-post press catalog retained as reference material. It is… | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-10-13 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | InReview | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | MULTIPRESS | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | MULTIPRESS Inc. | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/Multipress_4Post.pdf | <sub>0173-1#02-ABK126#002</sub> |

</details>

<a id="sm-3"></a>
<details>
<summary><b>3. TechnicalData</b> — 요소 63개</summary>

> 4주식 유압 성형 프레스의 설계·정격 사양입니다. PR-2000H 수치는 합성 예시이며 참고 사진의 사양을 채택한 것으로 해석하지 않습니다.

semanticId: `0173-1#01-AHX837#002`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **GeneralInformation** | 묶음&nbsp;(5) |  | <sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerName | 속성 | ExampleCompany | <sub>0173-1#02-AAO677#004</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerProductDesignation | 다국어&nbsp;속성 | ExampleCompany Hydraulic Forming Press | <sub>0173-1#02-AAW338#003</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerArticleNumber | 속성 | PR-2000H-ART | <sub>0173-1#02-AAO676#005</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerOrderCode | 속성 | PR-2000H-ORD | <sub>0173-1#02-AAO227#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductImages** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABM220#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(2) |  | <sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageFile | 파일 | /aasx/files/images/figure4_actual.png | <sub>0173-1#02-ABK291#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageNote | 다국어&nbsp;속성 | Hydraulic press cylinder and ram reference photo | <sub>0173-1#02-ABL423#001</sub> |
| **ProductClassifications** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABK162#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(5) |  | <sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | ECLASS | <sub>0173-1#02-ABL424#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemVersion | 속성 | ECLASS 16.0 | <sub>0173-1#02-AAR710#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassId | 속성 | 0173-1#01-AKK097#020 | <sub>0173-1#02-ABG776#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassCodedName | 속성 | 36630608 | <sub>0173-1#02-ABK128#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassName | 다국어&nbsp;속성 | Hydraulic column press (machine tool) | <sub>0173-1#02-ABK273#002</sub> |
| **TechnicalPropertyAreas** | 목록&nbsp;(1) |  | <sub>0173-1#02-ABK163#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음&nbsp;(6) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HydraulicPressCommonSpecifications** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/HydraulicPressCommonSpecification…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PressTypeAndApplication** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/PressTypeAndApplication/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressType | 다국어&nbsp;속성 | Four-column hydraulic press | <sub>https://www.smart-factory.kr/ids/cd/PressType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressApplicationField | 속성 | Cold forming of metal sheet blanks | <sub>https://www.smart-factory.kr/ids/cd/PressApplicationField/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FrameAndActuators** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/FrameAndActuators/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfCylinders | 속성 | 2 | <sub>0173-1#02-AAP412#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FrameStructureType | 속성 | Steel four-column frame | <sub>https://www.smart-factory.kr/ids/cd/FrameStructureType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FormingForceAndStrokeSpecifications** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/FormingForceAndStrokeSpecificatio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ForceRatings** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/ForceRatings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedFormingForce | 속성 | 2000 | <sub>https://www.smart-factory.kr/ids/cd/RatedFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxRamForce | 속성 | 19613.3 | <sub>https://www.smart-factory.kr/ids/cd/MaxRamForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **StrokeAndMotion** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/StrokeAndMotion/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxRamStroke | 속성 | 1200 | <sub>0173-1#02-BAA627#010</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RamSpeedRange | 범위 | 0 ~ 3.8 | <sub>https://www.smart-factory.kr/ids/cd/RamSpeedRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DaylightOpening | 속성 | 1500 | <sub>https://www.smart-factory.kr/ids/cd/DaylightOpening/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HydraulicSystemSpecifications** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/HydraulicSystemSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PressureAndFlow** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/PressureAndFlow/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SystemPressureRange | 범위 | 0 ~ 31.5 | <sub>https://www.smart-factory.kr/ids/cd/SystemPressureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/RatedSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PumpFlowRate | 속성 | 180 | <sub>0173-1#02-ABC593#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **OilStorageAndSpecification** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/OilStorageAndSpecification/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HydraulicOilTankCapacity | 속성 | 1200 | <sub>https://www.smart-factory.kr/ids/cd/HydraulicOilTankCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HydraulicOilType | 속성 | ISO VG46 anti-wear hydraulic oil | <sub>https://www.smart-factory.kr/ids/cd/HydraulicOilType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DieAndBolsterSpecifications** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/DieAndBolsterSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DieInstallation** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/DieInstallation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BolsterPlateSize | 속성 | 2000 x 1500 | <sub>https://www.smart-factory.kr/ids/cd/BolsterPlateSize/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxDieWeight | 속성 | 8000 | <sub>https://www.smart-factory.kr/ids/cd/MaxDieWeight/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DieClampingMethod | 속성 | Hydraulic die clamp | <sub>https://www.smart-factory.kr/ids/cd/DieClampingMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PartEjection** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/PartEjection/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EjectorForce | 속성 | 400 | <sub>https://www.smart-factory.kr/ids/cd/EjectorForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **StructureAndDimensionSpecifications** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/StructureAndDimensionSpecificatio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **OverallDimensions** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/OverallDimensions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Length | 속성 | 3500 | <sub>0173-1#02-BAB146#011</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Width | 속성 | 3000 | <sub>0173-1#02-BAA705#009</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Height | 속성 | 7000 | <sub>0173-1#02-BAB707#009</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WeightRatings** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/WeightRatings/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MachineWeight | 속성 | 65000 | <sub>0173-1#02-AAH829#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetySpecifications** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetySpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PowerSupply** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/PowerSupply/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedVoltage | 범위 | 380 ~ 415 | <sub>https://www.smart-factory.kr/ids/cd/RatedVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MainMotorPower | 속성 | 75 | <sub>0173-1#02-AAG926#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProtectionAndSafety** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectionAndSafety/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IPRating | 속성 | IP54 | <sub>0173-1#02-BAG975#017</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SafetyLightCurtainType | 속성 | Type 4 | <sub>https://www.smart-factory.kr/ids/cd/SafetyLightCurtainType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopCategory | 속성 | 0 | <sub>0173-1#02-AAC131#010</sub> |

</details>

<a id="sm-4"></a>
<details>
<summary><b>4. OperationalData</b> — 요소 34개</summary>

> 2026-06-22T08:15:30Z의 합성 운전 스냅샷으로 성형력·램 운동·유압·생산·장비 상태를 표현합니다.

semanticId: `https://www.smart-factory.kr/ids/sm/HydraulicFormingPress/OperationalData/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **FormingOperation** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/FormingOperation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ForceMeasurements** | 묶음&nbsp;(4) |  | <sub>https://www.smart-factory.kr/ids/cd/ForceMeasurements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1860 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -2.11 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PositionAndMotion** | 묶음&nbsp;(4) |  | <sub>https://www.smart-factory.kr/ids/cd/PositionAndMotion/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| **HydraulicOperation** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/HydraulicOperation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PressureAndOilCondition** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/PressureAndOilCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 24.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PumpCondition** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/PumpCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| **ProductionOperation** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/ProductionOperation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **CycleStatistics** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/CycleStatistics/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PerformanceIndicators** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/PerformanceIndicators/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **OperatingCondition** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/OperatingCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| **EquipmentCondition** | 묶음&nbsp;(3) |  | <sub>https://www.smart-factory.kr/ids/cd/EquipmentCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **RunAndAlarmState** | 묶음&nbsp;(2) |  | <sub>https://www.smart-factory.kr/ids/cd/RunAndAlarmState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **GuardCondition** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/GuardCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **MaintenanceHistory** | 묶음&nbsp;(1) |  | <sub>https://www.smart-factory.kr/ids/cd/MaintenanceHistory/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |

</details>

<a id="sm-5"></a>
<details>
<summary><b>5. TimeSeries</b> — 요소 1,431개</summary>

> 22개 필드의 공통 레코드 구조, 외부 1일 CSV와 내부 1초 간격 60개 레코드를 사용합니다. CSV는 기록 구조의 합성 예시이며 유압 연성 해석의 검증 자료가 아닙니다.

semanticId: `https://admin-shell.io/idta/TimeSeries/1/1`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Metadata** | 묶음&nbsp;(3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Name | 다국어&nbsp;속성 | Hydraulic forming press operation time series | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Description | 다국어&nbsp;속성 | Time series data for hydraulic forming press operation values | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **Record** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1860 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 24.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -2.11 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT4H | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| **Segments** | 묶음&nbsp;(2) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **ExternalSegment** | 묶음&nbsp;(11) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/ExternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어&nbsp;속성 | Hydraulic press historian file data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어&nbsp;속성 | Hydraulic forming press time series data stored in external CSV file | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 86400 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-22T00:00:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-22T23:59:59Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT24H | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-23T00:00:05Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ File | 파일 | /aasx/files/timeseries/PR_TS_20260622.csv | <sub>https://admin-shell.io/idta/TimeSeries/File/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **InternalSegment** | 묶음&nbsp;(11) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/InternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어&nbsp;속성 | Recent hydraulic press operation data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어&nbsp;속성 | Recent hydraulic forming press operation records stored directly in AAS | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 60 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-22T08:15:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-22T08:15:59Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT1M | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-22T08:16:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Records** | 묶음&nbsp;(60) |  | <sub>https://admin-shell.io/idta/TimeSeries/Records/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record00** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:00Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 585.2 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14370S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record01** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:01Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 589.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14371S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record02** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:02Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 592.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14372S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record03** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:03Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 596.6 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14373S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record04** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:04Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 600.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14374S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record05** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:05Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 76.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 76.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 602.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -96.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14375S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record06** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:06Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 152.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 152.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 604.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -92.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14376S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record07** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:07Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 228.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 228.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 606.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -88.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14377S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record08** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:08Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 304.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 304.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 608.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -84.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14378S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record09** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:09Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 380.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 380.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 610.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -80.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14379S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record10** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:10Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 456.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 456.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 612.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -76.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14380S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record11** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:11Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 532.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 532.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 614.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -72.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14381S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record12** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:12Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 608.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 608.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 616.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -68.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14382S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record13** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:13Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 684.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 684.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 618.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -64.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14383S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record14** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:14Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 760.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 760.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 620.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -60.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14384S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record15** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:15Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 836.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 836.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 622.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -56.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14385S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record16** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:16Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 912.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 912.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 624.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -52.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14386S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record17** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:17Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 988.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 988.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 626.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -48.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14387S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record18** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:18Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1064.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1064.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 628.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -44.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14388S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record19** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:19Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1140.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1140.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 630.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -40.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14389S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record20** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:20Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1216.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1216.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 632.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -36.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14390S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record21** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:21Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1292.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1292.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 634.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -32.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14391S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record22** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:22Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1368.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1368.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 636.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -28.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14392S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record23** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:23Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1444.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1444.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 638.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -24.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14393S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record24** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:24Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1520.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1520.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 640.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -20.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14394S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record25** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:25Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1596.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1596.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 642.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -16.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14395S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record26** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:26Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1672.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1672.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 644.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -12.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14396S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record27** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:27Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1748.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1748.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 646.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -8.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14397S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record28** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:28Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1824.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1824.0 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 648.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -4.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14398S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record29** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:29Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1860.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 24.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -2.11 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245869 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14399S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record30** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:30Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 1860 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 24.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -2.11 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT4H | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record31** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:31Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14401S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record32** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:32Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 646.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14402S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record33** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:33Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 642.7 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14403S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record34** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:34Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 638.9 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14404S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record35** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:35Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 635.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14405S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record36** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:36Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 631.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14406S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record37** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:37Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 627.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14407S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record38** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:38Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 623.7 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14408S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record39** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:39Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 619.9 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14409S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record40** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:40Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 616.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14410S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record41** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:41Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 612.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14411S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record42** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:42Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 608.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14412S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record43** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:43Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 604.7 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14413S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record44** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:44Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 600.9 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14414S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record45** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:45Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 597.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14415S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record46** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:46Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 593.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14416S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record47** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:47Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 589.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14417S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record48** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:48Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 585.7 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14418S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record49** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:49Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 581.9 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14419S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record50** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:50Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 578.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14420S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record51** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:51Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 574.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14421S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record52** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:52Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 570.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14422S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record53** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:53Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 566.7 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14423S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record54** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:54Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 562.9 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14424S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record55** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:55Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 559.1 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14425S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record56** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:56Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 555.3 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14426S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record57** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:57Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 551.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14427S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record58** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:58Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 547.7 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14428S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record59** | 묶음&nbsp;(22) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-22T08:15:59Z | <sub>https://admin-shell.io/idta/TimeSeries/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOperatingMode | 속성 | Auto | <sub>https://www.smart-factory.kr/ids/cd/PressOperatingMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentCycleTime | 속성 | 480 | <sub>0173-1#02-AAF891#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentFormingForce | 속성 | 0.0 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPeakForceThisCycle | 속성 | 1925 | <sub>https://www.smart-factory.kr/ids/cd/PressPeakForceThisCycle/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamPosition | 속성 | 543.9 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressBottomDeadCenterPosition | 속성 | 650.3 | <sub>https://www.smart-factory.kr/ids/cd/PressBottomDeadCenterPosition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentRamSpeed | 속성 | 3.8 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentRamSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressRamPositionDeviation | 속성 | 0.3 | <sub>https://www.smart-factory.kr/ids/cd/PressRamPositionDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentSystemPressure | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressHydraulicOilTemperature | 속성 | 48 | <sub>https://www.smart-factory.kr/ids/cd/PressHydraulicOilTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressPumpVibrationLevel | 속성 | 2.8 | <sub>https://www.smart-factory.kr/ids/cd/PressPumpVibrationLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressForceDeviation | 속성 | -100.00 | <sub>https://www.smart-factory.kr/ids/cd/PressForceDeviation/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressStrokeCountAccumulated | 속성 | 1245870 | <sub>https://www.smart-factory.kr/ids/cd/PressStrokeCountAccumulated/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressCurrentOEE | 속성 | 82.4 | <sub>https://www.smart-factory.kr/ids/cd/PressCurrentOEE/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressTonnageStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressTonnageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressOilLevelStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/PressOilLevelStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressSafetyDoorStatus | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/PressSafetyDoorStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressAlarmCode | 속성 | A0000 | <sub>https://www.smart-factory.kr/ids/cd/PressAlarmCode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressDeviceRunStateDuration | 속성 | PT14429S | <sub>https://www.smart-factory.kr/ids/cd/PressDeviceRunStateDuration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressLastMaintenanceDate | 속성 | 2026-05-20 | <sub>https://www.smart-factory.kr/ids/cd/PressLastMaintenanceDate/1/0</sub> |

</details>

<a id="sm-6"></a>
<details>
<summary><b>6. ProcessParameters</b> — 요소 26개</summary>

> 제품 목표·공정 설정·자원 조건·투입 자재를 구분한 냉간 성형 합성 레시피입니다. 계획 공정 시간은 셋업 시간을 제외합니다.

semanticId: `https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Processes** | 묶음&nbsp;(1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Processes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **Process__00__** | 묶음&nbsp;(8) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Process/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessId | 속성 | PR-P-001 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessName | 속성 | Hydraulic forming production order | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessDescription | 다국어&nbsp;속성 | Process parameters for hydraulic forming press operation | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlannedProcessTime | 속성 | PT2H | <sub>https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductParameters** | 묶음&nbsp;(4) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPartName | 속성 | Cold-formed test part | <sub>https://www.smart-factory.kr/ids/cd/TargetPartName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPartMaterial | 속성 | Low-carbon steel sheet | <sub>https://www.smart-factory.kr/ids/cd/TargetPartMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPartThickness | 속성 | 12 | <sub>https://www.smart-factory.kr/ids/cd/TargetPartThickness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetDimensionTolerance | 속성 | 0.15 | <sub>https://www.smart-factory.kr/ids/cd/TargetDimensionTolerance/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessParameters** | 묶음&nbsp;(5) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SetFormingForce | 속성 | 1900 | <sub>https://www.smart-factory.kr/ids/cd/SetFormingForce/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SetBottomDeadCenter | 속성 | 650.0 | <sub>https://www.smart-factory.kr/ids/cd/SetBottomDeadCenter/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SetPressingSpeed | 속성 | 2.0 | <sub>https://www.smart-factory.kr/ids/cd/SetPressingSpeed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SetDwellTime | 속성 | PT2S | <sub>https://www.smart-factory.kr/ids/cd/SetDwellTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SetSystemPressure | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/SetSystemPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ResourceParameters** | 묶음&nbsp;(5) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ InstalledDieId | 속성 | DIE-SA-0457 | <sub>https://www.smart-factory.kr/ids/cd/InstalledDieId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HydraulicOilGrade | 속성 | ISO VG46 | <sub>https://www.smart-factory.kr/ids/cd/HydraulicOilGrade/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperatorId | 속성 | OP-2031 | <sub>https://www.smart-factory.kr/ids/cd/OperatorId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LubricantType | 속성 | Water-soluble cold-forming lubricant | <sub>https://www.smart-factory.kr/ids/cd/LubricantType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DieLubricantConsumption | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/DieLubricantConsumption/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessBoM** | 묶음&nbsp;(2) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RawBlankQuantity | 속성 | 1 | <sub>https://www.smart-factory.kr/ids/cd/RawBlankQuantity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RawMaterialLotNo | 속성 | LOT-STEEL-260612 | <sub>https://www.smart-factory.kr/ids/cd/RawMaterialLotNo/1/0</sub> |

</details>
