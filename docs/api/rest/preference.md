## Service: preference

- **base path**: `/preference/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: PreferenceController

- **module**: `source/bqserver/bq/preference/controllers/service.py`
- **base path**: `/preference/`

#### `reset()`

replaces the system preferences with the default document

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/preference/reset'
```

#### `user()`

The entry point for the user and resource level preferences

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/preference/user'
```

