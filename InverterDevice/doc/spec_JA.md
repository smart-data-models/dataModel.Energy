<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティインバーターデバイス  
================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Energy/blob/master/InverterDevice/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述である。**このデータモデルは、インバータの機械的、電気的特性を、入力として供給される*DC - 直流情報*と出力として返される*AC - 交流情報*に従って記述することを意図している。*備考このデータモデルは、デバイス[Inverter]を記述する主エンティティとして直接使用することも、[refDevice]属性による参照を用いてデータモデル｛DEVICE｝の副エンティティとして使用することもできる。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `application[array]`: 環境に関する本デバイスのターゲットアプリケーション。ユニークな値。Enum:'electricMobility, energyStorage, emergencyStorage, lighting, industrialStorage, houseHoldStorage, robotics, production, other' （電気移動、エネルギー貯蔵、緊急貯蔵、照明、産業貯蔵、家庭貯蔵、ロボット工学、生産、その他  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: アイテムのブランド名  . Model: [https://schema.org/brand](https://schema.org/brand)- `coolingSystem[string]`: デバイスの冷却方式。Enum:'Convection, OptiCool, Regulated-fan, Other' （対流式、オプティクール、調節機能付きファン、その他  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateLastReported[string]`: デバイスが正常にデータを報告した最後の時刻を示すタイムスタンプ。ISO8601 UTCフォーマットでの日付と時間  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `dimension[object]`: Panel の外形寸法。フォーマットは、3 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与え る。例えば、**CMT** はセンチメートルを表す。  - `documentation[string]`: 技術ドキュメント（インストール/メンテナンス/使用済み）  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: エンティティの一意な識別子  - `installationCondition[array]`: 以下の環境下での使用条件と可能性。Enum:'extremeHeat, extremeCold, extremeHumidity, extremeClimate, desert, sand, marine, saline, dust, seismic, other'（砂漠、砂浜、海洋、塩水、粉塵、地震、その他）。  - `installationMode[string]`: 地上基準系に対する装置の位置決め。一意の値。Enum:'aerial, ground, pole, roofing, underGround, wall, other'.  - `inverterStatus[array]`: インバータの状態。値の組み合わせ。  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `mPPTPVVoltageDC[object]`: 最小・最大光起電力範囲、MPPT を許可する。フォーマットは、2 項目のサブプロパティで構成する。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与え る。例えば，**VLT** は Volt を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `manufacturerName[string]`: メーカー名 品名  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maxInputCurrentParallelAssembly[number]`: Max.パラレルアセンブリを使用した場合の最大入力電流です。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて記載する。例えば、**AMP**はAmpere（アンペア）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxOutputPowerAC[number]`: Maximum Power または Apparent Power。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**D46**はVolt Ampereを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: アイテムのモデル名  . Model: [https://schema.org/model](https://schema.org/model)- `moduleYieldRate[object]`: デバイスの歩留まり。フォーマットは2項目（欧州規格-メーカー規格）のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**P1** は Percent（パーセント）を表す。  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `name[string]`: このアイテムの名称です。  - `nbInputParallelDC[string]`: 最大入力数（並列）  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `nbMPPTrackersDC[number]`: MPPトラッカー数  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `noiseLevel[number]`: 本装置の音響パワーレベル。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を使用して示されます。例えば、**2N**はDecibel（デシベル）を表します。  . Model: [http://schema.org/Number](http://schema.org/Number)- `nominalAmpereAC[number]`: 公称アンペア数 *(コードI)*。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**AMP**はAmpere（アンペア）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalAmpereDC[number]`: 公称アンペア数。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**AMP**はAmpere（アンペア）を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequencyAC[number]`: 公称周波数。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**HTZ** はヘルツを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequencyDC[number]`: 公称周波数。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**HTZ** はヘルツを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalPowerAC[number]`: 公称電力．単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**WTT** はワットを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalPowerDC[number]`: cos phi=1 のときの公称電力または最大電力係数。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**WTT**はWattを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltageAC[number]`: 公称電池電圧 *(Code U)*。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**VLT**はVolt（ボルト）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltageDC[number]`: 公称電圧。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示される。例えば、**VLT**はVolt（ボルト）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAirHumidity[object]`: 動作環境 Air Humidity の範囲。フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**P1** は Percent を表す。  - `operatingAmpereAC[object]`: 最小・最大許容アンペア...フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**AMP** は Ampere を表す。  . Model: [http://schema.org/Number](http://schema.org/Number)- `operatingAmpereDC[object]`: 最小・最大許容アンペア...フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与する。例えば、**AMP** は Ampere を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingFrequencyAC[object]`: 許容される最小頻度および最大頻度。フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与え る。例えば、**HTZ** はヘルツを表す。  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `operatingFrequencyDC[object]`: 許容される最小頻度および最大頻度。フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与え る。例えば、**HTZ** はヘルツを表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingTemperature[object]`: 動作周囲温度範囲。寒さや暑さに対する耐性の最小値と最大値を示す。フォーマットは 2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**CEL** は摂氏を表す。  - `operatingVoltageAC[object]`: 許容される最小電圧と最大電圧。フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**VLT** は Volt を表す。  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `operatingVoltageDC[object]`: 許容される最小電圧と最大電圧。フォーマットは、2 項目のサブプロパティで構成される。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて与える。例えば、**VLT** は Volt を表す。  . Model: [https://schema.org/Number](https://schema.org/Number)- `overVoltageCategory[string]`: 過電圧カテゴリ。- I : 適切な低レベルの過渡的過電圧のある回路に接続する。- II : 主絶縁および付加絶縁（アース端子）。- III : 特定の仕様に従った信頼性と可用性を持つ固定設備。- IV : 電気メーターや主材料の過電流保護など、電気設備の起点にある材料。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `phaseType[string]`: 位相の種類。一意の値。Enum:'singlePhase,threePhase'.  - `possibilityOfUse[string]`: 使用可能なこと。Enum:'混合、モバイル、据え置き、その他'  - `powerFactorAC[number]`: cos Φの力率  . Model: [http://schema.org/Number](http://schema.org/Number)- `protectionClassSLK[string]`: 保護等級(SKL).- 0 : 主絶縁、アース接続なし。- 1 : 主絶縁と付加絶縁（アース端子）。- 2 : 2重または強化絶縁（主絶縁の2倍に相当）、アクセス可能な金属部分なし。- 3 : 超低安全電圧(SELV)(最大50V)で動作します。  - `protectionIK[number]`: IK '*Mecanic Protection*' レベルは、国際電気技術委員会規格（EN 62-262）に基づき、電気機器の筐体が外部の機械的衝撃に対してどの程度保護されているかを数値で分類したものである。- IKは0（最小抵抗）から10（最大抵抗）まであり、これは衝撃エネルギー（単位ジュール）を表しています。  . Model: [https://schema.org/Number](https://schema.org/Number)- `protectionIP[string]`: ジャンクション・ボックスのIP '*Ingress Protection*'。国際電気標準会議規格（EN 60-529）に基づき、機械筐体や電気筐体の侵入、粉塵、偶発的な接触、水に対する保護の度合いを分類・評価したレベルです。- 1桁目1桁目：固体粒子に対する保護等級（数字1桁：0～6または'X'）。- 2桁目3 桁目：危険な部品へのアクセスに対する個人保護（オプションで追加可能な文字） - 4 桁目：その他の保護（オプションで追加可能な文字）。4桁目：その他の保護（オプションで追加可能な文字）。  - `refDevice[*]`: 2番目のリンクとして使用される場合、メインエンティティ[デバイス](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)への参照。  - `refPointOfInterest[*]`: PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)の参照は、観測とリンクしている。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `self-consumption[number]`: ニグス中の自己消費。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて付与される。  例えば、**WTT**はワットを表す。  . Model: [http://schema.org/Number](http://schema.org/Number)- `serialNumber[string]`: 商品のシリアルナンバー  . Model: [https://schema.org/brand](https://schema.org/brand)- `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `startingVoltageDC[number]`: 始動電圧。単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示されます。例えば、**VLT**はVolt（ボルト）を表します。  . Model: [https://schema.org/Number](https://schema.org/Number)- `supplyPhaseNb[number]`: 電源フェーズ数  . Model: [https://schema.org/Number](https://schema.org/Number)- `topology[string]`: インストールのトポロジーの説明。  - `type[string]`: NGSI Entity タイプ。InverterDeviceでなければならない。  - `typeOfUse[string]`: 屋内／屋外環境での位置づけに関する使用可否。Enum:'屋内, 屋外, 混合, その他'.  - `weight[number]`: 重量単位コード（テキスト）は、[UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)を用いて示されます。例えば、**KGM**はキログラムを表します。  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `dateLastReported`  - `id`  - `location`  - `phaseType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
データモデルに関する追加情報。このデータモデルは、デバイス[INVERTER]を記述するメインエンティティとして直接使用することも、`refDevice`属性による参照を用いてデータモデル[DEVICE]のサブエンティティとして使用することもできる。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
InverterDevice:    
  description: 'The data model is intended to describe the mechanical, electrical characteristics of an Inverter according to *DC - Direct Current Information* supplied as input and *AC - Alternating Current Information*  returned as output. *Remark*: This Data Model can be used directly as a main entity to describe the device [Inverter] or as a sub-entity of the Data Model {DEVICE] using a reference by the [refDevice] attribute.'    
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
      description: 'Target application of the Device regarding the environment. A unique value. Enum:''electricMobility, energyStorage, emergencyStorage, lighting, industrialStorage, houseHoldStorage, robotics, production, other'''    
      items:    
        enum:    
          - electricMobility    
          - energyStorage    
          - emergencyStorage    
          - lighting    
          - industrialStorage    
          - houseHoldStorage    
          - robotics    
          - production    
          - other    
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
      description: 'Brand Name of the item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    coolingSystem:    
      description: ' Cooling System of the Device. Enum:''Convection, OptiCool, Regulated-fan, Other'''    
      enum:    
        - Convection    
        - OptiCool    
        - Regulated-fan    
        - Other    
      type: string    
      x-ngsi:    
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
      description: 'A timestamps which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat'    
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
    dimension:    
      description: 'External dimension of a Panel. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter'    
      properties:    
        depth:    
          minimum: 0    
          type: number    
        height:    
          minimum: 0    
          type: number    
        length:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
        units: Centimeters    
    documentation:    
      description: 'Technical Documentation (Installation / maintenance / used)'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    id:    
      anyOf: &inverterdevice_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Condition and possibility of use in the following environments. Enum:''extremeHeat, extremeCold, extremeHumidity, extremeClimate, desert, sand, marine, saline, dust, seismic, other''.'    
      items:    
        enum:    
          - extremeHeat    
          - extremeCold    
          - extremeHumidity    
          - extremeClimate    
          - desert    
          - sand    
          - marine    
          - saline    
          - dust    
          - seismic    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    installationMode:    
      description: 'Positioning of the device in relation to a ground reference system. A unique value. Enum:''aerial, ground, pole, roofing, underGround, wall, other'''    
      enum:    
        - aerial    
        - ground    
        - pole    
        - roofing    
        - underGround    
        - wall    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    inverterStatus:    
      description: 'Status of the inverter. A combination of values.'    
      items:    
        enum:    
          - 00-OnSector    
          - 01-PowerFailure/OnBattery    
          - 02-LossCommunication    
          - 03-BatteryFault    
          - 04-SystemShutDown    
          - 05-TensionDip    
          - 06-OverVoltage    
          - 07-VoltageDrop    
          - 08-VoltageIncrease    
          - 09-LineNoise    
          - 10-FrequencyVariation    
          - 11-TransientDistortion    
          - 12-HarmonicDistortion    
        type: string    
      type: array    
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
    mPPTPVVoltageDC:    
      description: 'Minimum and Maximum Photo-voltaic voltage range, MPPT allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    manufacturerName:    
      description: 'Manufacturer Name of the item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/manufacturer    
        type: Property    
    maxInputCurrentParallelAssembly:    
      description: 'Max. Current Input with an Parallel Assembly. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
    maxOutputPowerAC:    
      description: 'Maximum Power or Apparent Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **D46** represents Volt Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: 'Volt Ampere'    
    modelName:    
      description: 'Model name of the item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/model    
        type: Property    
    moduleYieldRate:    
      description: 'Yield Rate of the Device. The format is structured by a sub-property of 2 items (European Standard - Manufacturer Standard). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent'    
      properties:    
        eta:    
          type: number    
        euro:    
          type: number    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nbInputParallelDC:    
      description: 'Maximum Number of inputs (in parallel)'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    nbMPPTrackersDC:    
      description: 'Number of MPP trackers'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number.    
        type: Property    
    noiseLevel:    
      description: 'Sound Power level of the Device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **2N** represents Decibel'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: dB    
    nominalAmpereAC:    
      description: 'Nominal Amperage *(Code I)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
    nominalAmpereDC:    
      description: 'Nominal Amperage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
    nominalFrequencyAC:    
      description: 'Nominal Frequency. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hertz    
    nominalFrequencyDC:    
      description: ' Nominal Frequency. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hertz    
    nominalPowerAC:    
      description: 'Nominal Power . The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **WTT** represents Watt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt    
    nominalPowerDC:    
      description: 'Nominal Power or Maximum Power factor for cos phi=1. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **WTT** represents Watt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Watt    
    nominalVoltageAC:    
      description: 'Nominal battery voltage *(Code U)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    nominalVoltageDC:    
      description: 'Nominal voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    operatingAirHumidity:    
      description: 'Ambient operating Air Humidity range. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent.'    
      properties:    
        max:    
          maximum: 1    
          minimum: 0    
          type: number    
        min:    
          maximum: 1    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    operatingAmpereAC:    
      description: 'Minimum and Maximum Ampere allowed.. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Ampere    
    operatingAmpereDC:    
      description: 'Minimum and Maximum Ampere allowed.. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Ampere    
    operatingFrequencyAC:    
      description: 'Minimum and Maximum Frequency allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: Hertz    
    operatingFrequencyDC:    
      description: 'Minimum and Maximum Frequency allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Hertz    
    operatingTemperature:    
      description: 'Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius.'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: -50    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    operatingVoltageAC:    
      description: 'Minimum and Maximum voltage allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        type: Property    
        units: Volt    
    operatingVoltageDC:    
      description: 'Minimum and Maximum voltage allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt.'    
      properties:    
        max:    
          minimum: 0    
          type: number    
        min:    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    overVoltageCategory:    
      description: 'Over voltage category. - I : connection to circuits with transient over voltages at an appropriate low level. - II : main insulation and additional insulation (earth terminal). - III : fixed installations with reliability and availability making subject to specific specifications. - IV : materials at the origin of the electrical installation such as electric meters and main materials over current protection.'    
      enum:    
        - I    
        - II    
        - III    
        - IV    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *inverterdevice_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    phaseType:    
      description: 'Type of Phase. A unique value. Enum:''singlePhase,threePhase'''    
      enum:    
        - singlePhase    
        - threePhase    
      type: string    
      x-ngsi:    
        type: Property    
    possibilityOfUse:    
      description: 'Possibility of use. Enum:''mixed, mobile, stationary, other'''    
      enum:    
        - mixed    
        - mobile    
        - stationary    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    powerFactorAC:    
      description: 'Power factor for cos phi'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: 'A value between [0,1] Volt'    
    protectionClassSLK:    
      description: 'Protection class (SKL). - 0 : main insulation without earth connection. - 1 : main insulation and additional insulation (earth terminal). - 2 : double or reinforced insulation (equivalent to twice the main insulation) without accessible metal part. - 3 : operating in very low safety voltage (SELV) (50V maximum).'    
      enum:    
        - 0    
        - 1    
        - 2    
        - 3    
      type: string    
      x-ngsi:    
        type: Property    
    protectionIK:    
      description: 'IK ''*Mecanic Protection*'' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    protectionIP:    
      description: 'IP ''*Ingress Protection*'' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). - First digit: Solid particle protection (Single numeral: 0–6 or ''X''). - Second digit: Liquid ingress protection (Single numeral: 0–9 or ''X'' ).- Third digit: Personal Protection  against access to dangerous parts (optional additional letter).- Fourth digit: Other protections (optional additional letter).'    
      type: string    
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
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link.'    
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
    self-consumption:    
      description: 'Self-consumption during nigth. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  For instance, **WTT** represents Watt'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: Watt    
    serialNumber:    
      description: 'Serial numbers of the item'    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startingVoltageDC:    
      description: 'Starting voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volt    
    supplyPhaseNb:    
      description: 'Number of power supply phases'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    topology:    
      description: 'Description of the topology of the installation.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be InverterDevice'    
      enum:    
        - InverterDevice    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfUse:    
      description: 'Accepted use regarding its positioning in an indoor / outdoor environment.. Enum:''indoor, outdoor, mixed, other'''    
      enum:    
        - indoor    
        - outdoor    
        - mixed    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    weight:    
      description: 'Weight. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilogram'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kilograms    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - phaseType    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Energy/blob/master/InverterDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/InverterDevice/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### InverterDevice NGSI-v2 key-value の例。  
ここでは、InverterDeviceをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues`を使った場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InverterDevice:InverterDevice:MNCA-INVDEV-T1-G0-027",  
  "type": "InverterDevice",  
  "name": "INVDEV-T1-G0-027",  
  "alternateName": "AirPort – global Observation",  
  "description": "Description of the Inverter linked to Battery and PhotoVoltaic Devices",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "address": {  
    "addressCountry": "FR",  
    "addressLocality": "Nice",  
    "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
  },  
  "areaServed": "Nice Aeroport",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "brandName": "KOSTAL ELEC",  
  "modelName": "SB 4000TL-20",  
  "manufacturerName": "SOLAR ELECTRIC CPY",  
  "serialNumber": "SEKOPI10327458712",  
  "application": [  
    "robotics"  
  ],  
  "typeOfUse": "indoor",  
  "installationMode": "wall",  
  "installationCondition": [  
    "extremeClimate"  
  ],  
  "possibilityOfUse": "stationary",  
  "documentation": "https://www.myInverter.fr",  
  "owners": [  
    "Airport-Division Maintenance"  
  ],  
  "phaseType": "threePhase",  
  "supplyPhaseNb": 3,  
  "dimension": {  
    "length": 52.75,  
    "depth": 23.5,  
    "height": 45.25  
  },  
  "weight": 34,  
  "protectionIP": "55",  
  "protectionIK": 10,  
  "protectionClassSLK": "1",  
  "overVoltageCategory": "III",  
  "operatingTemperature": {  
    "min": -25,  
    "max": 60  
  },  
  "operatingAirHumidity": {  
    "min": 0,  
    "max": 0.95  
  },  
  "nominalPowerDC": 4200,  
  "nominalVoltageDC": 400,  
  "nominalAmpereDC ": 17,  
  "nominalFrequencyDC": 50,  
  "operatingVoltageDC": {  
    "min": 125,  
    "max": 550  
  },  
  "operatingAmpereDC": {  
    "min": 17,  
    "max": 17  
  },  
  "operatingFrequencyDC": {  
    "min": 50,  
    "max": 50  
  },  
  "mPPTPVVoltageDC": {  
    "min": 188,  
    "max": 440  
  },  
  "startingVoltageDC": 150,  
  "nbMPPTrackersDC": 3,  
  "nbInputParallelDC": "A:2,B:2",  
  "maxInputCurrentParallelAssembly": 25,  
  "nominalPowerAC": 3680,  
  "maxOutputPowerAC": 4000,  
  "nominalVoltageAC": 230,  
  "nominalAmpereAC ": 16,  
  "nominalFrequencyAC": 50,  
  "operatingVoltageAC": {  
    "min": 180,  
    "max": 280  
  },  
  "operatingAmpereAC": {  
    "min": 16,  
    "max": 22  
  },  
  "operatingFrequencyAC": {  
    "min": 50,  
    "max": 60  
  },  
  "powerFactorAC": 1,  
  "moduleYieldRate": {  
    "euro": 97.1,  
    "eta": 96.4  
  },  
  "noiseLevel": 29,  
  "self-consumption": 0.5,  
  "topology": "without transformer",  
  "coolingSystem": "OptiCool",  
  "inverterStatus": [  
    "00-OnSector",  
    "06-OverVoltage"  
  ]  
}  
```  
</details>  
#### InverterDevice NGSI-v2 正規化例  
ここでは、InverterDeviceをJSON-LD形式で正規化した例を示す。これはオプションを使用しない場合のNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:InverterDevice:InverterDevice:MNCA-INVDEV-T1-G0-027",  
  "type": "InverterDevice",  
  "name": {  
    "type": "Property",  
    "value": "INVDEV-T1-G0-027"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort – global Observation"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Description of the Inverter linked to Battery and PhotoVoltaic Devices"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates ": [  
        43.664810,  
        7.196545  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Aeroport"  
  },  
  "dateLastReported": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "KOSTAL ELEC"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "SB 4000TL-20"  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "SOLAR ELECTRIC CPY"  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "SEKOPI10327458712"  
  },  
  "application": {  
    "type": "Property",  
    "value": [  
      "robotics"  
    ]  
  },  
  "typeOfUse": {  
    "type": "Property",  
    "value": "indoor"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "wall"  
  },  
  "installationCondition": {  
    "type": "Property",  
    "value": [  
      "extremeClimate"  
    ]  
  },  
  "possibilityOfUse": {  
    "type": "Property",  
    "value": "stationary"  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myInverter.fr"  
  },  
  "owners": {  
    "type": "Property",  
    "value": [  
      "Airport-Division Maintenance"  
    ]  
  },  
  "phaseType": {  
    "type": "Property",  
    "value": "threePhase"  
  },  
  "supplyPhaseNb": {  
    "type": "Property",  
    "value": 3  
  },  
  "dimension": {  
    "type": "Property",  
    "value": {  
      "length": 52.75,  
      "depth": 23.5,  
      "height": 45.25  
    }  
  },  
  "weight": {  
    "type": "Property",  
    "value": 34  
  },  
  "protectionIP": {  
    "type": "Property",  
    "value": "55"  
  },  
  "protectionIK": {  
    "type": "Property",  
    "value": 10  
  },  
  "protectionClassSLK": {  
    "type": "Property",  
    "value": "1"  
  },  
  "overVoltageCategory": {  
    "type": "Property",  
    "value": "III"  
  },  
  "operatingTemperature": {  
    "type": "Property",  
    "value": {  
      "min": -25,  
      "max": 60  
    }  
  },  
  "operatingAirHumidity": {  
    "type": "Property",  
    "value": {  
      "min": 0,  
      "max": 0.95  
    }  
  },  
  "nominalPowerDC": {  
    "type": "Property",  
    "value": 4200  
  },  
  "nominalVoltageDC": {  
    "type": "Property",  
    "value": 400  
  },  
  "nominalAmpereDC ": {  
    "type": "Property",  
    "value": 17  
  },  
  "nominalFrequencyDC": {  
    "type": "Property",  
    "value": 50  
  },  
  "operatingVoltageDC": {  
    "type": "Property",  
    "value": {  
      "min": 125,  
      "max": 550  
    }  
  },  
  "operatingAmpereDC": {  
    "type": "Property",  
    "value": {  
      "min": 17,  
      "max": 17  
    }  
  },  
  "operatingFrequencyDC": {  
    "type": "Property",  
    "value": {  
      "min": 50,  
      "max": 50  
    }  
  },  
  "mPPTPVVoltageDC": {  
    "type": "Property",  
    "value": {  
      "min": 188,  
      "max": 440  
    }  
  },  
  "startingVoltageDC": {  
    "type": "Property",  
    "value": 150  
  },  
  "nbMPPTrackersDC": {  
    "type": "Property",  
    "value": 3  
  },  
  "nbInputParallelDC": {  
    "type": "Property",  
    "value": "A:2,B:2"  
  },  
  "maxInputCurrentParallelAssembly": {  
    "type": "Property",  
    "value": 25  
  },  
  "nominalPowerAC": {  
    "type": "Property",  
    "value": 3680  
  },  
  "maxOutputPowerAC": {  
    "type": "Property",  
    "value": 4000  
  },  
  "nominalVoltageAC": {  
    "type": "Property",  
    "value": 230  
  },  
  "nominalAmpereAC ": {  
    "type": "Property",  
    "value": 16  
  },  
  "nominalFrequencyAC": {  
    "type": "Property",  
    "value": 50  
  },  
  "operatingVoltageAC": {  
    "type": "Property",  
    "value": {  
      "min": 180,  
      "max": 280  
    }  
  },  
  "operatingAmpereAC": {  
    "type": "Property",  
    "value": {  
      "min": 16,  
      "max": 22  
    }  
  },  
  "operatingFrequencyAC": {  
    "type": "Property",  
    "value": {  
      "min": 50,  
      "max": 60  
    }  
  },  
  "powerFactorAC": {  
    "type": "Property",  
    "value": 1  
  },  
  "moduleYieldRate": {  
    "type": "Property",  
    "value": {  
      "euro": 97.1,  
      "eta": 96.4  
    }  
  },  
  "noiseLevel": {  
    "type": "Property",  
    "value": 29  
  },  
  "self-consumption": {  
    "type": "Property",  
    "value": 0.5  
  },  
  "topology": {  
    "type": "Property",  
    "value": "without transformer"  
  },  
  "coolingSystem": {  
    "type": "Property",  
    "value": "OptiCool"  
  },  
  "inverterStatus": {  
    "type": "Property",  
    "value": [  
      "00-OnSector",  
      "06-OverVoltage"  
    ]  
  }  
}  
```  
</details>  
#### InverterDevice NGSI-LD key-value Example  
ここでは、InverterDeviceをJSON-LD形式でkey-valuesにした例を示す。これは、`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:InverterDevice:InverterDevice:MNCA-INVDEV-T1-G0-027",  
    "type": "InverterDevice",  
    "address": {  
        "addressCountry": "FR",  
        "addressLocality": "Nice",  
        "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
    },  
    "alternateName": "AirPort \u2013 global Observation",  
    "application": [  
        "robotics"  
    ],  
    "areaServed": "Nice Aeroport",  
    "brandName": "KOSTAL ELEC",  
    "coolingSystem": "OptiCool",  
    "dateLastReported": "2020-03-17T08:45:00Z",  
    "description": "Description of the Inverter linked to Battery and PhotoVoltaic Devices",  
    "dimension": {  
        "length": 52.75,  
        "depth": 23.5,  
        "height": 45.25  
    },  
    "documentation": "https://www.myInverter.fr",  
    "installationCondition": [  
        "extremeClimate"  
    ],  
    "installationMode": "wall",  
    "inverterStatus": [  
        "00-OnSector",  
        "06-OverVoltage"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "mPPTPVVoltageDC": {  
        "min": 188,  
        "max": 440  
    },  
    "manufacturerName": "SOLAR ELECTRIC CPY",  
    "maxInputCurrentParallelAssembly": 25,  
    "maxOutputPowerAC": 4000,  
    "modelName": "SB 4000TL-20",  
    "moduleYieldRate": {  
        "euro": 97.1,  
        "eta": 96.4  
    },  
    "name": "INVDEV-T1-G0-027",  
    "nbInputParallelDC": "A:2,B:2",  
    "nbMPPTrackersDC": 3,  
    "noiseLevel": 29,  
    "nominalAmpereAC ": 16,  
    "nominalAmpereDC ": 17,  
    "nominalFrequencyAC": 50,  
    "nominalFrequencyDC": 50,  
    "nominalPowerAC": 3680,  
    "nominalPowerDC": 4200,  
    "nominalVoltageAC": 230,  
    "nominalVoltageDC": 400,  
    "operatingAirHumidity": {  
        "min": 0,  
        "max": 0.95  
    },  
    "operatingAmpereAC": {  
        "min": 16,  
        "max": 22  
    },  
    "operatingAmpereDC": {  
        "min": 17,  
        "max": 17  
    },  
    "operatingFrequencyAC": {  
        "min": 50,  
        "max": 60  
    },  
    "operatingFrequencyDC": {  
        "min": 50,  
        "max": 50  
    },  
    "operatingTemperature": {  
        "min": -25,  
        "max": 60  
    },  
    "operatingVoltageAC": {  
        "min": 180,  
        "max": 280  
    },  
    "operatingVoltageDC": {  
        "min": 125,  
        "max": 550  
    },  
    "overVoltageCategory": "III",  
    "owners": [  
        "Airport-Division Maintenance"  
    ],  
    "phaseType": "threePhase",  
    "possibilityOfUse": "stationary",  
    "powerFactorAC": 1,  
    "protectionClassSLK": "1",  
    "protectionIK": 10,  
    "protectionIP": "55",  
    "self-consumption": 0.5,  
    "serialNumber": "SEKOPI10327458712",  
    "startingVoltageDC": 150,  
    "supplyPhaseNb": 3,  
    "topology": "without transformer",  
    "typeOfUse": "indoor",  
    "weight": 34,  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### InverterDevice NGSI-LD 正規化例  
InverterDeviceをJSON-LD形式で正規化した例である。これはオプションを使わない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:InverterDevice:InverterDevice:MNCA-INVDEV-T1-G0-027",  
    "type": "InverterDevice",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressCountry": "FR",  
            "addressLocality": "Nice",  
            "streetAddress": "Airport - Terminal 1 - Ground 0 - Local  27"  
        }  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": "AirPort \u2013 global Observation"  
    },  
    "application": {  
        "type": "Property",  
        "value": [  
            "robotics"  
        ]  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Aeroport"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "KOSTAL ELEC"  
    },  
    "coolingSystem": {  
        "type": "Property",  
        "value": "OptiCool"  
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
        "value": "Description of the Inverter linked to Battery and PhotoVoltaic Devices"  
    },  
    "dimension": {  
        "type": "Property",  
        "value": {  
            "length": 52.75,  
            "depth": 23.5,  
            "height": 45.25  
        }  
    },  
    "documentation": {  
        "type": "Property",  
        "value": "https://www.myInverter.fr"  
    },  
    "installationCondition": {  
        "type": "Property",  
        "value": [  
            "extremeClimate"  
        ]  
    },  
    "installationMode": {  
        "type": "Property",  
        "value": "wall"  
    },  
    "inverterStatus": {  
        "type": "Property",  
        "value": [  
            "00-OnSector",  
            "06-OverVoltage"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates ": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "mPPTPVVoltageDC": {  
        "type": "Property",  
        "value": {  
            "min": 188,  
            "max": 440  
        }  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "SOLAR ELECTRIC CPY"  
    },  
    "maxInputCurrentParallelAssembly": {  
        "type": "Property",  
        "value": 25  
    },  
    "maxOutputPowerAC": {  
        "type": "Property",  
        "value": 4000  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "SB 4000TL-20"  
    },  
    "moduleYieldRate": {  
        "type": "Property",  
        "value": {  
            "euro": 97.1,  
            "eta": 96.4  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "INVDEV-T1-G0-027"  
    },  
    "nbInputParallelDC": {  
        "type": "Property",  
        "value": "A:2,B:2"  
    },  
    "nbMPPTrackersDC": {  
        "type": "Property",  
        "value": 3  
    },  
    "noiseLevel": {  
        "type": "Property",  
        "value": 29  
    },  
    "nominalAmpereAC ": {  
        "type": "Property",  
        "value": 16  
    },  
    "nominalAmpereDC ": {  
        "type": "Property",  
        "value": 17  
    },  
    "nominalFrequencyAC": {  
        "type": "Property",  
        "value": 50  
    },  
    "nominalFrequencyDC": {  
        "type": "Property",  
        "value": 50  
    },  
    "nominalPowerAC": {  
        "type": "Property",  
        "value": 3680  
    },  
    "nominalPowerDC": {  
        "type": "Property",  
        "value": 4200  
    },  
    "nominalVoltageAC": {  
        "type": "Property",  
        "value": 230  
    },  
    "nominalVoltageDC": {  
        "type": "Property",  
        "value": 400  
    },  
    "operatingAirHumidity": {  
        "type": "Property",  
        "value": {  
            "min": 0,  
            "max": 0.95  
        }  
    },  
    "operatingAmpereAC": {  
        "type": "Property",  
        "value": {  
            "min": 16,  
            "max": 22  
        }  
    },  
    "operatingAmpereDC": {  
        "type": "Property",  
        "value": {  
            "min": 17,  
            "max": 17  
        }  
    },  
    "operatingFrequencyAC": {  
        "type": "Property",  
        "value": {  
            "min": 50,  
            "max": 60  
        }  
    },  
    "operatingFrequencyDC": {  
        "type": "Property",  
        "value": {  
            "min": 50,  
            "max": 50  
        }  
    },  
    "operatingTemperature": {  
        "type": "Property",  
        "value": {  
            "min": -25,  
            "max": 60  
        }  
    },  
    "operatingVoltageAC": {  
        "type": "Property",  
        "value": {  
            "min": 180,  
            "max": 280  
        }  
    },  
    "operatingVoltageDC": {  
        "type": "Property",  
        "value": {  
            "min": 125,  
            "max": 550  
        }  
    },  
    "overVoltageCategory": {  
        "type": "Property",  
        "value": "III"  
    },  
    "owners": {  
        "type": "Property",  
        "value": [  
            "Airport-Division Maintenance"  
        ]  
    },  
    "phaseType": {  
        "type": "Property",  
        "value": "threePhase"  
    },  
    "possibilityOfUse": {  
        "type": "Property",  
        "value": "stationary"  
    },  
    "powerFactorAC": {  
        "type": "Property",  
        "value": 1  
    },  
    "protectionClassSLK": {  
        "type": "Property",  
        "value": "1"  
    },  
    "protectionIK": {  
        "type": "Property",  
        "value": 10  
    },  
    "protectionIP": {  
        "type": "Property",  
        "value": "55"  
    },  
    "self-consumption": {  
        "type": "Property",  
        "value": 0.5  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "SEKOPI10327458712"  
    },  
    "startingVoltageDC": {  
        "type": "Property",  
        "value": 150  
    },  
    "supplyPhaseNb": {  
        "type": "Property",  
        "value": 3  
    },  
    "topology": {  
        "type": "Property",  
        "value": "without transformer"  
    },  
    "typeOfUse": {  
        "type": "Property",  
        "value": "indoor"  
    },  
    "weight": {  
        "type": "Property",  
        "value": 34  
    },  
    "@context": [  
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
