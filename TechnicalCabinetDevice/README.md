[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)
# TechnicalCabinetDevice
Version: 0.0.1

## Description 

Technical Cabinet Device Data Model is intended to to describe the technical characteristics of the Device, designed to be placed in an urban or interurban environment. The main objective of these cabinets for this Data Model is to protect the electrical equipment necessary for the control, surveillance, reading and management of urban lighting, signaling, video and electrical distribution. The scope of use of some of these cabinets can extend to an additional protection for installations of modular apparatuses of telephony, data processing, meteorological stations, photo-voltaic stations, wind turbines stations, telecommunications, networks, data, bre Optics , etc. *Remark* : This Data Model can be used directly as a main entity to describe the device `Technical Cabinet`  or as a sub-entity of the Data Model  `DEVICE` using a reference by the `refDevice` attribute. It can also refer to the list of all the components it contains, with the `refDeviceList` attribute, using the Data Model 'DEVICE'
### Specification

Link to the [interactive specification](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/TechnicalCabinetDevice/swagger.yaml)

Link to the [specification](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec.md)

Enlace a la [Especificación en español](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec_ES.md)

Lien vers le [spécification en français](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec_FR.md)

Link zur [deutschen Spezifikation](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec_DE.md)

Link alla [specifica](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec_IT.md)

[仕様へのリンク](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec_JA.md)

[链接到规范](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/doc/spec_ZH.md)
### Examples

Link to the [example](https://smart-data-models.github.io/dataModel.Energy/TechnicalCabinetDevice/examples/example.json) (keyvalues) for NGSI v2

Link to the [example](https://smart-data-models.github.io/dataModel.Energy/TechnicalCabinetDevice/examples/example.jsonld) (keyvalues) for NGSI-LD

Link to the [example](https://smart-data-models.github.io/dataModel.Energy/TechnicalCabinetDevice/examples/example-normalized.json) (normalized) for NGSI-V2

Link to the [example](https://smart-data-models.github.io/dataModel.Energy/TechnicalCabinetDevice/examples/example-normalized.jsonld) (normalized) for NGSI-LD
### Dynamic Examples generation

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/TechnicalCabinetDevice/schema.json&email=info@smartdatamodels.org) of NGSI-LD normalized payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/ngsi-ld_generator_keyvalues.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/TechnicalCabinetDevice/schema.json&email=info@smartdatamodels.org) of NGSI-LD keyvalues payloads compliant with this data model. Refresh for new values

Link to the [Generator](https://smartdatamodels.org/extra/geojson_features_generator.php?schemaUrl=https://raw.githubusercontent.com/smart-data-models/dataModel.Energy/master/TechnicalCabinetDevice/schema.json&email=info@smartdatamodels.org) of geojson feature format payloads compliant with this data model. Refresh for new values
### PostgreSQL schema

Link to the [PostgreSQL schema](https://github.com/smart-data-models/dataModel.Energy/blob/master/TechnicalCabinetDevice/schema.sql) of this data model
### Contribution

 If you have any issue on this data model you can raise an [issue](https://github.com/smart-data-models/dataModel.Energy/issues)  or contribute with a [PR](https://github.com/smart-data-models/dataModel.Energy/pulls)

 If you wish to develop your own data model you can start from [contribution manual](https://bit.ly/contribution_manual). Several services have been developed to help with: 
 - [Test data model repository](https://smartdatamodels.org/index.php/data-models-contribution-api/) including the schema and example payloads, etc
 - [Generate PostgreSQL schema](https://smartdatamodels.org/index.php/sql-service/) to help create a table, create type, etc