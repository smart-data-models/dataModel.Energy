<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : TechnicalCabinetDevice  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Energy/blob/master/TechnicalCabinetDevice/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Le modèle de données des armoires techniques est destiné à décrire les caractéristiques techniques de l'appareil, conçu pour être placé dans un environnement urbain ou interurbain. L'objectif principal de ces armoires pour ce Modèle de Données est de protéger les équipements électriques nécessaires au contrôle, à la surveillance, à la lecture et à la gestion de l'éclairage urbain, de la signalisation, de la vidéo et de la distribution électrique. Le champ d'application de certaines de ces armoires peut s'étendre à une protection supplémentaire pour des installations d'appareils modulaires de téléphonie, d'informatique, de stations météorologiques, de stations photo-voltaïques, de stations d'éoliennes, de télécommunications, de réseaux, de données, d'optique, etc. *Remarque* : Ce modèle de données peut être utilisé directement comme entité principale pour décrire le dispositif `Cabinet technique` ou comme sous-entité du modèle de données `DEVICE` en utilisant une référence par l'attribut `refDevice`. Il peut également faire référence à la liste de tous les composants qu'il contient, avec l'attribut `refDeviceList`, en utilisant le modèle de données 'DEVICE'**.  
version :  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nom alternatif pour cet élément  - `application[array]`: Application cible du dispositif concernant l'environnement. Une combinaison de ces valeurs. Enum : 'commercial, distributionService, industriel, autre, travaux publics, route, tertiaire, service urbain'.  - `areaServed[string]`: La zone géographique où un service ou un article offert est fourni  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nom de la marque  . Model: [https://schema.org/brand](https://schema.org/brand)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastReported[string]`: Un horodatage qui indique la dernière fois que le dispositif a transmis des données avec succès. Date et heure dans le format ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `designMaterials[array]`: Concevoir les matériaux pour construire l'armoire. Une combinaison de ces valeurs. Enum : 'ABS-Plastique, aluminium, fibre de verre, acier galvanisé, autre, polyester, acier inoxydable'.  - `dimension[object]`: Le format est structuré par une sous-propriété de 3 éléments. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **CMT** représente le centimètre.  - `documentation[string]`: Un lien vers la documentation de l'appareil  . Model: [https://schema.org/URL](https://schema.org/URL)- `doorClosingMode[array]`: Mode de fermeture de la porte. Une valeur unique de ces valeurs. Enum : 'fixedHandle, other, revolvingHandle, triangleHandle' (poignée fixe, autre, poignée tournante, triangle)  - `doorCount[number]`: Nombre de portes de l'armoire technique.  - `doorOpeningAngle[number]`: Angle d'ouverture de la porte exprimé en degrés décimaux avec une plage de 0 à 180 degrés. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **DD** représente les degrés décimaux.  - `doorType[string]`: Type de porte de l'armoire technique. Une valeur unique parmi ces valeurs. Enum : 'mixte, autre, pleine, transparente'.  - `exteriorCoating[array]`: Revêtement intérieur. Une combinaison de ces valeurs. Enum : "fibreGlass, autre, plastique, polyester, polyesterResin, acier  - `exteriorFinish[array]`: Finition extérieure. Une combinaison de ces valeurs. Enum : 'graffiti, autre, surélevé, crépi, lisse, texturé'.  - `id[*]`: Identifiant unique de l'entité  - `installationCondition[array]`: État et possibilité d'utilisation dans les environnements suivants. Une combinaison de ces valeurs. Enum : 'desert, dust, extremeCold, extremeClimate, extremeHeat, extremeHumidity, marine, none, other, saline, seismic, sand'.  - `installationMode[string]`: Positionnement de l'appareil par rapport à un système de référence au sol. Enum : 'aérien, sol, autre, poteau, toiture, souterrain, mur'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `interiorCoating[array]`: Revêtement intérieur. Une combinaison de ces valeurs. Enum : 'fibre de verre, isolant thermique, autre, plastique, polyester, résine polyester, acier'.  - `internalDimension[object]`: Dimension interne correspondant à l'emplacement de travail à l'intérieur de l'armoire technique. Le format est structuré par une sous-propriété de 3 éléments. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **CMT** représente Centimètre  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `manufacturerName[string]`: Nom du fabricant  . Model: [https://schema.org/manufacturer](https://schema.org/manufacturer)- `maximumSystemVoltage[number]`: Tension maximale du système autorisée pour le **module**. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **VLT** représente Volt  - `modelName[string]`: Nom du modèle tel qu'indiqué par le fabricant.  - `name[string]`: Le nom de cet élément.  - `operatingTemperature[object]`: Plage de températures de fonctionnement ambiantes. Il s'agit de la résistance minimale et maximale au froid et à la chaleur. Le format est structuré par une sous-propriété de 2 éléments. Le code d'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **CEL** représente le degré Celsius.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `possibilityOfUse[string]`: Possibilité d'utilisation. Une valeur unique. Enum : 'mixte, mobile, autre, stationnaire'.  - `protectionIK[number]`: Niveau IK "*Protection mécanique*" relatif à la classification numérique des degrés de protection fournis par les boîtiers d'équipements électriques contre les impacts mécaniques externes, conformément à la norme de la Commission électrotechnique internationale (EN 62-262). - L'IK varie de 0 (résistance minimale) à 10 (résistance maximale), ce qui représente une énergie d'impact (unité Joule).  - `protectionIP[string]`: IP "Ingress Protection" pour la boîte de jonction. Il s'agit du niveau qui classe et évalue le degré de protection offert par les boîtiers mécaniques et les enveloppes électriques contre les intrusions, la poussière, les contacts accidentels et l'eau, conformément à la norme de la Commission électrotechnique internationale (EN 60-529). Premier chiffre : Protection contre les particules solides (chiffre unique : 06 ou "X"). Deuxième chiffre : Protection contre la pénétration de liquides (chiffre unique : 09 ou 'X'). 3 : Troisième chiffre : protection personnelle contre l'accès aux parties dangereuses (lettre supplémentaire facultative). Quatrième chiffre : Autres protections (lettre supplémentaire facultative)  - `protectionOthers[array]`: Autres protection de l'armoire technique. Une combinaison de ces valeurs. Enum : 'abrasion, sous-sol, anti-humidité, affichage, arrachage de porte, poussière, ouverture forcée, graffiti, insecte, autre, surcharge du toit, brouillard salin, blindage, solaire, vandalisme, eau'.  - `refDevice[*]`: Le dispositif utilisé pour obtenir les données exprimées par cet enregistrement  - `refDeviceList[array]`: Une liste de référence aux [Dispositifs] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) qui se trouvent à l'intérieur du dispositif de l'armoire technique.  - `refPointOfInterest[*]`: Référence à un [PointOfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) lié à l'observation.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'article  - `serialNumber[string]`: Numéro de série du conteneur  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type[string]`: Type d'entité NGSI. Il doit être TechnicalCabinetDevice.  - `typeOfUse[string]`: Une utilisation acceptée quant à son positionnement dans un environnement intérieur / extérieur. Une valeur unique de ces valeurs. Enum : 'indoor, mixed, outdoor, other' (intérieur, mixte, extérieur, autre)  - `ventilationMode[array]`: Mode de ventilation. Une combinaison de ces valeurs. Enum : 'airConditioners, dehumidifier, none, other, selfVentilatedGills' (climatiseurs, déshumidificateurs, aucun, autres, branchages auto-ventilés)  - `weight[number]`: Poids de l'article. Le code d'unité (texte) de mesure est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **KGM** représente les kilogrammes.  . Model: [https://schema.org/weigth](https://schema.org/weigth)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `dateLastReported`  - `dimension`  - `id`  - `location`  - `type`  - `typeOfUse`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### TechnicalCabinetDevice Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'un TechnicalCabinetDevice au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### TechnicalCabinetDevice NGSI-v2 normalisé Exemple  
Voici un exemple d'un TechnicalCabinetDevice au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### TechnicalCabinetDevice Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'un TechnicalCabinetDevice au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### TechnicalCabinetDevice NGSI-LD normalisé Exemple  
Voici un exemple d'un TechnicalCabinetDevice au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
