## Module `source/bqserver/bq/export_service/controllers/archiver/archiver_factory.py`

### Classes

#### `AbstractArchiver`

Methods:
- `getContentType()`
- `getFileExtension()`
- `beginFile(file)`
- `readBlock(block_size)`
- `EOF()`
- `endFile()`
- `readEnding()`
- `close()`
- `destinationPath(file)`

#### `ArchiverFactory`

Methods:
- `getClass(compressionType)`
