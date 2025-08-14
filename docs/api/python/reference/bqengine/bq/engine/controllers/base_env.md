## Module `source/bqengine/bq/engine/controllers/base_env.py`

### Functions

#### `strtobool(x)`

#### `strtolist(x, sep)`

### Classes

#### `ModuleEnvironmentError`

For errors while setting up or tearing down environments

#### `ModuleEnvironment`

The default Env (users can derive from this) which
reads the module config

Methods:
- `setup_environment(runner)`
- `teardown_environment(runner)`

#### `BaseEnvironment`

A BaseEnvironment is a helper script for running bisque modules.

An enviroment provide a framework for constructing a runtime
environment for a module that will work several platforms,

Base class for creating module environment which can process MEX
amd MODULE arguments.

Methods:
- `process_config(runner)`
- `strtotype(value, value_type)`
- `parse_mex_inputs(module, mex)`
- `setup_environment(runner)`
- `teardown_environment(runner)`
