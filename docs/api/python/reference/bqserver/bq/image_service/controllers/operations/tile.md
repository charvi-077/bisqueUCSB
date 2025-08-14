## Module `source/bqserver/bq/image_service/controllers/operations/tile.py`

Provides a tile of an image :
       arg = l,tnx,tny,tsz
       or
       arg = s,x1,y1,x2,y2

       # 4 parameter request:
       # gridded tile size interface,
       # it is the fastest possible especially if hitting the native tile size
       l: level of the pyramid, 0=100%, 1=50%, 2=25%, ...
       tnx, tny: x and y tile number on the grid
       tsz: tile size
       All values are in range [0..N]
       ex: tile=0,2,3,512

       # 5 parameter request:
       # arbitrary size and scale that uses tiled-pyramidal files
       # this might get slower with unfavorable tile sizes
       # scale will currently only support available pyramidal power of two levels
       s: scale, 1.0=100%, 0.5=50%, 0.25=25%, ...
       x1, y1: x and y coordinates of the top-left corner, same as ROI interface
       x2, y2: x and y coordinates of the bottom-right corner, same as ROI interface
       All values are in range [0..N]
       ex: tile=1.0,10,10,999,999

### Classes

#### `TileOperation`

Provides a tile of an image :
arg = l,tnx,tny,tsz
l: level of the pyramid, 0 - initial level, 1 - scaled down by a factor of 2
tnx, tny: x and y tile number on the grid
tsz: tile size
All values are in range [0..N]
ex: tile=0,2,3,512

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
