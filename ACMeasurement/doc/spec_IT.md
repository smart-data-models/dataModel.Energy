<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: ACMeasurement    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.Energy/blob/master/ACMeasurement/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Il Modello di dati destinato a misurare l'energia elettrica consumata da un sistema elettrico che utilizza una corrente alternata (AC) per un sistema trifase (L1, L2, L3) o monofase (L) e neutro (N). Integra la versione iniziale del Modem dati [THREEPHASEMEASUREMENT], estesa per eseguire anche misure monofase. Include gli attributi per varie misure elettriche come potenza, frequenza, corrente e tensione.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `activeEnergyExport[object]`: Energia attiva esportata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dell'esportazione di energia attiva      
	- `L2[number]`: Valore per la fase 2 dell'esportazione di energia attiva      
	- `L3[number]`: Valore per la fase 3 dell'esportazione di energia attiva      
- `activeEnergyImport[object]`: Energia attiva importata, cioè consumata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dell'importazione di energia attiva      
	- `L2[number]`: Valore per la fase 2 dell'importazione attiva di energia      
	- `L3[number]`: Valore per la fase 3 dell'importazione attiva di energia      
- `activePower[object]`: Potenza attiva consumata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore della fase 1 della potenza attiva      
	- `L2[number]`: Valore della fase 2 della potenza attiva      
	- `L3[number]`: Valore della fase 3 della potenza attiva      
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel Paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica      
- `alternateName[string]`: Un nome alternativo per questa voce  - `apparentEnergyExport[object]`: Energia apparente esportata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dell'esportazione apparente di energia      
	- `L2[number]`: Valore per la fase 2 dell'esportazione apparente di energia      
	- `L3[number]`: Valore per la fase 3 dell'esportazione apparente di energia      
- `apparentEnergyImport[object]`: Energia apparente importata, cioè consumata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dell'importazione apparente di energia      
	- `L2[number]`: Valore per la fase 2 dell'importazione apparente di energia      
	- `L3[number]`: Valore per la fase 3 dell'importazione apparente di energia      
- `apparentPower[object]`: Potenza apparente consumata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore della fase 1 della potenza apparente      
	- `L2[number]`: Valore della fase 2 della potenza apparente      
	- `L3[number]`: Valore della fase 3 della potenza apparente      
- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[object]`: Corrente elettrica. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 della corrente      
	- `L2[number]`: Valore per la fase 2 della corrente      
	- `L3[number]`: Valore per la fase 3 della corrente      
	- `N[number]`: Valore per la fase neutra della corrente      
- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateEnergyMeteringStarted[date-time]`: La data di inizio della misurazione dell'energia in formato ISO8601 UTC.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateObserved[date-time]`: Data e ora di questa osservazione rappresentate in formato ISO8601 UTC. Può essere rappresentata da un istante di tempo specifico o da un intervallo ISO8601 per separare gli attributi `dateObservedFrom`,`dateObservedTo`.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedFrom[date-time]`: Periodo di osservazione: Data e ora di inizio in formato ISO8601 UTC. Questo attributo può essere usato in aggiunta all'attributo `dateObserved` quando corrisponde a un intervallo di tempo da evidenziare.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateObservedTo[date-time]`: Periodo di osservazione: Data e ora finale in formato ISO8601 UTC. Questo attributo può essere utilizzato in aggiunta all'attributo `dateObserved` quando corrisponde a un intervallo di tempo da evidenziare.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: Descrizione dell'articolo  - `displacementPowerFactor[object]`: Fattore di potenza di spostamento per ciascuna fase. La quantità si basa sulla frequenza fondamentale del sistema  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dello spostamento Fattore di potenza      
	- `L2[number]`: Valore per la fase 2 dello spostamento Fattore di potenza      
	- `L3[number]`: Valore per la fase 3 dello spostamento Fattore di potenza      
- `frequency[number]`: La frequenza del circuito. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `phaseToPhaseVoltage[object]`: Tensione tra le fasi. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L12[number]`: Valore della tensione tra fase 1 e fase 2      
	- `L23[number]`: Valore della tensione tra fase 2 e fase 3      
	- `L31[number]`: Valore della tensione tra fase 3 e fase 1      
- `phaseType[string]`: Tipo di fase. Un valore unico. Enum:'monofase, trifase'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `phaseVoltage[object]`: La tensione tra ciascun conduttore di fase e neutro. Il codice dell'unità di misura (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 della tensione      
	- `L2[number]`: Valore per la fase 2 della tensione      
	- `L3[number]`: Valore per la fase 3 della tensione      
- `powerFactor[object]`: Fattore di potenza per ogni fase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore del fattore di potenza per la fase 1      
	- `L2[number]`: Valore del fattore di potenza per la fase 2      
	- `L3[number]`: Valore del fattore di potenza per la fase 3      
- `reactiveEnergyExport[object]`: Energia reattiva a frequenza fondamentale esportata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dell'esportazione di energia reattiva      
	- `L2[number]`: Valore per la fase 2 dell'esportazione di energia reattiva      
	- `L3[number]`: Valore per la fase 3 dell'esportazione di energia reattiva      
- `reactiveEnergyImport[object]`: Energia reattiva a frequenza fondamentale importata, cioè consumata per fase. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 dell'importazione di energia reattiva      
	- `L2[number]`: Valore per la fase 2 dell'importazione di energia reattiva      
	- `L3[number]`: Valore per la fase 3 dell'importazione di energia reattiva      
- `reactivePower[object]`: Potenza reattiva a frequenza fondamentale. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore della fase 1 della potenza reattiva      
	- `L2[number]`: Valore della fase 2 della potenza reattiva      
	- `L3[number]`: Valore della fase 3 della potenza reattiva      
- `refDevice[array]`: Riferimento ai dispositivi che hanno catturato questa osservazione  . Model: [https://schema.org/URL](https://schema.org/URL)- `refTargetDevice[array]`: Riferimento a un elenco dei dispositivi per i quali è stata effettuata la misurazione  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `thdCurrent[object]`: Distorsione armonica totale della corrente per ogni fase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 della corrente di td      
	- `L2[number]`: Valore per la fase 2 della corrente di td      
	- `L3[number]`: Valore per la fase 3 della corrente di td      
- `thdVoltage[object]`: Distorsione armonica totale della tensione per ogni fase  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `L1[number]`: Valore per la fase 1 della tensione thd      
	- `L2[number]`: Valore per la fase 2 della tensione thd      
	- `L3[number]`: Valore per la fase 3 della tensione thd      
- `totalActiveEnergyExport[number]`: Energia totale importata, cioè consumata. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActiveEnergyImport[number]`: Energia totale importata, cioè consumata. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalActivePower[number]`: Potenza attiva totale consumata. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentEnergyExport[number]`: Energia totale esportata (in termini di potenza apparente). Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalApparentEnergyImport[number]`: Energia totale importata, cioè consumata (in termini di potenza apparente). Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalApparentPower[number]`: Potenza apparente totale consumata. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalDisplacementPowerFactor[number]`: Somma del fattore di potenza di spostamento comprendente tutte le fasi. La quantità si basa sulla frequenza fondamentale del sistema  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalPowerFactor[number]`: Somma del fattore di potenza di tutte le fasi  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalReactiveEnergyExport[number]`: Energia reattiva totale a frequenza fondamentale esportata. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `totalReactiveEnergyImport[number]`: Energia totale importata, cioè consumata (per quanto riguarda la potenza reattiva a frequenza fondamentale). Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `totalReactivePower[number]`: Potenza reattiva totale consumata. Il codice dell'unità (testo) è fornito utilizzando i [Codici comuni UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: Tipo di proprietà NGSI. Deve essere ACMeasurement  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `dateObserved`  - `id`  - `location`  - `phaseType`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Informazioni aggiuntive sugli attributi.  Per alcuni attributi, come corrente e tensione, il valore è un valore strutturato con proprietà per la fase singola (L) o per tre fasi diverse (L1, L2 e L3). Per alcune misure, come i diversi tipi di potenza (attiva, reattiva e apparente), esiste un attributo per il totale di tutte le fasi. Le regole sono definite come segue: - Trifase - Totale = L1 + L2 + L3 - Monofase - Totale = L. Per la maggior parte degli attributi, esistono vari modi per misurarli. A tale scopo si può utilizzare l'attributo meta-dati measurementType. Può avere i seguenti valori: media, valore efficace, minimo, massimo. Quando si usano i valori [average, rms, minimum, maximum], si deve usare un altro attributo di metadati chiamato measurementInterval per indicare la durata del periodo di misurazione in secondi. Inoltre, un attributo timestamp dovrebbe essere l'ora di fine del periodo di misurazione.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
Nota. I valori saranno trasmessi da 1 o 3 proprietà secondarie a seconda del tipo di fase per ciascuna fase Monofase. Valori individuali L. Trifase. Somma dei valori individuali. L1, L2, L3. Tutti i valori sono calcolati a partire dalla data di inizio della misurazione [dateEnergyMeteringStarted].    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### Valori chiave ACMeasurement NGSI-v2 Esempio    
Ecco un esempio di ACMeasurement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### ACMeasurement NGSI-v2 normalizzato Esempio    
Ecco un esempio di ACMeasurement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
        43.66481,  
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
    "type": "StructuredValue",  
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
    "type": "Boolean",  
    "value": true  
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
#### Valori chiave ACMeasurement NGSI-LD Esempio    
Ecco un esempio di ACMeasurement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### ACMeasurement NGSI-LD normalizzato Esempio    
Ecco un esempio di ACMeasurement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
