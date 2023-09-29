<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: ACMeasurement  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Energy/blob/master/ACMeasurement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El Modelo de Datos destinado a medir las energías eléctricas consumidas por un sistema eléctrico que utiliza una Corriente Alterna (CA) para una red trifásica (L1, L2, L3) o monofásica (L) y neutro (N). Integra la versión inicial del módem de datos [THREEPHASEMEASUREMENT], ampliada para realizar también mediciones monofásicas. Incluye atributos para diversas mediciones eléctricas como potencia, frecuencia, corriente y tensión.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `activeEnergyExport[object]`: Energía activa exportada por fase. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `activeEnergyImport[object]`: Energía activa importada, es decir, consumida por fase. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `activePower[object]`: Potencia activa consumida por fase. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local    
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `apparentEnergyExport[object]`: Energía aparente exportada por fase. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `apparentEnergyImport[object]`: Energía aparente importada, es decir, consumida por fase. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `apparentPower[object]`: Potencia aparente consumida por fase. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: Corriente eléctrica. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
	- `N`:     
- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateEnergyMeteringStarted[date-time]`: La fecha de inicio de la medición de la energía en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `dateObserved[date-time]`: Fecha y hora de esta observación representadas por un formato ISO8601 UTC. Puede representarse por un instante de tiempo específico o por un intervalo ISO8601 para separar los atributos `dateObservedFrom`,`dateObservedTo`.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[date-time]`: Periodo de observación: Fecha y hora de inicio en formato ISO8601 UTC. El atributo puede utilizarse además del atributo `dateObserved` cuando corresponde a un intervalo de tiempo que debe resaltarse.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: Periodo de observación: Fecha y hora finales en formato ISO8601 UTC. El atributo puede utilizarse además del atributo `dateObserved` cuando corresponde a un intervalo de tiempo que debe resaltarse.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descripción de este artículo  - `displacementPowerFactor[object]`: Factor de potencia de desplazamiento para cada fase. La cantidad se basa en la frecuencia fundamental del sistema  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `frequency[number]`: La frecuencia del circuito. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `phaseToPhaseVoltage[object]`: Tensión entre fases. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L12`:     
	- `L23`:     
	- `L31`:     
- `phaseType[string]`: Tipo de fase. Un valor único. Enum:'monofásico, trifásico'  . Model: [https://schema.org/Text](https://schema.org/Text)- `phaseVoltage[object]`: La tensión entre cada conductor de fase y neutro. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `powerFactor[object]`: Factor de potencia de cada fase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `reactiveEnergyExport[object]`: Energía reactiva de frecuencia fundamental exportada por fase. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `reactiveEnergyImport[object]`: Energía reactiva de frecuencia fundamental importada, es decir, consumida por fase. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `reactivePower[object]`: Potencia reactiva de frecuencia fundamental. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `refDevice[array]`: Referencia a los dispositivos que captaron esta observación  . Model: [https://schema.org/URL](https://schema.org/URL)- `refTargetDevice[array]`: Referencia a una lista de los dispositivos para los que se ha realizado la medición  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `thdCurrent[object]`: Distorsión armónica total de la corriente para cada fase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `thdVoltage[object]`: Distorsión armónica total de la tensión para cada fase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1`:     
	- `L2`:     
	- `L3`:     
- `totalActiveEnergyExport[number]`: Energía total importada, es decir, consumida . El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActiveEnergyImport[number]`: Energía total importada, es decir, consumida. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActivePower[number]`: Potencia activa total consumida. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentEnergyExport[number]`: Energía total exportada (con respecto a la potencia aparente). El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalApparentEnergyImport[number]`: Energía total importada, es decir, consumida (con respecto a la potencia aparente). El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentPower[number]`: Potencia aparente total consumida. El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalDisplacementPowerFactor[number]`: Suma del factor de potencia de desplazamiento incluyendo todas las fases. La cantidad se basa en la frecuencia fundamental del sistema  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalPowerFactor[number]`: Suma del factor de potencia incluyendo todas las fases  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalReactiveEnergyExport[number]`: Energía reactiva total de frecuencia fundamental exportada. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalReactiveEnergyImport[number]`: Energía total importada, es decir, consumida (con respecto a la potencia reactiva de frecuencia fundamental). El código de la unidad (texto) se da utilizando los [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalReactivePower[number]`: Potencia reactiva total consumida. El código de la unidad (texto) se da utilizando los [Códigos Comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo de propiedad NGSI. Tiene que ser ACMeasurement  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateObserved`  - `id`  - `location`  - `phaseType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Información adicional sobre atributos.  Para algunos atributos como la corriente y la tensión, el valor es un valor estructurado con propiedades para la fase única (L) o tres fases diferentes (L1, L2 y L3). Para algunas medidas como los diferentes tipos de potencia (activa, reactiva y aparente) existe un atributo para el total de todas las fases. Las reglas se definen como - Trifásico - Total = L1 + L2 + L3 - Monofásico - Total = L. Para la mayoría de los atributos, existen varias formas en que pueden medirse realmente. Para ello se puede utilizar el metaatributo measurementType. Puede tener los siguientes valores: promedio, rms, mínimo, máximo. Si se utilizan los valores [promedio, rms, mínimo, máximo], debe utilizarse otro atributo de metadatos denominado measurementInterval para indicar la duración del periodo de medición en segundos. También debe utilizarse un atributo timestamp para indicar la hora de finalización del periodo de medición.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
Nota. Los valores serán transmitidos por 1 o 3 sub propiedades dependiendo El Tipo de Fase para cada fase Monofásica. Valores individuales L. Trifásica. Suma de los valores individuales. L1, L2, L3. Todos los valores se calculan a partir de la fecha de inicio de la medición [dateEnergyMeteringStarted].  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### ACMeasurement NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de una ACMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ACMeasurement NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de una ACMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
        43.664810,  
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
    "type": "URI",  
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
    "type": "Number",  
    "value": 1  
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
#### ACMeasurement NGSI-LD key-values Ejemplo  
He aquí un ejemplo de una ACMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### ACMeasurement NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de una ACMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
