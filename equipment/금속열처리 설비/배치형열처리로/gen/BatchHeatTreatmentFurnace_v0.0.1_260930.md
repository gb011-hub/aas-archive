# 🧩 BatchHeatTreatmentFurnace_v0.0.1_260930.aasx

[← 장비 페이지](../README.md) · [⤓ AASX 다운로드](../AASX/BatchHeatTreatmentFurnace_v0.0.1_260930.aasx) · 3.2 MB

> 🤖 AASX 파일을 열어 자동으로 만든 열람 페이지입니다. 직접 고치지 말고 AASX를 다시 올리세요.

<img src="BatchHeatTreatmentFurnace_v0.0.1_260930_thumbnail.jpg" alt="썸네일" height="180" align="right">

| 항목 | 내용 |
|---|---|
| AAS idShort | `BatchHeatTreatmentFurnace` |
| AAS id | <sub>https://www.smart-factory.kr/ids/aas/BatchHeatTreatmentFurnace/0/0</sub> |
| 자산 종류 (assetKind) | Type |
| globalAssetId | <sub>https://www.smart-factory.kr/ids/asset/BatchHeatTreatmentFurnace/0/0</sub> |
| 설명 | 배치형 열처리로 타입 참조모델. 제품 인증이나 실제 측정 데이터가 아닌 예시입니다. |
| 서브모델 | 8개 |
| 전체 요소 | 567개 |

## 서브모델 한눈에 보기

| # | 서브모델 | 요소 수 | semanticId |
|:-:|---|--:|---|
| 1 | [Nameplate](#sm-1) | 15 | <sub>https://admin-shell.io/idta/nameplate/3/0/Nameplate</sub> |
| 2 | [HandoverDocumentation](#sm-2) | 73 | <sub>0173-1#01-AHF578#003</sub> |
| 3 | [TechnicalData](#sm-3) | 104 | <sub>0173-1#01-AHX837#002</sub> |
| 4 | [OperationalData](#sm-4) | 59 | <sub>https://www.smart-factory.kr/ids/sm/BatchHeatTreatmentFurnace/OperationalData/1/0</sub> |
| 5 | [TimeSeries](#sm-5) | 122 | <sub>https://admin-shell.io/idta/TimeSeries/1/1</sub> |
| 6 | [ProcessParameters](#sm-6) | 55 | <sub>https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0</sub> |
| 7 | [PredictiveMaintenance](#sm-7) | 79 | <sub>https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0</sub> |
| 8 | [ProcessVariablesForManufacturingKPICalculation](#sm-8) | 60 | <sub>https://admin-shell.io/idta/SubmodelTemplate/ProcessVariablesForManufacturingKPICalculati…</sub> |

## 서브모델 상세

각 서브모델 이름을 누르면 펼쳐집니다. **굵은 글씨**는 하위 요소가 있는 묶음입니다.

<a id="sm-1"></a>
<details>
<summary><b>1. Nameplate</b> — 요소 15개</summary>

> 제품 명판(제조사와 제품을 식별하는 표기)의 정보를 담는 서브모델임. 제조사·제품명·제품 유형·주문 코드 등을 확인할 때 사용하는 정보임.

semanticId: `https://admin-shell.io/idta/nameplate/3/0/Nameplate`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| URIOfTheProduct | 속성 | https://www.smart-factory.kr/ids/asset/BatchHeatTreatmentFurnace/0/0 | <sub>0112/2///61987#ABN590#002</sub> |
| ManufacturerName | 다국어 속성 | ExampleCompany | <sub>0112/2///61987#ABA565#009</sub> |
| ManufacturerProductDesignation | 다국어 속성 | ExampleCompany Batch Atmosphere Heat Treatment Furnace | <sub>0112/2///61987#ABA567#009</sub> |
| **AddressInformation** | 묶음 (5) |  | <sub>https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/Address…</sub> |
| &nbsp;&nbsp;&nbsp;└ Company | 다국어 속성 | ExampleCompany | <sub>0173-1#02-AAW001#001</sub> |
| &nbsp;&nbsp;&nbsp;└ NationalCode | 다국어 속성 | KR | <sub>0173-1#02-AAO134#002</sub> |
| &nbsp;&nbsp;&nbsp;└ CityTown | 다국어 속성 | Example City | <sub>0173-1#02-AAO132#002</sub> |
| &nbsp;&nbsp;&nbsp;└ Street | 다국어 속성 | Example Industrial Road | <sub>0173-1#02-AAO128#002</sub> |
| &nbsp;&nbsp;&nbsp;└ Zipcode | 다국어 속성 | 00000 | <sub>0173-1#02-AAO129#002</sub> |
| ManufacturerProductRoot | 다국어 속성 | Heat treatment furnace | <sub>0112/2///61360_7#AAS011#001</sub> |
| ManufacturerProductFamily | 다국어 속성 | Batch atmosphere furnace | <sub>0112/2///61987#ABP464#002</sub> |
| ManufacturerProductType | 속성 | BHF-1200 | <sub>0112/2///61987#ABA300#008</sub> |
| OrderCodeOfManufacturer | 속성 | BHF-1200-ORD | <sub>0112/2///61987#ABA950#008</sub> |
| ProductArticleNumberOfManufacturer | 속성 | BHF-1200-ART | <sub>0112/2///61987#ABA581#007</sub> |
| CompanyLogo | 파일 | /aasx/files/logo/CompanyLogo.svg | <sub>0112/2///61987#ABP463#001</sub> |

</details>

<a id="sm-2"></a>
<details>
<summary><b>2. HandoverDocumentation</b> — 요소 73개</summary>

> 산업 장비 제조사가 운영자에게 문서를 인계할 때 필요한 문서 식별·분류·버전 정보를 담는 서브모델임.

semanticId: `0173-1#01-AHF578#003`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Documents** | 목록 (3) |  | <sub>0173-1#02-ABI500#003</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | https://example.com/bhf/documents | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | BHF-TD-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | TD | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Technical specification | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | BHF reference document types (project-specific) | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | en | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 0.0.1 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Technical specification | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Illustrative reference-model documentation for a batch atmosphere heat treatmen… | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-09-14 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | InReview | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany (fictional example) | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/BHF_TechnicalSpecification.html | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | https://example.com/bhf/documents | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | BHF-GUIDE-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | GUIDE | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | AAS reference model guidance | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | BHF reference document types (project-specific) | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | en | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 0.0.1 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | AAS reference model guidance | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Illustrative reference-model documentation for a batch atmosphere heat treatmen… | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-09-14 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | InReview | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany (fictional example) | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/BHF_Guidance.html | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI500#003/0173-1#01-AHF579#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentIds** | 목록 (1) |  | <sub>0173-1#02-ABI501#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI501#003/0173-1#01-AHF580#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentDomainId | 속성 | https://example.com/bhf/documents | <sub>0173-1#02-ABH994#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIdentifier | 속성 | BHF-MAINT-001 | <sub>0173-1#02-AAO099#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DocumentIsPrimary | 속성 | true | <sub>0173-1#02-ABH995#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentClassifications** | 목록 (1) |  | <sub>0173-1#02-ABI502#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (3) |  | <sub>0173-1#02-ABI502#003/0173-1#01-AHF581#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassId | 속성 | MAINT | <sub>0173-1#02-ABH996#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassName | 다국어 속성 | Predictive maintenance example | <sub>0173-1#02-ABJ219#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | BHF reference document types (project-specific) | <sub>0173-1#02-ABH997#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DocumentVersions** | 목록 (1) |  | <sub>0173-1#02-ABI503#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>0173-1#02-ABI503#003/0173-1#01-AHF582#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Language** | 목록 (1) |  | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 속성 | en | <sub>0173-1#02-AAN468#008</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Version | 속성 | 0.0.1 | <sub>0173-1#02-AAP003#005</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Title | 다국어 속성 | Predictive maintenance example | <sub>0173-1#02-ABG940#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Illustrative reference-model documentation for a batch atmosphere heat treatmen… | <sub>0173-1#02-AAN466#004</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusSetDate | 속성 | 2026-09-14 | <sub>0173-1#02-ABI000#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StatusValue | 속성 | InReview | <sub>0173-1#02-ABI001#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationShortName | 속성 | ExampleCompany | <sub>https://api.eclass-cdp.com/0173-1-02-ABI002-003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OrganizationOfficialName | 속성 | ExampleCompany (fictional example) | <sub>0173-1#02-ABI004#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **DigitalFiles** | 목록 (1) |  | <sub>0173-1#02-ABK126#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└  | 파일 | /aasx/files/BHF_MaintenanceExample.html | <sub>0173-1#02-ABK126#002</sub> |

</details>

<a id="sm-3"></a>
<details>
<summary><b>3. TechnicalData</b> — 요소 104개</summary>

> 장비의 기술 사양과 관련 제품 분류를 담는 서브모델임. 처리 능력·온도·가스·챔버 치수·전원·안전 기능의 사양을 확인할 때 사용하는 정보임.

semanticId: `0173-1#01-AHX837#002`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **GeneralInformation** | 묶음 (6) |  | <sub>0173-1#02-ABK161#002/0173-1#01-AHX838#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerName | 속성 | ExampleCompany | <sub>0173-1#02-AAO677#004</sub> |
| &nbsp;&nbsp;&nbsp;└ CompanyLogo | 파일 | /aasx/files/logo/CompanyLogo.svg | <sub>0173-1#02-ABI776#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerProductDesignation | 다국어 속성 | ExampleCompany Batch Atmosphere Heat Treatment Furnace | <sub>0173-1#02-AAW338#003</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerArticleNumber | 속성 | BHF-1200-ART | <sub>0173-1#02-AAO676#005</sub> |
| &nbsp;&nbsp;&nbsp;└ ManufacturerOrderCode | 속성 | BHF-1200-ORD | <sub>0173-1#02-AAO227#004</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProductImages** | 목록 (1) |  | <sub>0173-1#02-ABM220#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>0173-1#02-ABM220#001/0173-1#01-AHY911#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageFile | 파일 | /aasx/files/images/BATCHFURNACE_ProductImage.png | <sub>0173-1#02-ABK291#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ImageNote | 다국어 속성 | Side view of ExampleCompany batch Chamber furnace | <sub>0173-1#02-ABL423#001</sub> |
| **ProductClassifications** | 목록 (1) |  | <sub>0173-1#02-ABK162#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (6) |  | <sub>0173-1#02-ABK162#002/0173-1#01-AHX839#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystem | 속성 | ECLASS | <sub>0173-1#02-ABL424#001</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemVersion | 속성 | 16.0 | <sub>0173-1#02-AAR710#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ClassificationSystemUrl | 속성 | https://eclass.eu/en/eclass-standard/search-content | <sub>https://admin-shell.io/IDTA/TechnicalData/ProductClassifications/Prod…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassId | 속성 | 0173-1#01-AKL340#010 | <sub>0173-1#02-ABG776#003</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassCodedName | 속성 | 36-08-01-00 | <sub>0173-1#02-ABK128#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductClassName | 다국어 속성 | Chamber furnace | <sub>0173-1#02-ABK273#002</sub> |
| **TechnicalPropertyAreas** | 목록 (6) |  | <sub>0173-1#02-ABK163#002</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FurnaceCommonSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/FurnaceCommonSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessAndMaterialSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ProcessAndMaterialSpecifications/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentProcessType | 속성 | Carburizing / hardening / tempering (batch atmosphere) | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentProcessType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceType | 속성 | Sealed quench batch furnace (integral quench) | <sub>https://www.smart-factory.kr/ids/cd/FurnaceType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationType | 속성 | Batch | <sub>https://www.smart-factory.kr/ids/cd/OperationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkpieceMaterialType | 속성 | Alloy and carbon steel parts (gears, shafts, fasteners) | <sub>https://www.smart-factory.kr/ids/cd/WorkpieceMaterialType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **InstallationSpecifications** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/InstallationSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SystemConfiguration | 속성 | Batch atmosphere furnace with recirculation fan, controlled endothermic atmosph… | <sub>https://www.smart-factory.kr/ids/cd/SystemConfiguration/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ InstallationType | 속성 | Floor-mounted refractory-lined chamber with front charge door and quench vestib… | <sub>https://www.smart-factory.kr/ids/cd/InstallationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NetWeight | 속성 | 38000 | <sub>https://www.smart-factory.kr/ids/cd/NetWeight/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HeatTreatmentCapacityAndProductionSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentCapacityAndProductio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **LoadAndCycleSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/LoadAndCycleSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxChargeWeightPerBatch | 속성 | 1500 | <sub>https://www.smart-factory.kr/ids/cd/MaxChargeWeightPerBatch/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProductionCapacity | 속성 | 4.5 | <sub>https://www.smart-factory.kr/ids/cd/ProductionCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CyclesPerDay | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/CyclesPerDay/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BatchCycleTime | 속성 | PT6H | <sub>https://www.smart-factory.kr/ids/cd/BatchCycleTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductQualitySpecifications** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/ProductQualitySpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetEffectiveCaseDepth | 속성 | 0.8 | <sub>https://www.smart-factory.kr/ids/cd/TargetEffectiveCaseDepth/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSurfaceHardness | 범위 | 58 ~ 62 | <sub>https://www.smart-factory.kr/ids/cd/TargetSurfaceHardness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ApplicableWorkpieceRange | 속성 | Gears, shafts, bearings, fasteners, tooling steels | <sub>https://www.smart-factory.kr/ids/cd/ApplicableWorkpieceRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **TemperatureAndAtmosphereSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/TemperatureAndAtmosphereSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **AtmosphereSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceAtmosphereType | 속성 | Endothermic gas (RX gas) with nitrogen carrier | <sub>https://www.smart-factory.kr/ids/cd/FurnaceAtmosphereType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetCarbonPotential | 속성 | 0.90 | <sub>https://www.smart-factory.kr/ids/cd/TargetCarbonPotential/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CarbonPotentialRange | 범위 | 0.20 ~ 1.20 | <sub>https://www.smart-factory.kr/ids/cd/CarbonPotentialRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereGasFlowRate | 속성 | 20 | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereGasFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereControlType | 속성 | Carbon potential control via oxygen (lambda) probe | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereControlType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ThermalSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxOperatingTemperature | 속성 | 1000 | <sub>https://www.smart-factory.kr/ids/cd/MaxOperatingTemperature/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperatingTemperatureRange | 범위 | 150 ~ 1000 | <sub>https://www.smart-factory.kr/ids/cd/OperatingTemperatureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperatureUniformity | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/TemperatureUniformity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureUniformityClass | 속성 | AMS 2750G Class 2 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureUniformityClass…</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ChamberAndDimensionSystem** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/ChamberAndDimensionSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ChamberConstructionSpecifications** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/ChamberConstructionSpecifications…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChamberType | 속성 | Rectangular refractory-lined batch heating chamber | <sub>https://www.smart-factory.kr/ids/cd/ChamberType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChamberLiningMaterial | 속성 | Ceramic fiber and firebrick lining with heat-resistant alloy retort | <sub>https://www.smart-factory.kr/ids/cd/ChamberLiningMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceDoorType | 속성 | Vertical-lift atmosphere-sealed front door | <sub>https://www.smart-factory.kr/ids/cd/FurnaceDoorType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WorkingEnvelopeSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/WorkingEnvelopeSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ UsableChamberVolume | 속성 | 0.72 | <sub>https://www.smart-factory.kr/ids/cd/UsableChamberVolume/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkZoneLength | 속성 | 1200 | <sub>https://www.smart-factory.kr/ids/cd/WorkZoneLength/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkZoneWidth | 속성 | 800 | <sub>https://www.smart-factory.kr/ids/cd/WorkZoneWidth/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkZoneHeight | 속성 | 750 | <sub>https://www.smart-factory.kr/ids/cd/WorkZoneHeight/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **InstallationEnvelopeSpecifications** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/InstallationEnvelopeSpecification…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsHeight | 속성 | 3200 | <sub>https://www.smart-factory.kr/ids/cd/DimensionsHeight/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsWidth | 속성 | 2600 | <sub>https://www.smart-factory.kr/ids/cd/DimensionsWidth/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DimensionsDepth | 속성 | 5200 | <sub>https://www.smart-factory.kr/ids/cd/DimensionsDepth/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoundPowerLevel | 속성 | 76 | <sub>https://www.smart-factory.kr/ids/cd/SoundPowerLevel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HeatingAndQuenchingSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatingAndQuenchingSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **HeatingSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatingSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatingMethod | 속성 | Gas-fired radiant tube heating (electric resistance heating optional) | <sub>https://www.smart-factory.kr/ids/cd/HeatingMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatingPowerRating | 속성 | 300 | <sub>https://www.smart-factory.kr/ids/cd/HeatingPowerRating/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatingZoneCount | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/HeatingZoneCount/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereCirculationFanType | 속성 | Top-mounted high-temperature recirculation fan | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereCirculationFanType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CirculationFanFlowRate | 속성 | 12000 | <sub>https://www.smart-factory.kr/ids/cd/CirculationFanFlowRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **QuenchingSpecifications** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/QuenchingSpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchType | 속성 | Integral agitated oil quench | <sub>https://www.smart-factory.kr/ids/cd/QuenchType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchMedium | 속성 | Fast quench oil | <sub>https://www.smart-factory.kr/ids/cd/QuenchMedium/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchTankCapacity | 속성 | 8000 | <sub>https://www.smart-factory.kr/ids/cd/QuenchTankCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchOilTemperatureRange | 범위 | 60 ~ 120 | <sub>https://www.smart-factory.kr/ids/cd/QuenchOilTemperatureRange/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChargeLoadingMethod | 속성 | Front charge car with load table | <sub>https://www.smart-factory.kr/ids/cd/ChargeLoadingMethod/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **** | 묶음 (1) |  | <sub>0173-1#02-ABL358#002/0173-1#01-AHX773#002</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ElectricalAndSafetySystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetySystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PowerSupplySpecifications** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplySpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedVoltage | 범위 | 380 ~ 415 | <sub>https://www.smart-factory.kr/ids/cd/RatedVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupplyPhase | 속성 | 3-phase | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplyPhase/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerSupplyFrequency | 속성 | 50/60 | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplyFrequency/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RatedPower | 속성 | 320 | <sub>https://www.smart-factory.kr/ids/cd/RatedPower/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaxRunningCurrent | 속성 | 520 | <sub>https://www.smart-factory.kr/ids/cd/MaxRunningCurrent/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LeakageBreakerCapacity | 속성 | 630 | <sub>https://www.smart-factory.kr/ids/cd/LeakageBreakerCapacity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **SafetySpecifications** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/SafetySpecifications/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SupportedSafetyFunctions | 속성 | Emergency stop, over-temperature cutout, atmosphere burn-off pilot, door interl… | <sub>https://www.smart-factory.kr/ids/cd/SupportedSafetyFunctions/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereBurnOffSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereBurnOffSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DoorInterlockSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/DoorInterlockSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopSupported/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OverTemperatureProtectionSupported | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/OverTemperatureProtectionSupporte…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IPRating | 속성 | IP54 | <sub>https://www.smart-factory.kr/ids/cd/IPRating/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GroundingRequired | 속성 | true | <sub>https://www.smart-factory.kr/ids/cd/GroundingRequired/1/0</sub> |
| **FurtherInformation** | 묶음 (2) |  | <sub>0173-1#02-ABK164#002</sub> |
| &nbsp;&nbsp;&nbsp;└ TextStatement | 다국어 속성 | Reference model examples only. Values do not certify a real furnace or prescrib… | <sub>0173-1#02-ABK134#002</sub> |
| &nbsp;&nbsp;&nbsp;└ ValidDate | 속성 | 2026-09-14 | <sub>0173-1#02-ABL775#001</sub> |

</details>

<a id="sm-4"></a>
<details>
<summary><b>4. OperationalData</b> — 요소 59개</summary>

> 배치형 분위기 열처리로의 제어기에서 읽거나 계산한 현재 운전·감시 값을 담는 서브모델임. 이 참조모델의 값은 실제 장비의 측정값이 아닌 예시임.

semanticId: `https://www.smart-factory.kr/ids/sm/BatchHeatTreatmentFurnace/OperationalData/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **DeviceOperationSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/DeviceOperationSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **OperatingStateMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/OperatingStateMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Batch heat treatment | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentPhase | 속성 | Carburizing soak | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentPhase/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **BatchAndHistoryMonitoring** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/BatchAndHistoryMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ActiveProcessId | 속성 | BHF-P-001 | <sub>https://www.smart-factory.kr/ids/cd/ActiveProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentBatchId | 속성 | BATCH-2026-0617-03 | <sub>https://www.smart-factory.kr/ids/cd/CurrentBatchId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentRecipeId | 속성 | RECIPE-BHF-001 | <sub>https://www.smart-factory.kr/ids/cd/CurrentRecipeId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativeBatchCount | 속성 | 1280 | <sub>https://www.smart-factory.kr/ids/cd/CumulativeBatchCount/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CumulativeOperatingHours | 속성 | 24800 | <sub>https://www.smart-factory.kr/ids/cd/CumulativeOperatingHours/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationStartTimestamp | 속성 | 2026-06-17T04:00:00Z | <sub>https://www.smart-factory.kr/ids/cd/OperationStartTimestamp/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdateTimestamp | 속성 | 2026-06-17T08:20:30Z | <sub>https://www.smart-factory.kr/ids/cd/LastUpdateTimestamp/1/0</sub> |
| **HeatTreatmentProcessSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentProcessSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **TemperatureMonitoring** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/TemperatureMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureActual | 속성 | 928 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureSetpoint | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone1TemperatureActual | 속성 | 926 | <sub>https://www.smart-factory.kr/ids/cd/Zone1TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone2TemperatureActual | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/Zone2TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone3TemperatureActual | 속성 | 929 | <sub>https://www.smart-factory.kr/ids/cd/Zone3TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperatureDeviationActual | 속성 | 4 | <sub>https://www.smart-factory.kr/ids/cd/TemperatureDeviationActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatUpRateActual | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/HeatUpRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ProcessProgressAndQualityMonitoring** | 묶음 (5) |  | <sub>https://www.smart-factory.kr/ids/cd/ProcessProgressAndQualityMonitori…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoakingTimeElapsed | 속성 | PT1H30M | <sub>https://www.smart-factory.kr/ids/cd/SoakingTimeElapsed/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CurrentProcessStep | 속성 | Carburizing | <sub>https://www.smart-factory.kr/ids/cd/CurrentProcessStep/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentThroughputRate | 속성 | 12 | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentThroughputRate/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HardnessConformityIndex | 속성 | 0.96 | <sub>https://www.smart-factory.kr/ids/cd/HardnessConformityIndex/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RejectPartRate | 속성 | 1.5 | <sub>https://www.smart-factory.kr/ids/cd/RejectPartRate/1/0</sub> |
| **AtmosphereAndQuenchSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereAndQuenchSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AtmosphereMonitoring** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CarbonPotentialActual | 속성 | 0.88 | <sub>https://www.smart-factory.kr/ids/cd/CarbonPotentialActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OxygenProbeVoltage | 속성 | 1120 | <sub>https://www.smart-factory.kr/ids/cd/OxygenProbeVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereGasFlowActual | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereGasFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmospherePressureActual | 속성 | 3 | <sub>https://www.smart-factory.kr/ids/cd/AtmospherePressureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFanRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFanRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFanCurrentActual | 속성 | 42 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFanCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **QuenchAndChargeMonitoring** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/QuenchAndChargeMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchOilTemperatureActual | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/QuenchOilTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchAgitatorRunState | 속성 | Stopped | <sub>https://www.smart-factory.kr/ids/cd/QuenchAgitatorRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChargeWeightActual | 속성 | 1450 | <sub>https://www.smart-factory.kr/ids/cd/ChargeWeightActual/1/0</sub> |
| **ProtectionAndSafetyStateSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ProtectionAndSafetyStateSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ThermalAndAtmosphereProtectionMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalAndAtmosphereProtectionMon…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OverTemperatureAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/OverTemperatureAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereFlowAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereFlowAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BurnOffFlameStatus | 속성 | Ignited | <sub>https://www.smart-factory.kr/ids/cd/BurnOffFlameStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FurnaceAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AccessAndStopProtectionMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/AccessAndStopProtectionMonitoring…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DoorInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/DoorInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| **ElectricalAndSafetyConditionSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ElectricalAndSafetyConditionSyste…</sub> |
| &nbsp;&nbsp;&nbsp;└ **PowerSupplyMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/PowerSupplyMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 245000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AccessAndOperationSafetyMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/AccessAndOperationSafetyMonitorin…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ GuardInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/GuardInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SafetyCoverState | 속성 | Closed | <sub>https://www.smart-factory.kr/ids/cd/SafetyCoverState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |

</details>

<a id="sm-5"></a>
<details>
<summary><b>5. TimeSeries</b> — 요소 122개</summary>

> 시간 순서로 기록되는 운전 데이터를 담는 서브모델임. 기록 구조와 함께 외부 파일·외부 조회 서비스·AAS 내부 저장 방식의 시계열을 찾고 해석하는 데 사용하는 정보임.

semanticId: `https://admin-shell.io/idta/TimeSeries/1/1`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Metadata** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Batch heat treatment furnace operation time series | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Time series data for batch heat treatment furnace operation values | <sub>https://admin-shell.io/idta/TimeSeries/Metadata/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **Record** | 묶음 (6) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-17T08:15:30Z | <sub>https://www.smart-factory.kr/ids/cd/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordDeviceOperationSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordDeviceOperationSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordOperatingStateMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordOperatingStateMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Batch heat treatment | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentPhase | 속성 | Carburizing soak | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentPhase/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordHeatTreatmentProcessSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordHeatTreatmentProcessSystem/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordTemperatureMonitoring** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordTemperatureMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureActual | 속성 | 928 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureSetpoint | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone1TemperatureActual | 속성 | 926 | <sub>https://www.smart-factory.kr/ids/cd/Zone1TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone2TemperatureActual | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/Zone2TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone3TemperatureActual | 속성 | 929 | <sub>https://www.smart-factory.kr/ids/cd/Zone3TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperatureDeviationActual | 속성 | 4 | <sub>https://www.smart-factory.kr/ids/cd/TemperatureDeviationActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatUpRateActual | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/HeatUpRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAtmosphereAndQuenchSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAtmosphereAndQuenchSystem/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAtmosphereMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAtmosphereMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CarbonPotentialActual | 속성 | 0.88 | <sub>https://www.smart-factory.kr/ids/cd/CarbonPotentialActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OxygenProbeVoltage | 속성 | 1120 | <sub>https://www.smart-factory.kr/ids/cd/OxygenProbeVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereGasFlowActual | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereGasFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFanCurrentActual | 속성 | 42 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFanCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordQuenchAndChargeMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordQuenchAndChargeMonitoring/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchOilTemperatureActual | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/QuenchOilTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChargeWeightActual | 속성 | 1450 | <sub>https://www.smart-factory.kr/ids/cd/ChargeWeightActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordProtectionAndSafetyStateSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordProtectionAndSafetyStateSys…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordThermalAndAtmosphereProtectionMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordThermalAndAtmosphereProtect…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OverTemperatureAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/OverTemperatureAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FurnaceAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAccessAndStopProtectionMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAccessAndStopProtectionMoni…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DoorInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/DoorInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordElectricalAndSafetyConditionSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordElectricalAndSafetyConditio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordPowerSupplyMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordPowerSupplyMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 245000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAccessAndOperationSafetyMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAccessAndOperationSafetyMon…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |
| **Segments** | 묶음 (3) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **ExternalSegment** | 묶음 (12) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/ExternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Furnace historian file data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Furnace time series data stored in external CSV file | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 86400 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T00:00:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T23:59:59Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT24H | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-18T00:00:05Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ File | 파일 | /aasx/files/timeseries/BHF_TS_20260617.csv | <sub>https://admin-shell.io/idta/TimeSeries/File/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Blob | 바이너리 | application/gzip | <sub>https://admin-shell.io/idta/TimeSeries/Blob/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **LinkedSegment** | 묶음 (12) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/LinkedSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Furnace historian API data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Furnace time series data queried from external historian API | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 86400 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T00:00:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T23:59:59Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT24H | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-18T00:00:05Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Endpoint | 속성 | https://historian.example.com/api/timeseries | <sub>https://admin-shell.io/idta/TimeSeries/Endpoint/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Query | 속성 | assetId=BHF-SN-2026-0001&from=2026-06-17T00:00:00Z&to=2026-06-18T00:00:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Query/1/1</sub> |
| &nbsp;&nbsp;&nbsp;└ **InternalSegment** | 묶음 (11) |  | <sub>https://admin-shell.io/idta/TimeSeries/Segments/InternalSegment/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Name | 다국어 속성 | Recent furnace operation data | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 다국어 속성 | Recent furnace operation records stored directly in AAS | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Description/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecordCount | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartTime | 속성 | 2026-06-17T08:15:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndTime | 속성 | 2026-06-17T08:15:00Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Duration | 속성 | PT1S | <sub>https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingInterval | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SamplingRate | 속성 | 1 | <sub>https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ State | 속성 | completed | <sub>https://admin-shell.io/idta/TimeSeries/Segment/State/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ LastUpdate | 속성 | 2026-06-17T08:15:01Z | <sub>https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Records** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/TimeSeries/Records/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **Record00000** | 묶음 (6) |  | <sub>https://admin-shell.io/idta/TimeSeries/Record/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Time | 속성 | 2026-06-17T08:15:00Z | <sub>https://www.smart-factory.kr/ids/cd/UtcTime/1/1</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordDeviceOperationSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordDeviceOperationSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordOperatingStateMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordOperatingStateMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DeviceRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/DeviceRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Batch heat treatment | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentPhase | 속성 | Carburizing soak | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentPhase/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatTreatmentRunState | 속성 | Running | <sub>https://www.smart-factory.kr/ids/cd/HeatTreatmentRunState/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordHeatTreatmentProcessSystem** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordHeatTreatmentProcessSystem/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordTemperatureMonitoring** | 묶음 (7) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordTemperatureMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureActual | 속성 | 928 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceTemperatureSetpoint | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/FurnaceTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone1TemperatureActual | 속성 | 926 | <sub>https://www.smart-factory.kr/ids/cd/Zone1TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone2TemperatureActual | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/Zone2TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Zone3TemperatureActual | 속성 | 929 | <sub>https://www.smart-factory.kr/ids/cd/Zone3TemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperatureDeviationActual | 속성 | 4 | <sub>https://www.smart-factory.kr/ids/cd/TemperatureDeviationActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatUpRateActual | 속성 | 6 | <sub>https://www.smart-factory.kr/ids/cd/HeatUpRateActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAtmosphereAndQuenchSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAtmosphereAndQuenchSystem/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAtmosphereMonitoring** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAtmosphereMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CarbonPotentialActual | 속성 | 0.88 | <sub>https://www.smart-factory.kr/ids/cd/CarbonPotentialActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OxygenProbeVoltage | 속성 | 1120 | <sub>https://www.smart-factory.kr/ids/cd/OxygenProbeVoltage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereGasFlowActual | 속성 | 18 | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereGasFlowActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RecirculationFanCurrentActual | 속성 | 42 | <sub>https://www.smart-factory.kr/ids/cd/RecirculationFanCurrentActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordQuenchAndChargeMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordQuenchAndChargeMonitoring/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchOilTemperatureActual | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/QuenchOilTemperatureActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChargeWeightActual | 속성 | 1450 | <sub>https://www.smart-factory.kr/ids/cd/ChargeWeightActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordProtectionAndSafetyStateSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordProtectionAndSafetyStateSys…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordThermalAndAtmosphereProtectionMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordThermalAndAtmosphereProtect…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OverTemperatureAlarmStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/OverTemperatureAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ FurnaceAlarmStatus | 속성 | None | <sub>https://www.smart-factory.kr/ids/cd/FurnaceAlarmStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAccessAndStopProtectionMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAccessAndStopProtectionMoni…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DoorInterlockStatus | 속성 | Locked | <sub>https://www.smart-factory.kr/ids/cd/DoorInterlockStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProtectionStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/ProtectionStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordElectricalAndSafetyConditionSystem** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordElectricalAndSafetyConditio…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordPowerSupplyMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordPowerSupplyMonitoring/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PowerConsumptionActual | 속성 | 245000 | <sub>https://www.smart-factory.kr/ids/cd/PowerConsumptionActual/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ElectricalSupplyStatus | 속성 | Normal | <sub>https://www.smart-factory.kr/ids/cd/ElectricalSupplyStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **RecordAccessAndOperationSafetyMonitoring** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/RecordAccessAndOperationSafetyMon…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EmergencyStopStatus | 속성 | Released | <sub>https://www.smart-factory.kr/ids/cd/EmergencyStopStatus/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationPermittedState | 속성 | Permitted | <sub>https://www.smart-factory.kr/ids/cd/OperationPermittedState/1/0</sub> |

</details>

<a id="sm-6"></a>
<details>
<summary><b>6. ProcessParameters</b> — 요소 55개</summary>

> 제품 제조에 필요한 공정 조건을 구조적으로 정리하는 서브모델임.

semanticId: `https://admin-shell-io/idta/SubmodelTemplate/ProcessParameters/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **Processes** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Processes/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **Process__00__** | 묶음 (8) |  | <sub>https://admin-shell.io/idta/ProcessParameters/Process/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessId | 속성 | BHF-P-001 | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessName | 속성 | Batch atmosphere carburizing and quenching | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessDescription | 다국어 속성 | Process parameters for batch atmosphere heat treatment furnace carburizing-hard… | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PlannedProcessTime | 속성 | PT6H | <sub>https://admin-shell.io/idta/ProcessParameters/PlannedProcessTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProductParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProductParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WorkpieceRequirements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/WorkpieceRequirements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MaterialRequirements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/MaterialRequirements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkpieceMaterial | 속성 | Alloy steel (SCM420 / 20MnCr5) | <sub>https://www.smart-factory.kr/ids/cd/WorkpieceMaterial/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkpieceType | 속성 | Automotive transmission gears | <sub>https://www.smart-factory.kr/ids/cd/WorkpieceType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **LoadAndQualityTargets** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/LoadAndQualityTargets/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ChargeWeightTarget | 속성 | 1500 | <sub>https://www.smart-factory.kr/ids/cd/ChargeWeightTarget/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetSurfaceHardness | 속성 | 60 | <sub>https://www.smart-factory.kr/ids/cd/TargetSurfaceHardness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetEffectiveCaseDepth | 속성 | 0.8 | <sub>https://www.smart-factory.kr/ids/cd/TargetEffectiveCaseDepth/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TargetProductionQuantity | 속성 | 480 | <sub>https://www.smart-factory.kr/ids/cd/TargetProductionQuantity/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessParameters** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ThermalRecipe** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/ThermalRecipe/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **SequenceAndTemperatureTargets** | 묶음 (8) |  | <sub>https://www.smart-factory.kr/ids/cd/SequenceAndTemperatureTargets/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationRecipeId | 속성 | RECIPE-BHF-001 | <sub>https://www.smart-factory.kr/ids/cd/OperationRecipeId/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OperationMode | 속성 | Batch heat treatment | <sub>https://www.smart-factory.kr/ids/cd/OperationMode/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ProcessStepSequence | 속성 | Charge-Purge-HeatUp-Carburize-Diffuse-Quench-Temper | <sub>https://www.smart-factory.kr/ids/cd/ProcessStepSequence/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoakingTemperatureSetpoint | 속성 | 930 | <sub>https://www.smart-factory.kr/ids/cd/SoakingTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ SoakingTimeSetpoint | 속성 | PT2H | <sub>https://www.smart-factory.kr/ids/cd/SoakingTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ HeatUpRateSetpoint | 속성 | 8 | <sub>https://www.smart-factory.kr/ids/cd/HeatUpRateSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperingTemperatureSetpoint | 속성 | 180 | <sub>https://www.smart-factory.kr/ids/cd/TemperingTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ TemperingTimeSetpoint | 속성 | PT2H | <sub>https://www.smart-factory.kr/ids/cd/TemperingTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **AtmosphereQuenchAndProtectionTargets** | 묶음 (6) |  | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereQuenchAndProtectionTarg…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ CarbonPotentialSetpoint | 속성 | 0.90 | <sub>https://www.smart-factory.kr/ids/cd/CarbonPotentialSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AtmosphereGasFlowSetpoint | 속성 | 20 | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereGasFlowSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchOilTemperatureSetpoint | 속성 | 80 | <sub>https://www.smart-factory.kr/ids/cd/QuenchOilTemperatureSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchDelaySetpoint | 속성 | PT30S | <sub>https://www.smart-factory.kr/ids/cd/QuenchDelaySetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ QuenchTimeSetpoint | 속성 | PT10M | <sub>https://www.smart-factory.kr/ids/cd/QuenchTimeSetpoint/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ OverTemperatureAlarmThreshold | 속성 | 970 | <sub>https://www.smart-factory.kr/ids/cd/OverTemperatureAlarmThreshold/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **AtmosphereConsumables** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereConsumables/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **AtmosphereFormationGases** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/AtmosphereFormationGases/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EndothermicGasConsumable | 속성 | ENDOGAS-RX-001 | <sub>https://www.smart-factory.kr/ids/cd/EndothermicGasConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EnrichingGasConsumable | 속성 | PROPANE-ENRICH-001 | <sub>https://www.smart-factory.kr/ids/cd/EnrichingGasConsumable/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **PurgeGases** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/PurgeGases/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ NitrogenPurgeUtility | 속성 | NITROGEN-001 | <sub>https://www.smart-factory.kr/ids/cd/NitrogenPurgeUtility/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ResourceParameters** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ResourceParameters/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **FurnaceResourceRequirements** | 묶음 (2) |  | <sub>https://www.smart-factory.kr/ids/cd/FurnaceResourceRequirements/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **MeasurementResources** | 묶음 (3) |  | <sub>https://www.smart-factory.kr/ids/cd/MeasurementResources/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredTemperatureSensor | 속성 | Thermocouple01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredTemperatureSensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredCarbonProbe | 속성 | OxygenProbe01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredCarbonProbe/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredAtmosphereFlowSensor | 속성 | FlowSensor01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredAtmosphereFlowSensor/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ActuationResources** | 묶음 (4) |  | <sub>https://www.smart-factory.kr/ids/cd/ActuationResources/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredRecirculationFan | 속성 | RecirculationFan01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredRecirculationFan/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredHeatingSystem | 속성 | HeatingSystem01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredHeatingSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredQuenchSystem | 속성 | QuenchSystem01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredQuenchSystem/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ RequiredChargeCar | 속성 | ChargeCar01 | <sub>https://www.smart-factory.kr/ids/cd/RequiredChargeCar/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **ProcessBoM** | 묶음 (1) |  | <sub>https://admin-shell.io/idta/ProcessParameters/ProcessBoM/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **BatchMaterialInputs** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/BatchMaterialInputs/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **WorkpieceInputs** | 묶음 (1) |  | <sub>https://www.smart-factory.kr/ids/cd/WorkpieceInputs/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ WorkpieceMaterialInput | 속성 | STEEL-SCM420-001 | <sub>https://www.smart-factory.kr/ids/cd/WorkpieceMaterialInput/1/0</sub> |

</details>

<a id="sm-7"></a>
<details>
<summary><b>7. PredictiveMaintenance</b> — 요소 79개</summary>

> 예지보전(상태를 예측해 미리 정비하는 방식)에 필요한 정보를 제공하는 서브모델임. 생산라인의 하위 장치와 예지보전 소프트웨어에서 남은 수명·예측 적용 조건·모델·알림을 설명하는 데 사용함.

semanticId: `https://admin-shell.io/idta/SubmodelTemplate/PredictiveMaintenance/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **RemainingUsefulLifePrediction** | 묶음 (7) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;└ **RemainingUsefulLifetime** | 엔티티 (6) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsefulLife…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IndicationType | 속성 | operating hours | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IndicationType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DurationValue | 속성 | 9000 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DurationValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ EngineeringUnit | 속성 | h | <sub>https://admin-shell.io/idta/PredictiveMaintenance/EngineeringUnit/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartValue | 속성 | 24800 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ StartDateTime | 속성 | 2026-06-26T09:00:00+09:00 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/StartDateTime/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Description | 속성 | 대표 예측 대상은 배치형열처리로의 순환팬 베어링과 발열체임. 잔여수명 예측 시작시점의 누적 열처리로 운전시간은 24800 h이고, 순환팬 베어… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Description/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ RemainingUsfulLifeDateTime | 속성 | 2027-07-06T09:00:00+09:00 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RemainingUsfulLifeD…</sub> |
| &nbsp;&nbsp;&nbsp;└ ConfidenceInterval | 범위 | 7800 ~ 10200 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConfidenceInterval/…</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListRULBoundaryConditions** | 목록 (7) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListRULBoundaryCond…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | HeatingElementCurrentActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 320.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | A | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.07 ~ 0.07 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 250.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 22.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | -0.40 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Heating-element load-current band within which the RUL model stays valid; a sus… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | FanBearingVibrationRMS | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 7.1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | mm/s | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.10 ~ 0.10 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 2.8 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.8 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.9 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Recirculation-fan bearing vibration velocity RMS range (ISO 10816 zones A-C) ov… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | RetortWallThicknessActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 10.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | mm | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.05 ~ 0.05 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 8.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 0.6 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | -0.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Residual alloy retort/muffle (and radiant-tube) wall-thickness band; a sustaine… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (9) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | BearingTemperatureActual | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 90.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | °C | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ DriftInfoAIModel | 범위 | 0.06 ~ 0.06 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/DriftInfoAIModel/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MeanValue | 속성 | 55.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MeanValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Standarddeviation | 속성 | 7.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Standarddeviation/1…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ Skewness | 속성 | 0.7 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/Skewness/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | Fan bearing temperature window used as an alarm guard; persistent excursions ab… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (5) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | RefractoryDegradationLoadIndex | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.0 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 누적 부하·열화 진행을 종합한 지수. 예시 관측값 0.58. Valid interval: [0.0, 1.0] 1. Upper-bound sto… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (5) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | HeatingElementOxidationFactor | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 마모·부하 변동에 따른 보정 계수. 예시 관측값 1.18. Valid interval: [1.0, 1.5] 1. Upper-bound stor… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (5) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/RULCondition/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ConditionName | 속성 | ThermalLoadCorrectionFactor | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ConditionName/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ IsBoundaryConditionUsedInModel | 속성 | true | <sub>https://admin-shell.io/idta/PredictiveMaintenance/IsBoundaryCondition…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryValueRange | 속성 | 1.5 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryValueRange/…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryEngineeringUnit | 속성 | 1 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryEngineering…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ BoundaryDescription | 속성 | 마모·부하 변동에 따른 보정 계수. 예시 관측값 1.10. Valid interval: [1.0, 1.5] 1. Upper-bound stor… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/BoundaryDescription…</sub> |
| &nbsp;&nbsp;&nbsp;└ **PredictionModelInformation** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PredictionModelInfo…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelType | 속성 | ModelTypeHybrid | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelType/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ ModelDescription | 속성 | Hybrid RUL model combining a physics-based element-oxidation and fan-bearing fa… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ModelDescription/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **ListPreAlerts** | 목록 (1) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/ListPreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ **** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlerts/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertMessage | 속성 | Pre-alert: predicted remaining useful life of the furnace recirculation fan / h… | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ PreAlertValue | 속성 | 1200 | <sub>https://admin-shell.io/idta/PredictiveMaintenance/PreAlertValue/1/0</sub> |
| &nbsp;&nbsp;&nbsp;└ **AlertAfterExceedingRemainingUsableLife** | 묶음 (2) |  | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertAfterExceeding…</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ AlertMessage | 속성 | Alert: the furnace has reached the end of its remaining usable life. Stop heat … | <sub>https://admin-shell.io/idta/PredictiveMaintenance/AlertMessage/1/0</sub> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└ MaintenanceRequired | 속성 | false | <sub>https://admin-shell.io/idta/PredictiveMaintenance/MaintenanceRequired…</sub> |

</details>

<a id="sm-8"></a>
<details>
<summary><b>8. ProcessVariablesForManufacturingKPICalculation</b> — 요소 60개</summary>

> 제조 KPI(생산 성과를 나타내는 지표)를 계산할 때 사용하는 공정 변수들을 정리한 서브모델임.

semanticId: `https://admin-shell.io/idta/SubmodelTemplate/ProcessVariablesForManufacturingKPICalculation/1/0`

| idShort | 종류 | 값 | semanticId |
|---|---|---|---|
| **PlannedBusyTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#PlannedBusyTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | PBT | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT22H | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Planned busy time per shift Illustrative reporting-period value; do not sum ove… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualUnitBusyTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitBusyTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | AUBT | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT21H30M | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual unit busy time Illustrative reporting-period value; do not sum overlappi… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualProductionTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualProductionTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | APT | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT20H48M | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual production time Illustrative reporting-period value; do not sum overlapp… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualUnitProcessingTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitProcessingTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | AUPT | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT20H30M | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual unit processing time Illustrative reporting-period value; do not sum ove… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualUnitSetupTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualSetupTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | AUST | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT48M | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual unit setup time (charge loading & atmosphere purge) Illustrative reporti… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualUnitDownTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitDownTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | ADOT | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT54M | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual unit down time Illustrative reporting-period value; do not sum overlappi… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualUnitDelayTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualUnitDelayTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | ADET | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT24M | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual unit delay time Illustrative reporting-period value; do not sum overlapp… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ActualOrderExecutionTime** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ActualOrderExecutionTime</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | AOET | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT21H | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Actual order execution time Illustrative reporting-period value; do not sum ove… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **PlannedRuntimePerItem** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#PlannedRuntimePerUnit</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | PRI | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | PT45S | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Planned equivalent runtime per part: 6 h batch / 480 target parts = 45 s/part. … | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ProducedQuantity** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ProducedQuantity</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | PQ | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | 200 | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Produced quantity per shift (parts) Illustrative reporting-period value; do not… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **GoodQuantity** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#GoodQuantity</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | GQ | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | 194 | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Good quantity (parts) Illustrative reporting-period value; do not sum overlappi… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ScrapQuantity** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ScrapQuantity</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | SQ | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | 3 | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Scrap quantity (parts) Illustrative reporting-period value; do not sum overlapp… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **ReworkQuantity** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#ReworkQuantity</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | RQ | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | 3 | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Rework quantity (parts) Illustrative reporting-period value; do not sum overlap… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **GoodPart** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#GoodPart</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | GP | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | 194 | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Good parts passing inspection (parts) Illustrative reporting-period value; do n… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| **InspectedPart** | 묶음 (3) |  | <sub>http://www.w3id.org/hsu-aut/ISO22400-2#InspectedPart</sub> |
| &nbsp;&nbsp;&nbsp;└ key | 속성 | IP | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ currentValue | 속성 | 200 | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |
| &nbsp;&nbsp;&nbsp;└ comment | 다국어 속성 | Inspected parts (parts) Illustrative reporting-period value; do not sum overlap… | <sub>https://admin-shell.io/idta/ProcessVariablesForManufacturingKPICalcul…</sub> |

</details>
