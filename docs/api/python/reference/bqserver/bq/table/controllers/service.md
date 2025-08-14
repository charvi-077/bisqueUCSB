## Module `source/bqserver/bq/table/controllers/service.py`

Table server : access to tabular data, e.g. files CSV, HDF5, or other services...

DESCRIPTION
===========

URL:

/table/ID[/PATH1/PATH2/...][/RANGE][/COMMAND:PARS]

PATH:
    Path components must be URL encoded to be valid URL path elements:
    For example for an HDF table stored in:
        '/arrays/Vdata table: PerBlockMetadataCommon'
    The URL should be:
        /arrays/Vdata%20table%3A%20PerBlockMetadataCommon
    The full info call would look like:
        /table/XXXXX/arrays/Vdata%20table%3A%20PerBlockMetadataCommon/info/format:json

RANGE:
    defines region of interest within an N-D matrix, only valid if the path points to a matrix element
    range specifies a comma separated list of ranges for N-D data
    dimension order is column wise: i,j,k,... column, row, ....
    elements start at 0
    empty element means full range
    i - each range item can be a simple integer defining one element in that dimension,
    i:j - colon separated elements define range               [i...j[
    i:-j - minus sign defines element positions from the end  [i...length-j[
    i:  - elements from i to end                              [i...length-1]
    :j  - elements from beginning to j                        [0...j[


    Note:
      In current v5.X implementation TurboGears URL parsing is breaking on parsing the ":" sign
      which is currently augmented with ";" separator. Both characters are currently legal.

    ex:
    /table/00-XXXXX/mynode123/mytable123/12:15  - defines raws 12 through 15
    /table/00-XXXXX/mynode123/mytable123/12:15,2:3  - defines cells in raws 12 through 15 and cols 2 thtough 3


COMMAND:
    info - returns elemnets within a path, column headers, sizes and datatypes
           info call on an HDF5 root will list all available nodes
           info call on a CSV file will list column headers, column sizes and datatypes
           info call on an Excel root will list all available sheets
    format - xml,json,csv - format:json


RESTful API
=============

    GET - reads elements in the requested range returning in the requested format
          specified either by HTTP Content negotiation (Accept header) - Accept: text/csv
          or a format command - format:csv
    PUT - replaces elements in the requested range from data posted in one of supported formats
          defined by the HTTP Content-Type header - Content-Type: application/json
    POST - same as PUT
    DELETE - removes elements if possible

Responses:
    400 Bad Request
    401 Unauthorized
    500 Internal Server Error
    501 Not Implemented


Examples:

For HDF5 input
-----------------

/table/00-XXXXX/mynode123/mytable123/info/format:json
/table/00-XXXXX/mynode123/mytable123/12:16/format:json


For CSV input
----------------

/table/00-XXXXX/info/format:json
/table/00-XXXXX/12:16/format:xml



ARCHITECTURE
==============

  url_string
      |
[input driver] - consumes URL path while possible, reads data and returns the rest of uninterpreted URL path plus numpy matrix with data
      |
numpy_array, sub_url_string
      |
[operations] - operates on data matrix and removes its own operations from path
      |
numpy_array, sub_url_string
      |
[output driver] - converts numpy matrix into output format and streams out
      |
    stream

### Functions

#### `get_arg(table, name, defval, **kw)`

#### `is_arg(table, name)`

#### `parse_subrange(rng)`

#### `initialize(uri)`

Initialize the top level server for this microapp

### Classes

#### `TableController`

Methods:
- `index(**kw)`
- `check_access(uniq)`
- `get_table(path, **kw)`
