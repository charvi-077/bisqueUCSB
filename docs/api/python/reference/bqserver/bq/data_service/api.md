## Module `source/bqserver/bq/data_service/api.py`

SYNOPSIS
========


DESCRIPTION
===========

  Interface to an data server for other bisquik components.
  Abstract access to local, remote and multiple actual datas servers

### Functions

#### `find_server(server)`

#### `uri()`

#### `new_image(server, **kw)`

Find the preferred data server and store the data there
Excess named arguments are used as attributes for the image object

#### `append_resource(resource, tree, server, **kw)`

Append (an) element(s) to an existing resource

#### `new_resource(resource, server, **kw)`

Create a new resource

#### `resource_load(uniq, server, **kw)`

Create a new resource

#### `get_resource(resource, server, **kw)`

Create a new resource

#### `del_resource(resource, server, **kw)`

Create a new resource

#### `auth_resource(resource, server, **kw)`

Create a new resource

#### `update_resource(resource, server, new_resource, replace, **kw)`

Create a new resource

#### `resource_uniq(server, **kw)`

Create a new resource

#### `load(resource_url, **kw)`

Return XML resource document

#### `query(resource_type, server, **kw)`

Return query results as list of XML documents

#### `count(resource_type, server, **kw)`

Return query results as list of XML documents

#### `retrieve(resource_type, token, server, **kw)`

#### `update(resource_tree, server, replace_all, **kw)`

Update an existing resource with the given tree

#### `resource_controller(token, server, **kw)`

#### `cache_invalidate(url, user_id, server)`

#### `default(*path, **kw)`
