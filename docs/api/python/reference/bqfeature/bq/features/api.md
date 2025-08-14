## Module `source/bqfeature/bq/features/api.py`

SYNOPSIS
========


DESCRIPTION
===========

  Interface to an feature server for other bisquik components.
  Abstract access to local feature server

### Functions

#### `find_server()`

#### `return_feature_vector(feature_name, **resource)`

returns feature on the resource from the feature service

#### `return_feature_location_in_tables(feature_name, **resource)`

returns the location of the features requested on the resource from the stored tables

#### `return_feature_list()`

returns a list of registered features
