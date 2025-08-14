## Module `source/bqserver/bq/image_service/controllers/operations/rotate.py`

Provides rotated versions for requested images:
       arg = angle
       At this moment only supported values are 90, -90, 270, 180 and guess
       ex: rotate=90

### Functions

#### `compute_rotated_size(w, h, arg)`

### Classes

#### `RotateOperation`

Provides rotated versions for requested images:
arg = angle
At this moment only supported values are 90, -90, 270, 180 and guess
ex: rotate=90

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
