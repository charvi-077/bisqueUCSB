## Module `source/bqserver/bq/data_service/model/tag_model.py`

SYNOPSIS
========

 Main model for bisquik database

DESCRIPTION
===========

 Usage::
   image = Image()
   image.addTag ('name', 'image 1')
   for tg in image.tags:
       print tg.name, tg.value

### Functions

#### `create_tables1(bind)`

#### `parse_uri(uri)`

Parse a bisquik uri into host , dbclass , and ID
@type  uri: string
@param uri: a bisquik uri representation of a resourc
@rtype:  A triplet (host, dbclass, id)
@return: The parse resouece

#### `map_url(uri)`

Load the object specified by the root tree and return a rsource
@type   root: Element
@param  root: The db object root with a uri attribute
@rtype:  tag_model.Taggable
@return: The resource loaded from the database

#### `bquser_callback(tg_user, operation, **kw)`

#### `registration_hook(action, **kw)`

#### `current_mex_id()`

#### `dbtype_from_name(table)`

Return a tuple of table name and the most specific database type

#### `dbtype_from_tag(tag)`

Given a tag,
Return a tuple of table name and the most specific database type

#### `all_resources()`

Return the setof unique names that are taggable objects

### Classes

#### `Taggable`

Base type for taggable objects.  Taggable
objects can have any number of name/value pairs
associated with it.

Methods:
- `resource()`
- `uri()`
- `validate_owner(key, owner)`
- `clear(what)`
- `findtag(nm, create)`
- `loadFull()`
- `get_index()`
- `set_index(v)`
- `get_name()`
- `set_name(v)`
- `get_type()`
- `set_type(v)`
- `get_permission()`
- `set_permission(pmv)`
- `get_hidden()`
- `set_hidden(hdv)`
- `getval()`
- `setval(v)`

#### `Image`

Image object

#### `Tag`

Tag object (name,value) pair.
Tag have for the following properties:

#### `Value`

Methods:
- `geturi()`
- `clear()`
- `getvalue()`
- `setvalue(v)`
- `remvalue()`
- `gettype()`
- `settype(x)`
- `getobjid()`
- `get_index()`
- `set_index(v)`

#### `Vertex`

Methods:
- `geturi()`
- `clear()`
- `get_index()`
- `set_index(v)`

#### `GObject`

#### `BQUser`

User object

Methods:
- `new_user(email, password, create_tg)`
- `user_id()`
- `get_groups()`

#### `Template`

A pre-canned group of tags

#### `Module`

A module is a runnable routine that modifies the database
There are several required tags for every module:
for each input/output a type tag exists:
   (formal_input: [string, float, tablename])
   (formal_output: [tagname, tablename])

#### `ModuleExecution`

A module execution is an actual execution of a module.
Executions must have the folling tags available:
  (actual_input: taggable_id)
  (actual_output: taggable_id)

Methods:
- `closed()`
- `getstatus()`
- `setstatus(v)`

#### `Dataset`

#### `BQStore`

#### `TaggableAcl`

A permission for EDIT or READ on a taggable object

Methods:
- `setaction(perm)`
- `getaction()`

#### `Service`

A executable service
