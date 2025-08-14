## Module `source/bqserver/bq/data_service/controllers/resource_auth.py`

SYNOPSIS
========


DESCRIPTION
===========
   RESTful access to DoughDB resources

### Functions

#### `append_share_handler(resource_type, handler)`

Add  share handler

@param resource_type : a string resource type e.g. mex, dataset
@param hander: a callable (resource_uniq, user_uniq, auth, action)

#### `force_dbload(item)`

#### `check_access(query, action)`

#### `resource_acl_query(resource, user_uniq, recurse, filter_resource_type, response)`

Query a set of resource acl

#### `resource_acls(resources, newauth, user, acl, notify, invalidate, action)`

Update the list of resources with a new

#### `resource_acl(resource, newauth, user, acl, notify, invalidate, action)`

Create or modify resource acls

@param resource:  resource (Taggable)
@param newauth :  an etree of the acl record or None if deleting
@param user    :  the user (Taggable) of the acl  or None (will be determined from newauth)
@param acl     :  the acl (TaggableAcl) or None (will be found or created)
@param notify  :  send an email on state change (boolean)
@param invalidate: Invalidate caches (boolean)
@parama delete : Append/modify or Delete record (boolean)

@return an etree acl record

#### `notify_user(action, resource, user, passwd)`

Send Notification to user of sharing event

#### `match_user(user, user_uniq, email)`

Match a user by user url or email creating a new one if needed.

@return: tuple (new user, passwd if created otherwise None)

#### `invited_user(email)`

#### `resource_auth(resource, action, newauth, notify, invalidate)`

DEPRECATED user resource_acl

#### `mex_acl_handler(resource_uniq, user_uniq, newauth, action)`

Special handling for mexes

Share A mexes input and outputs

### Classes

#### `ResourceAuth`

Handle resource authorization records

Listing :
GET /data_service/<uniq>/auth/

Create:
POST /data_service/<uniq>/auth/[?notify=false]
<auth email="ab@com" permission="edit" /> -->
         <auth user="<user uniq>" email="ab@com" permission="edit" />
<auth user=="<user uniq>" permission="edit" /> -->
         <auth user="<user uniq>" email="ab@com" permission="edit" />


POST /data_service/<uniq>/auth/[?notify=false]
<auth email="ab@com" permission="edit" />

Delete:
DELETE /data_service/<uniq>/auth/<user uniq>

Modify::
POST /data_service/<uniq>/auth/<user uniq>[?notify=false]
<auth user="<user uniq> email="ab@com" permission="edit" />

Methods:
- `load(token, **kw)`
- `create(**kw)`
- `dir(resource, **kw)`
- `get(useracl, **kw)`
- `replace_all(resource, xml, notify, **kw)`
- `modify(useracl, xml, notify, **kw)`
- `delete(useracl, **kw)`
- `new(factory, xml, notify, **kw)`
- `append(useracl, xml, notify, **kw)`
