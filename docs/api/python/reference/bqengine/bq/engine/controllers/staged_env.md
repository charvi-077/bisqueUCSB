## Module `source/bqengine/bq/engine/controllers/staged_env.py`

### Classes

#### `StagedEnvironment`

A staged environment creates a temporary staging area
for a module run.  This is usefull for launcher that need
local files or simply shouldn't be run in source area

Methods:
- `process_config(runner)`
- `setup_environment(runner, **kw)`
- `teardown_environment(runner, **lw)`
