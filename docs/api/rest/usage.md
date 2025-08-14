## Service: usage

- **base path**: `/usage/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: usageController

- **module**: `source/bqserver/bq/usage/controllers/usage.py`
- **base path**: `/usage/`

#### `analysis()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/usage/analysis'
```

#### `analysis_monthly()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/usage/analysis_monthly'
```

#### `index()`

Add your first page here..

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/usage'
```

#### `stats()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/usage/stats'
```

#### `uploads()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/usage/uploads'
```

#### `uploads_monthly()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/usage/uploads_monthly'
```

