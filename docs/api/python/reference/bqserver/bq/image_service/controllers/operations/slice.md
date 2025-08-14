## Module `source/bqserver/bq/image_service/controllers/operations/slice.py`

Provide a slice of an image :
       arg = x1-x2,y1-y2,z|z1-z2,t|t1-t2
       Each position may be specified as a range
       empty params imply entire available range
       all values are in ranges [1..N]
       0 or empty - means first element
       ex: slice=,,1,

### Functions

#### `pop_dimension_range(dims, dim)`

#### `get_dimension_string(dims, dim)`

### Classes

#### `SliceOperation`

Provide a slice of an image :
arg = x1-x2,y1-y2,z|z1-z2,t|t1-t2
Each position may be specified as a range
empty params imply entire available range
all values are in ranges [1..N]
0 or empty - means first element
ex: slice=,,1,

extended way supporting more dimensions:
arg = z:(v|v1-v2),t:(v|v1-v2),fov:(v|v1-v2),serie:(v|v1-v2),rotation:(v|v1-v2),...
Each dimension may be specified as a range, dimension order does not matter, empty dimensions imply entire available range
all values are in ranges [0..N-1] !!!!
ex: slice=fov:345,z:0

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
