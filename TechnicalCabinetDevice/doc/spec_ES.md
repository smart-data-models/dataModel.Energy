<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: GabineteTécnicoDispositivo  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El Modelo de Datos del Dispositivo de Armario Técnico tiene por objeto describir las características técnicas del Dispositivo, diseñado para ser colocado en un entorno urbano o interurbano. El objetivo principal de estos armarios para este Modelo de Datos es proteger los equipos eléctricos necesarios para el control, vigilancia, lectura y gestión del alumbrado urbano, señalización, vídeo y distribución eléctrica. El ámbito de utilización de algunos de estos armarios puede extenderse a una protección adicional para instalaciones de aparatos modulares de telefonía, proceso de datos, estaciones meteorológicas, estaciones fotovoltaicas, estaciones eólicas, telecomunicaciones, redes, datos, bre Óptica , etc. *Nota* : Este Modelo de Datos puede utilizarse directamente como entidad principal para describir el dispositivo `Gabinete Técnico` o como subentidad del Modelo de Datos `DEVICE` utilizando una referencia mediante el atributo `refDevice`. También puede hacer referencia a la lista de todos los componentes que contiene, con el atributo `refDeviceList`, utilizando el Modelo de Datos `DEVICE'**.  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `application[array]`: Objetivo de aplicación del Dispositivo en relación con el medio ambiente. Una combinación de estos valores. Enum:'comercial, distribuciónServicio, industrial, otros, obraspúblicas, carretera, terciario, urbanoServicio'  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nombre de la marca  . Model: [https://schema.org/brand](https://schema.org/brand)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateLastReported[date-time]`: Marca de tiempo que indica la última vez que el dispositivo notificó datos correctamente. Fecha y hora en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `designMaterials[array]`: Materiales de diseño para construir el armario. Una combinación de estos valores. Enum:'ABS-Plástico, aluminio, fibra de vidrio, acero galvanizado, otros, poliéster, acero inoxidable'  - `dimension[object]`: El formato está estructurado por una subpropiedad de 3 elementos. El código de unidad (texto) de medida se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **CMT** representa Centímetro  	- `depth[number]`:     
	- `height`:     
- `documentation[uri]`: Enlace a la documentación del dispositivo  . Model: [https://schema.org/URL](https://schema.org/URL)- `doorClosingMode[array]`: Modo de cierre de la puerta. Un valor único de estos valores. Enum:'empuñadura fija, otro, empuñadura giratoria, empuñadura triangular'  - `doorCount[number]`: Recuento de puertas del Gabinete técnico  - `doorOpeningAngle[number]`: Ángulo de apertura de la puerta expresado en grados decimales con un rango de 0 a 180 grados. El código de unidad (texto) de medida se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **DD** representa Grados Decimales  - `doorType[string]`: Tipo de puerta del Gabinete técnico. Un valor único de estos valores. Enum:'mixta, otra, maciza, transparente'  - `exteriorCoating[array]`: Revestimiento interior. Una combinación de estos valores. Enum:'fibraGlass, otro, plástico, poliéster, poliésterResina, acero  - `exteriorFinish[array]`: Acabado exterior. Combinación de estos valores. Enum:'graffiti, otro, en relieve, rugoso, liso, texturado'  - `id[*]`: Identificador único de la entidad  - `installationCondition[array]`: Condición y posibilidad de uso en los siguientes entornos. Una combinación de estos valores. Enum:'desierto, polvo, frío extremo, clima extremo, calor extremo, humedad extrema, marino, ninguno, otro, salino, sísmico, arena'.  - `installationMode[string]`: Posicionamiento del dispositivo en relación con un sistema de referencia terrestre. Enum:'aéreo, tierra, otro, poste, tejado, subterráneo, pared'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `interiorCoating[array]`: Revestimiento interior. Una combinación de estos valores. Enum:'fibra de vidrio, aislante térmico, otro, plástico, poliéster, resina de poliéster, acero'  - `internalDimension[object]`: Dimensión interna correspondiente al lugar de trabajo dentro del armario técnico. El formato está estructurado por una subpropiedad de 3 elementos. El código de unidad (texto) de medida se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **CMT** representa Centímetro  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `depth`:     
	- `height`:     
- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `manufacturerName[string]`: Nombre del fabricante  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumSystemVoltage[number]`: Tensión máxima del sistema permitida para el **módulo**. El código de unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **VLT** representa Volt  - `modelName[string]`: Nombre del modelo facilitado por el fabricante  - `name[string]`: El nombre de este artículo  - `operatingTemperature[object]`: Temperatura ambiente de funcionamiento. Se trata de la resistencia mínima y máxima al frío y al calor. El formato está estructurado por una subpropiedad de 2 elementos. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **CEL** representa Grado Celsius  	- `max`:     
- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `possibilityOfUse[string]`: Posibilidad de uso. Un valor único. Enum:'mixto, móvil, otro, fijo'  - `protectionIK[number]`: Nivel IK "*Protección Mecánica*" relativo a la clasificación numérica de los grados de protección que ofrecen las envolventes de equipos eléctricos frente a impactos mecánicos externos, según la norma de la Comisión Electrotécnica Internacional (EN 62-262). - IK varía de 0 (resistencia mínima) a 10 (resistencia máxima), lo que representa una energía de impacto (unidad Joule)  - `protectionIP[string]`: IP 'Ingress Protection' para la caja de conexiones. Es el nivel que clasifica y valora el grado de protección que ofrecen las carcasas mecánicas y los armarios eléctricos contra la intrusión, el polvo, el contacto accidental y el agua según la norma de la Comisión Electrotécnica Internacional (EN 60-529). Primer dígito: Protección contra partículas sólidas (Número único: 06 o "X"). Segundo dígito: Protección contra la penetración de líquidos (número único: 09 o "X"): Protección personal contra el acceso a partes peligrosas (letra adicional opcional). Cuarto dígito: Otras protecciones (letra adicional opcional)  - `protectionOthers[array]`: Otros protección del armario técnico. Una combinación de estos valores. Enum:'abrasión, sótano, dampProof, pantalla, doorTearing, polvo, forcedOpening, graffiti, insecto, otros, roofOverload, saltSpray, blindaje, solar, vandalismo, agua'  - `refDevice[*]`: Dispositivo utilizado para obtener los datos expresados por este registro  - `refDeviceList[array]`: Una lista de referencia a los [Dispositivos](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) que se encuentran dentro del Gabinete técnico Dispositivo  - `refPointOfInterest[*]`: Referencia a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) vinculado a la observación  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `serialNumber[string]`: Número de serie del contenedor  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser TechnicalCabinetDevice  - `typeOfUse[string]`: Uso aceptado en cuanto a su colocación en un entorno interior / exterior. Un valor único de estos valores. Enum:'interior, mixto, exterior, otro'  - `ventilationMode[array]`: Modo de ventilación. Una combinación de estos valores. Enum:'aires acondicionados, deshumidificador, ninguno, otro, autoventilación'  - `weight[number]`: Peso del artículo. El código de la unidad (texto) de medida se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **KGM** representa Kilogramos  . Model: [https://schema.org/weigth](https://schema.org/weigth)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateLastReported`  - `dimension`  - `id`  - `location`  - `type`  - `typeOfUse`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TechnicalCabinetDevice:    
  description: 'Technical Cabinet Device Data Model is intended to to describe the technical characteristics of the Device, designed to be placed in an urban or interurban environment. The main objective of these cabinets for this Data Model is to protect the electrical equipment necessary for the control, surveillance, reading and management of urban lighting, signaling, video and electrical distribution. The scope of use of some of these cabinets can extend to an additional protection for installations of modular apparatuses of telephony, data processing, meteorological stations, photo-voltaic stations, wind turbines stations, telecommunications, networks, data, bre Optics , etc. *Remark* : This Data Model can be used directly as a main entity to describe the device `Technical Cabinet`  or as a sub-entity of the Data Model  `DEVICE` using a reference by the `refDevice` attribute. It can also refer to the list of all the components it contains, with the `refDeviceList` attribute, using the Data Model ''DEVICE'''    
  properties:    
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
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: Name of the brand    
      type: string    
      x-ngsi:    
        model: https://schema.org/brand    
        type: Property    
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
    dateLastReported:    
      description: A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat    
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
    description:    
      description: A description of this item    
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
      description: 'The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter'    
      properties:    
        depth:    
          description: ""    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
        height:    
          minimum: 0    
          type: number    
        width:    
          description: ""    
          minimum: 0    
          type: number    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    documentation:    
      description: A link to device's documentation    
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
      description: Count of doors of the technical Cabinet    
      type: number    
      x-ngsi:    
        type: Property    
    doorOpeningAngle:    
      description: 'Door opening angle expressed in decimal degrees with a range from 0 to 180 degree. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **DD** represents Decimal Degrees'    
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
    manufacturerName:    
      description: Name of the manufacturer    
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
      description: Name of the model as given by the manufacturer    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    operatingTemperature:    
      description: 'Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius'    
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
      description: The device used to obtain the data expressed by this record    
      x-ngsi:    
        type: Relationship    
    refDeviceList:    
      description: 'A list of reference to the [Devices](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which are inside the technical Cabinet Device'    
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
      type: array    
      x-ngsi:    
        type: Relationship    
    refPointOfInterest:    
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
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation'    
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
    serialNumber:    
      description: Serial number of the container    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be TechnicalCabinetDevice    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/data-models.Energy/TechnicalCabinetDevice/schema.json    
  x-model-tags: Energy    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### TechnicalCabinetDevice NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de TechnicalCabinetDevice en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### TechnicalCabinetDevice NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de TechnicalCabinetDevice en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
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
    "value": "outdoor"  
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
    "type": "array",  
    "value": [  
      "fixedHandle"  
    ]  
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
#### TechnicalCabinetDevice NGSI-LD key-values Ejemplo  
He aquí un ejemplo de TechnicalCabinetDevice en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TechnicalCabinetDevice NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de TechnicalCabinetDevice en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "value": [  
      "fixedHandle"  
    ]  
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
      "type": "Point",  
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
    "value": "outdoor"  
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
    "https://smart-data-models.github.io/data-models/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
