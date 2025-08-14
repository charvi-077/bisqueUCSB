## Module `source/bqapi/bqapi/comm.py`

SYNOPSIS
========

DESCRIPTION
===========

### Classes

#### `MexAuth`

Bisque's Mex Authentication

#### `BQServer`

A reference to Bisque server
Allow communucation with a bisque server

A wrapper over requests.Session

Methods:
- `authenticate_mex(token, user)`
- `authenticate_basic(user, pwd)`
- `prepare_headers(user_headers)`
- `prepare_url(url, **params)`
- `webreq(method, url, headers, path, **params)`
- `fetch(url, headers, path)`
- `push(url, content, files, headers, path, method, boundary, timeout)`

#### `BQSession`

Top level Bisque communication object

Methods:
- `init(bisque_url, credentials, moduleuri, create_mex)`
- `init_local(user, pwd, moduleuri, bisque_root, create_mex)`
- `init_mex(mex_url, token, user, bisque_root)`
- `init_cas(user, pwd, moduleuri, bisque_root, create_mex)`
- `init_session(user, pwd, moduleuri, bisque_root, create_mex)`
- `close()`
- `parameter(name)`
- `get_value_safe(v, t)`
- `parameter_value(name, p)`
- `parameters()`
- `get_mex_inputs()`
- `get_mex_execute_options()`
- `fetchxml(url, path, **params)`
- `postxml(url, xml, path, method, **params)`
- `deletexml(url)`
- `fetchblob(url, path, **params)`
- `postblob(filename, xml, path, method, **params)`
- `service_url(service_type, path, query)`
- `service(service_name)`
- `element(ty, **attrib)`
- `append(mex, tags, gobjects, children)`
- `update_mex(status, tags, gobjects, children, reload, merge)`
- `finish_mex(status, tags, gobjects, children, msg)`
- `fail_mex(msg)`
- `run_modules(module_list, pre_run, post_run, callback_fct)`
- `query(resource_type, **kw)`
- `load(url, **params)`
- `delete(bqo, url, **kw)`
- `save(bqo, url, **kw)`
- `saveblob(bqo, filename)`
