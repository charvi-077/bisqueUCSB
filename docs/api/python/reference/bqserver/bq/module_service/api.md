## Module `source/bqserver/bq/module_service/api.py`

SYNOPSIS
========


DESCRIPTION
===========
  module service

### Functions

#### `find_server(server)`

#### `uri()`

#### `register_engine(body, server)`

request registration of the engine to the module server
given the module URI and the ElementTree Module descriptor

#### `begin_internal_mex(**kw)`

Begin an internal mex for tracking changes from users

#### `end_internal_mex(mexid)`

#### `begin_execute(mex_request, server)`

#### `end_execute(mex_request, server)`

#### `heartbeat(hbdoc, server)`

#### `engines(server)`
