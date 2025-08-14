## Service: data_service

- **base path**: `/data_service/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: DataServerController

- **module**: `source/bqserver/bq/data_service/controllers/data_service.py`
- **base path**: `/data_service/`

#### `index()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/data_service'
```

