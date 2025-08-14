## Module `source/bqserver/bq/blob_service/api.py`

### Functions

#### `find_server()`

#### `store_blob(resource, fileobj, rooturl)`

create and store a resource blob

#### `create_resource(resource)`

create a resource blob

#### `localpath(uniq_ident, resource, blocking)`

return localpath of resource by ident (uniq)

#### `delete_blob(uniq_ident)`

return localpath of resource by ident (uniq)

#### `original_name(ident)`

create  localpath if possible of resource by ident (uniq)

#### `url2local(path)`

decode url into a local path

#### `local2url(path)`

decode local path as a url

#### `get_import_plugins()`

return a listr of plugins with import function
