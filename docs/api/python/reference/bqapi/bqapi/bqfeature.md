## Module `source/bqapi/bqapi/bqfeature.py`

### Classes

#### `FeatureError`

Feature Communication Exception

#### `Feature`

Methods:
- `fetch(session, name, resource_list, path)`
- `fetch_vector(session, name, resource_list)`
- `length(session, name)`

#### `ParallelFeature`

Methods:
- `request_thread_pool(request_queue, errorcb, thread_count)`
- `set_thread_num(n)`
- `set_chunk_size(n)`
- `calculate_request_plan(l)`
- `chunk(l, chunk_size)`
- `fetch(session, name, resource_list, path)`
- `errorcb(e)`
- `fetch_vector(session, name, resource_list)`
