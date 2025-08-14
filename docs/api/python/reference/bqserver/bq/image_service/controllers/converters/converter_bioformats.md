## Module `source/bqserver/bq/image_service/controllers/converters/converter_bioformats.py`

BioFormats command line converter

### Functions

#### `bfColorToString(v)`

#### `bfReadAndSet(el, attr, d, key, defval, f)`

### Classes

#### `ConverterBioformats`

Methods:
- `get_version()`
- `get_formats()`
- `supported(token, **kw)`
- `meta(token, **kw)`
- `info(token, **kw)`
- `convert(token, ofnm, fmt, extra, **kw)`
- `convertToOmeTiff(token, ofnm, extra, **kw)`
- `thumbnail(token, ofnm, width, height, **kw)`
- `slice(token, ofnm, z, t, roi, **kw)`
