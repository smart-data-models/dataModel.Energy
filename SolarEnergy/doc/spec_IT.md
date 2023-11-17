<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: SolarEnergy    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.Energy/blob/master/SolarEnergy/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un modello di dati per la generazione di energia solare.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `activePower[object]`: I valori effettivi saranno rilevati da sottoproprietà il cui nome sarà uguale al nome di ciascuna delle fasi della corrente alternata: L1, L2, L3.  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: Corrente elettrica. I valori effettivi saranno trasmessi da una sottoproprietà per ogni fase di corrente alternata e per il filo neutro: L1, L2, L3 e N  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
	- `L3`:       
- `dataDescriptor[string]`: URI che punta all'entità descrittore di dati  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `energyGenerated[number]`: Energia generata in un intervallo di tempo specifico dalla risorsa energetica corrispondente a questa osservazione.  - `frequency[number]`: Frequenza osservata dall'entità corrispondente a questa osservazione  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `maxSolarPowerMeasure[number]`: Misura dell'energia solare massima che può essere generata  - `name[string]`: Il nome di questo elemento  - `observationDateTime[date-time]`: Ultima ora di osservazione segnalata  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `phaseCurrent[object]`: Corrente per fase. Triplice ordinata comprendente la potenza attiva di tre fasi nel seguente ordine: [R Y B]  	- `L1`:       
	- `L2`:       
- `phaseVoltage[object]`: La tensione tra ogni fase e il conduttore neutro. I valori effettivi saranno trasmessi da una sottoproprietà per ogni fase della corrente alternata: L1, L2 e L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
- `powerFactor[object]`: Fattore di potenza per ogni fase. I valori effettivi saranno trasmessi da una sottoproprietà per ogni fase della corrente alternata: L1, L2 e L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
- `reactivePower[object]`: Potenza reattiva a frequenza fondamentale. I valori effettivi saranno trasmessi da sottoproprietà il cui nome sarà uguale al nome di ciascuna delle fasi della corrente alternata: L1, L2, L3  . Model: [http://schema.org/StructuredValue](http://schema.org/StructuredValue)	- `L1`:       
	- `L2`:       
- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `totalActivePower[number]`: Potenza attiva totale consumata da tutte le fasi  - `totalEnergyGenerated[number]`: Energia totale generata dalla risorsa energetica corrispondente a questa osservazione  - `totalReactivePower[number]`: Potenza reattiva totale per tutte le fasi  - `type[string]`: Tipo di entità NGSI. Deve essere SolarEnergy  - `voltage[number]`: Il valore di Tensione nell'entità corrispondente a questa osservazione  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### SolarEnergy NGSI-v2 valori-chiave Esempio    
Ecco un esempio di SolarEnergy in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### SolarEnergy NGSI-v2 normalizzato Esempio    
Ecco un esempio di SolarEnergy in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### SolarEnergy NGSI-LD valori chiave Esempio    
Ecco un esempio di SolarEnergy in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### SolarEnergy NGSI-LD normalizzato Esempio    
Ecco un esempio di SolarEnergy in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
