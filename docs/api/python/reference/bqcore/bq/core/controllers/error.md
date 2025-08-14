## Module `source/bqcore/bq/core/controllers/error.py`

Error controller

### Classes

#### `ErrorController`

Generates error documents as and when they are required.

The ErrorDocuments middleware forwards to ErrorController when error
related status codes are returned from the application.

This behaviour can be altered by changing the parameters to the
ErrorDocuments middleware in your config/middleware.py file.

Methods:
- `document(*args, **kwargs)`
