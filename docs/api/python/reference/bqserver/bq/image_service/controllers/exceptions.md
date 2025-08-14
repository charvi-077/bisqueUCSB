## Module `source/bqserver/bq/image_service/controllers/exceptions.py`

Provides typical exceptions thrown by the image service

### Classes

#### `ImageServiceException`

Raised when any operation or decoder fails

Attributes:
    code: Response error code, same as HTTP response code
    message: String explaining the exact reason for the failure

#### `ImageServiceFuture`

Raised when any operation timeout or is already locked

Attributes:
    timeout_range: a range of seconds for a re-request: (1, 15)
