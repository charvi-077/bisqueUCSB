## Module `source/bqfeature/bq/features/controllers/TablesInterface.py`

Handles tables for the feature server

### Classes

#### `TablesLock`

Provides locks for hdf5 files

Methods:
- `debug(msg)`
- `acquire()`
- `release()`

#### `QueryPlan`

Generates a queue of querys to be requested on
the tables at once.

Methods:
- `push(hash)`
- `keys()`

#### `Rows`

Generates rows to be placed into the tables

Methods:
- `keys()`

#### `CachedRows`

Generates rows from the feature cache

Methods:
- `construct_row(feature, feature_resource)`
- `push(request_resource)`

#### `WorkDirRows`

Generates rows to be placed into the uncached tables

Methods:
- `construct_row(feature, feature_resource, row)`
- `construct_error_row(feature, error)`
- `push(request_resource)`

#### `Tables`

Methods:
- `set_path(path)`
- `write_to_table(filename, func)`
- `read_from_table(filename, func)`
- `append_to_table(filename, func)`
- `create_h5_file(filename, func)`

#### `CachedTables`

Creates tables in the cache

Methods:
- `store(rows)`
- `get(query_queue)`
- `find(query_queue)`
- `delete()`

#### `WorkDirTable`

Places a table into the workdir without index

Methods:
- `set_path(path)`
- `find(query_plan)`
- `store(row_genorator)`
- `get()`
- `remove(resource)`
- `delete()`
