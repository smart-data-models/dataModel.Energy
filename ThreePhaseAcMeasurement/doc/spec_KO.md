<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: ThreePhaseAcMeasurement  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Energy/blob/master/ThreePhaseAcMeasurement/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **3상 교류를 사용하는 시스템의 전기 측정값입니다.**  
버전: 0.0.4  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `activeEnergyExport[object]`: 계량 시작일 이후 위상별로 내보낸 유효 에너지입니다. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 활성 에너지 수출의 1줄    
	- `L2[number]`: 활성 에너지 수출의 2번 라인    
	- `L3[number]`: 활성 에너지 수출의 3번째 라인    
- `activeEnergyImport[object]`: 수입된 유효 에너지, 즉 계량 시작일 이후 라인당 소비된 에너지입니다. 실제 값은 각 교류 단계의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 활성 에너지 가져오기 1줄    
	- `L2[number]`: 활성 에너지 가져오기의 2번째 줄    
	- `L3[number]`: 활성 에너지 가져오기의 3번째 줄    
- `activePower[object]`: 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 프로퍼티로 전달됩니다: L1, L2, L3.  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 유효 전력의 1줄    
	- `L2[number]`: 활성 전력의 2번째 라인    
	- `L3[number]`: 유효 전력의 3번째 라인    
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예: 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `apparentEnergyExport[object]`: 계량 시작일 이후 위상별로 내보낸 겉보기 에너지입니다. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 겉보기 에너지 수출의 1줄    
	- `L2[number]`: 겉보기 에너지 수출의 2번째 줄    
	- `L3[number]`: 겉보기 에너지 수출의 3번째 줄    
- `apparentEnergyImport[object]`: 수입된 겉보기 에너지, 즉 계량 시작일 이후 위상별로 소비된 에너지입니다. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 겉보기 에너지 수입의 1줄    
	- `L2[number]`: 겉보기 에너지 수입의 2번째 줄    
	- `L3[number]`: 겉보기 에너지 수입의 3번째 줄    
- `apparentPower[object]`: 위상당 소비되는 겉보기 전력입니다. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 피상 전력의 1줄    
	- `L2[number]`: 피상 전력의 2번째 줄    
	- `L3[number]`: 피상 전력의 3번째 줄    
- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: 전류. 실제 값은 교류 위상 및 중성선당 하나의 하위 속성에 의해 전달됩니다: L1, L2, L3 및 N  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 전류의 1줄    
	- `L2[number]`: 전류의 2번째 줄    
	- `L3[number]`: 전류의 3번째 줄    
	- `N[number]`: 전류의 중립    
- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자열입니다.  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateEnergyMeteringStarted[date-time]`: 에너지 계량 시작 날짜  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `displacementPowerFactor[object]`: 각 위상에 대한 변위 역률입니다. 이 수치는 시스템의 기본 주파수를 기준으로 합니다. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2 및 L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 변위 역률의 1줄    
	- `L2[number]`: 변위 역률의 2번째 줄    
	- `L3[number]`: 변위 역률의 3번째 줄    
- `frequency[number]`: 회로의 주파수  . Model: [http://schema.org/Number](http://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `phaseToPhaseVoltage[object]`: 위상 간 전압. 각 위상 쌍에 대한 값: 1상 및 2상(L12), 2상 및 3상(L32), 3상 및 1상(L31)  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L12[number]`: 위상 전압의 라인 1과 2 사이의 위상    
	- `L23[number]`: 위상 전압의 2번 라인과 3번 라인 사이의 위상    
	- `L31[number]`: 위상 전압의 3번 라인과 1번 라인 사이의 위상    
- `phaseVoltage[object]`: 각 위상과 중성 도체 사이의 전압입니다. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 위상 전압의 1라인    
	- `L2[number]`: 위상 전압의 2번째 라인    
	- `L3[number]`: 위상 전압의 3번째 라인    
- `powerFactor[object]`: 각 위상의 역률. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2 및 L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 역률 1줄    
	- `L2[number]`: 역률의 2번째 라인    
	- `L3[number]`: 역률의 3번째 라인    
- `reactiveEnergyExport[object]`: 계량 시작일 이후 위상별로 내보낸 기본 주파수 무효 에너지입니다. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 무효 에너지 수출의 첫 번째 라인    
	- `L2[number]`: 무효 에너지 수출의 2번 라인    
	- `L3[number]`: 무효 에너지 수출의 3번째 라인    
- `reactiveEnergyImport[object]`: 계량 시작일 이후 위상별로 소비된 기본 주파수 무효 에너지, 즉 수입된 기본 주파수 무효 에너지입니다. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 무효 에너지 가져오기 1줄    
	- `L2[number]`: 무효 에너지 가져오기의 2번째 줄    
	- `L3[number]`: 무효 에너지 가져오기의 3번째 줄    
- `reactivePower[object]`: 기본 주파수 무효 전력. 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성을 통해 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 무효 전력 1줄    
	- `L2[number]`: 무효 전력의 2번째 라인    
	- `L3[number]`: 무효 전력의 3번째 라인    
- `refDevice[array]`: 측정값을 얻는 데 사용된 디바이스  - `refTargetDevice[array]`: 측정이 수행된 디바이스(들)  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 일련의 문자입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `thdCurrent[object]`: 전류의 총 고조파 왜곡입니다. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2 및 L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 총 고조파 왜곡 전류의 1줄    
	- `L2[number]`: 총 고조파 왜곡 전류의 2번째 줄    
	- `L3[number]`: 총 고조파 왜곡 전류의 3번째 라인    
- `thdVoltage[object]`: 각 위상에 대한 전압의 총 고조파 왜곡입니다. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2 및 L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1[number]`: 총 고조파 왜곡 전압의 1번째 라인    
	- `L2[number]`: 총 고조파 왜곡 전압의 2번째 라인    
	- `L3[number]`: 총 고조파 왜곡 전압의 3번째 라인    
- `totalActiveEnergyExport[number]`: 계량 시작 이후 내보낸 총 에너지(`dateEnergyMeteringStarted` 이후)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActiveEnergyImport[number]`: 수입된 총 에너지, 즉 계량 시작 이후 소비된 에너지(`dateEnergyMeteringStarted` 이후)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActivePower[number]`: 소비된 유효 전력(모든 단계 계산)  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalApparentEnergyExport[number]`: 계량 시작 날짜(`dateEnergyMeteringStarted`) 이후 내보낸 총 에너지(피상 전력 관련)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentEnergyImport[number]`: 계량 시작 날짜(`dateEnergyMeteringStarted`) 이후 수입된 총 에너지, 즉 소비된 (피상 전력과 관련하여) 에너지입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentPower[number]`: 소비된 겉보기 전력(모든 단계 계산)  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalDisplacementPowerFactor[number]`: 모든 위상을 포함한 변위 역률입니다. 이 수치는 시스템의 기본 주파수를 기준으로 합니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalPowerFactor[number]`: 모든 단계를 포함한 역률  . Model: [http://schema.org/Number](http://schema.org/Number)- `totalReactiveEnergyExport[number]`: 계량 시작 이후 내보낸 총 기본 주파수 무효 에너지(`dateEnergyMeteringStarted` 이후)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalReactiveEnergyImport[number]`: 계량 시작 날짜(`dateEnergyMeteringStarted`) 이후 수입된 총 에너지, 즉 소비된 (기본 주파수 무효 전력 관련) 에너지입니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalReactivePower[number]`: 소비된 무효 전력(모든 단계 계산)  . Model: [http://schema.org/Number](http://schema.org/Number)- `type[string]`: 이 값은 `ThreePhaseAcMeasurement`와 같아야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
전체 제목과 설명 사이에 포함할 텍스트입니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ThreePhaseAcMeasurement:    
  description: An electrical  measurement from a system that uses three phase alternating current.    
  properties:    
    activeEnergyExport:    
      description: 'Active energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the active energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the active energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the active energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: kilowatt hour (kWh)    
    activeEnergyImport:    
      description: 'Active energy imported i.e. consumed per Line since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the active energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the active energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the active energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: kilowatt hour (kWh)    
    activePower:    
      description: 'The actual values will beconveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3. '    
      properties:    
        L1:    
          description: Line 1 of the active power    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the active power    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the active power    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: watt (W).Active power consumed per phase    
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
      description: 'Apparent energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the apparent energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the apparent energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the apparent energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-hour (kVAh)    
    apparentEnergyImport:    
      description: 'Apparent energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the apparent energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the apparent energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the apparent energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-hour (kVAh)    
    apparentPower:    
      description: 'Apparent power consumed per phase. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the apparent power    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the apparent power    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the apparent power    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: volt-ampere (VA)    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    current:    
      description: 'Electrical current. The actual values will be conveyed by one subproperty per alternating current phase and the neutral wire: L1, L2, L3 and N'    
      properties:    
        L1:    
          description: Line 1 of the current    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the current    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the current    
          type: number    
          x-ngsi:    
            type: Property    
        N:    
          description: Neutral of the current    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: Ampers (A)    
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
      description: The starting date for metering energy    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    displacementPowerFactor:    
      description: 'Displacement power factor for each phase. The quantity is based on the fundamental frequency of the system. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          description: Line 1 of the displacement power factor    
          maximum: 1    
          minimum: -1    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the displacement power factor    
          maximum: 1    
          minimum: -1    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the displacement power factor    
          maximum: 1    
          minimum: -1    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: -1 to +1    
    frequency:    
      description: The frequency of the circuit    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Hertz (Hz)    
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
      description: 'Voltage between phases. A value for each phase pair: phases 1 and 2 (L12), phases 2 and 3 (L32), phases 3 and 1 (L31)'    
      properties:    
        L12:    
          description: Phase between line 1 and 2 of the phase voltage    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L23:    
          description: Phase between line 2 and 3 of the phase voltage    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L31:    
          description: Phase between line 3 and 1 of the phase voltage    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: Volts (V)    
    phaseVoltage:    
      description: 'The voltage between each phase and neutral conductor. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          description: Line 1 of the phase voltage    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the phase voltage    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the phase voltage    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: Volts (V)    
    powerFactor:    
      description: 'Power factor for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          description: Line 1 of the power factor    
          maximum: 1    
          minimum: -1    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the power factor    
          maximum: 1    
          minimum: -1    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the power factor    
          maximum: 1    
          minimum: -1    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: -1 to +1    
    reactiveEnergyExport:    
      description: 'Fundamental frequency reactive energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the reactive energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the reactive energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the reactive energy export    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-reactive-hour (kVArh)    
    reactiveEnergyImport:    
      description: 'Fundamental frequency reactive energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the reactive energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the reactive energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the reactive energy import    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: kilovolt-ampere-reactive-hour (kVArh)    
    reactivePower:    
      description: 'Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
      properties:    
        L1:    
          description: Line 1 of the reactive power    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the reactive power    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the reactive power    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: volts-ampere-reactive (VAr)    
    refDevice:    
      description: Device(s) used to obtain the measurement    
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
    refTargetDevice:    
      description: Device(s) for which the measurement was taken    
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
      description: 'Total harmonic distortion of electrical current. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          description: Line 1 of the total harmonic distortion current    
          maximum: 1    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the total harmonic distortion current    
          maximum: 1    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the total harmonic distortion current    
          maximum: 1    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: 0 to 1    
    thdVoltage:    
      description: 'Total harmonic distortion of voltage for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          description: Line 1 of the total harmonic distortion voltage    
          maximum: 1    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L2:    
          description: Line 2 of the total harmonic distortion voltage    
          maximum: 1    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        L3:    
          description: Line 3 of the total harmonic distortion voltage    
          maximum: 1    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: 0 to 1    
    totalActiveEnergyExport:    
      description: Total energy exported since metering started (since `dateEnergyMeteringStarted`)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilowatt hour (kWh)    
    totalActiveEnergyImport:    
      description: Total energy imported i.e. consumed since metering started (since `dateEnergyMeteringStarted`)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilowatt hour (kWh)    
    totalActivePower:    
      description: Active power consumed (counting all phases)    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: watt (W)    
    totalApparentEnergyExport:    
      description: Total energy exported (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-reactive-hour (kVArh)    
    totalApparentEnergyImport:    
      description: Total energy imported i.e. consumed (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-hour (kVAh)    
    totalApparentPower:    
      description: Apparent power consumed (counting all phases)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: volt-ampere (VA)    
    totalDisplacementPowerFactor:    
      description: Displacement power factor including all phases. The quantity is based on the fundamental frequency of the system    
      maximum: 1    
      minimum: -1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: -1 to +1    
    totalPowerFactor:    
      description: Power factor including all phases    
      maximum: 1    
      minimum: -1    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: -1 to +1    
    totalReactiveEnergyExport:    
      description: Total fundamental frequency reactive energy exported since metering started (since `dateEnergyMeteringStarted`)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-reactive-hour (kVArh)    
    totalReactiveEnergyImport:    
      description: Total energy imported i.e. consumed (with regards to fundamental frequency reactive power) since the metering start date (`dateEnergyMeteringStarted`)    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: kilovolt-ampere-reactive-hour (kVArh)    
    totalReactivePower:    
      description: Reactive power consumed (counting all phases)    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: volt-ampere-reactive (VAr)    
    type:    
      description: It must be equal to `ThreePhaseAcMeasurement`    
      enum:    
        - ThreePhaseAcMeasurement    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Energy/blob/master/ThreePhaseAcMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Energy/ThreePhaseAcMeasurement/schema.json    
  x-model-tags: ""    
  x-version: 0.0.4    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
속성 목록 뒤에 포함할 텍스트  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### ThreePhaseAcMeasurement NGSI-v2 키 값 예시  
다음은 JSON-LD 형식의 ThreePhaseAcMeasurement를 키 값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "dateEnergyMeteringStarted": "2018-07-07T15:05:59.408Z",  
  "refDevice": [  
    "Device:eQL-EDF3GL-2006201705"  
  ],  
  "name": "HKAPK0200",  
  "description": "measurement corresponding to the ventilation machine rooms",  
  "totalActiveEnergyImport": 150781.96448,  
  "totalReactiveEnergyImport": 20490.3392,  
  "totalActiveEnergyExport": 1059.80176,  
  "totalReactiveEnergyExport": 93275.02176,  
  "totalActivePower": 31700.269531,  
  "activePower": {  
    "L1": 11996.416016,  
    "L2": 9461.501953,  
    "L3": 10242.351562  
  },  
  "totalReactivePower": -7830.332031,  
  "reactivePower": {  
    "L1": -2612.606934,  
    "L2": -2209.906006,  
    "L3": -3007.81958  
  },  
  "totalApparentPower": 36019.089844,  
  "apparentPower": {  
    "L1": 13201.412109,  
    "L2": 10755.304688,  
    "L3": 11941.094727  
  },  
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
  "frequency": 50.020672,  
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
#### ThreePhaseAcMeasurement NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 ThreePhaseAcMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "dateEnergyMeteringStarted": {  
    "type": "DateTime",  
    "value": "2018-07-07T15:05:59.408Z"  
  },  
  "refDevice": {  
    "type": "StructuredValue",  
    "value": [  
      "Device:eQL-EDF3GL-2006201705"  
    ]  
  },  
  "name": {  
    "type": "Text",  
    "value": "HKAPK0200"  
  },  
  "description": {  
    "type": "Text",  
    "value": "measurement corresponding to the ventilation machine rooms"  
  },  
  "totalActiveEnergyImport": {  
    "type": "Number",  
    "value": 150781.96448,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    }  
  },  
  "totalReactiveEnergyImport": {  
    "type": "Number",  
    "value": 20490.3392,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    }  
  },  
  "totalActiveEnergyExport": {  
    "type": "Number",  
    "value": 1059.80176,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    }  
  },  
  "totalReactiveEnergyExport": {  
    "type": "Number",  
    "value": 93275.02176,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    }  
  },  
  "totalActivePower": {  
    "type": "Number",  
    "value": 31700.269531,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "activePower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 11996.416016,  
      "L2": 9461.501953,  
      "L3": 10242.351562  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "totalReactivePower": {  
    "type": "Number",  
    "value": -7830.332031,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "reactivePower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": -2612.606934,  
      "L2": -2209.906006,  
      "L3": -3007.81958  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "totalApparentPower": {  
    "type": "Number",  
    "value": 36019.089844,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "apparentPower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 13201.412109,  
      "L2": 10755.304688,  
      "L3": 11941.094727  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "powerFactor": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.908817,  
      "L2": 0.879906,  
      "L3": 0.859293  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      },  
      "onlyPositive": {  
        "value": true  
      }  
    }  
  },  
  "displacementPowerFactor": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.978013,  
      "L2": 0.973317,  
      "L3": 0.960382  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      },  
      "onlyPositive": {  
        "value": true  
      }  
    }  
  },  
  "frequency": {  
    "type": "Number",  
    "value": 50.020672,  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "current": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 56.126038,  
      "L2": 45.894356,  
      "L3": 50.872452,  
      "N": 0.0  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "rms"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "phaseVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 234.961304,  
      "L2": 234.563477,  
      "L3": 235.354034  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "rms"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "phaseToPhaseVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L12": 406.769196,  
      "L23": 407.081238,  
      "L31": 407.734558  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "rms"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "thdVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.01471114,  
      "L2": 0.01600046,  
      "L3": 0.01541459  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  },  
  "thdCurrent": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.38497337,  
      "L2": 0.45807529,  
      "L3": 0.4938652  
    },  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    }  
  }  
}  
```  
</details>  
#### ThreePhaseAcMeasurement NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 ThreePhaseAcMeasurement를 키 값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ThreePhaseAcMeasurement:ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "activePower": {  
    "L1": 11996.416016,  
    "L2": 9461.501953,  
    "L3": 10242.351562  
  },  
  "apparentPower": {  
    "L1": 13201.412109,  
    "L2": 10755.304688,  
    "L3": 11941.094727  
  },  
  "current": {  
    "L1": 56.126038,  
    "L2": 45.894356,  
    "L3": 50.872452,  
    "N": 0.0  
  },  
  "dateEnergyMeteringStarted": "2018-07-07T15:05:59.408Z",  
  "description": "measurement corresponding to the ventilation machine rooms",  
  "displacementPowerFactor": {  
    "L1": 0.978013,  
    "L2": 0.973317,  
    "L3": 0.960382  
  },  
  "frequency": 50.020672,  
  "name": "HKAPK0200",  
  "phaseToPhaseVoltage": {  
    "L12": 406.769196,  
    "L23": 407.081238,  
    "L31": 407.734558  
  },  
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
    "urn:ngsi-ld:Device:Device:eQL-EDF3GL-2006201705"  
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
#### ThreePhaseAcMeasurement NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 ThreePhaseAcMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ThreePhaseAcMeasurement:ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "activePower": {  
    "type": "Property",  
    "value": {  
      "L1": 11996.416016,  
      "L2": 9461.501953,  
      "L3": 10242.351562  
    }  
  },  
  "apparentPower": {  
    "type": "Property",  
    "value": {  
      "L1": 13201.412109,  
      "L2": 10755.304688,  
      "L3": 11941.094727  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "current": {  
    "type": "Property",  
    "value": {  
      "L1": 56.126038,  
      "L2": 45.894356,  
      "L3": 50.872452,  
      "N": 0.0  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-07-07T15:05:59.408Z"  
    }  
  },  
  "description": {  
    "type": "Property",  
    "value": "measurement corresponding to the ventilation machine rooms"  
  },  
  "displacementPowerFactor": {  
    "type": "Property",  
    "value": {  
      "L1": 0.978013,  
      "L2": 0.973317,  
      "L3": 0.960382  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "name": {  
    "type": "Property",  
    "value": "HKAPK0200"  
  },  
  "phaseToPhaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L12": 406.769196,  
      "L23": 407.081238,  
      "L31": 407.734558  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "phaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L1": 234.961304,  
      "L2": 234.563477,  
      "L3": 235.354034  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
      "urn:ngsi-ld:Device:Device:eQL-EDF3GL-2006201705"  
    ]  
  },  
  "thdCurrent": {  
    "type": "Property",  
    "value": {  
      "L1": 0.38497337,  
      "L2": 0.45807529,  
      "L3": 0.4938652  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalActiveEnergyImport": {  
    "type": "Property",  
    "value": 150781.96448,  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalActivePower": {  
    "type": "Property",  
    "value": 31700.269531,  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalReactiveEnergyImport": {  
    "type": "Property",  
    "value": 20490.3392,  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalReactivePower": {  
    "type": "Property",  
    "value": -7830.332031,  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
결국 텍스트  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
크기 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
