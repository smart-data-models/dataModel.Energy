<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
事業者ソーラーエナジー  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Energy/blob/master/SolarEnergy/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**太陽光発電のデータモデル。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `activePower[object]`: 実際の値は、交流の各相の名前と同じ名前のサブプロパティによって管理される。L1、L2、L3。  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: 電流。実際の値は、交流の各相と中性線につき1つのサブプロパティで伝達される。L1、L2、L3、N。  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `dataDescriptor[string]`: データ記述子実体を指すURI  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `energyGenerated[number]`: この観測に対応するエネルギー資源から特定の時間範囲に発生したエネルギー。  - `frequency[number]`: この観測に対応する実体から観測された周波数。  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `maxSolarPowerMeasure[number]`: 発電可能な最大太陽エネルギーの指標。  - `name[string]`: このアイテムの名称です。  - `observationDateTime[string]`: 最後に報告された観測時刻。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `phaseCurrent[object]`: 各相の電流。三相の有効電力を次の順序で並べたもの。[R Y B］  - `phaseVoltage[object]`: 各相と中性導体間の電圧。実際の値は、交流の各相ごとに1つのサブプロパティで伝えられる。L1、L2、L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `powerFactor[object]`: 各相の力率。実際の値は、交流の各相ごとに1つのサブプロパティで伝達される。L1、L2、L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `reactivePower[object]`: 基本周波数無効電力。実際の値は、交流の各相の名前と同じ名前のサブプロパティによって伝達される。L1、L2、L3。  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `totalActivePower[number]`: 全相で消費される総活動電力。  - `totalEnergyGenerated[number]`: この観測に対応するエネルギー資源による総発電量。  - `totalReactivePower[number]`: 全相の総無効電力。  - `type[string]`: NGSI Entityタイプ。SolarEnergyでなければならない。  - `voltage[number]`: この観測に対応するエンティティのVoltageの値。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SolarEnergy:    
  description: 'A Data Model for Solar Energy generation.'    
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
        units: 'watt (W).Active power consumed per phase'    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    current:    
      description: 'Electrical current. The actual values will be conveyed by one subproperty per alternating current phase and the neutral wire: L1, L2, L3 and N.'    
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
        units: 'Ampers (A)'    
    dataDescriptor:    
      description: 'URI pointing to the data-descriptor entity'    
      type: string    
      x-ngsi:    
        type: Relationship    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    energyGenerated:    
      description: 'Energy generated over a specific time range from the energy resource corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    frequency:    
      description: 'Frequency observed from the entity corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &solarenergy_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    maxSolarPowerMeasure:    
      description: 'A measure of maximum solar energy that can be generated.'    
      type: number    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *solarenergy_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
        units: 'Volts (V)'    
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
        units: '-1 to +1'    
    reactivePower:    
      description: 'Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
        units: 'volts-ampere-reactive (VAr)'    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalActivePower:    
      description: 'Total active power consumed by all phases.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalEnergyGenerated:    
      description: 'Total energy generated by the energy resource corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    totalReactivePower:    
      description: 'Total reactive power for all phases.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be SolarEnergy'    
      enum:    
        - SolarEnergy    
      type: string    
      x-ngsi:    
        type: Property    
    voltage:    
      description: 'The value of Voltage in the entity corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://voc.iudx.org.in/SolarEnergy    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### SolarEnergy NGSI-v2 key-value の例。  
ここでは、SolarEnergyをJSON-LD形式でkey-valuesにした例を示します。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
  "voltage": 122.0  
}  
```  
</details>  
#### SolarEnergy NGSI-v2 正規化例  
以下は、SolarEnergyをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
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
  "id": "urn:ngsi-ld:SolarEnergy:id:BHDU:88967916",  
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
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:SolarEnergy:items:DACI:25767721",  
      "urn:ngsi-ld:SolarEnergy:items:YVQJ:55840840"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:SolarEnergy:items:XREG:08856151"  
    ]  
  },  
  "type": "SolarEnergy",  
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
    "type": "Relationship",  
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
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.Energy/context.jsonld"  
  ]  
}  
```  
</details>  
#### SolarEnergy NGSI-LD キー値例  
ここでは、SolarEnergyをJSON-LD形式でkey-valuesにした例を示します。これは `options=keyValues` を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### SolarEnergy NGSI-LD 正規化例  
以下は、SolarEnergyをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "location": {  
        "type": "Property",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -35.589575,  
                -78.339812  
            ]  
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
    "id": "urn:ngsi-ld:SolarEnergy:id:BHDU:88967916",  
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
    "type": "SolarEnergy",  
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
        "type": "object",  
        "value": "urn:ngsi-ld:SolarEnergy:dataDescriptor:TTTK:11491249"  
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
        "https://smart-data-models.github.io/dataModel.Energy/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
