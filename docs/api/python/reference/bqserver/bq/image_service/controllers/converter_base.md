## Module `source/bqserver/bq/image_service/controllers/converter_base.py`

Base class defining command line converter API

### Classes

#### `Format`

Methods:
- `supportToString()`

#### `ConverterBase`

Methods:
- `init()`
- `get_version()`
- `get_installed()`
- `check_version(needed)`
- `ensure_version(needed)`
- `get_formats()`
- `formats()`
- `supported(token, **kw)`
- `meta(token, **kw)`
- `info(token, **kw)`
- `run_command(command)`
- `run_read(ifnm, command)`
- `run(ifnm, ofnm, args, **kw)`
- `convert(token, ofnm, fmt, extra, **kw)`
- `convertToOmeTiff(token, ofnm, extra, **kw)`
- `thumbnail(token, ofnm, width, height, **kw)`
- `slice(token, ofnm, z, t, roi, **kw)`
- `tile(token, ofnm, level, x, y, sz, **kw)`
- `writeHistogram(token, ofnm, **kw)`
