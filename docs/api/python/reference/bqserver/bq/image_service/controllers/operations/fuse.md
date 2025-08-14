## Module `source/bqserver/bq/image_service/controllers/operations/fuse.py`

Provide an RGB image with the requested channel fusion
       arg = W1R,W1G,W1B;W2R,W2G,W2B;W3R,W3G,W3B;W4R,W4G,W4B
       output image will be constructed from channels 1 to n from input image mapped to RGB components with desired weights

       fuse=display: will use preferred mapping found in file's metadata
       fuse=gray: will return gray scale image with visual weighted mapping from RGB or equal weights for other number of channels
       fuse=grey: will return gray scale image with visual weighted mapping from RGB or equal weights for other number of channels

       ex: fuse=255,0,0;0,255,0;0,0,255;255,255,255:A

### Classes

#### `FuseOperation`

Provide an RGB image with the requested channel fusion
arg = W1R,W1G,W1B;W2R,W2G,W2B;W3R,W3G,W3B;W4R,W4G,W4B
output image will be constructed from channels 1 to n from input image mapped to RGB components with desired weights

fuse=display: will use preferred mapping found in file's metadata
fuse=gray: will return gray scale image with visual weighted mapping from RGB or equal weights for other number of channels
fuse=grey: will return gray scale image with visual weighted mapping from RGB or equal weights for other number of channels

ex: fuse=255,0,0;0,255,0;0,0,255;255,255,255:A

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
