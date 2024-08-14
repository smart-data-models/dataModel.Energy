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


class ActiveEnergyExport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the active Energy Export'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the active Energy Export'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the active Energy Export'
    )


class ActiveEnergyImport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the active Energy Import'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the active Energy Import'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the active Energy Import'
    )


class ActivePower(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the active power'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the active power'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the active power'
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


class ApparentEnergyExport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the apparent Energy Export'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the apparent Energy Export'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the apparent Energy Export'
    )


class ApparentEnergyImport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the apparent Energy Import'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the apparent Energy Import'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the apparent Energy Import'
    )


class ApparentPower(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the apparent power'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the apparent power'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the apparent power'
    )


class Current(BaseModel):
    L1: Optional[float] = Field(None, description='Value for phase 1 of the current')
    L2: Optional[float] = Field(None, description='Value for phase 2 of the current')
    L3: Optional[float] = Field(None, description='Value for phase 3 of the current')
    N: Optional[float] = Field(
        None, description='Value for phase neutral of the current'
    )


class DisplacementPowerFactor(BaseModel):
    L1: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Value for phase 1 of the displacement Power Factor'
    )
    L2: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Value for phase 2 of the displacement Power Factor'
    )
    L3: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Value for phase 3 of the displacement Power Factor'
    )


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


class PhaseToPhaseVoltage(BaseModel):
    L12: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 to phase 2 voltage'
    )
    L23: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 to phase 3 voltage'
    )
    L31: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 to phase 1 voltage'
    )


class PhaseType(Enum):
    singlePhase = 'singlePhase'
    threePhase = 'threePhase'


class PhaseVoltage(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the voltage'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the voltage'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the voltage'
    )


class PowerFactor(BaseModel):
    L1: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Value for phase 1 of the power factor'
    )
    L2: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Value for phase 2 of the power factor'
    )
    L3: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Value for phase 3 of the power factor'
    )


class ReactiveEnergyExport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the reactive Energy Export'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the reactive Energy Export'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the reactive Energy Export'
    )


class ReactiveEnergyImport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 1 of the reactive Energy Import'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 2 of the reactive Energy Import'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Value for phase 3 of the reactive Energy Import'
    )


class ReactivePower(BaseModel):
    L1: Optional[float] = Field(
        None, description='Value for phase 1 of the reactive power'
    )
    L2: Optional[float] = Field(
        None, description='Value for phase 2 of the reactive power'
    )
    L3: Optional[float] = Field(
        None, description='Value for phase 3 of the reactive power'
    )


class ThdCurrent(BaseModel):
    L1: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Value for phase 1 of the thd current'
    )
    L2: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Value for phase 2 of the thd current'
    )
    L3: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Value for phase 3 of the thd current'
    )


class ThdVoltage(BaseModel):
    L1: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Value for phase 1 of the thd voltage'
    )
    L2: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Value for phase 2 of the thd voltage'
    )
    L3: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Value for phase 3 of the thd voltage'
    )


class Type6(Enum):
    ACMeasurement = 'ACMeasurement'


class ACMeasurement(BaseModel):
    activeEnergyExport: Optional[ActiveEnergyExport] = Field(
        None,
        description='Active energy exported per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    activeEnergyImport: Optional[ActiveEnergyImport] = Field(
        None,
        description='Active energy imported i.e. consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    activePower: Optional[ActivePower] = Field(
        None,
        description='Active power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    apparentEnergyExport: Optional[ApparentEnergyExport] = Field(
        None,
        description='Apparent energy exported per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    apparentEnergyImport: Optional[ApparentEnergyImport] = Field(
        None,
        description='Apparent energy imported i.e. consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    apparentPower: Optional[ApparentPower] = Field(
        None,
        description='Apparent power consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    current: Optional[Current] = Field(
        None,
        description='Electrical current. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateEnergyMeteringStarted: Optional[AwareDatetime] = Field(
        None,
        description='The starting date for metering energy in an ISO8601 UTC format',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateObserved: Optional[AwareDatetime] = Field(
        None,
        description='Date and time of this observation represented by an ISO8601 UTC format. It can be represented by an specific time instant or by an ISO8601 interval to separate attributes `dateObservedFrom`,`dateObservedTo`',
    )
    dateObservedFrom: Optional[AwareDatetime] = Field(
        None,
        description='Observation period: Start date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted',
    )
    dateObservedTo: Optional[AwareDatetime] = Field(
        None,
        description='Observation period: End date and time in an ISO8601 UTC format. The attribute can be used in addition to the `dateObserved` attribute when it corresponds to a time interval to be highlighted',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    displacementPowerFactor: Optional[DisplacementPowerFactor] = Field(
        None,
        description='Displacement power factor for each phase. The quantity is based on the fundamental frequency of the system',
    )
    frequency: Optional[confloat(ge=0.0)] = Field(
        None,
        description='The frequency of the circuit. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
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
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    phaseToPhaseVoltage: Optional[PhaseToPhaseVoltage] = Field(
        None,
        description='Voltage between phases. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    phaseType: Optional[PhaseType] = Field(
        None,
        description="Type of Phase. A unique value. Enum:'singlePhase, threePhase'",
    )
    phaseVoltage: Optional[PhaseVoltage] = Field(
        None,
        description='The voltage between each phase and neutral conductor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    powerFactor: Optional[PowerFactor] = Field(
        None, description='Power factor for each phase'
    )
    reactiveEnergyExport: Optional[ReactiveEnergyExport] = Field(
        None,
        description='Fundamental frequency reactive energy exported per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    reactiveEnergyImport: Optional[ReactiveEnergyImport] = Field(
        None,
        description='Fundamental frequency reactive energy imported i.e. consumed per phase. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    reactivePower: Optional[ReactivePower] = Field(
        None,
        description='Fundamental frequency reactive power. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    refDevice: Optional[
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
        None, description='Reference to the devices which captured this observation'
    )
    refTargetDevice: Optional[
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
        description='Reference to a list of the devices for which the measurement was taken',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    thdCurrent: Optional[ThdCurrent] = Field(
        None, description='Total harmonic distortion of current for each phase'
    )
    thdVoltage: Optional[ThdVoltage] = Field(
        None, description='Total harmonic distortion of voltage for each phase'
    )
    totalActiveEnergyExport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed . The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalActiveEnergyImport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalActivePower: Optional[float] = Field(
        None,
        description='Total Active Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalApparentEnergyExport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy exported (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalApparentEnergyImport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed (with regards to apparent power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalApparentPower: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total Apparent Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalDisplacementPowerFactor: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None,
        description='Sum of Displacement power factor including all phases. The quantity is based on the fundamental frequency of the system',
    )
    totalPowerFactor: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Sum of Power factor including all phases'
    )
    totalReactiveEnergyExport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total fundamental frequency reactive energy exported. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalReactiveEnergyImport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed (with regards to fundamental frequency reactive power). The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    totalReactivePower: Optional[float] = Field(
        None,
        description='Total Reactive Power consumed. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI property type. It has to be ACMeasurement'
    )
