## Module `source/bqserver/bq/dataset_service/controllers/dataset_service.py`

### Functions

#### `dataset_share_handler(resource_uniq, user_uniq, auth, action)`

Apply share to all members

resource dataset
auth   xml auth record
acl    acl of dataset

#### `iterate(duri, operation, dataset, members, last, **kw)`

Iterate over a dataset executing an operation on each member

@param  duri: dataset uri
@param operation: an operation name (i.e. module, permisssion)
@param kw : operation parameters by name

#### `initialize(uri)`

Initialize the top level server for this microapp

#### `get_static_dirs()`

Return the static directories for this server

### Classes

#### `DatasetOp`

Methods:
- `action(member, **kw)`

#### `IdemOp`

An idempotent operation

Methods:
- `action(member, **kw)`

#### `PermissionOp`

change permission on member

Methods:
- `action(member, permission)`

#### `DeleteOp`

Delete each member

Methods:
- `action(member, **kw)`

#### `TagEditOp`

Add/Remove/Modify Tags on each member

Methods:
- `action(member, action, tagdoc, **kw)`

#### `ShareOp`

Apply sharing options to  each member

Methods:
- `action(member, auth, action, last, **kw)`

#### `DatasetServer`

Server side actions on datasets

Methods:
- `iterate(duri, operation, dataset, members, last, **kw)`
- `index(**kw)`
- `add_query(duri, resource_tag, tag_query, **kw)`
- `delete(duri, **kw)`
- `permission(duri, **kw)`
- `tagedit(duri, **kw)`
- `share(duri, **kw)`
