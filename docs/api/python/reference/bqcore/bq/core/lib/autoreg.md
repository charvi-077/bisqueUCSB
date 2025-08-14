## Module `source/bqcore/bq/core/lib/autoreg.py`

### Classes

#### `AutoRegister`

This plugin attempts to register users that are so far unknown
to the system.  During the metadata phase it looks to see if the user
name is currently known and if  not so will create a local user structure

Methods:
- `login_group(login_identifier)`
- `validate_user(user_name, values)`
- `register_user(user_name, values)`
- `add_metadata(environ, identity)`
