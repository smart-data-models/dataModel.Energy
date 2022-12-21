/* (Beta) Export of data model ACMeasurement of the subject dataModel.Energy for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE phaseType_type AS ENUM ('singlePhase', 'threePhase');CREATE TYPE ACMeasurement_type AS ENUM ('ACMeasurement');
CREATE TABLE ACMeasurement (activeEnergyExport json, activeEnergyImport json, activePower json, address json, alternateName text, apparentEnergyExport json, apparentEnergyImport json, apparentPower json, areaServed text, current json, dataProvider text, dateCreated timestamp, dateEnergyMeteringStarted timestamp, dateModified timestamp, dateObserved timestamp, dateObservedFrom timestamp, dateObservedTo timestamp, description text, displacementPowerFactor json, frequency text, id text, location json, name text, owner json, phaseToPhaseVoltage json, phaseType phaseType_type, phaseVoltage json, powerFactor json, reactiveEnergyExport json, reactiveEnergyImport json, reactivePower json, refDevice json, refTargetDevice json, seeAlso json, source text, thdCurrent json, thdVoltage json, totalActiveEnergyExport text, totalActiveEnergyImport text, totalActivePower text, totalApparentEnergyExport text, totalApparentEnergyImport text, totalApparentPower text, totalDisplacementPowerFactor text, totalPowerFactor text, totalReactiveEnergyExport text, totalReactiveEnergyImport text, totalReactivePower text, type ACMeasurement_type);