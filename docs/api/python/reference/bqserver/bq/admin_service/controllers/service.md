## Module `source/bqserver/bq/admin_service/controllers/service.py`

SYNOPSIS
========


DESCRIPTION
===========

### Functions

#### `initialize(url)`

Initialize the top level server for this microapp

### Classes

#### `AdminController`

The admin controller is a central point for
adminstrative tasks such as monitoring, data, user management, etc.

Methods:
- `manager()`
- `notify_users(*arg, **kw)`
- `message_variables(**kw)`
- `add_admin_info2node(user_node, view)`
- `loggers(*arg, **kw)`
- `logs(*arg, **kw)`
- `cache(*arg, **kw)`
- `user(*arg, **kw)`
- `get_all_users(*arg, **kw)`
- `get_user(uniq, **kw)`
- `post_user(doc, **kw)`
- `put_user(uniq, doc, **kw)`
- `delete_user(uniq)`
- `deleteimage(imageid, **kw)`
- `deleteuser(username, **kw)`
- `deleteimages(username, will_redirect, **kw)`
- `loginasuser(uniq)`
- `clearcache()`
- `get_variables()`
- `do_notify_users(userlist, message)`
- `group(*args, **kw)`
- `get_groups(*args, **kw)`
- `delete_group(*args, **kw)`
- `new_group(*args, **kw)`
