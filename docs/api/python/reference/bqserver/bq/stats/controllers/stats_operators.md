## Module `source/bqserver/bq/stats/controllers/stats_operators.py`

Statistics operatiors : map a vector of object into a vector of strings or numbers

DESCRIPTION
===========

 2) MAP: [vector of objects -> uniform vector of numbers or strings]
    An operator is applied onto the vector of objects to produce a vector of numbers or strings
    The operator is specified by the user and can take specific elements and produces specific result
    for example: operator "area" could take polygon or rect and produce a number
                 operator "numeric-value" can take a "tag" and return tag's value as a number
                 possible operator functions should be extensible and maintained by the stat service

EXTENSIONS
===========

Operations are added by simply deriving from StatOperator and adding your code here

### Functions

#### `mapflat(f, l)`

#### `gobNumber(gob)`

#### `gobType(gob)`

#### `gobName(gob)`

#### `gobPerimeter(gob)`

#### `gobArea(gob)`

#### `gobVertexStr(gob)`

#### `gobVertexType(gob)`

#### `gobVertexName(gob)`

#### `gobVertexV(gob, f)`

#### `gobVertexX(gob)`

#### `gobVertexY(gob)`

#### `gobVertexZ(gob)`

#### `gobVertexT(gob)`

#### `gobVertexC(gob)`

#### `gobVertexI(gob)`

### Classes

#### `StatOperator`

Maps vector of objects into a vector of numbers or strings

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorResourceUri`

maps resource into a vector of their uri as strings

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorTagName`

maps tags into a vector of their names as strings

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorTagValue`

maps tags into a vector of their values as strings

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorTagType`

maps tags into a vector of their types as strings

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorTagNameNumeric`

maps tags into a vector of their names as numbers

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorTagValueNumeric`

maps tags into a vector of their values as numbers

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobName`

maps GObjects into a vector of their names

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobType`

maps GObjects into a vector of their types

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobTypePrimitive`

returns only present primitive types

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobTypeComposed`

maps GObjects into a vector of their types

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobLength`

maps GObjects into a vector of their perimeters or lengths

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobPerimeter`

maps GObjects into a vector of their perimeters or lengths

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobArea`

maps GObjects into a vector of their areas

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobNumber`

maps GObjects into a vector of their number, each number is object + children

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexString`

maps gobjects into a vector of their vertices as strings: "X, Y, Z, T, C, I"

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexType`

maps gobjects into a vector of their types given for every vertex

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexName`

maps gobjects into a vector of their names given for every vertex

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexX`

maps gobjects into a vector of their vertices''s x coordinate

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexY`

maps gobjects into a vector of their vertices''s y coordinate

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexZ`

maps gobjects into a vector of their vertices''s z coordinate

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexT`

maps gobjects into a vector of their vertices''s t coordinate

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexC`

maps gobjects into a vector of their vertices''s c coordinate

Methods:
- `do_map(v_in, **kw)`

#### `StatOperatorGobVertexI`

maps gobjects into a vector of their vertices''s index

Methods:
- `do_map(v_in, **kw)`
