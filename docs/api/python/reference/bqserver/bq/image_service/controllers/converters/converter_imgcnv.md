## Module `source/bqserver/bq/image_service/controllers/converters/converter_imgcnv.py`

BioImageConvert command line converter

### Functions

#### `readAndSet(el, attr, d, key, defval, f)`

#### `dicom_init_encoding(dataset)`

#### `safedecode(s, encoding)`

#### `dicom_parse_date(v)`

#### `dicom_parse_time(v)`

### Classes

#### `ConverterImgcnv`

Methods:
- `get_version()`
- `get_formats()`
- `supported(token, **kw)`
- `run_command(command)`
- `run_read(ifnm, command)`
- `run(ifnm, ofnm, args, **kw)`
- `meta(token, **kw)`
- `info(token, **kw)`
- `write_files(files, ofnm)`
- `convert(token, ofnm, fmt, extra, **kw)`
- `thumbnail(token, ofnm, width, height, **kw)`
- `slice(token, ofnm, z, t, roi, **kw)`
- `tile(token, ofnm, level, x, y, sz, **kw)`
- `writeHistogram(token, ofnm, **kw)`
- `group_files_dicom(files, **kw)`
- `meta_dicom(ifnm, series, xml, **kw)`
- `meta_dicom_parsed(ifnm, xml, **kw)`
