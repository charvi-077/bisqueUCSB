## Module `source/bqserver/bq/image_service/controllers/operations/roi.py`

Provides ROI for requested images
       arg = x1,y1,x2,y2
       x1,y1 - top left corner
       x2,y2 - bottom right
       all values are in ranges [1..N]
       0 or empty - means first/last element
       supports multiple ROIs in which case those will be only cached
       ex: roi=10,10,100,100

### Classes

#### `RoiOperation`

Provides ROI for requested images
arg = x1,y1,x2,y2
x1,y1 - top left corner
x2,y2 - bottom right
all values are in ranges [1..N]
0 or empty - means first/last element
supports multiple ROIs in which case those will be only cached
ex: roi=10,10,100,100

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
