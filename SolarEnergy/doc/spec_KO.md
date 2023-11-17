<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: SolarEnergy    
================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Energy/blob/master/SolarEnergy/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **태양 에너지 생성을 위한 데이터 모델.**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `activePower[object]`: 실제 값은 각 교류 위상의 이름과 동일한 이름의 하위 속성에 의해 전달됩니다: L1, L2, L3.  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
	- `L3`:       
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: 전류. 실제 값은 교류 위상 및 중성선당 하나의 하위 속성에 의해 전달됩니다: L1, L2, L3 및 N  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
	- `L3`:       
	- `N`:       
- `dataDescriptor[string]`: 데이터 기술자 엔티티를 가리키는 URI  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `energyGenerated[number]`: 이 관측에 해당하는 에너지 자원에서 특정 시간 범위에 걸쳐 생성된 에너지  - `frequency[number]`: 이 관측에 해당하는 엔티티에서 관측된 주파수  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maxSolarPowerMeasure[number]`: 생성할 수 있는 최대 태양 에너지의 측정값입니다.  - `name[string]`: 이 항목의 이름  - `observationDateTime[date-time]`: 마지막으로 보고된 관찰 시간  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `phaseCurrent[object]`: 위상별 전류. 다음 순서로 세 단계의 유효 전력으로 구성된 트리플을 순서대로 나열합니다: [R Y B]  	- `L1`:       
	- `L2`:       
	- `L3`:       
- `phaseVoltage[object]`: 각 위상과 중성 도체 사이의 전압입니다. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2 및 L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
	- `L3`:       
- `powerFactor[object]`: 각 상에 대한 역률. 실제 값은 교류 위상당 하나의 하위 속성에 의해 전달됩니다: L1, L2 및 L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
	- `L3`:       
- `reactivePower[object]`: 기본 주파수 무효 전력. 실제 값은 각 교류 위상의 이름과 동일한 이름을 가진 하위 속성으로 전달됩니다: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
	- `L3`:       
- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `totalActivePower[number]`: 모든 단계에서 소비되는 총 유효 전력  - `totalEnergyGenerated[number]`: 이 관측에 해당하는 에너지 자원이 생성한 총 에너지량  - `totalReactivePower[number]`: 모든 단계의 총 무효 전력  - `type[string]`: NGSI 엔티티 유형. SolarEnergy여야 합니다.  - `voltage[number]`: 이 관찰에 해당하는 엔티티의 전압 값입니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SolarEnergy:      
  description: A Data Model for Solar Energy generation.      
  properties:      
    activePower:      
      description: 'The actual values will beconveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3. '      
      properties:      
        L1:      
          type: number      
        L2:      
          type: number      
        L3:      
          type: number      
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
          type: number      
        L2:      
          type: number      
        L3:      
          type: number      
        N:      
          type: number      
      type: object      
      x-ngsi:      
        model: http://schema.org/StructuredValue      
        type: Property      
        units: Ampers (A)      
    dataDescriptor:      
      description: URI pointing to the data-descriptor entity      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    energyGenerated:      
      description: Energy generated over a specific time range from the energy resource corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    frequency:      
      description: Frequency observed from the entity corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
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
    maxSolarPowerMeasure:      
      description: A measure of maximum solar energy that can be generated      
      type: number      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
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
    phaseCurrent:      
      description: 'Current per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]'      
      properties:      
        L1:      
          type: number      
        L2:      
          type: number      
        L3:      
          type: number      
      type: object      
      x-ngsi:      
        type: Property      
    phaseVoltage:      
      description: 'The voltage between each phase and neutral conductor. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'      
      properties:      
        L1:      
          minimum: 0      
          type: number      
        L2:      
          minimum: 0      
          type: number      
        L3:      
          minimum: 0      
          type: number      
      type: object      
      x-ngsi:      
        model: http://schema.org/StructuredValue      
        type: Property      
        units: Volts (V)      
    powerFactor:      
      description: 'Power factor for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'      
      properties:      
        L1:      
          maximum: 1      
          minimum: -1      
          type: number      
        L2:      
          maximum: 1      
          minimum: -1      
          type: number      
        L3:      
          maximum: 1      
          minimum: -1      
          type: number      
      type: object      
      x-ngsi:      
        model: http://schema.org/StructuredValue      
        type: Property      
        units: -1 to +1      
    reactivePower:      
      description: 'Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3'      
      properties:      
        L1:      
          type: number      
        L2:      
          type: number      
        L3:      
          type: number      
      type: object      
      x-ngsi:      
        model: http://schema.org/StructuredValue      
        type: Property      
        units: volts-ampere-reactive (VAr)      
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
    totalActivePower:      
      description: Total active power consumed by all phases      
      type: number      
      x-ngsi:      
        type: Property      
    totalEnergyGenerated:      
      description: Total energy generated by the energy resource corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    totalReactivePower:      
      description: Total reactive power for all phases      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be SolarEnergy      
      enum:      
        - SolarEnergy      
      type: string      
      x-ngsi:      
        type: Property      
    voltage:      
      description: The value of Voltage in the entity corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://voc.iudx.org.in/SolarEnergy      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Energy/blob/master/SolarEnergy/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/schema.json      
  x-model-tags: IUDX      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### SolarEnergy NGSI-v2 키값 예시    
다음은 키 값으로 JSON-LD 형식의 SolarEnergy의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SolarEnergy:id:BHDU:88967916",  
  "type": "SolarEnergy",  
  "activePower": {  
    "L1": 36,  
    "L2": 35.1,  
    "L3": 35.6  
  },  
  "address": {  
    "addressCountry": "India",  
    "addressLocality": "New Delhi",  
    "addressRegion": "Delhi",  
    "postOfficeBoxNumber": "",  
    "postalCode": "110001",  
    "streetAddress": "Jai Singh Marg, Hanuman Road Area, Connaught Place"  
  },  
  "alternateName": "Solar energy source 1",  
  "areaServed": "",  
  "current": {  
    "L1": 1.2,  
    "L2": 1.2,  
    "L3": 1.3,  
    "N": 0.7  
  },  
  "dataDescriptor": "urn:ngsi-ld:SolarEnergy:dataDescriptor:TTTK:11491249",  
  "dataProvider": "",  
  "dateCreated": "2022-01-10T01:49:09Z",  
  "dateModified": "2022-01-10T01:50:52Z",  
  "description": "Solar energy source 1",  
  "energyGenerated": 766.1,  
  "frequency": 50,  
  "location": {  
    "coordinates": [  
      -35.589575,  
      -78.339812  
    ],  
    "type": "Point"  
  },  
  "maxSolarPowerMeasure": 989.8,  
  "name": "Solar Energy measured at resource 1",  
  "observationDateTime": "2022-01-20T20:02:52Z",  
  "owner": [  
    "urn:ngsi-ld:SolarEnergy:items:DACI:25767721",  
    "urn:ngsi-ld:SolarEnergy:items:YVQJ:55840840"  
  ],  
  "phaseCurrent": {  
    "L1": 111.5,  
    "L2": 109.3,  
    "L3": 111.0  
  },  
  "phaseVoltage": {  
    "L1": 120.5,  
    "L2": 116.4,  
    "L3": 119.8  
  },  
  "powerFactor": {  
    "L1": 0.7,  
    "L2": 0.7,  
    "L3": 0.5  
  },  
  "reactivePower": {  
    "L1": 108.1,  
    "L2": 107.0,  
    "L3": 106.5  
  },  
  "seeAlso": [  
    "urn:ngsi-ld:SolarEnergy:items:XREG:08856151"  
  ],  
  "source": "",  
  "totalActivePower": 873.9,  
  "totalEnergyGenerated": 527.6,  
  "totalReactivePower": 8690,  
  "voltage": 122.0  
}  
```  
</details>    
#### SolarEnergy NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SolarEnergy의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SolarEnergy:id:BHDU:88967916",  
  "type": "SolarEnergy",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -35.589575,  
        -78.339812  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "streetAddress": "Jai Singh Marg, Hanuman Road Area, Connaught Place",  
      "addressLocality": "New Delhi",  
      "addressRegion": "Delhi",  
      "addressCountry": "India",  
      "postalCode": "110001",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2022-01-10T01:49:09Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2022-01-10T01:50:52Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": "Solar Energy measured at resource 1"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Solar energy source 1"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Solar energy source 1"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SolarEnergy:items:DACI:25767721",  
      "urn:ngsi-ld:SolarEnergy:items:YVQJ:55840840"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:SolarEnergy:items:XREG:08856151"  
    ]  
  },  
  "totalActivePower": {  
    "type": "Number",  
    "value": 873.9  
  },  
  "phaseCurrent": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 111.5,  
      "L2": 109.3,  
      "L3": 111.0  
    }  
  },  
  "reactivePower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 108.1,  
      "L2": 107.0,  
      "L3": 106.5  
    }  
  },  
  "voltage": {  
    "type": "Number",  
    "value": 122.0  
  },  
  "powerFactor": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.7,  
      "L2": 0.7,  
      "L3": 0.5  
    }  
  },  
  "current": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 1.2,  
      "L2": 1.2,  
      "L3": 1.3,  
      "N": 0.7  
    }  
  },  
  "totalReactivePower": {  
    "type": "Number",  
    "value": 110.8  
  },  
  "phaseVoltage": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 120.5,  
      "L2": 116.4,  
      "L3": 119.8  
    }  
  },  
  "activePower": {  
    "type": "StructuredValue",  
    "value": {  
      "L1": 17.3,  
      "L2": 19.5,  
      "L3": 20.4  
    }  
  },  
  "dataDescriptor": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SolarEnergy:dataDescriptor:TTTK:11491249"  
  },  
  "energyGenerated": {  
    "type": "Number",  
    "value": 766.1  
  },  
  "maxSolarPowerMeasure": {  
    "type": "Number",  
    "value": 989.8  
  },  
  "frequency": {  
    "type": "Number",  
    "value": 50  
  },  
  "totalEnergyGenerated": {  
    "type": "Number",  
    "value": 527.6  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2022-01-20T20:02:52Z"  
  }  
}  
```  
</details>    
#### SolarEnergy NGSI-LD 키값 예시    
다음은 키 값으로 JSON-LD 형식의 SolarEnergy의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SolarEnergy:id:BHDU:88967916",  
  "type": "SolarEnergy",  
  "activePower": {  
    "L1": 17.3,  
    "L2": 19.5,  
    "L3": 20.4  
  },  
  "address": {  
    "addressCountry": "India",  
    "addressLocality": "New Delhi",  
    "addressRegion": "Delhi",  
    "postOfficeBoxNumber": "",  
    "postalCode": "110001",  
    "streetAddress": "Jai Singh Marg, Hanuman Road Area, Connaught Place"  
  },  
  "alternateName": "Solar energy source 1",  
  "areaServed": "",  
  "current": {  
    "L1": 1.2,  
    "L2": 1.2,  
    "L3": 1.3,  
    "N": 0.7  
  },  
  "dataDescriptor": "urn:ngsi-ld:SolarEnergy:dataDescriptor:TTTK:11491249",  
  "dataProvider": "",  
  "dateCreated": "2022-01-10T01:49:09Z",  
  "dateModified": "2022-01-10T01:50:52Z",  
  "description": "Solar energy source 1",  
  "energyGenerated": 766.1,  
  "frequency": 50,  
  "location": {  
    "coordinates": [  
      -35.589575,  
      -78.339812  
    ],  
    "type": "Point"  
  },  
  "maxSolarPowerMeasure": 989.8,  
  "name": "Solar Energy measured at resource 1",  
  "observationDateTime": "2022-01-20T20:02:52Z",  
  "owner": [  
    "urn:ngsi-ld:SolarEnergy:items:DACI:25767721",  
    "urn:ngsi-ld:SolarEnergy:items:YVQJ:55840840"  
  ],  
  "phaseCurrent": {  
    "L1": 111.5,  
    "L2": 109.3,  
    "L3": 111.0  
  },  
  "phaseVoltage": {  
    "L1": 120.5,  
    "L2": 116.4,  
    "L3": 119.8  
  },  
  "powerFactor": {  
    "L1": 0.7,  
    "L2": 0.7,  
    "L3": 0.5  
  },  
  "reactivePower": {  
    "L1": 108.1,  
    "L2": 107.0,  
    "L3": 106.5  
  },  
  "seeAlso": [  
    "urn:ngsi-ld:SolarEnergy:items:XREG:08856151"  
  ],  
  "source": "",  
  "totalActivePower": 873.9,  
  "totalEnergyGenerated": 527.6,  
  "totalReactivePower": 110.8,  
  "voltage": 122.0,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Energy/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### SolarEnergy NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 SolarEnergy의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:SolarEnergy:id:BHDU:88967916",  
  "type": "SolarEnergy",  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [[  
        -35.589575,  
        -78.339812  
      ]]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Jai Singh Marg, Hanuman Road Area, Connaught Place",  
      "addressLocality": "New Delhi",  
      "addressRegion": "Delhi",  
      "addressCountry": "India",  
      "postalCode": "110001",  
      "postOfficeBoxNumber": ""  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": ""  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-01-10T01:49:09Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-01-10T01:50:52Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": "Solar Energy measured at resource 1"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Solar energy source 1"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Solar energy source 1"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SolarEnergy:items:DACI:25767721",  
      "urn:ngsi-ld:SolarEnergy:items:YVQJ:55840840"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:SolarEnergy:items:XREG:08856151"  
    ]  
  },  
  "totalActivePower": {  
    "type": "Property",  
    "value": 873.9  
  },  
  "phaseCurrent": {  
    "type": "Property",  
    "value": {  
      "L1": 111.5,  
      "L2": 109.3,  
      "L3": 111.0  
    }  
  },  
  "reactivePower": {  
    "type": "Property",  
    "value": {  
      "L1": 108.1,  
      "L2": 107.0,  
      "L3": 106.5  
    }  
  },  
  "voltage": {  
    "type": "Property",  
    "value": 122.0  
  },  
  "powerFactor": {  
    "type": "Property",  
    "value": {  
      "L1": 0.7,  
      "L2": 0.7,  
      "L3": 0.5  
    }  
  },  
  "current": {  
    "type": "Property",  
    "value": {  
      "L1": 1.2,  
      "L2": 1.2,  
      "L3": 1.3,  
      "N": 0.7  
    }  
  },  
  "totalReactivePower": {  
    "type": "Property",  
    "value": 110.8  
  },  
  "phaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L1": 120.5,  
      "L2": 116.4,  
      "L3": 119.8  
    }  
  },  
  "activePower": {  
    "type": "Property",  
    "value": {  
      "L1": 17.3,  
      "L2": 19.5,  
      "L3": 20.4  
    }  
  },  
  "dataDescriptor": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SolarEnergy:dataDescriptor:TTTK:11491249"  
  },  
  "energyGenerated": {  
    "type": "Property",  
    "value": 766.1  
  },  
  "maxSolarPowerMeasure": {  
    "type": "Property",  
    "value": 989.8  
  },  
  "frequency": {  
    "type": "Property",  
    "value": 50  
  },  
  "totalEnergyGenerated": {  
    "type": "Property",  
    "value": 527.6  
  },  
  "observationDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2022-01-20T20:02:52Z"  
    }  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Energy/context.jsonld"  
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
