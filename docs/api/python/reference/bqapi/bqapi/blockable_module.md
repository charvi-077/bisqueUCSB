## Module `source/bqapi/bqapi/blockable_module.py`

### Classes

#### `BlockableModule`

Base class for module that can run over blocks of parameters

Methods:
- `main(mex_url, auth_token, bq, **kw)`
- `start_block(bq, all_kw)`
- `end_block(bq)`
- `process_single(bq, **kw)`
