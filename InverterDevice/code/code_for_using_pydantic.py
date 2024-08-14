from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class ApplicationEnum(Enum):
    electricMobility = 'electricMobility'
    energyStorage = 'energyStorage'
    emergencyStorage = 'emergencyStorage'
    lighting = 'lighting'
    industrialStorage = 'industrialStorage'
    houseHoldStorage = 'houseHoldStorage'
    robotics = 'robotics'
    production = 'production'
    other = 'other'


class CoolingSystem(Enum):
    Convection = 'Convection'
    OptiCool = 'OptiCool'
    Regulated_fan = 'Regulated-fan'
    Other = 'Other'


class Dimension(BaseModel):
    depth: Optional[confloat(ge=0.0)] = None
    height: Optional[confloat(ge=0.0)] = None
    length: Optional[confloat(ge=0.0)] = None


class InstallationConditionEnum(Enum):
    extremeHeat = 'extremeHeat'
    extremeCold = 'extremeCold'
    extremeHumidity = 'extremeHumidity'
    extremeClimate = 'extremeClimate'
    desert = 'desert'
    sand = 'sand'
    marine = 'marine'
    saline = 'saline'
    dust = 'dust'
    seismic = 'seismic'
    other = 'other'


class InstallationMode(Enum):
    aerial = 'aerial'
    ground = 'ground'
    pole = 'pole'
    roofing = 'roofing'
    underGround = 'underGround'
    wall = 'wall'
    other = 'other'


class InverterStatu(Enum):
    field_00_OnSector = '00-OnSector'
    field_01_PowerFailure_OnBattery = '01-PowerFailure/OnBattery'
    field_02_LossCommunication = '02-LossCommunication'
    field_03_BatteryFault = '03-BatteryFault'
    field_04_SystemShutDown = '04-SystemShutDown'
    field_05_TensionDip = '05-TensionDip'
    field_06_OverVoltage = '06-OverVoltage'
    field_07_VoltageDrop = '07-VoltageDrop'
    field_08_VoltageIncrease = '08-VoltageIncrease'
    field_09_LineNoise = '09-LineNoise'
    field_10_FrequencyVariation = '10-FrequencyVariation'
    field_11_TransientDistortion = '11-TransientDistortion'
    field_12_HarmonicDistortion = '12-HarmonicDistortion'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class MPPTPVVoltageDC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class ModuleYieldRate(BaseModel):
    eta: Optional[float] = None
    euro: Optional[float] = None


class OperatingAirHumidity(BaseModel):
    max: Optional[confloat(ge=0.0, le=1.0)] = None
    min: Optional[confloat(ge=0.0, le=1.0)] = None


class OperatingAmpereAC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingAmpereDC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingFrequencyAC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingFrequencyDC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingTemperature(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=-50.0)] = None


class OperatingVoltageAC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OperatingVoltageDC(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=0.0)] = None


class OverVoltageCategory(Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'


class PhaseType(Enum):
    singlePhase = 'singlePhase'
    threePhase = 'threePhase'


class PossibilityOfUse(Enum):
    mixed = 'mixed'
    mobile = 'mobile'
    stationary = 'stationary'
    other = 'other'


class ProtectionClassSLK(Enum):
    field_0 = 0
    field_1 = 1
    field_2 = 2
    field_3 = 3


class Type6(Enum):
    InverterDevice = 'InverterDevice'


class TypeOfUse(Enum):
    indoor = 'indoor'
    outdoor = 'outdoor'
    mixed = 'mixed'
    other = 'other'


class InverterDevice(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    application: Optional[List[ApplicationEnum]] = Field(
        None,
        description="Target application of the Device regarding the environment. A unique value. Enum:'electricMobility, energyStorage, emergencyStorage, lighting, industrialStorage, houseHoldStorage, robotics, production, other'",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    brandName: Optional[str] = Field(None, description='Brand Name of the item')
    coolingSystem: Optional[CoolingSystem] = Field(
        None,
        description=" Cooling System of the Device. Enum:'Convection, OptiCool, Regulated-fan, Other'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastReported: Optional[AwareDatetime] = Field(
        None,
        description='A timestamps which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dimension: Optional[Dimension] = Field(
        None,
        description='External dimension of a Panel. The format is structured by a sub-property of 3 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter',
    )
    documentation: Optional[AnyUrl] = Field(
        None, description='Technical Documentation (Installation / maintenance / used)'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    installationCondition: Optional[List[InstallationConditionEnum]] = Field(
        None,
        description="Condition and possibility of use in the following environments. Enum:'extremeHeat, extremeCold, extremeHumidity, extremeClimate, desert, sand, marine, saline, dust, seismic, other'",
    )
    installationMode: Optional[InstallationMode] = Field(
        None,
        description="Positioning of the device in relation to a ground reference system. A unique value. Enum:'aerial, ground, pole, roofing, underGround, wall, other'",
    )
    inverterStatus: Optional[List[InverterStatu]] = Field(
        None, description='Status of the inverter. A combination of values'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mPPTPVVoltageDC: Optional[MPPTPVVoltageDC] = Field(
        None,
        description='Minimum and Maximum Photo-voltaic voltage range, MPPT allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    manufacturerName: Optional[str] = Field(
        None, description='Manufacturer Name of the item'
    )
    maxInputCurrentParallelAssembly: Optional[float] = Field(
        None,
        description='Max. Current Input with an Parallel Assembly. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    maxOutputPowerAC: Optional[float] = Field(
        None,
        description='Maximum Power or Apparent Power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **D46** represents Volt Ampere',
    )
    modelName: Optional[str] = Field(None, description='Model name of the item')
    moduleYieldRate: Optional[ModuleYieldRate] = Field(
        None,
        description='Yield Rate of the Device. The format is structured by a sub-property of 2 items (European Standard - Manufacturer Standard). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nbInputParallelDC: Optional[str] = Field(
        None, description='Maximum Number of inputs (in parallel)'
    )
    nbMPPTrackersDC: Optional[float] = Field(None, description='Number of MPP trackers')
    noiseLevel: Optional[float] = Field(
        None,
        description='Sound Power level of the Device. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **2N** represents Decibel',
    )
    nominalAmpereAC: Optional[float] = Field(
        None,
        description='Nominal Amperage *(Code I)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    nominalAmpereDC: Optional[float] = Field(
        None,
        description='Nominal Amperage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    nominalFrequencyAC: Optional[float] = Field(
        None,
        description='Nominal Frequency. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz',
    )
    nominalFrequencyDC: Optional[float] = Field(
        None,
        description=' Nominal Frequency. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz',
    )
    nominalPowerAC: Optional[float] = Field(
        None,
        description='Nominal Power . The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **WTT** represents Watt',
    )
    nominalPowerDC: Optional[float] = Field(
        None,
        description='Nominal Power or Maximum Power factor for cos phi=1. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **WTT** represents Watt',
    )
    nominalVoltageAC: Optional[float] = Field(
        None,
        description='Nominal battery voltage *(Code U)*. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    nominalVoltageDC: Optional[float] = Field(
        None,
        description='Nominal voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    operatingAirHumidity: Optional[OperatingAirHumidity] = Field(
        None,
        description='Ambient operating Air Humidity range. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **P1** represents Percent',
    )
    operatingAmpereAC: Optional[OperatingAmpereAC] = Field(
        None,
        description='Minimum and Maximum Ampere allowed.. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    operatingAmpereDC: Optional[OperatingAmpereDC] = Field(
        None,
        description='Minimum and Maximum Ampere allowed.. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **AMP** represents Ampere',
    )
    operatingFrequencyAC: Optional[OperatingFrequencyAC] = Field(
        None,
        description='Minimum and Maximum Frequency allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz',
    )
    operatingFrequencyDC: Optional[OperatingFrequencyDC] = Field(
        None,
        description='Minimum and Maximum Frequency allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **HTZ** represents Hertz',
    )
    operatingTemperature: Optional[OperatingTemperature] = Field(
        None,
        description='Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius',
    )
    operatingVoltageAC: Optional[OperatingVoltageAC] = Field(
        None,
        description='Minimum and Maximum voltage allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    operatingVoltageDC: Optional[OperatingVoltageDC] = Field(
        None,
        description='Minimum and Maximum voltage allowed. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt.',
    )
    overVoltageCategory: Optional[OverVoltageCategory] = Field(
        None,
        description='Over voltage category. - I : connection to circuits with transient over voltages at an appropriate low level. - II : main insulation and additional insulation (earth terminal). - III : fixed installations with reliability and availability making subject to specific specifications. - IV : materials at the origin of the electrical installation such as electric meters and main materials over current protection',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    phaseType: Optional[PhaseType] = Field(
        None, description="Type of Phase. A unique value. Enum:'singlePhase,threePhase'"
    )
    possibilityOfUse: Optional[PossibilityOfUse] = Field(
        None, description="Possibility of use. Enum:'mixed, mobile, stationary, other'"
    )
    powerFactorAC: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Power factor for cos phi'
    )
    protectionClassSLK: Optional[ProtectionClassSLK] = Field(
        None,
        description='Protection class (SKL). - 0 : main insulation without earth connection. - 1 : main insulation and additional insulation (earth terminal). - 2 : double or reinforced insulation (equivalent to twice the main insulation) without accessible metal part. - 3 : operating in very low safety voltage (SELV) (50V maximum)',
    )
    protectionIK: Optional[float] = Field(
        None,
        description="IK '*Mecanic Protection*' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)",
    )
    protectionIP: Optional[str] = Field(
        None,
        description="IP '*Ingress Protection*' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). - First digit: Solid particle protection (Single numeral: 0–6 or 'X'). - Second digit: Liquid ingress protection (Single numeral: 0–9 or 'X' ).- Third digit: Personal Protection  against access to dangerous parts (optional additional letter).- Fourth digit: Other protections (optional additional letter)",
    )
    refDevice: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link',
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the observation',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    self_consumption: Optional[float] = Field(
        None,
        alias='self-consumption',
        description='Self-consumption during nigth. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes).  For instance, **WTT** represents Watt',
    )
    serialNumber: Optional[str] = Field(None, description='Serial numbers of the item')
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startingVoltageDC: Optional[float] = Field(
        None,
        description='Starting voltage. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    supplyPhaseNb: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of power supply phases'
    )
    topology: Optional[str] = Field(
        None, description='Description of the topology of the installation'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be InverterDevice'
    )
    typeOfUse: Optional[TypeOfUse] = Field(
        None,
        description="Accepted use regarding its positioning in an indoor / outdoor environment.. Enum:'indoor, outdoor, mixed, other'",
    )
    weight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Weight. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilogram',
    )
