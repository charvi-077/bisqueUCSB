## Module `source/bqengine/bq/engine/controllers/condor_templates.py`

### Functions

#### `load_engines(wanted, defaults)`

Load and initialize all templating engines.

This is called during startup after the configuration has been loaded.
You can call this earlier if you need the engines before startup;
the engines will then be reloaded with the custom configuration later.

### Classes

#### `CondorTemplates`

Condor script construction helper

Used to construct condor execution scripts based
on internal or user defined templates.

you can define the condor submit script using
[condor]
condor.template_engine="mako" # cheetah, genshi..
condot.dag_config_template=dag_config_filepath
condot.dag_template=dag_config_filepath
condot.submit_template=submit_filepath
# any template engine initialization variables go here
# i.e.
# mako.directories = .

Any variables contained in [condor_submit] will
be added automatically to the condor_submitfile i.e.
[condor_submit]
requirements = (Memory>2048)
request_cpus =2
request_memory = 2048

Methods:
- `mk_path(name, mapping)`
- `create_file(output_path, template, mapping)`
- `construct_launcher(mapping)`
- `prepare_submit(mapping)`
