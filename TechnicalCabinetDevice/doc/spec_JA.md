<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティTechnicalCabinetDevice（テクニカルキャビネットデバイス  
============================================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**技術キャビネットのデータモデルは、都市や郊外の環境に配置されるように設計されたデバイスの技術的な特性を記述することを目的としています。このデータモデルのこれらのキャビネットの主な目的は、都市の照明、信号、ビデオ、配電の制御、監視、読み取り、管理に必要な電気機器を保護することである。これらのキャビネットのいくつかの使用範囲は、テレフォニー、データ処理、気象観測所、光発電所、風力発電所、通信、ネットワーク、データ、ブレオプティクスなどのモジュラー装置のインストールのための追加の保護に拡張することができますなどです。*備考このデータモデルは、デバイス `Technical Cabinet` を記述するためのメインエンティティとして直接使用することも、`refDevice` 属性による参照を使用してデータモデル `DEVICE` のサブエンティティとして使用することも可能である。また、データモデル 'DEVICE'** を使用して、`refDeviceList` 属性で、それが含むすべてのコンポーネントのリストを参照することができます。  
のバージョンです。  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `application[array]`: 環境に関する本装置の目標用途。これらの値の組み合わせ。Enum:'commercial, distributionService, industrial, other, publicWorks, road, tertiary, urbanService' （商業、流通サービス、工業、その他、公共事業、道路、第三次、都市サービス  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: ブランド名  . Model: [https://schema.org/brand](https://schema.org/brand)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateLastReported[string]`: デバイスが正常にデータを報告した最後の時刻を示すタイムスタンプ。ISO8601 UTCフォーマットでの日付と時間  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `designMaterials[array]`: キャビネットを作るためのデザイン素材。これらの値の組み合わせ。Enum:'ABS-Plastic, アルミニウム, fiberGlass, galvanizedSteel, その他, ポリエステル, stainlessSteel'.  - `dimension[object]`: フォーマットは、3 項目のサブプロパティで構成される。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**CMT** はセンチメートルを表す。  - `documentation[string]`: デバイスのドキュメントへのリンク  . Model: [https://schema.org/URL](https://schema.org/URL)- `doorClosingMode[array]`: ドアクロージングモード。これらの値のうち一意の値。Enum:'fixedHandle, other, revolvingHandle, triangleHandle'.  - `doorCount[number]`: テクニカルキャビネットの扉数。  - `doorOpeningAngle[number]`: ドア開口角度を 0 度から 180 度までの 10 進数で表したもの。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**DD**はDecimal Degreesを表します。  - `doorType[string]`: 技術キャビネットのドアのタイプ。これらの値のうちユニークな値。Enum:'混合、その他、ソリッド、透明'  - `exteriorCoating[array]`: 内装のコーティング。これらの値の組み合わせ。Enum:'fiberGlass, other, plastic, polyester, polyesterResin, steel.  - `exteriorFinish[array]`: 外装仕上げ。これらの値の組み合わせ。Enum:'graffiti, other, raised, roughcast, smooth, textured'.  - `id[*]`: エンティティの一意な識別子  - `installationCondition[array]`: 以下の環境下での使用状態、可能性。これらの値の組み合わせ。Enum:'desert, dust, extremeCold, extremeClimate, extremeHeat, extremeHumidity, marine, none, other, saline, seismic, sand' （砂漠、塵、極寒、極端な気候、極端な熱、極端な湿度、海洋、なし、その他、塩害、地震、砂  - `installationMode[string]`: 地上基準システムに対するデバイスの位置決め。Enum:'aerial, ground, other, pole, roofing, underground, wall'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `interiorCoating[array]`: 内装のコーティング。これらの値の組み合わせ。Enum:'fiberGlass, heatInsulating, other, plastic, polyester, polyesterResin, steel' （ガラス繊維、断熱材、その他、プラスチック、ポリエステル樹脂、スチール  - `internalDimension[object]`: テクニカルキャビネット内の作業する場所に対応する内寸。フォーマットは、3 項目のサブプロパティで構成される。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**CMT** はセンチメートルを表す。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `manufacturerName[string]`: メーカー名  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumSystemVoltage[number]`: モジュール**に許容される最大システム電圧です。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**VLT**はVolt（ボルト）を表します。  - `modelName[string]`: メーカーから提示された機種名。  - `name[string]`: このアイテムの名称です。  - `operatingTemperature[object]`: 動作周囲温度範囲。寒さや暑さに対する耐性の最小値と最大値を示す。フォーマットは 2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**CEL** は摂氏を表す。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `possibilityOfUse[string]`: 活用の可能性。ユニークな値。Enum:'mixed, mobile, other, stationary'.  - `protectionIK[number]`: IK '*Mecanic Protection*' レベルは、国際電気技術委員会規格（EN 62-262）に基づき、電気機器の筐体が外部の機械的衝撃に対してどの程度保護されているかを数値で分類したものである。- IKは0（最小抵抗）から10（最大抵抗）まであり、これは衝撃エネルギー（単位ジュール）を表しています。  - `protectionIP[string]`: ジャンクションボックスのIP 'Ingress Protection'。国際電気標準会議規格（EN 60-529）に基づき、機械筐体や電気筐体の侵入、粉塵、偶発的な接触、水に対する保護の度合いを分類・評価したレベルです。1桁目1桁目：固体粒子に対する保護（一桁の数字：06または'X'）。2桁目3桁目：液体侵入保護（一桁目：09または'X'）。3桁目：危険箇所への立ち入りに対する個人保護（オプションの追加文字）。4桁目その他の保護（オプションで追加可能な文字）  - `protectionOthers[array]`: その他 技術筐体の保護。これらの値の組み合わせ。Enum:'abrasion, basement, dampProof, display, doorTearing, dust, forcedOpening, graffiti, insect, other, roofOverload, saltSpray, shielding, solar, vandalism, water' （擦過傷、地下室、防湿、ディスプレイ、ドア破り、ほこり、強制開錠、落書き、虫、その他  - `refDevice[*]`: このレコードで表現されたデータを取得するために使用された装置  - `refDeviceList[array]`: テクニカルキャビネットデバイスの内部にある[デバイス](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)の参照先リストです。  - `refPointOfInterest[*]`: PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)の参照は、観測とリンクしている。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `serialNumber[string]`: 容器のシリアル番号  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: NGSI エンティティタイプ。これは TechnicalCabinetDevice でなければなりません。  - `typeOfUse[string]`: 屋内・屋外環境での位置づけを考慮した使用方法。これらの値のうち一意の値。Enum:'indoor, mixed, outdoor, other'.  - `ventilationMode[array]`: 換気モード。これらの値の組み合わせ。Enum:'airConditioners, dehumidifier, none, other, selfVentilatedGills' （エアコン、除湿機、なし、その他、自己換気口  - `weight[number]`: 品目の重量。計測の単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使って与えられます。例えば、**KGM**はキログラムを表します。  . Model: [https://schema.org/weigth](https://schema.org/weigth)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `dateLastReported`  - `dimension`  - `id`  - `location`  - `type`  - `typeOfUse`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TechnicalCabinetDevice:    
  description: 'Technical Cabinet Device Data Model is intended to to describe the technical characteristics of the Device, designed to be placed in an urban or interurban environment. The main objective of these cabinets for this Data Model is to protect the electrical equipment necessary for the control, surveillance, reading and management of urban lighting, signaling, video and electrical distribution. The scope of use of some of these cabinets can extend to an additional protection for installations of modular apparatuses of telephony, data processing, meteorological stations, photo-voltaic stations, wind turbines stations, telecommunications, networks, data, bre Optics , etc. *Remark* : This Data Model can be used directly as a main entity to describe the device `Technical Cabinet`  or as a sub-entity of the Data Model  `DEVICE` using a reference by the `refDevice` attribute. It can also refer to the list of all the components it contains, with the `refDeviceList` attribute, using the Data Model ''DEVICE'''    
  properties:    
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
    application:    
      description: 'Target application of the Device regarding the environment. A combination of these values. Enum:''commercial, distributionService, industrial, other, publicWorks, road, tertiary, urbanService'''    
      items:    
        enum:    
          - commercial    
          - distributionService    
          - industrial    
          - other    
          - publicWorks    
          - road    
          - tertiary    
          - urbanService    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: 'Name of the brand'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
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
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    designMaterials:    
      description: 'Design materials to build the cabinet. A combination of  these values. Enum:''ABS-Plastic, aluminum, fiberGlass, galvanizedSteel, other, polyester, stainlessSteel'''    
      items:    
        enum:    
          - ABS-Plastic    
          - aluminum    
          - fiberGlass    
          - galvanizedSteel    
          - other    
          - polyester    
          - stainlessSteel    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    dimension:    
      description: 'The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter.'    
      properties:    
        depth:    
          description: 'Property. '    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          description: 'Property. '    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    documentation:    
      description: 'A link to device''s documentation'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    doorClosingMode:    
      description: 'Door closing mode. A unique value of these values. Enum:''fixedHandle, other, revolvingHandle, triangleHandle'''    
      items:    
        enum:    
          - fixedHandle    
          - other    
          - revolvingHandle    
          - triangleHandle    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    doorCount:    
      description: 'Count of doors of the technical Cabinet.'    
      type: number    
      x-ngsi:    
        type: Property    
    doorOpeningAngle:    
      description: 'Door opening angle expressed in decimal degrees with a range from 0 to 180 degree. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **DD** represents Decimal Degrees.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    doorType:    
      description: 'Type of door of the technical Cabinet. A unique value of these values. Enum:''mixed, other, solid, transparent'''    
      enum:    
        - mixed    
        - other    
        - solid    
        - transparent    
      type: string    
      x-ngsi:    
        type: Property    
    exteriorCoating:    
      description: 'Interior Coating. A combination of these values. Enum:''fiberGlass, other, plastic, polyester, polyesterResin, steel'    
      items:    
        enum:    
          - fiberGlass    
          - other    
          - plastic    
          - polyester    
          - polyesterResin    
          - steel    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    exteriorFinish:    
      description: 'Exterior finish. A combination of these values. Enum:''graffiti, other, raised, roughcast, smooth, textured'''    
      items:    
        enum:    
          - graffiti    
          - other    
          - raised    
          - roughcast    
          - smooth    
          - textured    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &technicalcabinetdevice_-_properties_-_owner_-_items_-_anyof    
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
    installationCondition:    
      description: 'Condition and possibility of use in the following environments. A combination of these values. Enum:''desert, dust, extremeCold, extremeClimate, extremeHeat, extremeHumidity, marine, none, other, saline, seismic, sand'''    
      items:    
        enum:    
          - desert    
          - dust    
          - extremeCold    
          - extremeClimate    
          - extremeHeat    
          - extremeHumidity    
          - marine    
          - none    
          - other    
          - saline    
          - seismic    
          - sand    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    installationMode:    
      description: 'Positioning of the device in relation to a ground reference system. Enum:''aerial, ground, other, pole, roofing, underground, wall'''    
      enum:    
        - aerial    
        - ground    
        - other    
        - pole    
        - roofing    
        - underground    
        - wall    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    interiorCoating:    
      description: 'Interior Coating. A combination of these values. Enum:''fiberGlass, heatInsulating, other, plastic, polyester, polyesterResin, steel'''    
      items:    
        enum:    
          - fiberGlass    
          - heatInsulating    
          - other    
          - plastic    
          - polyester    
          - polyesterResin    
          - steel    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    internalDimension:    
      description: 'Internal dimension corresponding to the place to work inside the technical cabinet. The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        width:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        type: Geoproperty    
    manufacturerName:    
      description: 'Name of the manufacturer'    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    maximumSystemVoltage:    
      description: 'Maximum system voltage permitted for the **module**. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
    modelName:    
      description: 'Name of the model as given by the manufacturer.'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operatingTemperature:    
      description: 'Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius.'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: -80    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *technicalcabinetdevice_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    possibilityOfUse:    
      description: 'Possibility of use. A unique value. Enum:''mixed, mobile, other, stationary'''    
      enum:    
        - mixed    
        - mobile    
        - other    
        - stationary    
      type: string    
      x-ngsi:    
        type: Property    
    protectionIK:    
      description: 'IK ''*Mecanic Protection*'' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)'    
      type: number    
      x-ngsi:    
        type: Property    
    protectionIP:    
      description: 'IP ''Ingress Protection'' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). First digit: Solid particle protection (Single numeral: 06 or ''X''). Second digit: Liquid ingress protection (Single numeral: 09 or ''X'' ).Third digit: Personal Protection against access to dangerous parts (optional additional letter). Fourth digit: Other protections (optional additional letter)'    
      type: string    
      x-ngsi:    
        type: Property    
    protectionOthers:    
      description: 'Others protection of the technical cabinet. A combination of these values. Enum:''abrasion, basement, dampProof, display, doorTearing, dust, forcedOpening, graffiti, insect, other, roofOverload, saltSpray, shielding, solar, vandalism, water'''    
      items:    
        enum:    
          - abrasion    
          - basement    
          - dampProof    
          - display    
          - doorTearing    
          - dust    
          - forcedOpening    
          - graffiti    
          - insect    
          - other    
          - roofOverload    
          - saltSpray    
          - shielding    
          - solar    
          - vandalism    
          - water    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The device used to obtain the data expressed by this record'    
      x-ngsi:    
        type: Relationship    
    refDeviceList:    
      description: 'A list of reference to the [Devices](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which are inside the technical Cabinet Device.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation.'    
      x-ngsi:    
        type: Relationship    
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
    serialNumber:    
      description: 'Serial number of the container'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be TechnicalCabinetDevice'    
      enum:    
        - TechnicalCabinetDevice    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfUse:    
      description: 'Accepted use regarding its positioning in an indoor / outdoor environment. A unique value of these values. Enum:''indoor, mixed, outdoor, other'''    
      enum:    
        - indoor    
        - mixed    
        - outdoor    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    ventilationMode:    
      description: 'Ventilation mode. A combination of these values. Enum:''airConditioners, dehumidifier, none, other, selfVentilatedGills'''    
      items:    
        enum:    
          - airConditioners    
          - dehumidifier    
          - none    
          - other    
          - selfVentilatedGills    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    weight:    
      description: 'Weight of the item. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilograms'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/weigth    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - typeOfUse    
    - dimension    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/TechnicalCabinetDevice/schema.json    
  x-model-tags: Energy    
  x-version: ""    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### TechnicalCabinetDevice NGSI-v2 key-value の例。  
TechnicalCabinetDeviceをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返されます。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-TechnicalCabinetDevice:MNCA-TCD-AP-T2-F1-022",  
  "type": "TechnicalCabinetDevice",  
  "name": "MNCA-TCD-AP-T2-F1-022",  
  "alternateName": "AirPort – global Observation",  
  "description": "Technical Cabinet description",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      7.196545,  
      43.664810  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport Terminal 2 - Floor 1"  
  },  
  "areaServed": "Nice Aeroport",  
  "refDeviceList": [  
    "urn:ngsi-ld:Device:NCE-CE-025",  
    "urn:ngsi-ld:Device:NCE-FU-048",  
    "urn:ngsi-ld:Device:NCE-CE-058"  
  ],  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "brandName": "EATON",  
  "modelName": "xEnergy L",  
  "manufacturerName": "ElDorado",  
  "serialNumber": "L257589A4587J56",  
  "application": [  
    "industrial",  
    "distributionService"  
  ],  
  "typeOfUse": "outdoor",  
  "installationMode": "ground",  
  "installationCondition": [  
    "none"  
  ],  
  "possibilityOfUsed": "stationary",  
  "documentation": "https://www.myTechnicalCabinet.fr",  
  "deviceOwner": [  
    "Airport-Division Maintenance"  
  ],  
  "dimension": {  
    "width": 150,  
    "height": 175,  
    "depth": 75  
  },  
  "weight": 60,  
  "internalDimension": {  
    "width": 140,  
    "height": 165,  
    "depth": 70  
  },  
  "protectionIP": "65",  
  "protectionIK": 10,  
  "maximumSystemVoltage": 1000,  
  "operatingTemperature": {  
    "min": -40,  
    "max": 100  
  },  
  "protectionOthers": [  
    "dust",  
    "forcedOpening",  
    "saltSpray",  
    "abrasion",  
    "doorTearing",  
    "vandalism"  
  ],  
  "doorCount": 2,  
  "doorType": "solid",  
  "doorOpeningAngle": 180,  
  "doorClosingMode": [  
    "fixedHandle"  
  ],  
  "designMaterials": [  
    "stainlessSteel",  
    "polyester"  
  ],  
  "interiorCoating": [  
    "heatInsulating",  
    "polyesterResin"  
  ],  
  "exteriorCoating": [  
    "polyesterResin"  
  ],  
  "exteriorFinish": [  
    "roughcast"  
  ],  
  "ventilationMode": [  
    "selfVentilatedGills"  
  ]  
}  
```  
</details>  
#### TechnicalCabinetDevice NGSI-v2 正規化例  
TechnicalCabinetDevice を JSON-LD 形式で正規化した例です。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-TechnicalCabinetDevice:MNCA-TCD-AP-T2-F1-022",  
  "type": "TechnicalCabinetDevice",  
  "name": {  
    "type": "Text",  
    "value": "MNCA-TCD-AP-T2-F1-022"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "AirPort – global Observation"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Technical Cabinet description"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "point",  
      "coordinates": [  
        7.196545,  
        43.664810  
      ]  
    }  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport Terminal 2 - Floor 1"  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Aeroport"  
  },  
  "refDeviceList": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Device:NCE-CE-025",  
      "urn:ngsi-ld:Device:NCE-FU-048",  
      "urn:ngsi-ld:Device:NCE-CE-058"  
    ]  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "EATON"  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "xEnergy L"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "ElDorado"  
  },  
  "serialNumber": {  
    "type": "Text",  
    "value": "L257589A4587J56"  
  },  
  "application": {  
    "type": "array",  
    "value": [  
      "industrial",  
      "distributionService"  
    ]  
  },  
  "typeOfUse": {  
    "type": "Text",  
    "value": "outDoor"  
  },  
  "installationMode": {  
    "type": "Text",  
    "value": "ground"  
  },  
  "installationCondition": {  
    "type": "array",  
    "value": [  
      "none"  
    ]  
  },  
  "possibilityOfUsed": {  
    "type": "Text",  
    "value": "stationary"  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myTechnicalCabinet.fr"  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "Airport-Division Maintenance"  
    ]  
  },  
  "dimension": {  
    "type": "StructuredObject",  
    "value": {  
      "width": 150,  
      "height": 175,  
      "depth": 75  
    }  
  },  
  "weight": {  
    "type": "Number",  
    "value": 60  
  },  
  "internalDimension": {  
    "type": "StructuredObject",  
    "value": {  
      "width": 140,  
      "height": 165,  
      "depth": 70  
    }  
  },  
  "protectionIP": {  
    "type": "Text",  
    "value": "65"  
  },  
  "protectionIK": {  
    "type": "Number",  
    "value": 10  
  },  
  "maximumSystemVoltage": {  
    "type": "Number",  
    "value": 1000  
  },  
  "operatingTemperature": {  
    "type": "StructuredObject",  
    "value": {  
      "min": -40,  
      "max": 100  
    }  
  },  
  "protectionOthers": {  
    "type": "array",  
    "value": [  
      "dust",  
      "forcedOpening",  
      "saltSpray",  
      "abrasion",  
      "doorTearing",  
      "vandalism"  
    ]  
  },  
  "doorCount": {  
    "type": "Number",  
    "value": 2  
  },  
  "doorType": {  
    "type": "Text",  
    "value": "solid"  
  },  
  "doorOpeningAngle": {  
    "type": "Number",  
    "value": 180  
  },  
  "doorClosingMode": {  
    "type": "Text",  
    "value": "fixedHandle"  
  },  
  "designMaterials": {  
    "type": "array",  
    "value": [  
      "stainlessSteel",  
      "polyester"  
    ]  
  },  
  "interiorCoating": {  
    "type": "array",  
    "value": [  
      "heatInsulating",  
      "polyesterResin"  
    ]  
  },  
  "exteriorCoating": {  
    "type": "array",  
    "value": [  
      "polyesterResin"  
    ]  
  },  
  "exteriorFinish": {  
    "type": "array",  
    "value": [  
      "roughcast"  
    ]  
  },  
  "ventilationMode": {  
    "type": "array",  
    "value": [  
      "selfVentilatedGills"  
    ]  
  }  
}  
```  
</details>  
#### TechnicalCabinetDevice NGSI-LD key-value の例。  
TechnicalCabinetDeviceをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-TechnicalCabinetDevice:MNCA-TCD-AP-T2-F1-022",  
    "type": "TechnicalCabinetDevice",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Airport Terminal 2 - Floor 1"  
    },  
    "alternateName": "AirPort \u2013 global Observation",  
    "application": [  
        "industrial",  
        "distributionService"  
    ],  
    "areaServed": "Nice Aeroport",  
    "brandName": "EATON",  
    "dateLastReported": "2020-03-17T08:45:00Z",  
    "description": "Technical Cabinet description",  
    "designMaterials": [  
        "stainlessSteel",  
        "polyester"  
    ],  
    "deviceOwner": [  
        "Airport-Division Maintenance"  
    ],  
    "dimension": {  
        "width": 150,  
        "height": 175,  
        "depth": 75  
    },  
    "documentation": "https://www.myTechnicalCabinet.fr",  
    "doorClosingMode": [  
        "fixedHandle"  
    ],  
    "doorCount": 2,  
    "doorOpeningAngle": 180,  
    "doorType": "solid",  
    "exteriorCoating": [  
        "polyesterResin"  
    ],  
    "exteriorFinish": [  
        "roughcast"  
    ],  
    "installationCondition": [  
        "none"  
    ],  
    "installationMode": "ground",  
    "interiorCoating": [  
        "heatInsulating",  
        "polyesterResin"  
    ],  
    "internalDimension": {  
        "width": 140,  
        "height": 165,  
        "depth": 70  
    },  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            7.196545,  
            43.66481  
        ]  
    },  
    "manufacturerName": "ElDorado",  
    "maximumSystemVoltage": 1000,  
    "modelName": "xEnergy L",  
    "name": "MNCA-TCD-AP-T2-F1-022",  
    "operatingTemperature": {  
        "min": -40,  
        "max": 100  
    },  
    "possibilityOfUsed": "stationary",  
    "protectionIK": 10,  
    "protectionIP": "65",  
    "protectionOthers": [  
        "dust",  
        "forcedOpening",  
        "saltSpray",  
        "abrasion",  
        "doorTearing",  
        "vandalism"  
    ],  
    "refDeviceList": [  
        "urn:ngsi-ld:Device:NCE-CE-025",  
        "urn:ngsi-ld:Device:NCE-FU-048",  
        "urn:ngsi-ld:Device:NCE-CE-058"  
    ],  
    "serialNumber": "L257589A4587J56",  
    "typeOfUse": "outdoor",  
    "ventilationMode": [  
        "selfVentilatedGills"  
    ],  
    "weight": 60,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TechnicalCabinetDevice NGSI-LD 正規化例  
TechnicalCabinetDevice を JSON-LD 形式で正規化した例です。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-TechnicalCabinetDevice:MNCA-TCD-AP-T2-F1-022",  
    "type": "TechnicalCabinetDevice",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "Airport Terminal 2 - Floor 1"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "AirPort \u2013 global Observation"  
    },  
    "application": {  
        "type": "Property",  
        "value": [  
            "industrial",  
            "distributionService"  
        ]  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Aeroport"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "EATON"  
    },  
    "dateLastReported": {  
        "type": "Property",  
        "value": {  
            "type": "DateTime",  
            "value": "2020-03-17T08:45:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Technical Cabinet description"  
    },  
    "designMaterials": {  
        "type": "Property",  
        "value": [  
            "stainlessSteel",  
            "polyester"  
        ]  
    },  
    "dimension": {  
        "type": "Property",  
        "value": {  
            "width": 150,  
            "height": 175,  
            "depth": 75  
        }  
    },  
    "documentation": {  
        "type": "Property",  
        "value": "https://www.myTechnicalCabinet.fr"  
    },  
    "doorClosingMode": {  
        "type": "Property",  
        "value": "fixedHandle"  
    },  
    "doorCount": {  
        "type": "Property",  
        "value": 2  
    },  
    "doorOpeningAngle": {  
        "type": "Property",  
        "value": 180  
    },  
    "doorType": {  
        "type": "Property",  
        "value": "solid"  
    },  
    "exteriorCoating": {  
        "type": "Property",  
        "value": [  
            "polyesterResin"  
        ]  
    },  
    "exteriorFinish": {  
        "type": "Property",  
        "value": [  
            "roughcast"  
        ]  
    },  
    "installationCondition": {  
        "type": "Property",  
        "value": [  
            "none"  
        ]  
    },  
    "installationMode": {  
        "type": "Property",  
        "value": "ground"  
    },  
    "interiorCoating": {  
        "type": "Property",  
        "value": [  
            "heatInsulating",  
            "polyesterResin"  
        ]  
    },  
    "internalDimension": {  
        "type": "Property",  
        "value": {  
            "width": 140,  
            "height": 165,  
            "depth": 70  
        }  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "point",  
            "coordinates": [  
                7.196545,  
                43.66481  
            ]  
        }  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "ElDorado"  
    },  
    "maximumSystemVoltage": {  
        "type": "Property",  
        "value": 1000  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "xEnergy L"  
    },  
    "name": {  
        "type": "Property",  
        "value": "MNCA-TCD-AP-T2-F1-022"  
    },  
    "operatingTemperature": {  
        "type": "Property",  
        "value": {  
            "min": -40,  
            "max": 100  
        }  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "Airport-Division Maintenance"  
        ]  
    },  
    "possibilityOfUsed": {  
        "type": "Property",  
        "value": "stationary"  
    },  
    "protectionIK": {  
        "type": "Property",  
        "value": 10  
    },  
    "protectionIP": {  
        "type": "Property",  
        "value": "65"  
    },  
    "protectionOthers": {  
        "type": "Property",  
        "value": [  
            "dust",  
            "forcedOpening",  
            "saltSpray",  
            "abrasion",  
            "doorTearing",  
            "vandalism"  
        ]  
    },  
    "refDeviceList": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:Device:NCE-CE-025",  
            "urn:ngsi-ld:Device:NCE-FU-048",  
            "urn:ngsi-ld:Device:NCE-CE-058"  
        ]  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "L257589A4587J56"  
    },  
    "typeOfUse": {  
        "type": "Property",  
        "value": "outDoor"  
    },  
    "ventilationMode": {  
        "type": "Property",  
        "value": [  
            "selfVentilatedGills"  
        ]  
    },  
    "weight": {  
        "type": "Property",  
        "value": 60  
    },  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
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
