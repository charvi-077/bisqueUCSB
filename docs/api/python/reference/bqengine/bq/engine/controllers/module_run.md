## Module `source/bqengine/bq/engine/controllers/module_run.py`

### Classes

#### `ModuleRunner`

Top Level runner and entry point for the Runners and Environments

The module runner is responsible for reading the module-runtime.cfg
and choosing the proper runner based on system and module
preferences.
i.e.
  runtime-module.cfg:
    runner = condor, command

  site.cfg:
    engine_runner = command

Methods:
- `choose_runner(**kw)`
- `check(**kw)`
- `main(**kw)`
