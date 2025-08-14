## Module `source/bqserver/bq/blob_service/controllers/blobsrv.py`

SYNOPSIS
========
blob_service


DESCRIPTION
===========
Micro webservice to store and retrieve blobs(untyped binary storage) on a variety
of storage platforms: local, irods, s3

### Functions

#### `transfer_msg(flocal, transfer_t)`

return a human string for transfer time and size

#### `initialize(uri)`

Initialize the top level server for this microapp

### Classes

#### `TransferTimer`

#### `PathService`

Manipulate paths in the database

Service to be used by filesystem agents to move references to files

Methods:
- `index()`
- `list(path, *args, **kwargs)`
- `insert(path, user, **kwargs)`
- `move(path, destination, user, **kw)`
- `remove(path, delete_blob, user, **kwargs)`

#### `BlobServer`

Manage a set of blob files

Methods:
- `guess_type(filename)`
- `guess_mime(filename)`
- `get_import_plugins()`
- `check_access(ident, action)`
- `get_all()`
- `get_one(ident, **kw)`
- `post(**transfers)`
- `delete(ident, **kwargs)`
- `create_resource(resource)`
- `store_blob(resource, fileobj, rooturl)`
- `localpath(uniq_ident, resource, blocking)`
- `delete_blob(uniq_ident)`
- `originalFileName(ident)`
- `move_resource_store(srcstore, dststore)`
- `geturi(ident)`
