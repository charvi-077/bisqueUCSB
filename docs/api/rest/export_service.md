## Service: export_service

- **base path**: `/export_service/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: export_serviceController

- **module**: `source/bqserver/bq/export_service/controllers/export_service.py`
- **base path**: `/export_service/`

#### `index()`

Add your first page here..

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/export_service'
```

#### `initStream()`

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/export_service/initStream'
```

#### `stream()`

Create and return a streaming archive

        :param compression: tar, zip, gzip, bz2
        :param files: a comma separated list of resource URIs to include in the archive
        :param datasets: a comma separated list of dataset resource URIs to include in the archive
        :param urls: a comma separated list of any url accessible over HTTP to include in the archive

        ------------------------------------
        Sample XML when POSTing to this app
        ------------------------------------

        <resource>
            <value type="FILE">    ...    </value>
            <value type="URL">     ...    </value>
            <value type="DATASET"> ...    </value>
        </resource>

- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/export_service/stream'
```

#### `to_gdocs()`

- **decorators**: `expose(...)`, `require(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/export_service/to_gdocs'
```

#### `to_gdocs_send()`

- **decorators**: `expose(...)`, `require(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET '<host>/export_service/to_gdocs_send'
```

