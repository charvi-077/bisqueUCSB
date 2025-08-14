## Module `source/bqcore/bq/core/identity.py`

### Functions

#### `request_valid()`

#### `anonymous()`

#### `not_anonymous()`

#### `set_admin(admin)`

#### `get_admin()`

#### `get_admin_id()`

#### `is_admin(bquser)`

return whether current user has admin priveledges

#### `get_user_id()`

#### `get_username()`

#### `get_user()`

Get the current user object

#### `get_current_user()`

#### `set_current_user(username)`

set the current user by name
@param username: a string username or a bquser reference

#### `as_user(user)`

Do some action as a particular user and reset the current user

>>> with as_user('admin'):
>>>     action()
>>>     action

@param user:  a username or a bquser instance

#### `add_credentials(headers)`

add the current user credentials for outgoing http requests

This is a place holder for outgoing request made by the server
on behalf of the logged in user.  Will depend on login methods
(password, CAS, openid) and avaialble methods.

#### `set_admin_mode(groups)`

add or remove admin permissions.

on add return previous group permission.
to restome previous setting, call with groups

:param groups: None to set, False to remove, a set of groups to restore
:return a set of previous groups

#### `mex_authorization_token()`

### Classes

#### `BQIdentityException`

#### `BisqueIdentity`

helper class to fetch current user object

Methods:
- `get_username()`
- `set_current_user(user)`
