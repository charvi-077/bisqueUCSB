## Module `source/bqserver/bq/image_service/controllers/operations/transform.py`

Provide an image transform
       arg = transform
       Available transforms are: fourier, chebyshev, wavelet, radon, edge, wndchrmcolor, rgb2hsv, hsv2rgb, superpixels
       ex: transform=fourier
       superpixels requires two parameters: superpixel size in pixels and shape regularity 0-1, ex: transform=superpixels,32,0.5

### Classes

#### `TransformOperation`

Provide an image transform
arg = transform
Available transforms are: fourier, chebyshev, wavelet, radon, edge, wndchrmcolor, rgb2hsv, hsv2rgb, superpixels
ex: transform=fourier
superpixels requires two parameters: superpixel size in pixels and shape regularity 0-1, ex: transform=superpixels,32,0.5

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
