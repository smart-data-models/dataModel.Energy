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
        None, description='Line 1 of the active energy export'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the active energy export'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the active energy export'
    )


class ActiveEnergyImport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 1 of the active energy import'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the active energy import'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the active energy import'
    )


class ActivePower(BaseModel):
    L1: Optional[float] = Field(None, description='Line 1 of the active power')
    L2: Optional[float] = Field(None, description='Line 2 of the active power')
    L3: Optional[float] = Field(None, description='Line 3 of the active power')


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
        None, description='Line 1 of the apparent energy export'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the apparent energy export'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the apparent energy export'
    )


class ApparentEnergyImport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 1 of the apparent energy import'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the apparent energy import'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the apparent energy import'
    )


class ApparentPower(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 1 of the apparent power'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the apparent power'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the apparent power'
    )


class Current(BaseModel):
    L1: Optional[float] = Field(None, description='Line 1 of the current')
    L2: Optional[float] = Field(None, description='Line 2 of the current')
    L3: Optional[float] = Field(None, description='Line 3 of the current')
    N: Optional[float] = Field(None, description='Neutral of the current')


class DisplacementPowerFactor(BaseModel):
    L1: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Line 1 of the displacement power factor'
    )
    L2: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Line 2 of the displacement power factor'
    )
    L3: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Line 3 of the displacement power factor'
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
        None, description='Phase between line 1 and 2 of the phase voltage'
    )
    L23: Optional[confloat(ge=0.0)] = Field(
        None, description='Phase between line 2 and 3 of the phase voltage'
    )
    L31: Optional[confloat(ge=0.0)] = Field(
        None, description='Phase between line 3 and 1 of the phase voltage'
    )


class PhaseVoltage(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 1 of the phase voltage'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the phase voltage'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the phase voltage'
    )


class PowerFactor(BaseModel):
    L1: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Line 1 of the power factor'
    )
    L2: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Line 2 of the power factor'
    )
    L3: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Line 3 of the power factor'
    )


class ReactiveEnergyExport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 1 of the reactive energy export'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the reactive energy export'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the reactive energy export'
    )


class ReactiveEnergyImport(BaseModel):
    L1: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 1 of the reactive energy import'
    )
    L2: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 2 of the reactive energy import'
    )
    L3: Optional[confloat(ge=0.0)] = Field(
        None, description='Line 3 of the reactive energy import'
    )


class ReactivePower(BaseModel):
    L1: Optional[float] = Field(None, description='Line 1 of the reactive power')
    L2: Optional[float] = Field(None, description='Line 2 of the reactive power')
    L3: Optional[float] = Field(None, description='Line 3 of the reactive power')


class ThdCurrent(BaseModel):
    L1: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Line 1 of the total harmonic distortion current'
    )
    L2: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Line 2 of the total harmonic distortion current'
    )
    L3: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Line 3 of the total harmonic distortion current'
    )


class ThdVoltage(BaseModel):
    L1: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Line 1 of the total harmonic distortion voltage'
    )
    L2: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Line 2 of the total harmonic distortion voltage'
    )
    L3: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Line 3 of the total harmonic distortion voltage'
    )


class Type6(Enum):
    ThreePhaseAcMeasurement = 'ThreePhaseAcMeasurement'


class ThreePhaseAcMeasurement(BaseModel):
    activeEnergyExport: Optional[ActiveEnergyExport] = Field(
        None,
        description='Active energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    activeEnergyImport: Optional[ActiveEnergyImport] = Field(
        None,
        description='Active energy imported i.e. consumed per Line since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    activePower: Optional[ActivePower] = Field(
        None,
        description='The actual values will beconveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3. ',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    apparentEnergyExport: Optional[ApparentEnergyExport] = Field(
        None,
        description='Apparent energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    apparentEnergyImport: Optional[ApparentEnergyImport] = Field(
        None,
        description='Apparent energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    apparentPower: Optional[ApparentPower] = Field(
        None,
        description='Apparent power consumed per phase. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    current: Optional[Current] = Field(
        None,
        description='Electrical current. The actual values will be conveyed by one subproperty per alternating current phase and the neutral wire: L1, L2, L3 and N',
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
        None, description='The starting date for metering energy'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    displacementPowerFactor: Optional[DisplacementPowerFactor] = Field(
        None,
        description='Displacement power factor for each phase. The quantity is based on the fundamental frequency of the system. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    frequency: Optional[confloat(ge=0.0)] = Field(
        None, description='The frequency of the circuit'
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
        description='Voltage between phases. A value for each phase pair: phases 1 and 2 (L12), phases 2 and 3 (L32), phases 3 and 1 (L31)',
    )
    phaseVoltage: Optional[PhaseVoltage] = Field(
        None,
        description='The voltage between each phase and neutral conductor. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    powerFactor: Optional[PowerFactor] = Field(
        None,
        description='Power factor for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    reactiveEnergyExport: Optional[ReactiveEnergyExport] = Field(
        None,
        description='Fundamental frequency reactive energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    reactiveEnergyImport: Optional[ReactiveEnergyImport] = Field(
        None,
        description='Fundamental frequency reactive energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    reactivePower: Optional[ReactivePower] = Field(
        None,
        description='Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3',
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
    ] = Field(None, description='Device(s) used to obtain the measurement')
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
    ] = Field(None, description='Device(s) for which the measurement was taken')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    thdCurrent: Optional[ThdCurrent] = Field(
        None,
        description='Total harmonic distortion of electrical current. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    thdVoltage: Optional[ThdVoltage] = Field(
        None,
        description='Total harmonic distortion of voltage for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    totalActiveEnergyExport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy exported since metering started (since `dateEnergyMeteringStarted`)',
    )
    totalActiveEnergyImport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed since metering started (since `dateEnergyMeteringStarted`)',
    )
    totalActivePower: Optional[float] = Field(
        None, description='Active power consumed (counting all phases)'
    )
    totalApparentEnergyExport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy exported (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)',
    )
    totalApparentEnergyImport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)',
    )
    totalApparentPower: Optional[confloat(ge=0.0)] = Field(
        None, description='Apparent power consumed (counting all phases)'
    )
    totalDisplacementPowerFactor: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None,
        description='Displacement power factor including all phases. The quantity is based on the fundamental frequency of the system',
    )
    totalPowerFactor: Optional[confloat(ge=-1.0, le=1.0)] = Field(
        None, description='Power factor including all phases'
    )
    totalReactiveEnergyExport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total fundamental frequency reactive energy exported since metering started (since `dateEnergyMeteringStarted`)',
    )
    totalReactiveEnergyImport: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Total energy imported i.e. consumed (with regards to fundamental frequency reactive power) since the metering start date (`dateEnergyMeteringStarted`)',
    )
    totalReactivePower: Optional[float] = Field(
        None, description='Reactive power consumed (counting all phases)'
    )
    type: Optional[Type6] = Field(
        None, description='It must be equal to `ThreePhaseAcMeasurement`'
    )
