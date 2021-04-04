# dataModel.Energy
This folder contains domain specific data models related to energy. The adaptation of IEC standards (CIM) is one of the goals of this subject.

### List of data models

The following entity types are available:
- [ACMeasurement](https://github.com/smart-data-models/dataModel.Energy/blob/master/ACMeasurement/README.md). The Data Model intended to measure the electrical energies consumed by an electrical system which uses an Alternating Current (AC) for a three-phase (L1, L2, L3) or single-phase (L) and neutral (N). It integrates the initial version of the data Modem [THREEPHASEMEASUREMENT], extended to also perform single-phase measurements. It includes attributes for various electrical measurements such as power, frequency, current and voltage.

- [InverterDevice](https://github.com/smart-data-models/dataModel.Energy/blob/master/InverterDevice/README.md). The data model is intended to describe the mechanical, electrical characteristics of an Inverter according to *DC - Direct Current Information* supplied as input and *AC - Alternating Current Information*  returned as output. *Remark*: This Data Model can be used directly as a main entity to describe the device [Inverter] or as a sub-entity of the Data Model {DEVICE] using a reference by the [refDevice] attribute.

- [ThreePhaseAcMeasurement](https://github.com/smart-data-models/dataModel.Energy/blob/master/ThreePhaseAcMeasurement/README.md). An electrical  measurement from a system that uses three phase alternating current.



### Incubated data models
The list of incubated (on development) data models are:

  - [PhotovoltaicDevice_incubated](https://github.com/smart-data-models/dataModel.Energy/tree/master/PhotovoltaicDevice_incubated)


### Contributors
[Link](https://github.com/smart-data-models/dataModel.Energy/blob/master/CONTRIBUTORS.yaml) to the 4 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.Energy/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.Energy/pulls) on existing data models


