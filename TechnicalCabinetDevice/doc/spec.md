Entity: TechnicalCabinetDevice  
==============================  
[Open License](https://github.com/smart-data-models//dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **Technical Cabinet Device Data Model is intended to to describe the technical characteristics of the Device, designed to be placed in an urban or interurban environment. The main objective of these cabinets for this Data Model is to protect the electrical equipment necessary for the control, surveillance, reading and management of urban lighting, signaling, video and electrical distribution. The scope of use of some of these cabinets can extend to an additional protection for installations of modular apparatuses of telephony, data processing, meteorological stations, photo-voltaic stations, wind turbines stations, telecommunications, networks, data, bre Optics , etc. *Remark* : This Data Model can be used directly as a main entity to describe the device `Technical Cabinet`  or as a sub-entity of the Data Model  `DEVICE` using a reference by the `refDevice` attribute. It can also refer to the list of all the components it contains, with the `refDeviceList` attribute, using the Data Model  `DEVICE`**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `application`: Target application of the Device regarding the environment. A combination of these values. Enum:'commercial, distributionService, industrial, other, publicWorks, road, tertiary, urbanService'  - `areaServed`: The geographic area where a service or offered item is provided  - `brandName`: Name of the brand  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateLastReported`: A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `designMaterials`: Design materials to build the cabinet. A combination of  these values. Enum:'ABS-Plastic, aluminum, fiberGlass, galvanizedSteel, other, polyester, stainlessSteel'  - `dimension`: The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter.  - `documentation`: A link to device's documentation  - `doorClosingMode`: Door closing mode. A unique value of these values. Enum:'fixedHandle, other, revolvingHandle, triangleHandle'  - `doorCount`: Count of doors of the technical Cabinet.  - `doorOpeningAngle`: Door opening angle expressed in decimal degrees with a range from 0 to 180 degree. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **DD** represents Decimal Degrees.  - `doorType`: Type of door of the technical Cabinet. A unique value of these values. Enum:'mixed, other, solid, transparent'  - `exteriorCoating`: Interior Coating. A combination of these values. Enum:'fiberGlass, other, plastic, polyester, polyesterResin, steel  - `exteriorFinish`: Exterior finish. A combination of these values. Enum:'graffiti, other, raised, roughcast, smooth, textured'  - `id`: Unique identifier of the entity  - `installationCondition`: Condition and possibility of use in the following environments. A combination of these values. Enum:'desert, dust, extremeCold, extremeClimate, extremeHeat, extremeHumidity, marine, none, other, saline, seismic, sand'  - `installationMode`: Positioning of the device in relation to a ground reference system. Enum:'aerial, ground, other, pole, roofing, underground, wall'  - `interiorCoating`: Interior Coating. A combination of these values. Enum:'fiberGlass, heatInsulating, other, plastic, polyester, polyesterResin, steel'  - `internalDimension`: Internal dimension corresponding to the place to work inside the technical cabinet. The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `manufacturerName`: Name of the manufacturer  - `maximumSystemVoltage`: Maximum system voltage permitted for the **module**. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt  - `modelName`: Name of the model as given by the manufacturer.  - `name`: The name of this item.  - `operatingTemperature`: Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `possibilityOfUse`: Possibility of use. A unique value. Enum:'mixed, mobile, other, stationary'  - `protectionIK`: IK '*Mecanic Protection*' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)  - `protectionIP`: IP 'Ingress Protection' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). First digit: Solid particle protection (Single numeral: 06 or 'X'). Second digit: Liquid ingress protection (Single numeral: 09 or 'X' ).Third digit: Personal Protection against access to dangerous parts (optional additional letter). Fourth digit: Other protections (optional additional letter)  - `protectionOthers`: Others protection of the technical cabinet. A combination of these values. Enum:'abrasion, basement, dampProof, display, doorTearing, dust, forcedOpening, graffiti, insect, other, roofOverload, saltSpray, shielding, solar, vandalism, water'  - `refDevice`: The device used to obtain the data expressed by this record  - `refDeviceList`: A list of reference to the [Devices](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which are inside the technical Cabinet Device.  - `refPointOfInterest`: Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation.  - `seeAlso`: list of uri pointing to additional resources about the item  - `serialNumber`: Serial number of the container  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: NGSI Entity type. It has to be TechnicalCabinetDevice  - `typeOfUse`: Accepted use regarding its positioning in an indoor / outdoor environment. A unique value of these values. Enum:'indoor, mixed, outdoor, other'  - `ventilationMode`: Ventilation mode. A combination of these values. Enum:'airConditioners, dehumidifier, none, other, selfVentilatedGills'  - `weight`: Weight of the item. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilograms    
Required properties  
- `dateLastReported`  - `dimension`  - `id`  - `location`  - `type`  - `typeOfUse`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TechnicalCabinetDevice:    
  description: 'Technical Cabinet Device Data Model is intended to to describe the technical characteristics of the Device, designed to be placed in an urban or interurban environment. The main objective of these cabinets for this Data Model is to protect the electrical equipment necessary for the control, surveillance, reading and management of urban lighting, signaling, video and electrical distribution. The scope of use of some of these cabinets can extend to an additional protection for installations of modular apparatuses of telephony, data processing, meteorological stations, photo-voltaic stations, wind turbines stations, telecommunications, networks, data, bre Optics , etc. *Remark* : This Data Model can be used directly as a main entity to describe the device `Technical Cabinet`  or as a sub-entity of the Data Model  `DEVICE` using a reference by the `refDevice` attribute. It can also refer to the list of all the components it contains, with the `refDeviceList` attribute, using the Data Model  `DEVICE`'    
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
```  
</details>    
## Example payloads    
#### TechnicalCabinetDevice NGSI-v2 key-values Example    
Here is an example of a TechnicalCabinetDevice in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### TechnicalCabinetDevice NGSI-v2 normalized Example    
Here is an example of a TechnicalCabinetDevice in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### TechnicalCabinetDevice NGSI-LD key-values Example    
Here is an example of a TechnicalCabinetDevice in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-TechnicalCabinetDevice:MNCA-TCD-AP-T2-F1-022",  
  "type": "TechnicalCabinetDevice",  
  "name": "MNCA-TCD-AP-T2-F1-022",  
  "alternateName": "AirPort â€“ global Observation",  
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
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### TechnicalCabinetDevice NGSI-LD normalized Example    
Here is an example of a TechnicalCabinetDevice in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-TechnicalCabinetDevice:MNCA-TCD-AP-T2-F1-022",  
  "type": "TechnicalCabinetDevice",  
  "name": {  
    "type": "Property",  
    "value": "MNCA-TCD-AP-T2-F1-022"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "AirPort â€“ global Observation"  
  },  
  "description": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": {  
      "addressCountry": "FR",  
      "addressLocality": "Nice",  
      "streetAddress": "Airport Terminal 2 - Floor 1"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": {  
      "type": "DateTime",  
      "value": "2020-03-17T08:45:00Z"  
    }  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "EATON"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "xEnergy L"  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "ElDorado"  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "L257589A4587J56"  
  },  
  "application": {  
    "type": "Property",  
    "value": [  
      "industrial",  
      "distributionService"  
    ]  
  },  
  "typeOfUse": {  
    "type": "Property",  
    "value": "outDoor"  
  },  
  "installationMode": {  
    "type": "Property",  
    "value": "ground"  
  },  
  "installationCondition": {  
    "type": "Property",  
    "value": [  
      "none"  
    ]  
  },  
  "possibilityOfUsed": {  
    "type": "Property",  
    "value": "stationary"  
  },  
  "documentation": {  
    "type": "Property",  
    "value": "https://www.myTechnicalCabinet.fr"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "Airport-Division Maintenance"  
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
  "weight": {  
    "type": "Property",  
    "value": 60  
  },  
  "internalDimension": {  
    "type": "Property",  
    "value": {  
      "width": 140,  
      "height": 165,  
      "depth": 70  
    }  
  },  
  "protectionIP": {  
    "type": "Property",  
    "value": "65"  
  },  
  "protectionIK": {  
    "type": "Property",  
    "value": 10  
  },  
  "maximumSystemVoltage": {  
    "type": "Property",  
    "value": 1000  
  },  
  "operatingTemperature": {  
    "type": "Property",  
    "value": {  
      "min": -40,  
      "max": 100  
    }  
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
  "doorCount": {  
    "type": "Property",  
    "value": 2  
  },  
  "doorType": {  
    "type": "Property",  
    "value": "solid"  
  },  
  "doorOpeningAngle": {  
    "type": "Property",  
    "value": 180  
  },  
  "doorClosingMode": {  
    "type": "Property",  
    "value": "fixedHandle"  
  },  
  "designMaterials": {  
    "type": "Property",  
    "value": [  
      "stainlessSteel",  
      "polyester"  
    ]  
  },  
  "interiorCoating": {  
    "type": "Property",  
    "value": [  
      "heatInsulating",  
      "polyesterResin"  
    ]  
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
  "ventilationMode": {  
    "type": "Property",  
    "value": [  
      "selfVentilatedGills"  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units