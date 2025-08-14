## Module `source/bqserver/bq/client_service/controllers/auth_service.py`

SYNOPSIS
========

DESCRIPTION
===========
  Authorization for web requests

### Functions

#### `initialize(url)`

### Classes

#### `AuthenticationServer`

Methods:
- `login_map()`
- `login_providers()`
- `login_check(came_from, login, **kw)`
- `login(came_from, username, **kw)`
- `openid_login_handler(**kw)`
- `post_login(came_from, **kw)`
- `post_logout(came_from, **kw)`
- `credentials(**kw)`
- `session()`
- `newmex(module_url)`
- `setbasicauth(username, passwd, **kw)`
- `login_app()`
- `logout_app()`
