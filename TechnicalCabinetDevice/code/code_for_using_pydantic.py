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
    commercial = 'commercial'
    distributionService = 'distributionService'
    industrial = 'industrial'
    other = 'other'
    publicWorks = 'publicWorks'
    road = 'road'
    tertiary = 'tertiary'
    urbanService = 'urbanService'


class DesignMaterial(Enum):
    ABS_Plastic = 'ABS-Plastic'
    aluminum = 'aluminum'
    fiberGlass = 'fiberGlass'
    galvanizedSteel = 'galvanizedSteel'
    other = 'other'
    polyester = 'polyester'
    stainlessSteel = 'stainlessSteel'


class Dimension(BaseModel):
    depth: Optional[confloat(ge=0.0)] = Field(None, description='')
    height: Optional[confloat(ge=0.0)] = None
    width: Optional[confloat(ge=0.0)] = Field(None, description='')


class DoorClosingModeEnum(Enum):
    fixedHandle = 'fixedHandle'
    other = 'other'
    revolvingHandle = 'revolvingHandle'
    triangleHandle = 'triangleHandle'


class DoorType(Enum):
    mixed = 'mixed'
    other = 'other'
    solid = 'solid'
    transparent = 'transparent'


class ExteriorCoatingEnum(Enum):
    fiberGlass = 'fiberGlass'
    other = 'other'
    plastic = 'plastic'
    polyester = 'polyester'
    polyesterResin = 'polyesterResin'
    steel = 'steel'


class ExteriorFinishEnum(Enum):
    graffiti = 'graffiti'
    other = 'other'
    raised = 'raised'
    roughcast = 'roughcast'
    smooth = 'smooth'
    textured = 'textured'


class InstallationConditionEnum(Enum):
    desert = 'desert'
    dust = 'dust'
    extremeCold = 'extremeCold'
    extremeClimate = 'extremeClimate'
    extremeHeat = 'extremeHeat'
    extremeHumidity = 'extremeHumidity'
    marine = 'marine'
    none = 'none'
    other = 'other'
    saline = 'saline'
    seismic = 'seismic'
    sand = 'sand'


class InstallationMode(Enum):
    aerial = 'aerial'
    ground = 'ground'
    other = 'other'
    pole = 'pole'
    roofing = 'roofing'
    underground = 'underground'
    wall = 'wall'


class InteriorCoatingEnum(Enum):
    fiberGlass = 'fiberGlass'
    heatInsulating = 'heatInsulating'
    other = 'other'
    plastic = 'plastic'
    polyester = 'polyester'
    polyesterResin = 'polyesterResin'
    steel = 'steel'


class InternalDimension(BaseModel):
    depth: Optional[confloat(ge=0.0)] = None
    height: Optional[confloat(ge=0.0)] = None
    width: Optional[confloat(ge=0.0)] = None


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


class OperatingTemperature(BaseModel):
    max: Optional[confloat(ge=0.0)] = None
    min: Optional[confloat(ge=-80.0)] = None


class PossibilityOfUse(Enum):
    mixed = 'mixed'
    mobile = 'mobile'
    other = 'other'
    stationary = 'stationary'


class ProtectionOther(Enum):
    abrasion = 'abrasion'
    basement = 'basement'
    dampProof = 'dampProof'
    display = 'display'
    doorTearing = 'doorTearing'
    dust = 'dust'
    forcedOpening = 'forcedOpening'
    graffiti = 'graffiti'
    insect = 'insect'
    other = 'other'
    roofOverload = 'roofOverload'
    saltSpray = 'saltSpray'
    shielding = 'shielding'
    solar = 'solar'
    vandalism = 'vandalism'
    water = 'water'


class Type6(Enum):
    TechnicalCabinetDevice = 'TechnicalCabinetDevice'


class TypeOfUse(Enum):
    indoor = 'indoor'
    mixed = 'mixed'
    outdoor = 'outdoor'
    other = 'other'


class VentilationModeEnum(Enum):
    airConditioners = 'airConditioners'
    dehumidifier = 'dehumidifier'
    none = 'none'
    other = 'other'
    selfVentilatedGills = 'selfVentilatedGills'


class TechnicalCabinetDevice(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    application: Optional[List[ApplicationEnum]] = Field(
        None,
        description="Target application of the Device regarding the environment. A combination of these values. Enum:'commercial, distributionService, industrial, other, publicWorks, road, tertiary, urbanService'",
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    brandName: Optional[str] = Field(None, description='Name of the brand')
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
        description='A timestamp which denotes the last time when the device successfully reported data. Date and time in an ISO8601 UTCformat',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    designMaterials: Optional[List[DesignMaterial]] = Field(
        None,
        description="Design materials to build the cabinet. A combination of  these values. Enum:'ABS-Plastic, aluminum, fiberGlass, galvanizedSteel, other, polyester, stainlessSteel'",
    )
    dimension: Optional[Dimension] = Field(
        None,
        description='The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter',
    )
    documentation: Optional[AnyUrl] = Field(
        None, description="A link to device's documentation"
    )
    doorClosingMode: Optional[List[DoorClosingModeEnum]] = Field(
        None,
        description="Door closing mode. A unique value of these values. Enum:'fixedHandle, other, revolvingHandle, triangleHandle'",
    )
    doorCount: Optional[float] = Field(
        None, description='Count of doors of the technical Cabinet'
    )
    doorOpeningAngle: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Door opening angle expressed in decimal degrees with a range from 0 to 180 degree. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **DD** represents Decimal Degrees',
    )
    doorType: Optional[DoorType] = Field(
        None,
        description="Type of door of the technical Cabinet. A unique value of these values. Enum:'mixed, other, solid, transparent'",
    )
    exteriorCoating: Optional[List[ExteriorCoatingEnum]] = Field(
        None,
        description="Interior Coating. A combination of these values. Enum:'fiberGlass, other, plastic, polyester, polyesterResin, steel",
    )
    exteriorFinish: Optional[List[ExteriorFinishEnum]] = Field(
        None,
        description="Exterior finish. A combination of these values. Enum:'graffiti, other, raised, roughcast, smooth, textured'",
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
        description="Condition and possibility of use in the following environments. A combination of these values. Enum:'desert, dust, extremeCold, extremeClimate, extremeHeat, extremeHumidity, marine, none, other, saline, seismic, sand'",
    )
    installationMode: Optional[InstallationMode] = Field(
        None,
        description="Positioning of the device in relation to a ground reference system. Enum:'aerial, ground, other, pole, roofing, underground, wall'",
    )
    interiorCoating: Optional[List[InteriorCoatingEnum]] = Field(
        None,
        description="Interior Coating. A combination of these values. Enum:'fiberGlass, heatInsulating, other, plastic, polyester, polyesterResin, steel'",
    )
    internalDimension: Optional[InternalDimension] = Field(
        None,
        description='Internal dimension corresponding to the place to work inside the technical cabinet. The format is structured by a sub-property of 3 items. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CMT** represents Centimeter',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    manufacturerName: Optional[str] = Field(
        None, description='Name of the manufacturer'
    )
    maximumSystemVoltage: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum system voltage permitted for the **module**. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **VLT** represents Volt',
    )
    modelName: Optional[str] = Field(
        None, description='Name of the model as given by the manufacturer'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operatingTemperature: Optional[OperatingTemperature] = Field(
        None,
        description='Ambient operating temperature range. This is the minimum and maximum resistance to cold and heat. The format is structured by a sub-property of 2 items. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **CEL** represents Degree Celsius',
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
    possibilityOfUse: Optional[PossibilityOfUse] = Field(
        None,
        description="Possibility of use. A unique value. Enum:'mixed, mobile, other, stationary'",
    )
    protectionIK: Optional[float] = Field(
        None,
        description="IK '*Mecanic Protection*' level relating to numeric classification for the degrees of protection provided by enclosures for electrical equipment against external mechanical impacts, according to International Electro technical Commission standard (EN 62-262). - IK varies from 0 (minimum resistance) to 10 (maximum resistance) which represents an Impact Energy (Unit Joule)",
    )
    protectionIP: Optional[str] = Field(
        None,
        description="IP 'Ingress Protection' for the Junction Box. This is the level classifies and rates the degree of protection provided by mechanical casings and electrical enclosures against intrusion, dust, accidental contact, and water according to International Electrotechnical Commission standard (EN 60-529). First digit: Solid particle protection (Single numeral: 06 or 'X'). Second digit: Liquid ingress protection (Single numeral: 09 or 'X' ).Third digit: Personal Protection against access to dangerous parts (optional additional letter). Fourth digit: Other protections (optional additional letter)",
    )
    protectionOthers: Optional[List[ProtectionOther]] = Field(
        None,
        description="Others protection of the technical cabinet. A combination of these values. Enum:'abrasion, basement, dampProof, display, doorTearing, dust, forcedOpening, graffiti, insect, other, roofOverload, saltSpray, shielding, solar, vandalism, water'",
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
        None, description='The device used to obtain the data expressed by this record'
    )
    refDeviceList: Optional[
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
        description='A list of reference to the [Devices](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) which are inside the technical Cabinet Device',
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
    serialNumber: Optional[str] = Field(
        None, description='Serial number of the container'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be TechnicalCabinetDevice'
    )
    typeOfUse: Optional[TypeOfUse] = Field(
        None,
        description="Accepted use regarding its positioning in an indoor / outdoor environment. A unique value of these values. Enum:'indoor, mixed, outdoor, other'",
    )
    ventilationMode: Optional[List[VentilationModeEnum]] = Field(
        None,
        description="Ventilation mode. A combination of these values. Enum:'airConditioners, dehumidifier, none, other, selfVentilatedGills'",
    )
    weight: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Weight of the item. The unit code (text) of measurement  is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **KGM** represents Kilograms',
    )
