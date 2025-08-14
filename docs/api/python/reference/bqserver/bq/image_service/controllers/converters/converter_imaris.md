## Module `source/bqserver/bq/image_service/controllers/converters/converter_imaris.py`

Imaris command line converter

### Functions

#### `parse_format(l)`

#### `safeRead(config, section, option, defval)`

#### `safeReadAndSet(config, section, option, d, key, defval)`

#### `safe_config_read(config, sp)`

#### `imaris_to_rgb(color)`

### Classes

#### `ConverterImaris`

Methods:
- `get_version()`
- `get_formats()`
- `supported(token, **kw)`
- `meta(token, **kw)`
- `info(token, **kw)`
- `extension(token, ofnm, **kw)`
- `convert(token, ofnm, fmt, extra, **kw)`
- `convertToOmeTiff(token, ofnm, extra, **kw)`
- `thumbnail(token, ofnm, width, height, **kw)`
- `slice(token, ofnm, z, t, roi, **kw)`
