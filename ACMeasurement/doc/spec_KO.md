<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: ACMeasurement    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Energy/blob/master/ACMeasurement/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **3상(L1, L2, L3) 또는 단상(L) 및 중성(N)에 대해 교류(AC)를 사용하는 전기 시스템에서 소비되는 전기 에너지를 측정하기 위한 데이터 모델입니다. 단상 측정도 수행하도록 확장된 데이터 모뎀 [THREEPHASEMEASUREMENT]의 초기 버전을 통합합니다. 전력, 주파수, 전류 및 전압과 같은 다양한 전기 측정을 위한 속성을 포함합니다.**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `activeEnergyExport[object]`: 위상당 방출되는 유효 에너지. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 활성 에너지 수출 1단계의 값      
	- `L2[number]`: 활성 에너지 수출 2단계의 값      
	- `L3[number]`: 활성 에너지 수출 3단계의 값      
- `activeEnergyImport[object]`: 수입된 유효 에너지, 즉 위상당 소비된 에너지입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 활성 에너지 가져오기 1단계의 값      
	- `L2[number]`: 활성 에너지 가져오기 2단계의 값      
	- `L3[number]`: 활성 에너지 가져오기 3단계의 값      
- `activePower[object]`: 위상당 소비되는 유효 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 유효 전력의 1단계 값      
	- `L2[number]`: 유효 전력의 2단계 값      
	- `L3[number]`: 유효 전력의 3단계 값      
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `apparentEnergyExport[object]`: 위상당 방출되는 겉보기 에너지. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 겉보기 에너지 수출의 1단계 값      
	- `L2[number]`: 겉보기 에너지 수출의 2단계 값      
	- `L3[number]`: 겉보기 에너지 수출의 3단계 값      
- `apparentEnergyImport[object]`: 수입된 겉보기 에너지, 즉 단계당 소비된 에너지. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 겉보기 에너지 수입의 1단계 값      
	- `L2[number]`: 겉보기 에너지 수입의 2단계 값      
	- `L3[number]`: 겉보기 에너지 수입의 3단계 값      
- `apparentPower[object]`: 위상당 소비되는 겉보기 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 피상 전력의 1단계 값      
	- `L2[number]`: 피상 전력의 2단계 값      
	- `L3[number]`: 피상 전력의 3상 값      
- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: 전류. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 전류의 1단계 값      
	- `L2[number]`: 전류의 2단계 값      
	- `L3[number]`: 전류의 3단계에 대한 값      
	- `N[number]`: 전류의 위상 중립 값      
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateEnergyMeteringStarted[date-time]`: ISO8601 UTC 형식의 에너지 계량 시작 날짜  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateObserved[date-time]`: ISO8601 UTC 형식으로 표시되는 이 관측의 날짜 및 시간입니다. 특정 시간 순간으로 표시하거나 ISO8601 간격으로 표시하여 `dateObservedFrom`, `dateObservedTo` 속성을 구분할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[date-time]`: 관찰 기간: ISO8601 UTC 형식의 시작 날짜 및 시간입니다. 이 속성은 강조 표시할 시간 간격에 해당하는 경우 `dateObserved` 속성과 함께 사용할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: 관찰 기간: ISO8601 UTC 형식의 종료 날짜 및 시간입니다. 이 속성은 강조 표시할 시간 간격에 해당하는 경우 `dateObserved` 속성과 함께 사용할 수 있습니다.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 이 항목에 대한 설명  - `displacementPowerFactor[object]`: 각 위상에 대한 변위 역률. 수량은 시스템의 기본 주파수를 기준으로 합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 변위 역률의 1단계 값      
	- `L2[number]`: 변위 역률의 2단계 값      
	- `L3[number]`: 변위 역률의 3단계 값      
- `frequency[number]`: 회로의 주파수입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `phaseToPhaseVoltage[object]`: 위상 간 전압. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L12[number]`: 1상~2상 전압 값      
	- `L23[number]`: 2단계에서 3단계 전압에 대한 값      
	- `L31[number]`: 3단계에서 1단계 전압에 대한 값      
- `phaseType[string]`: 위상 유형. 고유 값입니다. 열거형:'단일 위상, 세 위상'  . Model: [https://schema.org/Text](https://schema.org/Text)- `phaseVoltage[object]`: 각 상과 중성 도체 사이의 전압입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 전압의 1단계 값      
	- `L2[number]`: 전압의 2단계 값      
	- `L3[number]`: 전압의 3단계 값      
- `powerFactor[object]`: 각 단계별 역률  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 역률 1단계의 값      
	- `L2[number]`: 역률 2단계의 값      
	- `L3[number]`: 역률 3단계의 값      
- `reactiveEnergyExport[object]`: 위상당 출력되는 기본 주파수 무효 에너지입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 무효 에너지 수출의 1단계 값      
	- `L2[number]`: 무효 에너지 수출 2단계 값      
	- `L3[number]`: 무효 에너지 수출의 3단계 값      
- `reactiveEnergyImport[object]`: 수입된 기본 주파수 무효 에너지, 즉 위상당 소비된 에너지입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 무효 에너지 가져오기 1단계 값      
	- `L2[number]`: 무효 에너지 가져오기 2단계 값      
	- `L3[number]`: 무효 에너지 가져오기 3단계 값      
- `reactivePower[object]`: 기본 주파수 무효 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: 무효 전력의 1단계 값      
	- `L2[number]`: 무효 전력의 2단계 값      
	- `L3[number]`: 무효 전력의 3단계 값      
- `refDevice[array]`: 이 관측을 캡처한 디바이스 참조  . Model: [https://schema.org/URL](https://schema.org/URL)- `refTargetDevice[array]`: 측정이 수행된 디바이스 목록에 대한 참조  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `thdCurrent[object]`: 각 위상별 전류의 총 고조파 왜곡률  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: d 전류의 1단계 값      
	- `L2[number]`: 전류의 2상 값      
	- `L3[number]`: 3d 전류의 3상 값      
- `thdVoltage[object]`: 각 위상별 전압의 총 고조파 왜곡률  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: thd 전압의 1단계 값      
	- `L2[number]`: thd 전압의 2단계 값      
	- `L3[number]`: thd 전압의 3상 값      
- `totalActiveEnergyExport[number]`: 수입된 총 에너지, 즉 소비된 에너지 . 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 부여합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActiveEnergyImport[number]`: 수입된 총 에너지, 즉 소비된 에너지입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActivePower[number]`: 소비된 총 유효 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentEnergyExport[number]`: 수출된 총 에너지(피상 전력 기준). 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalApparentEnergyImport[number]`: 수입된 총 에너지, 즉 소비된 에너지(피상 전력 기준). 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentPower[number]`: 소비된 총 피상 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalDisplacementPowerFactor[number]`: 모든 위상을 포함한 변위 역률의 합계입니다. 이 수량은 시스템의 기본 주파수를 기준으로 합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalPowerFactor[number]`: 모든 단계를 포함한 역률의 합계  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalReactiveEnergyExport[number]`: 수출된 총 기본 주파수 무효 에너지입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다.  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalReactiveEnergyImport[number]`: 수입된 총 에너지, 즉 소비된 에너지(기본 주파수 무효 전력과 관련하여). 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalReactivePower[number]`: 소비된 총 무효 전력. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 제공됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 속성 유형입니다. ACMeasurement여야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `dateObserved`  - `id`  - `location`  - `phaseType`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
속성에 대한 추가 정보.  전류 및 전압과 같은 일부 속성의 경우 값은 단상(L) 또는 세 가지 다른 위상(L1, L2 및 L3)에 대한 속성이 있는 구조화된 값입니다. 다양한 전력 유형(유효, 무효 및 피상 전력)과 같은 일부 측정의 경우 모든 위상의 총합에 대한 속성이 있습니다. 규칙은 다음과 같이 정의됩니다. - 3상 - 총계 = L1 + L2 + L3 - 단상 - 총계 = L. 대부분의 속성에 대해 실제로 측정할 수 있는 방법은 다양합니다. 이를 위해 측정 유형 메타 데이터 속성을 사용할 수 있습니다. 평균, rms, 최소, 최대 값을 가질 수 있습니다. 평균, rms, 최소, 최대] 값을 사용하는 경우 측정 기간(초)을 제공하기 위해 측정 간격이라는 다른 메타데이터 속성을 사용해야 합니다. 또한 타임스탬프 속성은 측정 기간의 종료 시간이어야 합니다.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ACMeasurement:      
  description: 'The Data Model intended to measure the electrical energies consumed by an electrical system which uses an Alternating Current (AC) for a three-phase (L1, L2, L3) or single-phase (L) and neutral (N). It integrates the initial version of the data Modem [THREEPHASEMEASUREMENT], extended to also perform single-phase measurements. It includes attributes for various electrical measurements such as power, frequency, current and voltage.'      
  properties:      
    activeEnergyExport:      
      description: 'Active energy exported per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the active Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the active Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the active Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilowatt hour      
    activeEnergyImport:      
      description: 'Active energy imported i.e. consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the active Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the active Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the active Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilowatt hour      
    activePower:      
      description: 'Active power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the active power      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the active power      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the active power      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: Watt      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    apparentEnergyExport:      
      description: 'Apparent energy exported per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the apparent Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the apparent Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the apparent Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilovolt-ampere-hour      
    apparentEnergyImport:      
      description: 'Apparent energy imported i.e. consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the apparent Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the apparent Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the apparent Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilovolt-ampere-hour      
    apparentPower:      
      description: 'Apparent power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the apparent power      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the apparent power      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the apparent power      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: Watt      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    current:      
      description: 'Electrical current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the current      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the current      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the current      
          type: number      
          x-ngsi:      
            type: Property      
        N:      
          description: Value for phase neutral of the current      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: Ampere      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateEnergyMeteringStarted:      
      description: The starting date for metering energy in an ISO8601 UTC format      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObserved:      
      description: 'Date and time of this observation represented by an ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval to separate attributes `dateObservedFrom`,`dateObservedTo`'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateObservedFrom:      
      description: 'Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateObservedTo:      
      description: 'Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    displacementPowerFactor:      
      description: Displacement power factor for each phase. The quantity is based on the fundamental frequency of the system      
      properties:      
        L1:      
          description: Value for phase 1 of the displacement Power Factor      
          maximum: 1      
          minimum: -1      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the displacement Power Factor      
          maximum: 1      
          minimum: -1      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the displacement Power Factor      
          maximum: 1      
          minimum: -1      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    frequency:      
      description: 'The frequency of the circuit. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Hertz      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    phaseToPhaseVoltage:      
      description: 'Voltage between phases. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L12:      
          description: Value for phase 1 to phase 2 voltage      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L23:      
          description: Value for phase 2 to phase 3 voltage      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L31:      
          description: Value for phase 3 to phase 1 voltage      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: Volts      
    phaseType:      
      description: 'Type of Phase. A unique value. Enum:''singlePhase, threePhase'''      
      enum:      
        - singlePhase      
        - threePhase      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    phaseVoltage:      
      description: 'The voltage between each phase and neutral conductor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the voltage      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the voltage      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the voltage      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: Volts      
    powerFactor:      
      description: Power factor for each phase      
      properties:      
        L1:      
          description: Value for phase 1 of the power factor      
          maximum: 1      
          minimum: -1      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the power factor      
          maximum: 1      
          minimum: -1      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the power factor      
          maximum: 1      
          minimum: -1      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    reactiveEnergyExport:      
      description: 'Fundamental frequency reactive energy exported per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the reactive Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the reactive Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the reactive Energy Export      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilovolt-ampere-reactive-hour      
    reactiveEnergyImport:      
      description: 'Fundamental frequency reactive energy imported i.e. consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the reactive Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the reactive Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the reactive Energy Import      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilovolt-ampere-reactive-hour      
    reactivePower:      
      description: 'Fundamental frequency reactive power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      properties:      
        L1:      
          description: Value for phase 1 of the reactive power      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the reactive power      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the reactive power      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: volts-ampere-reactive      
    refDevice:      
      description: Reference to the devices which captured this observation      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Property      
    refTargetDevice:      
      description: Reference to a list of the devices for which the measurement was taken      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        type: Relationship      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    thdCurrent:      
      description: Total harmonic distortion of current for each phase      
      properties:      
        L1:      
          description: Value for phase 1 of the thd current      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the thd current      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the thd current      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    thdVoltage:      
      description: Total harmonic distortion of voltage for each phase      
      properties:      
        L1:      
          description: Value for phase 1 of the thd voltage      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L2:      
          description: Value for phase 2 of the thd voltage      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
        L3:      
          description: Value for phase 3 of the thd voltage      
          maximum: 1      
          minimum: 0      
          type: number      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    totalActiveEnergyExport:      
      description: 'Total energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: kilowatt hour      
    totalActiveEnergyImport:      
      description: 'Total energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: kilowatt hour      
    totalActivePower:      
      description: 'Total Active Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: Watt      
    totalApparentEnergyExport:      
      description: 'Total energy exported (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilovolt-ampere-hour      
    totalApparentEnergyImport:      
      description: 'Total energy imported i.e. consumed (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: kilovolt-ampere-hour.      
    totalApparentPower:      
      description: 'Total Apparent Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: volt-ampere      
    totalDisplacementPowerFactor:      
      description: Sum of Displacement power factor including all phases. The quantity is based on the fundamental frequency of the system      
      maximum: 1      
      minimum: -1      
      type: number      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    totalPowerFactor:      
      description: Sum of Power factor including all phases      
      maximum: 1      
      minimum: -1      
      type: number      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    totalReactiveEnergyExport:      
      description: 'Total fundamental frequency reactive energy exported. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
        units: kilovolt-ampere-reactive-hour      
    totalReactiveEnergyImport:      
      description: 'Total energy imported i.e. consumed (with regards to fundamental frequency reactive power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: kilovolt-ampere-reactive-hour.      
    totalReactivePower:      
      description: 'Total Reactive Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)'      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: volt-ampere-reactive      
    type:      
      description: NGSI property type. It has to be ACMeasurement      
      enum:      
        - ACMeasurement      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
    - location      
    - dateObserved      
    - phaseType      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Energy/blob/master/ACMeasurement/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/ACMeasurement/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
참고. 값은 각 위상의 위상 유형에 따라 1개 또는 3개의 하위 속성으로 전달됩니다. 단상. 개별 값 L. 삼상. 개별 값의 합계. L1, L2, L3. 모든 값은 측정 시작 날짜 [dateEnergyMeteringStarted]부터 계산됩니다.    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### ACMeasurement NGSI-v2 키값 예시    
다음은 JSON-LD 형식의 ACMeasurement를 키값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ACMeasurement:ACMeasurement:MNCA-ACM-001",  
  "type": "ACMeasurement",  
  "name": " AirPort-NCE-T1-F01-TR05-ACTP",  
  "alternateName": "AirPort global Observation",  
  "description": " Measurement corresponding to the ventilation machine of the technical rooms Terminal 1 T1 Floor 01 Technical Room 05 for Triphase alternating current.",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Aeroport",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-F01-TR05-ACTP"  
  ],  
  "phaseType": "threePhase",  
  "frequency": 50.020672,  
  "dateEnergyMeteringStarted": "2020-07-07T15:05:59.408Z",  
  "totalActiveEnergyImport": 150781.96448,  
  "totalReactiveEnergyImport": 20490.3392,  
  "totalActiveEnergyExport": 1059.80176,  
  "totalReactiveEnergyExport": 93275.02176,  
  "activePower": {  
    "L1": 11996.416016,  
    "L2": 9461.501953,  
    "L3": 10242.351562  
  },  
  "reactivePower": {  
    "L1": -2612.606934,  
    "L2": -2209.906006,  
    "L3": -3007.81958  
  },  
  "apparentPower": {  
    "L1": 13201.412109,  
    "L2": 10755.304688,  
    "L3": 11941.094727  
  },  
  "totalActivePower": 31700.269531,  
  "totalReactivePower": -7830.332031,  
  "totalApparentPower": 36019.089844,  
  "powerFactor": {  
    "L1": 0.908817,  
    "L2": 0.879906,  
    "L3": 0.859293  
  },  
  "displacementPowerFactor": {  
    "L1": 0.978013,  
    "L2": 0.973317,  
    "L3": 0.960382  
  },  
  "current": {  
    "L1": 56.126038,  
    "L2": 45.894356,  
    "L3": 50.872452,  
    "N": 0.0  
  },  
  "phaseVoltage": {  
    "L1": 234.961304,  
    "L2": 234.563477,  
    "L3": 235.354034  
  },  
  "phaseToPhaseVoltage": {  
    "L12": 406.769196,  
    "L23": 407.081238,  
    "L31": 407.734558  
  },  
  "thdVoltage": {  
    "L1": 0.01471114,  
    "L2": 0.01600046,  
    "L3": 0.01541459  
  },  
  "thdCurrent": {  
    "L1": 0.38497337,  
    "L2": 0.45807529,  
    "L3": 0.4938652  
  }  
}  
```  
</details>    
#### ACMeasurement NGSI-v2 정규화 예시    
다음은 정규화된 JSON-LD 형식의 ACMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ACMeasurement:ACMeasurement:MNCA-ACM-001",  
  "type": "ACMeasurement",  
  "name": {  
    "type": "Text",  
    "value": " AirPort-NCE-T1-F01-TR05-ACTP"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AirPort global Observation"  
  },  
  "description": {  
    "type": "Text",  
    "value": " Measurement corresponding to the ventilation machine of the technical rooms Terminal 1 T1 Floor 01 Technical Room 05 for Triphase alternating current."  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Aeroport"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "refDevice": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:Device:T1-F01-TR05-ACTP"  
    ]  
  },  
  "phaseType": {  
    "type": "Text",  
    "value": "threePhase"  
  },  
  "frequency": {  
    "type": "Number",  
    "value": 50.020672  
  },  
  "measurementInterval": {  
    "type": "Boolean",  
    "value": true  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "DateTime",  
    "value": "2020-07-07T15:05:59.408Z"  
  },  
  "totalActiveEnergyImport": {  
    "type": "Number",  
    "value": 150781.96448  
  },  
  "totalReactiveEnergyImport": {  
    "type": "Number",  
    "value": 20490.3392  
  },  
  "totalActiveEnergyExport": {  
    "type": "Number",  
    "value": 1059.80176  
  },  
  "totalReactiveEnergyExport": {  
    "type": "Number",  
    "value": 93275.02176  
  },  
  "activePower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 11996.416016,  
      "L2": 9461.501953,  
      "L3": 10242.351562  
    }  
  },  
  "reactivePower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": -2612.606934,  
      "L2": -2209.906006,  
      "L3": -3007.81958  
    }  
  },  
  "apparentPower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 13201.412109,  
      "L2": 10755.304688,  
      "L3": 11941.094727  
    }  
  },  
  "totalActivePower": {  
    "type": "Number",  
    "value": 31700.269531  
  },  
  "totalReactivePower": {  
    "type": "Number",  
    "value": -7830.332031  
  },  
  "totalApparentPower": {  
    "type": "Number",  
    "value": 36019.089844  
  },  
  "powerFactor": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.908817,  
      "L2": 0.879906,  
      "L3": 0.859293  
    }  
  },  
  "displacementPowerFactor": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.978013,  
      "L2": 0.973317,  
      "L3": 0.960382  
    }  
  },  
  "current": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 56.126038,  
      "L2": 45.894356,  
      "L3": 50.872452,  
      "N": 0.0  
    }  
  },  
  "phaseVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 234.961304,  
      "L2": 234.563477,  
      "L3": 235.354034  
    }  
  },  
  "phaseToPhaseVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L12": 406.769196,  
      "L23": 407.081238,  
      "L31": 407.734558  
    }  
  },  
  "thdVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.01471114,  
      "L2": 0.01600046,  
      "L3": 0.01541459  
    }  
  },  
  "thdCurrent": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.38497337,  
      "L2": 0.45807529,  
      "L3": 0.4938652  
    }  
  }  
}  
```  
</details>    
#### ACMeasurement NGSI-LD 키값 예시    
다음은 키 값으로 JSON-LD 형식의 ACMeasurement의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ACMeasurement:ACMeasurement:MNCA-ACM-001",  
  "type": "ACMeasurement",  
  "activePower": {  
    "L1": 11996.416016,  
    "L2": 9461.501953,  
    "L3": 10242.351562  
  },  
  "alternateName": "AirPort global Observation",  
  "apparentPower": {  
    "L1": 13201.412109,  
    "L2": 10755.304688,  
    "L3": 11941.094727  
  },  
  "areaServed": "Nice Aeroport",  
  "current": {  
    "L1": 56.126038,  
    "L2": 45.894356,  
    "L3": 50.872452,  
    "N": 0.0  
  },  
  "dateEnergyMeteringStarted": "2020-07-07T15:05:59.408Z",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "description": " Measurement corresponding to the ventilation machine of the technical rooms Terminal 1 T1 Floor 01 Technical Room 05 for Triphase alternating current.",  
  "displacementPowerFactor": {  
    "L1": 0.978013,  
    "L2": 0.973317,  
    "L3": 0.960382  
  },  
  "frequency": 50.020672,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "name": " AirPort-NCE-T1-F01-TR05-ACTP",  
  "phaseToPhaseVoltage": {  
    "L12": 406.769196,  
    "L23": 407.081238,  
    "L31": 407.734558  
  },  
  "phaseType": "threePhase",  
  "phaseVoltage": {  
    "L1": 234.961304,  
    "L2": 234.563477,  
    "L3": 235.354034  
  },  
  "powerFactor": {  
    "L1": 0.908817,  
    "L2": 0.879906,  
    "L3": 0.859293  
  },  
  "reactivePower": {  
    "L1": -2612.606934,  
    "L2": -2209.906006,  
    "L3": -3007.81958  
  },  
  "refDevice": [  
    "urn:ngsi-ld:Device:T1-F01-TR05-ACTP"  
  ],  
  "thdCurrent": {  
    "L1": 0.38497337,  
    "L2": 0.45807529,  
    "L3": 0.4938652  
  },  
  "thdVoltage": {  
    "L1": 0.01471114,  
    "L2": 0.01600046,  
    "L3": 0.01541459  
  },  
  "totalActiveEnergyExport": 1059.80176,  
  "totalActiveEnergyImport": 150781.96448,  
  "totalActivePower": 31700.269531,  
  "totalApparentPower": 36019.089844,  
  "totalReactiveEnergyExport": 93275.02176,  
  "totalReactiveEnergyImport": 20490.3392,  
  "totalReactivePower": -7830.332031,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### ACMeasurement NGSI-LD 정규화 예시    
다음은 정규화된 JSON-LD 형식의 ACMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:ACMeasurement:ACMeasurement:MNCA-ACM-001",  
  "type": "ACMeasurement",  
  "activePower": {  
    "type": "Property",  
    "value": {  
      "L1": 11996.416016,  
      "L2": 9461.501953,  
      "L3": 10242.351562  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort  global Observation"  
  },  
  "apparentPower": {  
    "type": "Property",  
    "value": {  
      "L1": 13201.412109,  
      "L2": 10755.304688,  
      "L3": 11941.094727  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "current": {  
    "type": "Property",  
    "value": {  
      "L1": 56.126038,  
      "L2": 45.894356,  
      "L3": 50.872452,  
      "N": 0.0  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-07-07T15:05:59.408Z"  
    }  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-17TT08:45:00Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": " Measurement corresponding to the ventilation machine of the technical rooms Terminal 1 T1  Floor 01  Technical Room 05 for Triphase alternating current."  
  },  
  "displacementPowerFactor": {  
    "type": "Property",  
    "value": {  
      "L1": 0.978013,  
      "L2": 0.973317,  
      "L3": 0.960382  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    },  
    "onlyPositive": {  
      "type": "Property",  
      "value": true  
    }  
  },  
  "frequency": {  
    "type": "Property",  
    "value": 50.020672,  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": " AirPort-NCE-T1-F01-TR05-ACTP"  
  },  
  "phaseToPhaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L12": 406.769196,  
      "L23": 407.081238,  
      "L31": 407.734558  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "phaseType": {  
    "type": "Property",  
    "value": "threePhase"  
  },  
  "phaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L1": 234.961304,  
      "L2": 234.563477,  
      "L3": 235.354034  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "powerFactor": {  
    "type": "Property",  
    "value": {  
      "L1": 0.908817,  
      "L2": 0.879906,  
      "L3": 0.859293  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    },  
    "onlyPositive": {  
      "type": "Property",  
      "value": true  
    }  
  },  
  "reactivePower": {  
    "type": "Property",  
    "value": {  
      "L1": -2612.606934,  
      "L2": -2209.906006,  
      "L3": -3007.81958  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Device:T1-F01-TR05-ACTP"  
    ]  
  },  
  "thdCurrent": {  
    "type": "Property",  
    "value": {  
      "L1": 0.38497337,  
      "L2": 0.45807529,  
      "L3": 0.4938652  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "thdVoltage": {  
    "type": "Property",  
    "value": {  
      "L1": 0.01471114,  
      "L2": 0.01600046,  
      "L3": 0.01541459  
    },  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "totalActiveEnergyExport": {  
    "type": "Property",  
    "value": 1059.80176,  
    "observedAt": "2020-02-24T22:00:00.173Z"  
  },  
  "totalActiveEnergyImport": {  
    "type": "Property",  
    "value": 150781.96448,  
    "observedAt": "2020-02-24T22:00:00.173Z"  
  },  
  "totalActivePower": {  
    "type": "Property",  
    "value": 31700.269531,  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "totalApparentPower": {  
    "type": "Property",  
    "value": 36019.089844,  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "totalReactiveEnergyExport": {  
    "type": "Property",  
    "value": 93275.02176,  
    "observedAt": "2020-02-24T22:00:00.173Z"  
  },  
  "totalReactiveEnergyImport": {  
    "type": "Property",  
    "value": 20490.3392,  
    "observedAt": "2020-02-24T22:00:00.173Z"  
  },  
  "totalReactivePower": {  
    "type": "Property",  
    "value": -7830.332031,  
    "observedAt": "2020-02-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
