## Module `source/bqserver/bq/image_service/controllers/imgsrv.py`

ImageServer for Bisque system.

### Functions

#### `url2operationsOld(url, base)`

#### `url2operationsNew(url, base)`

#### `getOperations(url, base)`

### Classes

#### `ImageServer`

Methods:
- `init_converters()`
- `ensureOriginalFile(ident, resource)`
- `getImageInfo(filename, series, infofile, meta)`
- `process_queue(token)`
- `enqueue(token, op_name, ofnm, fmt, command, dims, **kw)`
- `imageconvert(token, ifnm, ofnm, fmt, extra, dims, **kw)`
- `initialWorkPath(image_id, user_name, series)`
- `ensureWorkPath(path, image_id, user_name, series)`
- `request(method, token, arguments)`
- `process(url, ident, resource, **kw)`
