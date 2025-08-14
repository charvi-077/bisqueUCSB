## Module `source/bqserver/bq/export_service/controllers/export_service.py`

SYNOPSIS
========

DESCRIPTION
===========

TODO
===========

  1. Accept metadata as XML file along with packed image files
  1.

### Functions

#### `initialize(uri)`

Initialize the top level server for this microapp

#### `get_static_dirs()`

Return the static directories for this server

### Classes

#### `export_serviceController`

Methods:
- `index(**kw)`
- `check_access(ident)`
- `to_gdocs(**kw)`
- `to_gdocs_send(**kw)`
- `stream(**kw)`
- `initStream(**kw)`
- `export(**kw)`

#### `ExporterGeo`

Supports exporting Bisque documents into geographical formats

Methods:
- `bq2format(resource)`
- `export(uniq)`
- `create_transform_function(resource, meta)`

#### `ExporterKML`

Supports exporting Bisque documents into KML

Methods:
- `bq2format(resource)`
- `convert_node(node, kml, cnvf)`
- `render_resouces(node, kml)`
- `render_tags(node, kml, ed, path)`
- `render_gobjects(node, kml, type, _val, cnvf)`
- `point(node, kml, vrtx, type, val)`
- `line(node, kml, vrtx, type, val)`
- `polygon(node, kml, vrtx, type, val)`
- `polyline(node, kml, vrtx, type, val)`
- `label(node, kml, vrtx, type, val)`
- `circle(node, kml, vrtx, type, val)`
- `ellipse(node, kml, vrtx, type, val)`
- `rectangle(node, kml, vrtx, type, val)`
- `square(node, kml, vrtx, type, val)`

#### `ExporterGeoJson`

Supports exporting Bisque documents into GeoJson

Methods:
- `bq2format(resource)`
- `convert_node(node, kml, cnvf)`
- `render_resouces(node, features)`
- `render_gobjects(node, features, type, _val, cnvf)`
- `render_tags(node, feature, ed, path)`
- `point(node, feature, vrtx, type, val)`
- `line(node, feature, vrtx, type, val)`
- `polygon(node, feature, vrtx, type, val)`
- `polyline(node, feature, vrtx, type, val)`
- `label(node, feature, vrtx, type, val)`
