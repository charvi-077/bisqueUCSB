## Module `source/bqserver/bq/usage/controllers/usage.py`

Main server for usage}

### Functions

#### `initialize(uri)`

Initialize the top level server for this microapp

#### `get_static_dirs()`

Return the static directories for this server

### Classes

#### `usageController`

Methods:
- `index(**kw)`
- `stats(**kw)`
- `get_counts(resource_type, num_days)`
- `get_counts_month(resource_type, num_months)`
- `uploads(**kw)`
- `uploads_monthly(**kw)`
- `analysis(**kw)`
- `analysis_monthly(**kw)`
