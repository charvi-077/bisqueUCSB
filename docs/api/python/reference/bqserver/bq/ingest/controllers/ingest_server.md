## Module `source/bqserver/bq/ingest/controllers/ingest_server.py`

Main server for ingest}

### Functions

#### `image_ingest(blob)`

Ingest a simple image given the blob..

#### `match_best_ingester(root, blob)`

#### `initialize(uri)`

Initialize the top level server for this microapp

#### `get_static_dirs()`

Return the static directories for this server

#### `get_model()`

### Classes

#### `IngestException`

Ingest Exceptions

#### `ingestController`

Methods:
- `get_all(**kw)`
- `post(*path, **kw)`
- `new_blobs(body, **kw)`
