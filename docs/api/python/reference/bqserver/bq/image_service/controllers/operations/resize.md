## Module `source/bqserver/bq/image_service/controllers/operations/resize.py`

Provide images in requested dimensions
       arg = w,h,method[,AR|,MX]
       w - new width
       h - new height
       method - NN or BL, or BC (Nearest neighbor, Bilinear, Bicubic respectively)
       if either w or h is ommited or 0, it will be computed using aspect ratio of the image
       if ,AR is present then the size will be used as bounding box and aspect ration preserved
       if ,MX is present then the size will be used as maximum bounding box and aspect ratio preserved
       with MX: if image is smaller it will not be resized!
       #size_arg = '-resize 128,128,BC,AR'
       ex: resize=100,100

### Functions

#### `compute_new_size(imw, imh, w, h, keep_aspect_ratio, no_upsample)`

### Classes

#### `ResizeOperation`

Provide images in requested dimensions
arg = w,h,method[,AR|,MX]
w - new width
h - new height
method - NN or BL, or BC (Nearest neighbor, Bilinear, Bicubic respectively)
if either w or h is ommited or 0, it will be computed using aspect ratio of the image
if ,AR is present then the size will be used as bounding box and aspect ration preserved
if ,MX is present then the size will be used as maximum bounding box and aspect ratio preserved
with MX: if image is smaller it will not be resized!
#size_arg = '-resize 128,128,BC,AR'
ex: resize=100,100

Methods:
- `action(token, arg)`

#### `Resize3DOperation`

Provide images in requested dimensions
arg = w,h,d,method[,AR|,MX]
w - new width
h - new height
d - new depth
method - NN or TL, or TC (Nearest neighbor, Trilinear, Tricubic respectively)
if either w or h or d are ommited or 0, missing value will be computed using aspect ratio of the image
if ,AR is present then the size will be used as bounding box and aspect ration preserved
if ,MX is present then the size will be used as maximum bounding box and aspect ratio preserved
with MX: if image is smaller it will not be resized!
ex: resize3d=100,100,100,TC

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
