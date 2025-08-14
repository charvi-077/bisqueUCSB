## Module `source/bqfeature/bq/features/controllers/extractors/VRL/extractor.py`

EHD library

### Classes

#### `EHD`

Initalizes table and calculates the Edge Histogram descriptor to be
placed into the HDF5 table

scale = 6
rotation = 4

Methods:
- `calculate(resource)`

#### `HTD`

Initalizes table and calculates the HTD descriptor to be
placed into the HDF5 table

scale = 6
rotation = 4

Methods:
- `cached_columns()`
- `workdir_columns()`
- `calculate(resource)`
