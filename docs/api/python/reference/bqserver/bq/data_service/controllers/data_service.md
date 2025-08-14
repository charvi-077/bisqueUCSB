## Module `source/bqserver/bq/data_service/controllers/data_service.py`

SYNOPSIS
========


DESCRIPTION
===========

  Data server for local database

### Functions

#### `initialize(uri)`

Initialize the top level server for this microapp

#### `get_static_dirs()`

Return the static directories for this server

#### `get_model()`

### Classes

#### `DataServerController`

Methods:
- `get_child_resource(token, **kw)`
- `index(**kw)`
- `cache_check(url, user_id, **kw)`
- `cache_save(url, user_id, response, **kw)`
- `cache_invalidate(url, user_id)`
- `cache_invalidate_resource(resource, user_id)`
- `flushchanges(*args)`
- `resource_uniq(**kw)`
- `resource_load(uniq, ident, action, view)`
- `append_resource(resource, tree, flush, **kw)`
- `new_resource(resource, parent, flush, **kw)`
- `get_resource(resource, **kw)`
- `del_resource(resource, **kw)`
- `update_resource(resource, new_resource, replace, flush, **kw)`
- `update(resource_tree, replace_all, flush, **kw)`
- `auth_resource(resource, auth, notify, invalidate, flush, action, **kw)`
- `query(resource_tag, parent, cache, **kw)`
- `load(resource_url, astree, **kw)`
- `count(resource_tag, **kw)`
- `retrieve(resource_tag, tag_query, **kw)`
