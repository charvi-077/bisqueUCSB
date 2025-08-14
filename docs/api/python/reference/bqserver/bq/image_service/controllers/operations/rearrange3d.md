## Module `source/bqserver/bq/image_service/controllers/operations/rearrange3d.py`

Rearranges dimensions of an image
       arg = xzy|yzx
       xz: XYZ -> XZY
       yz: XYZ -> YZX
       ex: rearrange3d=xz

### Classes

#### `Rearrange3DOperation`

Rearranges dimensions of an image
arg = xzy|yzx
xz: XYZ -> XZY
yz: XYZ -> YZX
ex: rearrange3d=xz

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
