## Module `source/bqserver/bq/image_service/controllers/process_token.py`

Token passed between image service operations

### Classes

#### `ProcessToken`

Keep data with correct content type and cache info

Methods:
- `init(resource_id, ifnm, fmt, series, imagemeta, files, timeout, dims, resource_name, initial_workpath, dryrun)`
- `setData(data_buf, content_type)`
- `setHtml(text)`
- `setXml(xml_str)`
- `setXmlFile(fname)`
- `setFormat(fmt)`
- `setImage(fname, fmt, series, meta, dims, input, hist, queue, **kw)`
- `setFile(fname, series)`
- `setNone()`
- `setHtmlErrorUnauthorized()`
- `setHtmlErrorNotFound()`
- `setHtmlErrorNotSupported()`
- `isValid()`
- `isImage()`
- `isFile()`
- `isText()`
- `isHtml()`
- `isXml()`
- `isHttpError()`
- `hasFileName()`
- `testFile()`
- `getDim(key, def_val)`
- `hasQueue()`
- `drainQueue()`
- `getQueue()`
- `is_multifile_series()`
- `first_input_file()`
- `get_speed_file()`
