## Module `source/bqserver/bq/image_service/controllers/operations/remap.py`

Listing of operations

### Classes

#### `RemapOperation`

Provide an image with the requested channel mapping
arg = channel,channel...
output image will be constructed from channels 1 to n from input image, 0 means black channel
remap=display - will use preferred mapping found in file's metadata
remap=gray - will return gray scale image with visual weighted mapping from RGB or equal weights for other number of channels
ex: remap=3,2,1

Methods:
- `action(token, arg)`
