## Module `source/bqserver/bq/image_service/controllers/converters/converter_ffmpeg.py`

FFMPEG command line converter

### Functions

#### `compute_new_size(imw, imh, w, h, keep_aspect_ratio, no_upsample)`

### Classes

#### `ConverterFfmpeg`

Methods:
- `get_version()`
- `get_formats()`
- `get_installed()`
- `supported(token, **kw)`
- `convert(token, ofnm, fmt, extra, **kw)`
- `thumbnail(token, ofnm, width, height, **kw)`
- `slice(token, ofnm, z, t, roi, **kw)`
- `tile(token, ofnm, level, x, y, sz, **kw)`
- `info(token, **kw)`
- `meta(token, **kw)`
