## Module `source/bqcore/bq/core/lib/cas_auth.py`

### Functions

#### `make_plugin(cas_base_url, saml_validate, login_path, logout_path, post_logout, remember_name, validate_plugin, registration_url)`

### Classes

#### `CASPlugin`

Methods:
- `challenge(environ, status, app_headers, forget_headers)`
- `remember(environ, identity)`
- `forget(environ, identity)`
- `identify(environ)`
- `authenticate(environ, identity)`
