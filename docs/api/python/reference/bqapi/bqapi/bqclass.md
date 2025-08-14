## Module `source/bqapi/bqapi/bqclass.py`

BQ API - a set of classes that represent Bisque objects

### Functions

#### `create_element(dbo, parent, baseuri, **kw)`

Create an etree element from BQ object

#### `toxmlnode(dbo, parent, baseuri, view)`

#### `make_owner(dbo, fn, baseuri)`

#### `make_uri(dbo, fn, baseuri)`

#### `get_email(dbo, fn, baseuri)`

#### `model_fields(dbo, baseuri)`

Extract known fields from a BQ object, while removing any known
from C{excluded_fields}

@rtype: dict
@return fields to be rendered in XML

### Classes

#### `BQNode`

Base class for parsing Bisque XML

Methods:
- `initialize()`
- `initializeXml(xmlnode)`
- `set_parent(parent)`
- `toTuple()`

#### `BQValue`

tag value

Methods:
- `set_parent(parent)`
- `initializeXml(xmlnode)`
- `toetree(parent, baseuri)`

#### `BQResource`

Base class for Bisque resources

Methods:
- `toDict()`
- `set_parent(parent)`
- `addTag(name, value, type, tag)`
- `addGObject(name, value, type, gob)`
- `findall(name, limit)`
- `find(name, limit)`
- `get_value()`
- `set_value(values)`
- `toetree(parent, baseuri)`

#### `BQImage`

Methods:
- `meta()`
- `info()`
- `geometry()`
- `pixels()`

#### `BQImagePixels`

manage requests to the image pixels

Methods:
- `fetch(path, stream)`
- `command(operation, arguments)`
- `slice(x, y, z, t)`
- `format(fmt)`
- `resize(w, h, interpolation)`
- `localpath()`
- `meta()`
- `info()`
- `asarray()`
- `savearray(fname, imdata, imshape, dtype, **kwargs)`

#### `BQTag`

tag resource

Methods:
- `set_parent(parent)`

#### `BQVertex`

gobject vertex

Methods:
- `set_parent(parent)`
- `toTuple()`
- `fromTuple(v)`
- `fromObj(**kw)`

#### `BQGObject`

Gobject resource: A grpahical annotation

Methods:
- `set_parent(parent)`
- `verticesAsTuples()`
- `perimeter()`
- `area()`

#### `BQPoint`

point gobject resource

#### `BQLabel`

label gobject resource

#### `BQPolyline`

polyline gobject resource

Methods:
- `perimeter()`

#### `BQPolygon`

Polygon gobject resource

Methods:
- `perimeter()`
- `area()`

#### `BQCircle`

circle gobject resource

Methods:
- `perimeter()`
- `area()`

#### `BQEllipse`

ellipse gobject resource

Methods:
- `perimeter()`
- `area()`

#### `BQRectangle`

rectangle gobject resource

Methods:
- `perimeter()`
- `area()`

#### `BQSquare`

square gobject resource

#### `BQDataset`

#### `BQUser`

#### `BQMex`

#### `BQFactory`

Factory for Bisque resources

Methods:
- `make(xmltag, type_attr)`
- `index(xmltag, parent, indx)`
- `from_etree(xmlResource, resource, parent)`
- `from_string(xmlstring)`
- `to_etree(dbo, parent, baseuri, view)`
- `to_string(node)`
- `string2etree(xmlstring)`
