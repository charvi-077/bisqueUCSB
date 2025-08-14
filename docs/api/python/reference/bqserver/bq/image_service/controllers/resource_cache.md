## Module `source/bqserver/bq/image_service/controllers/resource_cache.py`

ResourceCache used to cache resources to speed up retrieval of images without constantly
asking data service for meta-data view of a resource. It is required to have a fast etag
lookup on a data service in order to validate the cache state.

### Classes

#### `ResourceDescriptor`

cached and parsed descriptor of a system resource

Methods:
- `validate()`
- `get_resource()`
- `get_metadata()`
- `get_blobs(blocking)`

#### `ResourceCache`

Provide resource and blob caching

Methods:
- `get_descriptor(ident)`
- `get_resource(ident)`
- `get_meta(ident)`
- `get_blobs(ident, blocking)`
