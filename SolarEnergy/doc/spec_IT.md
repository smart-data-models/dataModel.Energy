[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: SolarEnergy  
===================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Energy/blob/master/SolarEnergy/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un modello di dati per la generazione di energia solare.  
versione: 0.0.1  

## Elenco delle proprietà  

- `activePower`: I valori reali saranno rilevati da sottoproprietà i cui nomi saranno uguali al nome di ciascuna delle fasi della corrente alternata: L1, L2, L3.  - `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `current`: Corrente elettrica. I valori reali saranno trasmessi da una sottoproprietà per fase di corrente alternata e il filo neutro: L1, L2, L3 e N.  - `dataDescriptor`: URI che punta all'entità descrittore di dati  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `energyGenerated`: Energia generata in un intervallo di tempo specifico dalla risorsa energetica corrispondente a questa osservazione.  - `frequency`: Frequenza osservata dall'entità corrispondente a questa osservazione.  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxSolarPowerMeasure`: Una misura dell'energia solare massima che può essere generata.  - `name`: Il nome di questo articolo.  - `observationDateTime`: Ultima ora di osservazione riportata.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `phaseCurrent`: Corrente per fase. Tripla ordinata che comprende la potenza attiva di tre fasi nel seguente ordine: [R Y B]  - `phaseVoltage`: La tensione tra ogni fase e il conduttore neutro. I valori effettivi saranno trasmessi da una sottoproprietà per fase di corrente alternata: L1, L2 e L3  - `powerFactor`: Fattore di potenza per ogni fase. I valori effettivi saranno trasmessi da una sottoproprietà per fase di corrente alternata: L1, L2 e L3  - `reactivePower`: Potenza reattiva a frequenza fondamentale. I valori effettivi saranno trasmessi da sottoproprietà i cui nomi saranno uguali al nome di ciascuna delle fasi della corrente alternata: L1, L2, L3.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `totalActivePower`: Potenza attiva totale consumata da tutte le fasi.  - `totalEnergyGenerated`: Energia totale generata dalla risorsa energetica corrispondente a questa osservazione.  - `totalReactivePower`: Potenza reattiva totale per tutte le fasi.  - `type`: Tipo di entità NGSI. Deve essere SolarEnergy  - `voltage`: Il valore di Tensione nell'entità corrispondente a questa osservazione.    
Proprietà richieste  
- `id`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempio di payloads  
#### SolarEnergy NGSI-v2 valori chiave Esempio  
Ecco un esempio di SolarEnergy in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### SolarEnergy NGSI-v2 normalizzato Esempio  
Ecco un esempio di un SolarEnergy in formato JSON-LD come normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### SolarEnergy NGSI-LD valori chiave Esempio  
Ecco un esempio di SolarEnergy in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
    "https://smart-data-models.github.io/dataModel.Energy/context.jsonld"  
  ]  
}  
```  
#### SolarEnergy NGSI-LD normalizzato Esempio  
Ecco un esempio di un SolarEnergy in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
    "https://smart-data-models.github.io/dataModel.Energy/context.jsonld"  
  ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza  
