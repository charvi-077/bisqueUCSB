## Service: ingest

- **base path**: `/ingest/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: ingestController

- **module**: `source/bqserver/bq/ingest/controllers/ingest_server.py`
- **base path**: `/ingest/`

#### `get_all()`

Add your first page here..

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/ingest/get_all'
```

#### `post()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X POST -H 'Content-Type: text/xml' -d '<payload>' '<host>/ingest'
```

