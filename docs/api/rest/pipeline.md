## Service: pipeline

- **base path**: `/pipeline/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: PipelineController

- **module**: `source/bqserver/bq/pipeline/controllers/service.py`
- **base path**: `/pipeline/`

#### `index()`

Add your service description here

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/pipeline'
```

