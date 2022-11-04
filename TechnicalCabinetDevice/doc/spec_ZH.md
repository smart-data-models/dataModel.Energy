<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。技术内阁设备（TechnicalCabinetDevice  
================================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**技术柜设备数据模型的目的是描述设备的技术特征，旨在放置在城市或城际环境中。本数据模型的这些机柜的主要目的是保护城市照明、信号、视频和配电的控制、监视、阅读和管理所需的电气设备。这些机柜的使用范围可以扩展到额外保护电话、数据处理、气象站、光电站、风力发电站、电信、网络、数据、光纤等模块化设备的安装。*注意* 。这个数据模型可以直接作为描述设备 "技术柜 "的主要实体，或者作为数据模型 "DEVICE "的子实体，通过 "refDevice "属性进行引用。它也可以通过`refDeviceList`属性，使用数据模型'DEVICE'**来引用它所包含的所有组件的列表。  
版本。  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `application[array]`: 设备关于环境的目标应用。这些值的组合。Enum:'商业，配送服务，工业，其他，公共工程，道路，第三产业，城市服务'  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 品牌名称  . Model: [https://schema.org/brand](https://schema.org/brand)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateLastReported[string]`: 一个时间戳，表示设备最后一次成功报告数据的时间。ISO8601 UTC格式的日期和时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `designMaterials[array]`: 设计材料来建造柜子。这些值的组合。Enum:'ABS-Plastic, aluminum, fiberGlass, galvanizedSteel, other, polyester, stainlessSteel'。  - `dimension[object]`: 该格式是由3个项目的子属性构成的。测量的单位代码（文本）使用[UN/CEFACT通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)给出。例如，**CMT**代表厘米。  - `documentation[string]`: 设备文件的链接  . Model: [https://schema.org/URL](https://schema.org/URL)- `doorClosingMode[array]`: 门的关闭模式。这些值的唯一值。Enum:'fixedHandle, other, revolvingHandle, triangleHandle'。  - `doorCount[number]`: 技术柜的门数。  - `doorOpeningAngle[number]`: 门打开的角度，以十进制度数表示，范围从0到180度。测量的单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**DD**代表十进制度数。  - `doorType[string]`: 技术柜的门的类型。这些值的唯一值。Enum:'混合，其他，实心，透明'  - `exteriorCoating[array]`: 内部涂层。这些值的组合。Enum:'fiberGlass, other, plastic, polyester, polyesterResin, steel  - `exteriorFinish[array]`: 外部装修。这些值的组合。Enum:'涂鸦, 其他, 凸起, 粗糙铸造, 平滑, 纹理'  - `id[*]`: 实体的唯一标识符  - `installationCondition[array]`: 在以下环境中使用的条件和可能性。这些值的组合。Enum:'沙漠, 灰尘, 极端寒冷, 极端气候, 极端炎热, 极端潮湿, 海洋, 无, 其他, 盐碱地, 地震, 沙子'  - `installationMode[string]`: 设备相对于地面参考系统的定位。枚举:'空中、地面、其他、杆、屋顶、地下、墙'  . Model: [https://schema.org/Text](https://schema.org/Text)- `interiorCoating[array]`: 内部涂层。这些值的组合。Enum:'fiberGlass, heatInsulating, other, plastic, polyester, polyesterResin, steel'。  - `internalDimension[object]`: 对应于技术柜内工作场所的内部尺寸。该格式是由3个项目的子属性构成的。测量的单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**CMT**代表厘米  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `manufacturerName[string]`: 制造商的名称  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumSystemVoltage[number]`: **模块**允许的最大系统电压。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**VLT**代表伏特  - `modelName[string]`: 制造商提供的型号名称。  - `name[string]`: 这个项目的名称。  - `operatingTemperature[object]`: 环境工作温度范围。这是对冷和热的最小和最大抵抗力。该格式是由2个项目的子属性构成的。单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**CEL**代表摄氏度。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `possibilityOfUse[string]`: 使用的可能性。一个独特的值。Enum:'混合、移动、其他、固定'。  - `protectionIK[number]`: IK "*机械保护*"级别与电气设备外壳对外部机械冲击的保护程度的数字分类有关，根据国际电工委员会标准（EN 62-262）。- IK从0（最小阻力）到10（最大阻力）不等，代表冲击能量（单位焦耳）。  - `protectionIP[string]`: 接线盒的IP "入侵保护"。这是根据国际电工委员会标准（EN 60-529），对机械外壳和电气外壳提供的保护程度进行分类和评级，以防止入侵、灰尘、意外接触和水。第一个数字。固体颗粒保护（单一数字：06或'X'）。第二位数字。第三位数：液体进入保护（单个数字：09或'X'）。个人防护，防止接触危险部件（可选附加字母）。第四位数。其他保护措施（可选附加字母）  - `protectionOthers[array]`: 其他保护的技术柜。这些值的组合。Enum:'磨损, 地下室, 防潮, 显示, 门撕裂, 灰尘, 强制打开, 涂鸦, 昆虫, 其他, 屋顶过载, 盐雾, 屏蔽, 太阳能, 破坏, 水'  - `refDevice[*]`: 用于获取该记录所表达的数据的设备  - `refDeviceList[array]`: 对技术柜设备内的[设备](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)的参考列表。  - `refPointOfInterest[*]`: 对与观测有关的[兴趣点](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)的引用。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `serialNumber[string]`: 容器的序列号  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体类型。它必须是TechnicalCabinetDevice。  - `typeOfUse[string]`: 关于其在室内/室外环境中的定位的接受使用。这些值的唯一值。枚举:'室内、混合、室外、其他'  - `ventilationMode[array]`: 通风模式。这些值的组合。Enum:'airConditioners, dehumidifier, none, other, selfVentilatedGills'（空调，除湿器，无，其他，自我通风）。  - `weight[number]`: 该物品的重量。计量单位代码（文本）使用[UN/CEFACT通用代码]（http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes）给出。例如，**KGM**代表公斤  . Model: [https://schema.org/weigth](https://schema.org/weigth)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `dateLastReported`  - `dimension`  - `id`  - `location`  - `type`  - `typeOfUse`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
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
## ＃＃＃＃有效载荷的例子  
#### TechnicalCabinetDevice NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为关键值的TechnicalCabinetDevice的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### TechnicalCabinetDevice NGSI-v2规范化实例  
下面是一个以JSON-LD格式规范化的TechnicalCabinetDevice的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### TechnicalCabinetDevice NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为关键值的TechnicalCabinetDevice的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### TechnicalCabinetDevice NGSI-LD规范化实例  
下面是一个以JSON-LD格式规范化的TechnicalCabinetDevice的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
