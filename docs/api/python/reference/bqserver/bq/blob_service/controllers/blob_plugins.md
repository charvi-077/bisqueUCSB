## Module `source/bqserver/bq/blob_service/controllers/blob_plugins.py`

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

#### `walk_deep(path, ext)`

Splits sub path that follows # sign if present

### Classes

#### `ResourcePlugin`

Maps vector of objects into a vector of numbers or strings

Methods:
- `is_supported(filename)`
- `guess_type(filename)`
- `guess_mime(filename)`
- `to_xml(filename)`

#### `ResourcePluginManager`

Methods:
- `guess_type(filename)`
- `guess_mime(filename)`
- `get_import_plugins()`
