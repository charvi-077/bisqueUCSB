## Module `source/bqcore/bq/core/service.py`

SYNOPSIS
========


DESCRIPTION
===========

### Functions

#### `load_services(wanted)`

#### `mount_services(root, enabled, disabled)`

#### `start_services(root, enabled, disabled)`

#### `urljoin(base, url, **kw)`

### Classes

#### `ServiceDirectory`

Specialized dict of service_type -> to bq.service

Methods:
- `register_service(name, service, service_type)`
- `register_instance(service)`
- `find_class(service_type)`
- `has_service(service_type, service_uri)`
- `find_service(service_type)`
- `get_services(service_type)`

#### `ServiceMixin`

Methods:
- `start()`
- `get_uri()`
- `makeurl(path, **kw)`
- `get_localurl()`
- `get_static()`
- `servicelist()`

#### `ServiceController`
