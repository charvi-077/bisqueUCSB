## Module `source/bqapi/bqapi/services.py`

### Functions

#### `id_generator(size, chars)`

#### `test_module()`

### Classes

#### `BaseServiceProxy`

Methods:
- `construct(path, params)`
- `request(path, params, method, render, **kw)`
- `fetch(path, params, render, **kw)`
- `get(path, params, render, **kw)`
- `post(path, params, render, **kw)`
- `put(path, params, render, **kw)`
- `delete(path, params, render, **kw)`

#### `AdminProxy`

Methods:
- `login_as(user_name)`

#### `AuthProxy`

Methods:
- `login_providers(**kw)`
- `credentials(**kw)`
- `get_session(**kw)`

#### `BlobProxy`

Methods:
- `path_link(srcpath, alias, resource_type, tag_file)`
- `path_delete(srcpath, alias)`
- `path_rename(srcpath, dstpath, alias)`
- `path_list(srcpath, alias)`

#### `ImportProxy`

Methods:
- `transfer(filename, fileobj, xml)`

#### `DatasetProxy`

Methods:
- `delete(dataset_uniq, members, **kw)`
- `append_member(dataset_uniq, resource_uniq, **kw)`
- `delete_member(dataset_uniq, resource_uniq, **kw)`

#### `ModuleProxy`

Methods:
- `execute(module_name, **module_parms)`
- `register(engine_url)`
- `unregister(engine_url)`

#### `TableProxy`

Methods:
- `load_array(table_uniq, path, slices)`
- `store_array(array, name)`

#### `ImageProxy`

Methods:
- `get_thumbnail(image_uniq, **kw)`

#### `ExportProxy`

Methods:
- `fetch_export(**kw)`
- `fetch_export_local(localpath, stream, **kw)`

#### `ServiceFactory`

Methods:
- `make(session, service_name)`
