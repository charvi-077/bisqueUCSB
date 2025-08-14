## Service: stats

- **base path**: `/stats/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: statsController

- **module**: `source/bqserver/bq/stats/controllers/stats_server.py`
- **base path**: `/stats/`

#### `compute()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/stats/compute'
```

#### `csv()`

- **content_type**: `text/csv`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/csv' '<host>/stats/csv'
```

#### `index()`

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/stats'
```

#### `json()`

- **content_type**: `application/json`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: application/json' '<host>/stats/json'
```

#### `maps()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/stats/maps'
```

#### `reduces()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/stats/reduces'
```

#### `xml()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/stats/xml'
```

