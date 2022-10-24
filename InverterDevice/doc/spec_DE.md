<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: InverterDevice  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Energy/blob/master/InverterDevice/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell dient der Beschreibung der mechanischen und elektrischen Eigenschaften eines Wechselrichters gemäß *DC - Direct Current Information*, die als Eingang geliefert wird, und *AC - Alternating Current Information*, die als Ausgang zurückgegeben wird. *Bemerkung*: Dieses Datenmodell kann direkt als Hauptentität zur Beschreibung des Geräts [Wechselrichter] oder als Unterentität des Datenmodells {DEVICE] unter Verwendung eines Verweises durch das Attribut [refDevice] verwendet werden.**  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `application[array]`: Zielanwendung des Geräts in Bezug auf die Umwelt. Ein eindeutiger Wert. Enum:'electricMobility, energyStorage, emergencyStorage, lighting, industrialStorage, houseHoldStorage, robotics, production, other'  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Markenname des Artikels  . Model: [https://schema.org/brand](https://schema.org/brand)- `coolingSystem[string]`:  Kühlsystem des Geräts. Enum:'Konvektion, OptiCool, Geregelter-Lüfter, Andere'  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateLastReported[string]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem das Gerät erfolgreich Daten gemeldet hat. Datum und Uhrzeit im ISO8601 UTC-Format  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `dimension[object]`: Externe Dimension eines Panels. Das Format ist durch eine Untereigenschaft mit 3 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CMT** für Zentimeter  - `documentation[string]`: Technische Dokumentation (Installation / Wartung / Gebrauch)  . Model: [https://schema.org/URL](https://schema.org/URL)- `id[*]`: Eindeutiger Bezeichner der Entität  - `installationCondition[array]`: Bedingung und Möglichkeit der Verwendung in den folgenden Umgebungen. Enum:'extremeHitze, extremeKälte, extremeFeuchtigkeit, extremesKlima, Wüste, Sand, Meer, salzhaltig, Staub, seismisch, andere'.  - `installationMode[string]`: Positionierung des Geräts in Bezug auf ein Bodenreferenzsystem. Ein eindeutiger Wert. Enum:'Antenne, Boden, Mast, Überdachung, Unterboden, Wand, andere'  - `inverterStatus[array]`: Status des Wechselrichters. Eine Kombination von Werten.  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mPPTPVVoltageDC[object]`: Minimaler und maximaler Photovoltaik-Spannungsbereich, MPPT erlaubt. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `manufacturerName[string]`: Hersteller Name des Artikels  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maxInputCurrentParallelAssembly[number]`: Max. Stromeingang mit einer parallelen Baugruppe. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxOutputPowerAC[number]`: Maximale Leistung oder Scheinleistung. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **D46** für Volt-Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `modelName[string]`: Modellbezeichnung des Artikels  . Model: [https://schema.org/model](https://schema.org/model)- `moduleYieldRate[object]`: Ausbeutesatz des Geräts. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert (Europäische Norm - Herstellernorm). Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `name[string]`: Der Name dieses Artikels.  - `nbInputParallelDC[string]`: Maximale Anzahl von Eingängen (parallel)  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `nbMPPTrackersDC[number]`: Anzahl der MPP-Tracker  . Model: [https://schema.org/Number.](https://schema.org/Number.)- `noiseLevel[number]`: Schallleistungspegel des Geräts. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **2N** für Dezibel  . Model: [http://schema.org/Number](http://schema.org/Number)- `nominalAmpereAC[number]`: Nennstromstärke *(Code I)*. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalAmpereDC[number]`: Nennstromstärke. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequencyAC[number]`: Nennfrequenz. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **HTZ** für Hertz  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalFrequencyDC[number]`:  Nennfrequenz. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **HTZ** für Hertz  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalPowerAC[number]`: Nennleistung . Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **WTT** für Watt  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalPowerDC[number]`: Nennleistung oder maximaler Leistungsfaktor für cos phi=1. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **WTT** für Watt  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltageAC[number]`: Nennspannung der Batterie *(Code U)*. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `nominalVoltageDC[number]`: Nennspannung. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingAirHumidity[object]`: Bereich der Luftfeuchtigkeit in der Betriebsumgebung. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **P1** für Prozent.  - `operatingAmpereAC[object]`: Erlaubte minimale und maximale Ampere. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [http://schema.org/Number](http://schema.org/Number)- `operatingAmpereDC[object]`: Erlaubte minimale und maximale Ampere. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **AMP** für Ampere  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingFrequencyAC[object]`: Zulässige Mindest- und Höchstfrequenz. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **HTZ** für Hertz  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `operatingFrequencyDC[object]`: Zulässige Mindest- und Höchstfrequenz. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **HTZ** für Hertz  . Model: [https://schema.org/Number](https://schema.org/Number)- `operatingTemperature[object]`: Betriebstemperaturbereich. Dies ist der minimale und maximale Widerstand gegen Kälte und Hitze. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **CEL** für Grad Celsius.  - `operatingVoltageAC[object]`: Zulässige Mindest- und Höchstspannung. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)- `operatingVoltageDC[object]`: Zulässige Mindest- und Höchstspannung. Das Format ist durch eine Untereigenschaft mit 2 Elementen strukturiert. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt.  . Model: [https://schema.org/Number](https://schema.org/Number)- `overVoltageCategory[string]`: Überspannungskategorie. - I : Anschluss an Stromkreise mit transienten Überspannungen auf einem angemessen niedrigen Niveau. - II : Hauptisolierung und zusätzliche Isolierung (Erdungsklemme). - III : Feste Installationen, deren Zuverlässigkeit und Verfügbarkeit spezifischen Spezifikationen unterliegt. - IV : Materialien am Ursprung der Elektroinstallation wie Stromzähler und Hauptmaterialien mit Überstromschutz.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `phaseType[string]`: Typ der Phase. Ein eindeutiger Wert. Enum:'singlePhase,threePhase'  - `possibilityOfUse[string]`: Möglichkeit der Verwendung. Enum:'gemischt, mobil, stationär, andere'  - `powerFactorAC[number]`: Leistungsfaktor für cos phi  . Model: [http://schema.org/Number](http://schema.org/Number)- `protectionClassSLK[string]`: Schutzklasse (SKL). - 0 : Hauptisolierung ohne Erdungsanschluss. - 1 : Hauptisolierung und zusätzliche Isolierung (Erdungsanschluss). - 2 : doppelte oder verstärkte Isolierung (entspricht dem Doppelten der Hauptisolierung) ohne zugängliches Metallteil. - 3 : Betrieb mit sehr niedriger Sicherheitsspannung (SELV) (maximal 50 V).  - `protectionIK[number]`: IK '*Mecanic Protection*'-Stufe, die sich auf die numerische Klassifizierung des Schutzgrades bezieht, den Gehäuse für elektrische Geräte gegen äußere mechanische Einwirkungen gemäß der Norm der Internationalen Elektrotechnischen Kommission (EN 62-262) bieten. - IK variiert von 0 (minimaler Widerstand) bis 10 (maximaler Widerstand), was einer Aufprallenergie (Einheit Joule) entspricht  . Model: [https://schema.org/Number](https://schema.org/Number)- `protectionIP[string]`: IP '*Eindringschutz*' für die Anschlussdose. Diese Stufe klassifiziert und bewertet den Grad des Schutzes, den mechanische und elektrische Gehäuse gegen Eindringen, Staub, versehentliche Berührung und Wasser gemäß der Norm der Internationalen Elektrotechnischen Kommission (EN 60-529) bieten. - Erste Ziffer: Schutz gegen feste Partikel (einzelne Ziffer: 0-6 oder 'X'). - Zweite Ziffer: Schutz gegen das Eindringen von Flüssigkeiten (Einzelne Ziffer: 0-9 oder 'X') - Dritte Ziffer: Personenschutz gegen den Zugang zu gefährlichen Teilen (optionaler Zusatzbuchstabe).- Vierte Ziffer: Sonstige Schutzmaßnahmen (optionaler Zusatzbuchstabe).  - `refDevice[*]`: Verweis auf die Haupteinheit [Gerät] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) bei Verwendung als zweite Verbindung.  - `refPointOfInterest[*]`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit der Beobachtung verknüpft ist.  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `self-consumption[number]`: Selbstverbrauch während der Nacht. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben.  Zum Beispiel steht **WTT** für Watt  . Model: [http://schema.org/Number](http://schema.org/Number)- `serialNumber[string]`: Seriennummern des Artikels  . Model: [https://schema.org/brand](https://schema.org/brand)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `startingVoltageDC[number]`: Startspannung. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **VLT** für Volt  . Model: [https://schema.org/Number](https://schema.org/Number)- `supplyPhaseNb[number]`: Anzahl der Stromversorgungsphasen  . Model: [https://schema.org/Number](https://schema.org/Number)- `topology[string]`: Beschreibung der Topologie der Anlage.  - `type[string]`: NGSI-Entitätstyp. Es muss InverterDevice sein  - `typeOfUse[string]`: Akzeptierte Verwendung hinsichtlich der Positionierung in einer Innen-/Außenumgebung. Enum:'innen, außen, gemischt, andere'  - `weight[number]`: Gewicht. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **KGM** für Kilogramm  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateLastReported`  - `id`  - `location`  - `phaseType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Zusätzliche Informationen zum Datenmodell. Dieses Datenmodell kann direkt als Hauptentität zur Beschreibung des Geräts [INVERTER] oder als Unterentität des Datenmodells [DEVICE] unter Verwendung eines Verweises über das Attribut `refDevice` verwendet werden.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### InverterDevice NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein InverterDevice im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### InverterDevice NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein InverterDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### InverterDevice NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein InverterDevice im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### InverterDevice NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein InverterDevice im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
