## Service: admin_service

- **base path**: `/admin_service/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: AdminController

- **module**: `source/bqserver/bq/admin_service/controllers/service.py`
- **base path**: `/admin_service/`

#### `cache()`

Deletes system cache

            DELETE cache

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/admin_service/cache'
```

#### `group()`

GET /admin/group: returns list of all groups <resource> <group name="a" /> <group ... /> </resource>

            POST /admin/group: creates new group,
                  <group name="new_group" /> or <resource> <group ..> <group ../> </resource>
                  shortcut:  POST /group/new_group with no body
            PUT /admin/group  : same as POST

            DELETE /admin/group/group_name : delete the group

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/admin_service/group'
```

#### `loggers()`

Set logging level dynamically
        post /admin/loggers

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/admin_service/loggers'
```

#### `logs()`

get /admin/logs/config or /admin/logs - log config, this will return a local or a remote url
        get /admin/logs/read - read local log lines, by default 1000 last lines
        get /admin/logs/read/172444095 - read local log lines starting from a given time stamp

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/admin_service/logs'
```

#### `manager()`

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/admin_service/manager'
```

#### `message_variables()`

Sends message to all system users

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/admin_service/message_variables'
```

#### `notify_users()`

Sends message to all system users

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/admin_service/notify_users'
```

#### `user()`

Main user expose

            Merges the shadow user with the normal user for admins easy access to the password
            columns

            GET user: returns list of all users in xml info see get_all_users for format

            GET user/uniq: returns user in xml info see get_user for format

            GET user/uniq/login: logins in the admin as the user resource provided

            POST user: creates new user, see post_user for format

            PUT user/uniq: update info on user see put_user for format

            DELETE user/uniq: deletes user, see delete user for format

            DELETE user/uniq/image
                Deletes only the users image data and not the user itself

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/admin_service/user'
```

