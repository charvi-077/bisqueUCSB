## Module `source/bqserver/bq/stats/controllers/bqapi.py`

BQ API - a set of classes that represent Bisque objects

### Classes

#### `BQNode`

Base class for parsing Bisque XML

Methods:
- `getAttr(a)`
- `fromEtree(element)`
- `toEtree(parent)`
- `toTuple()`

#### `BQResource`

Base class for Bisque resources

#### `BQValue`

tag value

Methods:
- `fromEtree(element)`
- `toEtree(element)`
- `toString()`

#### `BQTag`

tag resource

Methods:
- `fromEtree(element)`
- `toEtree(parent)`

#### `BQVertex`

gobject vertex

Methods:
- `fromEtree(element)`
- `toTuple()`
- `fromTuple(v)`
- `toString()`

#### `BQGObject`

tag resource

Methods:
- `fromEtree(element)`
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

#### `BQLine`

line gobject resource

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

#### `BQFactory`

Factory for Bisque resources

Methods:
- `make(element)`
