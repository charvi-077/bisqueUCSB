## Module `source/bqserver/bq/image_service/controllers/operations/depth.py`

Listing of operations

### Classes

#### `DepthOperation`

Provide an image with converted depth per pixel:
arg = depth,method[,format]
depth is in bits per pixel
method is: f or d or t or e
  f - full range
  d - data range
  t - data range with tolerance
  e - equalized
  hounsfield - hounsfield space enhancement
format is: u, s or f, if unset keeps image original
  u - unsigned integer
  s - signed integer
  f - floating point
channel mode is: cs or cc
  cs - channels separate
  cc - channels combined
enhancement granularity: patch,plane,volume,whole
  patch - enhances the image patch using its own histogram
  plane - enhances the image patch using the histogram of the whole image (if available)
  volume - enhances the image patch using the histogram of the whole image (not implemented)
  whole - enhances the image patch using the histogram of the whole image over time (not implemented)
or
window center, window width - only used for hounsfield enhancement
  ex: depth=8,hounsfield,u,,40,80
ex: depth=8,d or depth=8,d,u,cc

Methods:
- `action(token, arg)`
