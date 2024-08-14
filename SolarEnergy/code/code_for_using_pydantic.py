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


class ActivePower(BaseModel):
    L1: Optional[float] = None
    L2: Optional[float] = None
    L3: Optional[float] = None


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


class Current(BaseModel):
    L1: Optional[float] = None
    L2: Optional[float] = None
    L3: Optional[float] = None
    N: Optional[float] = None


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


class PhaseCurrent(BaseModel):
    L1: Optional[float] = None
    L2: Optional[float] = None
    L3: Optional[float] = None


class PhaseVoltage(BaseModel):
    L1: Optional[confloat(ge=0.0)] = None
    L2: Optional[confloat(ge=0.0)] = None
    L3: Optional[confloat(ge=0.0)] = None


class PowerFactor(BaseModel):
    L1: Optional[confloat(ge=-1.0, le=1.0)] = None
    L2: Optional[confloat(ge=-1.0, le=1.0)] = None
    L3: Optional[confloat(ge=-1.0, le=1.0)] = None


class ReactivePower(BaseModel):
    L1: Optional[float] = None
    L2: Optional[float] = None
    L3: Optional[float] = None


class Type6(Enum):
    SolarEnergy = 'SolarEnergy'


class SolarEnergy(BaseModel):
    activePower: Optional[ActivePower] = Field(
        None,
        description='The actual values will beconveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3. ',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    current: Optional[Current] = Field(
        None,
        description='Electrical current. The actual values will be conveyed by one subproperty per alternating current phase and the neutral wire: L1, L2, L3 and N',
    )
    dataDescriptor: Optional[str] = Field(
        None, description='URI pointing to the data-descriptor entity'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    energyGenerated: Optional[float] = Field(
        None,
        description='Energy generated over a specific time range from the energy resource corresponding to this observation',
    )
    frequency: Optional[float] = Field(
        None,
        description='Frequency observed from the entity corresponding to this observation',
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
    maxSolarPowerMeasure: Optional[float] = Field(
        None, description='A measure of maximum solar energy that can be generated'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observationDateTime: Optional[AwareDatetime] = Field(
        None, description='Last reported time of observation'
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
    phaseCurrent: Optional[PhaseCurrent] = Field(
        None,
        description='Current per phase. Ordered triple comprising of active power from three phases in the following order: [R Y B]',
    )
    phaseVoltage: Optional[PhaseVoltage] = Field(
        None,
        description='The voltage between each phase and neutral conductor. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    powerFactor: Optional[PowerFactor] = Field(
        None,
        description='Power factor for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3',
    )
    reactivePower: Optional[ReactivePower] = Field(
        None,
        description='Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    totalActivePower: Optional[float] = Field(
        None, description='Total active power consumed by all phases'
    )
    totalEnergyGenerated: Optional[float] = Field(
        None,
        description='Total energy generated by the energy resource corresponding to this observation',
    )
    totalReactivePower: Optional[float] = Field(
        None, description='Total reactive power for all phases'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be SolarEnergy'
    )
    voltage: Optional[float] = Field(
        None,
        description='The value of Voltage in the entity corresponding to this observation',
    )
