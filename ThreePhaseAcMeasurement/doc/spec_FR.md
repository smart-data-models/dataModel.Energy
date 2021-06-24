Entité : ThreePhaseAcMeasurement  
================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Energy/blob/master/ThreePhaseAcMeasurement/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Mesure électrique provenant d'un système qui utilise un courant alternatif triphasé.**  

## Liste des propriétés  

- `activeEnergyExport`: Énergie active exportée par phase depuis la date de début du comptage. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases de courant alternatif : L1, L2, L3.  - `activeEnergyImport`: Énergie active importée, c'est-à-dire consommée par phase depuis la date de début du comptage. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases de courant alternatif : L1, L2, L3.  - `activePower`: Les valeurs réelles seront contrôlées par des sous-propriétés dont le nom sera égal au nom de chacune des phases du courant alternatif : L1, L2, L3.  - `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `apparentEnergyExport`: Énergie apparente exportée par phase depuis la date de début du comptage. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases du courant alternatif : L1, L2, L3.  - `apparentEnergyImport`: Énergie apparente importée, c'est-à-dire consommée par phase depuis la date de début du comptage. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases du courant alternatif : L1, L2, L3.  - `apparentPower`: Puissance apparente consommée par phase. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases du courant alternatif : L1, L2, L3  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `current`: Le courant électrique. Les valeurs réelles seront véhiculées par une sous-propriété par phase de courant alternatif et le fil neutre : L1, L2, L3 et N.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateEnergyMeteringStarted`: La date de début du comptage de l'énergie.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `displacementPowerFactor`: Facteur de puissance de déplacement pour chaque phase. Cette quantité est basée sur la fréquence fondamentale du système. Les valeurs réelles seront véhiculées par une sous-propriété par phase de courant alternatif : L1, L2 et L3  - `frequency`: La fréquence du circuit.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `phaseToPhaseVoltage`: Tension entre phases. Une valeur pour chaque paire de phases : phases 1 et 2 (L12), phases 2 et 3 (L32), phases 3 et 1 (L31).  - `phaseVoltage`: La tension entre chaque phase et le conducteur neutre. Les valeurs réelles seront véhiculées par une sous-propriété par phase de courant alternatif : L1, L2 et L3  - `powerFactor`: Facteur de puissance pour chaque phase. Les valeurs réelles seront transmises par une sous-propriété par phase de courant alternatif : L1, L2 et L3  - `reactiveEnergyExport`: Énergie réactive à fréquence fondamentale exportée par phase depuis la date de début du comptage. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases de courant alternatif : L1, L2, L3.  - `reactiveEnergyImport`: Énergie réactive à fréquence fondamentale importée, c'est-à-dire consommée par phase depuis la date de début du comptage. Les valeurs réelles seront véhiculées par des sous-propriétés dont les noms seront égaux au nom de chacune des phases du courant alternatif : L1, L2, L3.  - `reactivePower`: Puissance réactive de la fréquence fondamentale. Les valeurs réelles seront véhiculées par des sous-propriétés dont le nom sera égal au nom de chacune des phases du courant alternatif : L1, L2, L3.  - `refDevice`: Dispositif(s) utilisé(s) pour obtenir la mesure.  - `refTargetDevice`: Dispositif(s) pour lequel (lesquels) la mesure a été prise.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `thdCurrent`: Distorsion harmonique totale du courant électrique. Les valeurs réelles seront véhiculées par une sous-propriété par phase de courant alternatif : L1, L2 et L3  - `thdVoltage`: Distorsion harmonique totale de la tension pour chaque phase. Les valeurs réelles seront véhiculées par une sous-propriété par phase de courant alternatif : L1, L2 et L3  - `totalActiveEnergyExport`: Énergie totale exportée depuis le début du comptage (depuis `dateEnergyMeteringStarted`).  - `totalActiveEnergyImport`: Énergie totale importée, c'est-à-dire consommée depuis le début du comptage (depuis `dateEnergyMeteringStarted`).  - `totalActivePower`: Puissance active consommée (en comptant toutes les phases)  - `totalApparentEnergyExport`: Énergie totale exportée (par rapport à la puissance apparente) depuis la date de début du comptage (`dateEnergyMeteringStarted`)  - `totalApparentEnergyImport`: Energie totale importée, c'est-à-dire consommée (par rapport à la puissance apparente) depuis la date de début du comptage (`dateEnergyMeteringStarted`)  - `totalApparentPower`: Puissance apparente consommée (en comptant toutes les phases).  - `totalDisplacementPowerFactor`: Facteur de puissance de déplacement incluant toutes les phases. Cette quantité est basée sur la fréquence fondamentale du système.  - `totalPowerFactor`: Facteur de puissance incluant toutes les phases  - `totalReactiveEnergyExport`: Total de l'énergie réactive à fréquence fondamentale exportée depuis le début du comptage (depuis `dateEnergyMeteringStarted`).  - `totalReactiveEnergyImport`: Énergie totale importée, c'est-à-dire consommée (en ce qui concerne la puissance réactive à fréquence fondamentale) depuis la date de début du comptage (`dateEnergyMeteringStarted`)  - `totalReactivePower`: Puissance réactive consommée (en comptant toutes les phases)  - `type`: Il doit être égal à `ThreePhaseAcMeasurement`.    
Propriétés requises  
- `id`  - `type`    
Texte à inclure entre le titre général et la description.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ThreePhaseAcMeasurement:    
  description: 'An electrical  measurement from a system that uses three phase alternating current.'    
  properties:    
    activeEnergyExport:    
      description: 'Active energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'kilowatt hour (kWh)'    
    activeEnergyImport:    
      description: 'Active energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'kilowatt hour (kWh)'    
    activePower:    
      description: 'The actual values will beconveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3. '    
      properties:    
        L1:    
          type: number    
        L2:    
          type: number    
        L3:    
          type: number    
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    apparentEnergyExport:    
      description: 'Apparent energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'kilovolt-ampere-hour (kVAh)'    
    apparentEnergyImport:    
      description: 'Apparent energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'kilovolt-ampere-hour (kVAh)'    
    apparentPower:    
      description: 'Apparent power consumed per phase. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'volt-ampere (VA)'    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'Ampers (A)'    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateEnergyMeteringStarted:    
      description: 'The starting date for metering energy.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    displacementPowerFactor:    
      description: 'Displacement power factor for each phase. The quantity is based on the fundamental frequency of the system. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: '-1 to +1'    
    frequency:    
      description: 'The frequency of the circuit.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'Hertz (Hz)'    
    id:    
      anyOf: &threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    phaseToPhaseVoltage:    
      description: 'Voltage between phases. A value for each phase pair: phases 1 and 2 (L12), phases 2 and 3 (L32), phases 3 and 1 (L31).'    
      properties:    
        L12:    
          minimum: 0    
          type: number    
        L23:    
          minimum: 0    
          type: number    
        L31:    
          minimum: 0    
          type: number    
      type: Property    
      x-ngsi:    
        model: (http://schema.org/StructuredValue    
        units: 'Volts (V)'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: '-1 to +1'    
    reactiveEnergyExport:    
      description: 'Fundamental frequency reactive energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'kilovolt-ampere-reactive-hour (kVArh)'    
    reactiveEnergyImport:    
      description: 'Fundamental frequency reactive energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
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
      type: Property    
      x-ngsi:    
        model: 'kilovolt-ampere-reactive-hour (kVArh)'    
        units: http://schema.org/StructuredValue    
    reactivePower:    
      description: 'Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3.'    
      properties:    
        L1:    
          type: number    
        L2:    
          type: number    
        L3:    
          type: number    
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: 'volts-ampere-reactive (VAr)'    
    refDevice:    
      description: 'Device(s) used to obtain the measurement.'    
      items:    
        anyOf: *threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Relationship    
      uniqueItems: true    
    refTargetDevice:    
      description: 'Device(s) for which the measurement was taken.'    
      items:    
        anyOf: *threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: Relationship    
      uniqueItems: true    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    thdCurrent:    
      description: 'Total harmonic distortion of electrical current. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          maximum: 1    
          minimum: 0    
          type: number    
        L2:    
          maximum: 1    
          minimum: 0    
          type: number    
        L3:    
          maximum: 1    
          minimum: 0    
          type: number    
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: '0 to 1'    
    thdVoltage:    
      description: 'Total harmonic distortion of voltage for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'    
      properties:    
        L1:    
          maximum: 1    
          minimum: 0    
          type: number    
        L2:    
          maximum: 1    
          minimum: 0    
          type: number    
        L3:    
          maximum: 1    
          minimum: 0    
          type: number    
      type: Property    
      x-ngsi:    
        model: http://schema.org/StructuredValue    
        units: '0 to 1'    
    totalActiveEnergyExport:    
      description: 'Total energy exported since metering started (since `dateEnergyMeteringStarted`).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'kilowatt hour (kWh)'    
    totalActiveEnergyImport:    
      description: 'Total energy imported i.e. consumed since metering started (since `dateEnergyMeteringStarted`).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'kilowatt hour (kWh)'    
    totalActivePower:    
      description: 'Active power consumed (counting all phases)'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'watt (W)'    
    totalApparentEnergyExport:    
      description: 'Total energy exported (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'kilovolt-ampere-reactive-hour (kVArh)'    
    totalApparentEnergyImport:    
      description: 'Total energy imported i.e. consumed (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'kilovolt-ampere-hour (kVAh)'    
    totalApparentPower:    
      description: 'Apparent power consumed (counting all phases).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'volt-ampere (VA)'    
    totalDisplacementPowerFactor:    
      description: 'Displacement power factor including all phases. The quantity is based on the fundamental frequency of the system'    
      maximum: 1    
      minimum: -1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: '-1 to +1'    
    totalPowerFactor:    
      description: 'Power factor including all phases'    
      maximum: 1    
      minimum: -1    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: '-1 to +1'    
    totalReactiveEnergyExport:    
      description: 'Total fundamental frequency reactive energy exported since metering started (since `dateEnergyMeteringStarted`).'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'kilovolt-ampere-reactive-hour (kVArh)'    
    totalReactiveEnergyImport:    
      description: 'Total energy imported i.e. consumed (with regards to fundamental frequency reactive power) since the metering start date (`dateEnergyMeteringStarted`)'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: 'kilovolt-ampere-reactive-hour (kVArh)'    
    totalReactivePower:    
      description: 'Reactive power consumed (counting all phases)'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: 'volt-ampere-reactive (VAr)'    
    type:    
      description: 'It must be equal to `ThreePhaseAcMeasurement`.'    
      enum:    
        - ThreePhaseAcMeasurement    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
Texte à inclure après la liste des propriétés  
## Exemples de charges utiles  
#### Valeurs-clés de la NGSI-v2 pour la mesure de l'acidité en trois phases Exemple  
Voici un exemple de ThreePhaseAcMeasurement au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec la NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "dateEnergyMeteringStarted": "2018-07-07T15:05:59.408Z",  
  "refDevice": ["Device:eQL-EDF3GL-2006201705"],  
  "name": "HKAPK0200",  
  "description": "measurement corresponding to the ventilation machine rooms",  
  "totalActiveEnergyImport": 150781.96448,  
  "totalReactiveEnergyImport": 20490.3392,  
  "totalActiveEnergyExport": 1059.80176,  
  "totalReactiveEnergyExport": 93275.02176,  
  "totalActivePower": 31700.269531,  
  "activePower": {  
    "L1": 11996.416016,  
    "L2": 9461.501953,  
    "L3": 10242.351562  
  },  
  "totalReactivePower": -7830.332031,  
  "reactivePower": {  
    "L1": -2612.606934,  
    "L2": -2209.906006,  
    "L3": -3007.81958  
  },  
  "totalApparentPower": 36019.089844,  
  "apparentPower": {  
    "L1": 13201.412109,  
    "L2": 10755.304688,  
    "L3": 11941.094727  
  },  
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
  "frequency": 50.020672,  
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
#### Mesure de l'ac en trois phases NGSI-v2 normalisée Exemple  
Voici un exemple de ThreePhaseAcMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "dateEnergyMeteringStarted": {  
    "type": "DateTime",  
    "value": "2018-07-07T15:05:59.408Z"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": ["Device:eQL-EDF3GL-2006201705"]  
  },  
  "name": {  
    "value": "HKAPK0200"  
  },  
  "description": {  
    "value": "measurement corresponding to the ventilation machine rooms"  
  },  
  "totalActiveEnergyImport": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    },  
    "value": 150781.96448  
  },  
  "totalReactiveEnergyImport": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    },  
    "value": 20490.3392  
  },  
  "totalActiveEnergyExport": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    },  
    "value": 1059.80176  
  },  
  "totalReactiveEnergyExport": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      }  
    },  
    "value": 93275.02176  
  },  
  "totalActivePower": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "value": 31700.269531  
  },  
  "activePower": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 11996.416016,  
      "L2": 9461.501953,  
      "L3": 10242.351562  
    }  
  },  
  "totalReactivePower": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "value": -7830.332031  
  },  
  "reactivePower": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": -2612.606934,  
      "L2": -2209.906006,  
      "L3": -3007.81958  
    }  
  },  
  "totalApparentPower": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "value": 36019.089844  
  },  
  "apparentPower": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 13201.412109,  
      "L2": 10755.304688,  
      "L3": 11941.094727  
    }  
  },  
  "powerFactor": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      },  
      "onlyPositive": {  
        "value": true  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.908817,  
      "L2": 0.879906,  
      "L3": 0.859293  
    }  
  },  
  "displacementPowerFactor": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      },  
      "onlyPositive": {  
        "value": true  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.978013,  
      "L2": 0.973317,  
      "L3": 0.960382  
    }  
  },  
  "frequency": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "value": 50.020672  
  },  
  "current": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "rms"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 56.126038,  
      "L2": 45.894356,  
      "L3": 50.872452,  
      "N": 0.0  
    }  
  },  
  "phaseVoltage": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "rms"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 234.961304,  
      "L2": 234.563477,  
      "L3": 235.354034  
    }  
  },  
  "phaseToPhaseVoltage": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "rms"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L12": 406.769196,  
      "L23": 407.081238,  
      "L31": 407.734558  
    }  
  },  
  "thdVoltage": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.01471114,  
      "L2": 0.01600046,  
      "L3": 0.01541459  
    }  
  },  
  "thdCurrent": {  
    "metadata": {  
      "timestamp": {  
        "type": "DateTime",  
        "value": "2019-01-24T22:00:00.173Z"  
      },  
      "measurementType": {  
        "value": "average"  
      },  
      "measurementInterval": {  
        "value": 1  
      }  
    },  
    "type": "StructuredValue",  
    "value": {  
      "L1": 0.38497337,  
      "L2": 0.45807529,  
      "L3": 0.4938652  
    }  
  }  
}  
```  
#### Valeurs clés de la NGSI-LD pour la mesure de l'acidité en trois phases Exemple  
Voici un exemple de ThreePhaseAcMeasurement au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:ThreePhaseAcMeasurement:ThreePhaseAcMeasurement:LV3_Ventilation",  
  "type": "ThreePhaseAcMeasurement",  
  "dateEnergyMeteringStarted": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2018-07-07T15:05:59.408Z"  
    }  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Device:Device:eQL-EDF3GL-2006201705"  
    ]  
  },  
  "name": {  
    "type": "Property",  
    "value": "HKAPK0200"  
  },  
  "description": {  
    "type": "Property",  
    "value": "measurement corresponding to the ventilation machine rooms"  
  },  
  "totalActiveEnergyImport": {  
    "type": "Property",  
    "value": 150781.96448,  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalReactiveEnergyImport": {  
    "type": "Property",  
    "value": 20490.3392,  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalActiveEnergyExport": {  
    "type": "Property",  
    "value": 1059.80176,  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalReactiveEnergyExport": {  
    "type": "Property",  
    "value": 93275.02176,  
    "observedAt": "2019-01-24T22:00:00.173Z"  
  },  
  "totalActivePower": {  
    "type": "Property",  
    "value": 31700.269531,  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "activePower": {  
    "type": "Property",  
    "value": {  
      "L1": 11996.416016,  
      "L2": 9461.501953,  
      "L3": 10242.351562  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "totalReactivePower": {  
    "type": "Property",  
    "value": -7830.332031,  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "reactivePower": {  
    "type": "Property",  
    "value": {  
      "L1": -2612.606934,  
      "L2": -2209.906006,  
      "L3": -3007.81958  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "apparentPower": {  
    "type": "Property",  
    "value": {  
      "L1": 13201.412109,  
      "L2": 10755.304688,  
      "L3": 11941.094727  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
  "displacementPowerFactor": {  
    "type": "Property",  
    "value": {  
      "L1": 0.978013,  
      "L2": 0.973317,  
      "L3": 0.960382  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "current": {  
    "type": "Property",  
    "value": {  
      "L1": 56.126038,  
      "L2": 45.894356,  
      "L3": 50.872452,  
      "N": 0.0  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "phaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L1": 234.961304,  
      "L2": 234.563477,  
      "L3": 235.354034  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "phaseToPhaseVoltage": {  
    "type": "Property",  
    "value": {  
      "L12": 406.769196,  
      "L23": 407.081238,  
      "L31": 407.734558  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "rms"  
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
    "observedAt": "2019-01-24T22:00:00.173Z",  
    "measurementType": {  
      "type": "Property",  
      "value": "average"  
    },  
    "measurementInterval": {  
      "type": "Property",  
      "value": 1  
    }  
  },  
  "thdCurrent": {  
    "type": "Property",  
    "value": {  
      "L1": 0.38497337,  
      "L2": 0.45807529,  
      "L3": 0.4938652  
    },  
    "observedAt": "2019-01-24T22:00:00.173Z",  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Mesure triphasée de l'acidité NGSI-LD normalisée Exemple  
Voici un exemple de ThreePhaseAcMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "activePower": {  
    "L1": 11996.416016,  
    "L2": 9461.501953,  
    "L3": 10242.351562  
  },  
  "apparentPower": {  
    "L1": 13201.412109,  
    "L2": 10755.304688,  
    "L3": 11941.094727  
  },  
  "current": {  
    "L1": 56.126038,  
    "L2": 45.894356,  
    "L3": 50.872452,  
    "N": 0.0  
  },  
  "dateEnergyMeteringStarted": {  
    "@type": "DateTime",  
    "@value": "2018-07-07T15:05:59.408Z"  
  },  
  "description": "measurement corresponding to the ventilation machine rooms",  
  "displacementPowerFactor": {  
    "L1": 0.978013,  
    "L2": 0.973317,  
    "L3": 0.960382  
  },  
  "frequency": 50.020672,  
  "id": "urn:ngsi-ld:ThreePhaseAcMeasurement:ThreePhaseAcMeasurement:LV3_Ventilation",  
  "name": "HKAPK0200",  
  "phaseToPhaseVoltage": {  
    "L12": 406.769196,  
    "L23": 407.081238,  
    "L31": 407.734558  
  },  
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
    "urn:ngsi-ld:Device:Device:eQL-EDF3GL-2006201705"  
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
  "type": "ThreePhaseAcMeasurement"  
}  
```  
Le texte après tout  
