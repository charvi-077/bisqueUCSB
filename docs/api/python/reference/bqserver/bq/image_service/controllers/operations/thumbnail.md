## Module `source/bqserver/bq/image_service/controllers/operations/thumbnail.py`

Create and provide thumbnails for images:
The default values are: 128,128,BL,,jpeg
arg = [w,h][,method][,preproc][,format]
w - thumbnail width, width and hight are defined as maximum boundary
h - thumbnail height, width and hight are defined as maximum boundary
method - ''|NN|BL|BC - default, Nearest neighbor, Bilinear, Bicubic respectively
preproc - ''|MID|MIP|NIP - empty (auto), middle slice, maximum intensity projection, minimum intensity projection
format - output image format, default is JPEG
ex: ?thumbnail
ex: ?thumbnail=200,200,BC,,png
ex: ?thumbnail=200,200,BC,mid,png

### Functions

#### `compute_new_size(imw, imh, w, h, keep_aspect_ratio, no_upsample)`

### Classes

#### `ThumbnailOperation`

Create and provide thumbnails for images:
The default values are: 128,128,BL,,jpeg
arg = [w,h][,method][,preproc][,format]
w - thumbnail width, width and hight are defined as maximum boundary
h - thumbnail height, width and hight are defined as maximum boundary
method - ''|NN|BL|BC - default, Nearest neighbor, Bilinear, Bicubic respectively
preproc - ''|MID|MIP|NIP - empty (auto), middle slice, maximum intensity projection, minimum intensity projection
format - output image format, default is JPEG
ex: ?thumbnail
ex: ?thumbnail=200,200,BC,,png
ex: ?thumbnail=200,200,BC,mid,png

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
