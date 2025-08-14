## Module `source/bqserver/bq/image_service/controllers/converters/converter_openslide.py`

Openslide python deep-zoom based driver

This converter will not support the full API for now since it would be really inefficient
trying to create ome-tiff out of pyramidal tiled images, instead it will only provide
tile and thumbnail access, this will work perfectly for the UI and module access
if tiles are used, better integration will be looked at later if need arises

### Classes

#### `ConverterOpenSlide`

Methods:
- `get_version()`
- `get_formats()`
- `supported(token, **kw)`
- `info(token, **kw)`
- `meta(token, **kw)`
- `convert(token, ofnm, fmt, extra, **kw)`
- `convertToOmeTiff(token, ofnm, extra, **kw)`
- `thumbnail(token, ofnm, width, height, **kw)`
- `slice(token, ofnm, z, t, roi, **kw)`
- `tile(token, ofnm, level, x, y, sz, **kw)`
- `writeHistogram(token, ofnm, **kw)`
