# 🧩 PlateHeatExchanger_AAS_v0.0.1.aasx

[← 장비 페이지](../README.md) · [⤓ AASX 다운로드](../AASX/PlateHeatExchanger_AAS_v0.0.1.aasx) · 2.8 MB

> 🤖 AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.

<img src="PlateHeatExchanger_AAS_v0.0.1_thumbnail.jpg" alt="썸네일" height="180" align="right">

| 항목 | 내용 |
|---|---|
| AAS idShort | `PlateHeatExchangerAAS` |
| AAS id | <sub>https://www.smart-factory.kr/ids/aas/PlateHeatExchangerAAS/1/0</sub> |
| 자산 종류 (assetKind) | Type |
| globalAssetId | <sub>https://www.smart-factory.kr/ids/asset/HeatExchanger/PHE-2026-0001</sub> |
| 설명 | 비식별 판형 열교환기 타입 참조모델이며 실물 자산 승인 정보가 아닙니다. |
| 서브모델 | 6개 |
| 전체 요소 | 273개 |

## 서브모델 한눈에 보기

| # | 서브모델 | 요소 수 | semanticId |
|:-:|---|--:|---|
| 1 | [Nameplate](#sm-1) | 34 | <sub>https://admin-shell.io/idta/nameplate/3/0/Nameplate</sub> |
| 2 | [HandoverDocumentation](#sm-2) | 38 | <sub>0173-1#01-AHF578#003</sub> |
| 3 | [TechnicalData](#sm-3) | 82 | <sub>0173-1#01-AHX837#002</sub> |
| 4 | [OperationalData](#sm-4) | 48 | <sub>https://www.smart-factory.kr/ids/sm/PlateHeatExchangerAAS/OperationalData/1/0</sub> |
| 5 | [Reliability](#sm-5) | 15 | <sub>https://admin-shell.io/idta/iec62683/1/0/Reliability</sub> |
| 6 | [ProcessParameters](#sm-6) | 56 | <sub>https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0</sub> |

## 서브모델 상세

각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.

<a id="sm-1"></a>
<details>
<summary><b>1. Nameplate</b> — 요소 34개</summary>

> Contains the nameplate information attached to the product

semanticId: `https://admin-shell.io/idta/nameplate/3/0/Nameplate`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| URIOfTheProduct | 속성 | https://www.smart-factory.kr/ids/asset/HeatExchanger/PHE-2026-0001 | <sub>0112/2///61987#ABN590#002</sub> |
| ManufacturerName | 다국어 속성 | Heat Exchanger Maker Co., Ltd. | <sub>0112/2///61987#ABA565#009</sub> |
| ManufacturerProductDesignation | 다국어 속성 | Plate Heat Exchanger | <sub>0112/2///61987#ABA567#009</sub> |
| ManufacturerProductRoot | 다국어 속성 | Heat Exchanger | <sub>0112/2///61360_7#AAS011#001</sub> |
| ManufacturerProductFamily | 다국어 속성 | Plate Heat Exchanger Series | <sub>0112/2///61987#ABP464#002</sub> |
| ManufacturerProductType | 속성 | PHE-Example-100 | <sub>0112/2///61987#ABA300#008</sub> |
| OrderCodeOfManufacturer | 속성 | PHE-100-STD | <sub>0112/2///61987#ABA950#008</sub> |
| ProductArticleNumberOfManufacturer | 속성 | ART-PHE-100 | <sub>0112/2///61987#ABA581#007</sub> |
| SerialNumber | 속성 | PHE-2026-0001 | <sub>0112/2///61987#ABA951#009</sub> |
| YearOfConstruction | 속성 | 2026 | <sub>0112/2///61987#ABP000#002</sub> |
| DateOfManufacture | 속성 | 2026-01-22 | <sub>0112/2///61987#ABB757#007</sub> |
| HardwareVersion | 속성 | HW-1.0 | <sub>0112/2///61987#ABA926#008</sub> |
| FirmwareVersion | 속성 | FW-1.0 | <sub>0112/2///61987#ABA302#006</sub> |
| SoftwareVersion | 속성 | SW-1.0 | <sub>0112/2///61987#ABA601#008</sub> |
| CountryOfOrigin | 속성 | KR | <sub>0112/2///61987#ABP462#001</sub> |
| UniqueFacilityIdentifier | 속성 | PHE-FAC-001 | <sub>https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier</sub> |
| **AddressInformation** | 묶음 (4) |  | <sub>https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/Address…</sub> |
| &nbsp;&nbsp;&nbsp;└ Street | 다국어 속성 | 123 Industrial-ro | <sub>0173-1#02-AAO128#002</sub> |
| &nbsp;&nbsp;&nbsp;└ Zipcode | 다국어 속성 | 12345 | <sub>0173-1#02-AAO129#002</sub> |
| &nbsp;&nbsp;&nbsp;└ CityTown | 다국어 속성 | Seoul | <sub>0173-1#02-AAO132#002</sub> |
| &nbsp;&nbsp;&nbsp;└ NationalCode | 다국어 속성 | KR | <sub>0173-1#02-AAO134#002</sub> |
| CompanyLogo | 파일 | /aasx/files/images/ExampleManufacturer.svg | <sub>0112/2///61987#ABP463#001</sub> |
| **Markings** | 목록 (1) |  | <sub>0112/2///61360_7#AAS006#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (6) |  | <sub>0112/2///61360_7#AAS009#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingName | 속성 | EXAMPLE - NOT CERTIFIED | <sub>0112/2///61987#ABA231#009</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DesignationOfCertificateOrApproval | 속성 | EXAMPLE-NO-APPROVAL | <sub>0112/2///61987#ABH783#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IssueDate | 속성 | 2026-06-03 | <sub>0112/2///61987#ABO097#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExpiryDate | 속성 | 2027-06-03 | <sub>0112/2///61987#ABH830#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingFile | 파일 | /aasx/files/documents/Example_NotCertified.txt | <sub>0112/2///61987#ABO100#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MarkingAdditionalText | 속성 | Fictional reference-model example only. No certification, pressure approval or … | <sub>0112/2///61987#ABB146#007</sub> |
| **AssetSpecificProperties** | 묶음 (1) |  | <sub>0173-1#02-ABI218#003/0173-1#01-AGZ672#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **GuidelineSpecificProperties** | 목록 (1) |  | <sub>0173-1#02-ABI219#003/0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#01-AHD205#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuidelineForConformityDeclaration | 속성 | Not applicable: no real conformity declaration is supplied for this fictional r… | <sub>0173-1#02-AAO856#002</sub> |

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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | HEAT_EXCHANGER_DOC | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | PHE-PLAN-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | 02-01 | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Technical specification | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | VDI 2770 Blatt 1:2020 | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (15) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | ko | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 1 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Plate Heat Exchanger Reference-Model Development Plan | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | 첨부파일은 기존 개발계획서이며 제조사 운전매뉴얼이나 시험성적서가 아니다. 이번 AASX 수정내용을 반영한 문서 개정은 후속 작업이다. | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ KeyWords | 다국어 속성 | plate heat exchanger, AAS, technical data, operation, reliability, process para… | <sub>0173-1#02-ABH999#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-08-21 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | Existing development plan; alignment update pending | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleOrganization | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | Example Organization Co., Ltd. | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/documents/HeatExchanger_DevelopmentPlan.hwpx | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreviewFile | 파일 |  | <sub>0173-1#02-ABK127#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Subtitle | 다국어 속성 | 판형 열교환기 참조모델 개발 목적과 구성에 관한 문서 | <sub>0173-1#02-ABH998#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RefersToEntities** | 목록 (1) |  | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/sm/PlateHeatExchangerAAS/HandoverDocumentation… | <sub>0173-1#02-ABK288#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BasedOnReferences** | 목록 (1) |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 |  | <sub>0173-1#02-ABK289#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TranslationOfEntities** | 목록 (1) |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 |  | <sub>0173-1#02-ABK290#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentedEntities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntities</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 참조 | https://www.smart-factory.kr/ids/sm/PlateHeatExchangerAAS/HandoverDocumentation… | <sub>https://admin-shell.io/vdi/2770/1/0/Document/DocumentedEntity</sub> |
| **Entities** | 목록 (1) |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntitiesForDocumentation</sub> |
| &nbsp;&nbsp;&nbsp;└  | 엔티티 |  | <sub>https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation</sub> |

</details>

<a id="sm-3"></a>
<details>
<summary><b>3. TechnicalData</b> — 요소 82개</summary>

> Submodel containing technical data of the asset and associated product classificatons

semanticId: `0173-1#01-AHX837#002`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **GeneralInformation** | 묶음 (6) |  | <sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerName | 속성 | Heat Exchanger Maker Co., Ltd. | <sub>0173-1#02-AAO677#004</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerProductDesignation | 다국어 속성 | Plate Heat Exchanger | <sub>0173-1#02-AAW338#003</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerArticleNumber | 속성 | ART-PHE-100 | <sub>0173-1#02-AAO676#005</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerOrderCode | 속성 | PHE-100-STD | <sub>0173-1#02-AAO227#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductImages** | 목록 (1) |  | <sub>0173-1#02-ABM220#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageFile | 파일 | /aasx/files/images/PHE_ProductImage.png | <sub>0173-1#02-ABK291#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageNote | 다국어 속성 | Three-quarter view of a gasketed plate heat exchanger | <sub>0173-1#02-ABL423#001</sub> |
| &nbsp;&nbsp;&nbsp;└ CompanyLogo | 파일 | /aasx/files/images/ExampleManufacturer.svg | <sub>0173-1#02-ABI776#002</sub> |
| **ProductClassifications** | 목록 (1) |  | <sub>0173-1#02-ABK162#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (7) |  | <sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | ECLASS | <sub>0173-1#02-ABL424#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemVersion | 속성 | ECLASS 16.0 | <sub>0173-1#02-AAR710#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemUrl | 속성 | https://eclass.eu | <sub>https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/Prod…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassId | 속성 | 0173-1#01-AAD341#021 | <sub>0173-1#02-ABG776#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassCodedName | 속성 | 36-04-01-02 | <sub>0173-1#02-ABK128#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassName | 다국어 속성 | Plate heat exchanger | <sub>0173-1#02-ABK273#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ReferenceToTechnicalPropertyArea | 참조 | https://www.smart-factory.kr/ids/sm/PlateHeatExchangerAAS/TechnicalData/2/0 / T… | <sub>0173-1#02-ABL358#002</sub> |
| **TechnicalPropertyAreas** | 목록 (6) |  | <sub>0173-1#02-ABK163#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HeatExchangerCommonSpecifications** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatExchangerCommonSpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ConstructionAndServiceability** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/ConstructionAndServiceability/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatExchangerType | 속성 | Plate Heat Exchanger | <sub>0173-1#02-ABI725#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlateType | 속성 | Chevron patterned plate | <sub>0173-1#02-AAP850#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NumberOfPlates | 속성 | 45 | <sub>0173-1#02-AAP475#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FlowArrangement | 속성 | Counter flow | <sub>https://www.smart-factory.kr/ids/cd/FlowArrangement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningSupport | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/CleaningSupport/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ThermalPerformanceSpecifications** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalPerformanceSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HeatTransferCapacityAndFlowDesign** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatTransferCapacityAndFlowDesign…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTransferArea | 속성 | 25 | <sub>0173-1#02-BAI259#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DesignHeatDuty | 속성 | 957.916667 | <sub>https://www.smart-factory.kr/ids/cd/DesignHeatDuty/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimarySideDesignFlowRate | 속성 | 15 | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideDesignFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondarySideDesignFlowRate | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideDesignFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DesignTemperatureProfile** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/DesignTemperatureProfile/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimarySideDesignInletTemperature | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideDesignInletTemperature…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimarySideDesignOutletTemperature | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideDesignOutletTemperatur…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondarySideDesignInletTemperature | 속성 | 20 | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideDesignInletTemperatu…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondarySideDesignOutletTemperature | 속성 | 65.833333 | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideDesignOutletTemperat…</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **OperatingTemperatureSpecifications** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/OperatingTemperatureSpecification…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PermissibleOperatingTemperatureRange** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/PermissibleOperatingTemperatureRa…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MinimumOperatingTemperature | 속성 | -10 | <sub>0173-1#02-BAA015#013</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumOperatingTemperature | 속성 | 150 | <sub>0173-1#02-AAN307#007</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PressureSpecifications** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/PressureSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PressureDesignAndLossLimits** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/PressureDesignAndLossLimits/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimaryDesignPressure | 속성 | 10 | <sub>0173-1#02-ABI795#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondaryDesignPressure | 속성 | 10 | <sub>0173-1#02-ABL372#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimaryMaximumOperatingPressure | 속성 | 10 | <sub>0173-1#02-ABL373#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondaryMaximumOperatingPressure | 속성 | 10 | <sub>0173-1#02-ABL374#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimaryTestPressure | 속성 | 15 | <sub>0173-1#02-ABL380#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondaryTestPressure | 속성 | 15 | <sub>0173-1#02-ABL381#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowablePressureDrop | 속성 | 0.6 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowablePressureDrop/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MaterialAndConnectionSpecifications** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/MaterialAndConnectionSpecificatio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ConstructionMaterials** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ConstructionMaterials/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlateMaterial | 속성 | Stainless steel 316L | <sub>0173-1#02-AAP103#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GasketMaterial | 속성 | EPDM | <sub>https://www.smart-factory.kr/ids/cd/GasketMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FrameMaterial | 속성 | Carbon steel coated | <sub>0173-1#02-AAP123#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlateThickness | 속성 | 0.5 | <sub>0173-1#02-BAI257#007</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessConnections** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ProcessConnections/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConnectionType | 속성 | Flanged connection | <sub>0173-1#02-AAH217#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PortSize | 속성 | DN50 | <sub>0173-1#02-AAO331#007</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetySpecifications** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetySpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalSupplyAndProtection** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyAndProtection/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupply | 속성 | 220 VAC ±10%, 50/60 Hz | <sub>https://www.smart-factory.kr/ids/cd/PowerSupply/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedPower | 속성 | 0.2 | <sub>0173-1#02-AAJ700#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedPowerConsumption | 속성 | 200 | <sub>0173-1#02-AAC970#010</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LeakageBreakerCapacity | 속성 | 5 | <sub>https://www.smart-factory.kr/ids/cd/LeakageBreakerCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FunctionalSafetyAndGrounding** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/FunctionalSafetyAndGrounding/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SupportedSafetyFunctions | 속성 | Emergency stop | <sub>0173-1#02-AAR796#006</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OverTemperatureProtectionSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/OverTemperatureProtectionSupporte…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GroundingRequired | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/GroundingRequired/1/0</sub> |
| **FurtherInformation** | 묶음 (2) |  | <sub>0173-1#02-ABK164#002</sub> |
| &nbsp;&nbsp;&nbsp;└ TextStatement | 다국어 속성 | This specification is based on clean heat-transfer conditions | <sub>0173-1#02-ABK134#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ValidDate | 속성 | 2026-01-22 | <sub>0173-1#02-ABL775#001</sub> |
| **SpecificDescriptions** | 목록 (1) |  | <sub>0173-1#02-ABM221#001</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABM221#001/0173-1#01-AHY912#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ExampleScope | 속성 | Fictional water-to-water counterflow plate heat exchanger. Values are illustrat… | <sub>https://www.smart-factory.kr/ids/cd/ExampleScope/1/0</sub> |

</details>

<a id="sm-4"></a>
<details>
<summary><b>4. OperationalData</b> — 요소 48개</summary>

> 판형 열교환기의 현재 운전값과 상태

semanticId: `https://www.smart-factory.kr/ids/sm/PlateHeatExchangerAAS/OperationalData/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **PlateHeatExchangerOperationData** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/PlateHeatExchangerOperationData/1…</sub> |
| &nbsp;&nbsp;&nbsp;└ **OperationStatus** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/OperationStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentOperationMode | 속성 | Continuous | <sub>https://www.smart-factory.kr/ids/cd/CurrentOperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EquipmentStatus | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/EquipmentStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/AlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LeakageStatus | 속성 | Not detected | <sub>https://www.smart-factory.kr/ids/cd/LeakageStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningRequiredStatus | 속성 | Not required | <sub>https://www.smart-factory.kr/ids/cd/CleaningRequiredStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdateTime | 속성 | 2026-06-03T09:00:00+09:00 | <sub>https://www.smart-factory.kr/ids/cd/LastUpdateTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PrimarySideFluidOperationData** | 묶음 (10) |  | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideFluidOperationData/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimarySideWorkingFluid | 속성 | Hot water | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideWorkingFluid/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryFlowRate | 속성 | 15 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentPrimaryFlowRate | 속성 | 14.8 | <sub>https://www.smart-factory.kr/ids/cd/CurrentPrimaryFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryInletTemperature | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryInletTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentPrimaryInletTemperature | 속성 | 79.6 | <sub>0173-1#02-BAI173#007</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryOutletTemperature | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryOutletTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentPrimaryOutletTemperature | 속성 | 26.2 | <sub>0173-1#02-BAI172#007</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryInletPressure | 속성 | 4.0 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryInletPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentPrimaryInletPressure | 속성 | 4.1 | <sub>https://www.smart-factory.kr/ids/cd/CurrentPrimaryInletPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentPrimaryPressureDrop | 속성 | 0.42 | <sub>https://www.smart-factory.kr/ids/cd/CurrentPrimaryPressureDrop/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **SecondarySideFluidOperationData** | 묶음 (10) |  | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideFluidOperationData/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondarySideWorkingFluid | 속성 | Cooling water | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideWorkingFluid/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryFlowRate | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentSecondaryFlowRate | 속성 | 18.2 | <sub>https://www.smart-factory.kr/ids/cd/CurrentSecondaryFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryInletTemperature | 속성 | 20 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryInletTemperature/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentSecondaryInletTemperature | 속성 | 20.4 | <sub>https://www.smart-factory.kr/ids/cd/CurrentSecondaryInletTemperature/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryOutletTemperature | 속성 | 65.833333 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryOutletTemperature/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentSecondaryOutletTemperature | 속성 | 63.824176 | <sub>https://www.smart-factory.kr/ids/cd/CurrentSecondaryOutletTemperature…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryInletPressure | 속성 | 3.5 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryInletPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentSecondaryInletPressure | 속성 | 3.4 | <sub>https://www.smart-factory.kr/ids/cd/CurrentSecondaryInletPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentSecondaryPressureDrop | 속성 | 0.38 | <sub>https://www.smart-factory.kr/ids/cd/CurrentSecondaryPressureDrop/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ThermalPerformanceOperationData** | 묶음 (11) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalPerformanceOperationData/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetHeatDuty | 속성 | 957.916667 | <sub>https://www.smart-factory.kr/ids/cd/TargetHeatDuty/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentHeatDuty | 속성 | 917.649333 | <sub>https://www.smart-factory.kr/ids/cd/CurrentHeatDuty/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetHeatTransferEfficiency | 속성 | 90 | <sub>https://www.smart-factory.kr/ids/cd/TargetHeatTransferEfficiency/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentHeatTransferEfficiency | 속성 | 90.202703 | <sub>https://www.smart-factory.kr/ids/cd/CurrentHeatTransferEfficiency/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetApproachTemperature | 속성 | 5 | <sub>https://www.smart-factory.kr/ids/cd/TargetApproachTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentApproachTemperature | 속성 | 5.8 | <sub>https://www.smart-factory.kr/ids/cd/CurrentApproachTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowableApproachTemperature | 속성 | 8 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowableApproachTemperatu…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowablePrimaryOutletTemperatureDeviation | 속성 | 2 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowablePrimaryOutletTemp…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowableSecondaryOutletTemperatureDeviation | 속성 | 2 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowableSecondaryOutletTe…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EstimatedFoulingFactor | 속성 | 0.00012 | <sub>https://www.smart-factory.kr/ids/cd/EstimatedFoulingFactor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowableFoulingFactor | 속성 | 0.0002 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowableFoulingFactor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **PressureAndDifferentialPressureOperationData** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/PressureAndDifferentialPressureOp…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowablePrimaryPressureDrop | 속성 | 0.6 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowablePrimaryPressureDr…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaximumAllowableSecondaryPressureDrop | 속성 | 0.6 | <sub>https://www.smart-factory.kr/ids/cd/MaximumAllowableSecondaryPressure…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressureDropWarningThreshold | 속성 | 0.5 | <sub>https://www.smart-factory.kr/ids/cd/PressureDropWarningThreshold/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighPressureAlarmThreshold | 속성 | 9 | <sub>https://www.smart-factory.kr/ids/cd/HighPressureAlarmThreshold/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HighPressureDropAlarmThreshold | 속성 | 0.7 | <sub>https://www.smart-factory.kr/ids/cd/HighPressureDropAlarmThreshold/1/0</sub> |

</details>

<a id="sm-5"></a>
<details>
<summary><b>5. Reliability</b> — 요소 15개</summary>

semanticId: `https://admin-shell.io/idta/iec62683/1/0/Reliability`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| NumberOfReliabilitySets | 속성 | 1 | <sub>0112/2///62683#ACE006#001</sub> |
| **OperatingConditionsOfReliabilityCharacteristics** | 묶음 (9) |  | <sub>0112/2///62683#ACG071#001</sub> |
| &nbsp;&nbsp;&nbsp;└ TypeOfVoltage | 속성 | AC | <sub>0112/2///61987#ABA969#007</sub> |
| &nbsp;&nbsp;&nbsp;└ RatedVoltage | 속성 | 220 | <sub>0112/2///61987#ABA588#004</sub> |
| &nbsp;&nbsp;&nbsp;└ MinimumRatedVoltage | 속성 | 198 | <sub>0112/2///61987#ABD461#004</sub> |
| &nbsp;&nbsp;&nbsp;└ MaximumRatedVoltage | 속성 | 242 | <sub>0112/2///61987#ABD462#004</sub> |
| &nbsp;&nbsp;&nbsp;└ RatedOperationalCurrent | 속성 | 1000 | <sub>https://admin-shell.io/idta/FunctionalSafety/RatedOperationalCurrent/…</sub> |
| &nbsp;&nbsp;&nbsp;└ TypeOfInterlockingDevice | 속성 | Pressure and leakage alarm interlock | <sub>0112/2///62683#ACE053#001</sub> |
| &nbsp;&nbsp;&nbsp;└ OtherOperatingConditions | 속성 | Illustrative steady-state water-to-water counterflow operation; design pressure… | <sub>0112/2///62683#ACE070#001</sub> |
| &nbsp;&nbsp;&nbsp;└ UsefulLifeInNumberOfOperations | 속성 | 20000 | <sub>0112/2///62683#ACE055#001</sub> |
| &nbsp;&nbsp;&nbsp;└ UsefulLifeInTimeInterval | 속성 | 10 | <sub>0112/2///62683#ACE054#001</sub> |
| **ReliabilityCharacteristics** | 묶음 (3) |  | <sub>0112/2///62683#ACG080#001</sub> |
| &nbsp;&nbsp;&nbsp;└ MTTF | 속성 | 10 | <sub>0112/2///62683#ACE061#001</sub> |
| &nbsp;&nbsp;&nbsp;└ MTBF | 속성 | 5 | <sub>0112/2///62683#ACE062#001</sub> |
| &nbsp;&nbsp;&nbsp;└ B10 | 속성 | 15000 | <sub>https://admin-shell.io/idta/Reliability/B10/1/0</sub> |

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
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessId | 속성 | PHE-P-001 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessName | 속성 | Plate heat exchange process | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessDescription | 다국어 속성 | Process parameters for plate heat-exchanger operation and CIP cleaning | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlannedProcessTime | 속성 | PT60M | <sub>https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PlateHeatExchangerProductRequirements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/PlateHeatExchangerProductRequirem…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FluidAndFoulingConditions** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/FluidAndFoulingConditions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetFluidType | 속성 | Water | <sub>https://www.smart-factory.kr/ids/cd/TargetFluidType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimarySideFluidCondition | 속성 | Hot water, clean condition | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideFluidCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondarySideFluidCondition | 속성 | Cooling water, clean condition | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideFluidCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FoulingAllowanceCondition | 속성 | Clean to light fouling condition | <sub>https://www.smart-factory.kr/ids/cd/FoulingAllowanceCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ThermalPerformanceRequirements** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalPerformanceRequirements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredOutletTemperature | 속성 | 65.833333 | <sub>https://www.smart-factory.kr/ids/cd/RequiredOutletTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredHeatDuty | 속성 | 957.916667 | <sub>https://www.smart-factory.kr/ids/cd/RequiredHeatDuty/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredHeatTransferEfficiency | 속성 | 91.666667 | <sub>https://www.smart-factory.kr/ids/cd/RequiredHeatTransferEfficiency/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredApproachTemperature | 속성 | 5 | <sub>https://www.smart-factory.kr/ids/cd/RequiredApproachTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PlateHeatExchangerOperatingRecipe** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/PlateHeatExchangerOperatingRecipe…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FlowTemperatureAndPressureSetpoints** | 묶음 (8) |  | <sub>https://www.smart-factory.kr/ids/cd/FlowTemperatureAndPressureSetpoin…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryFlowRate | 속성 | 15 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryFlowRate | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryInletTemperature | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryInletTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryOutletTemperature | 속성 | 25 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryOutletTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryInletTemperature | 속성 | 20 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryInletTemperature/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryOutletTemperature | 속성 | 65.833333 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryOutletTemperature/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetPrimaryInletPressure | 속성 | 4.0 | <sub>https://www.smart-factory.kr/ids/cd/TargetPrimaryInletPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSecondaryInletPressure | 속성 | 3.5 | <sub>https://www.smart-factory.kr/ids/cd/TargetSecondaryInletPressure/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ThermalPerformanceSetpoints** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalPerformanceSetpoints/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetApproachTemperature | 속성 | 5 | <sub>https://www.smart-factory.kr/ids/cd/TargetApproachTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetHeatDuty | 속성 | 957.916667 | <sub>https://www.smart-factory.kr/ids/cd/TargetHeatDuty/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CleaningSetpoints** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/CleaningSetpoints/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningFluidFlowRate | 속성 | 10 | <sub>https://www.smart-factory.kr/ids/cd/CleaningFluidFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningTemperature | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/CleaningTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningTime | 속성 | PT30M | <sub>https://www.smart-factory.kr/ids/cd/CleaningTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ResourceParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PlateHeatExchangerResourceRequirements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/PlateHeatExchangerResourceRequire…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MeasurementInstrumentRequirements** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/MeasurementInstrumentRequirements…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperatureSensorRequirement | 속성 | Primary and secondary inlet/outlet temperature sensors | <sub>https://www.smart-factory.kr/ids/cd/TemperatureSensorRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FlowMeterRequirement | 속성 | Primary and secondary flow meters | <sub>https://www.smart-factory.kr/ids/cd/FlowMeterRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PressureSensorRequirement | 속성 | Primary and secondary pressure sensors | <sub>https://www.smart-factory.kr/ids/cd/PressureSensorRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DifferentialPressureSensorRequirement | 속성 | Differential pressure monitoring supported | <sub>https://www.smart-factory.kr/ids/cd/DifferentialPressureSensorRequire…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CleaningControlAndDataRequirements** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/CleaningControlAndDataRequirement…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningSystemRequirement | 속성 | CIP cleaning connection required | <sub>https://www.smart-factory.kr/ids/cd/CleaningSystemRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ValveControlRequirement | 속성 | Flow-balancing valve control required | <sub>https://www.smart-factory.kr/ids/cd/ValveControlRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DataAcquisitionRequirement | 속성 | PLC or SCADA data acquisition required | <sub>https://www.smart-factory.kr/ids/cd/DataAcquisitionRequirement/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessBoM** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PlateHeatExchangerProcessMaterials** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/PlateHeatExchangerProcessMaterial…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HeatExchangeMedia** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatExchangeMedia/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PrimarySideMedium | 속성 | Hot water | <sub>https://www.smart-factory.kr/ids/cd/PrimarySideMedium/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SecondarySideMedium | 속성 | Cooling water | <sub>https://www.smart-factory.kr/ids/cd/SecondarySideMedium/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **CleaningAndMaintenanceConsumables** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/CleaningAndMaintenanceConsumables…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningChemical | 속성 | Mild alkaline CIP solution | <sub>https://www.smart-factory.kr/ids/cd/CleaningChemical/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CleaningWater | 속성 | Clean water | <sub>https://www.smart-factory.kr/ids/cd/CleaningWater/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GasketSparePart | 속성 | EPDM gasket set | <sub>https://www.smart-factory.kr/ids/cd/GasketSparePart/1/0</sub> |

</details>
