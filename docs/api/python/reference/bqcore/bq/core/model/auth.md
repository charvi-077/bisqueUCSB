## Module `source/bqcore/bq/core/model/auth.py`

Auth* related model.

This is where the models used by :mod:`repoze.who` and :mod:`repoze.what` are
defined.

It's perfectly fine to re-use this definition in the bqcore application,
though.

### Functions

#### `set_sqlite_pragma(dbapi_connection, connection_record)`

#### `do_connect(dbapi_connection, connection_record)`

#### `do_begin(conn)`

### Classes

#### `HashPassword`

Methods:
- `create_password(password)`
- `check_password(passval, password)`

#### `FreeTextPassword`

Methods:
- `create_password(password)`
- `check_password(passval, password)`

#### `Group`

Group definition for :mod:`repoze.what`.

Only the ``group_name`` column is required by :mod:`repoze.what`.

#### `User`

User definition.

This is the user definition used by :mod:`repoze.who`, which requires at
least the ``user_name`` column.

Methods:
- `permissions()`
- `by_email_address(email)`
- `by_user_name(username)`
- `validate_password(password)`
- `on_create()`
- `on_update()`

#### `Permission`

Permission definition for :mod:`repoze.what`.

Only the ``permission_name`` column is required by :mod:`repoze.what`.
