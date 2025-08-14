## Module `source/bqengine/bq/engine/controllers/condor_run.py`

### Classes

#### `CondorRunner`

A Runtime to execute a module on a condor enabled system

Methods:
- `read_config(**kw)`
- `process_config(**kw)`
- `setup_environments(**kw)`
- `command_start(**kw)`
- `command_execute(**kw)`
- `command_finish(**kw)`
- `command_failed(process, retcode)`
- `command_kill(**kw)`
- `command_status(**kw)`

#### `CondorMatlabRunner`

Methods:
- `process_config(**kw)`
