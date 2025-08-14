## Python Client: bqapi

- **package**: `bqapi`
- **modules**: `bqapi.comm`, `bqapi.services`, `bqapi.bqnode`, `bqapi.bqclass`, `bqapi.bqfeature`, `bqapi.util`

### Install

```bash
pip install -r /workspace/source/requirements.txt
pip install /workspace/source/bqapi
```

### Quick start

```python
from bqapi.comm import BQSession

# Create a session and authenticate
s = BQSession().init_local('https://<host>')
s.login('<user>', '<password>')

# Discover services
print(s.service_map)  # dict of service_name -> base URL

# Fetch an image's metadata as XML
image = s.service('data_service').fetch('image/<image_uniq>', render='etree')
print(image.tag, image.get('name'))

# Download a thumbnail
img = s.service('image_service')
th = img.get('thumbnail/<image_uniq>')
open('thumb.jpg', 'wb').write(th.content)
```

### Sessions

- **`BQSession`**: top-level API
  - `init_local(root_url: str)` initialize server root
  - `login(user: str, password: str)` basic auth
  - `login_mex(token: str, user: Optional[str]=None)` MEX auth
  - `service(name: str)` returns a typed proxy (see below)

### Service proxies

- **`AuthProxy`** (`service('auth_service')`)
  - `login_providers()`
  - `credentials()`
  - `get_session()`

- **`BlobProxy`** (`service('blob_service')`)
  - `path_link(srcpath, alias=None, resource_type=None, tag_file=None)`
  - `path_delete(srcpath, alias=None)`
  - `path_rename(srcpath, dstpath, alias=None)`
  - `path_list(srcpath, alias=None)`

- **`ImportProxy`** (`service('import')`)
  - `transfer(filename, fileobj=None, xml=None)` upload files/resources

- **`DatasetProxy`** (`service('dataset_service')`)
  - `delete(dataset_uniq, members=False, **kw)`
  - `append_member(dataset_uniq, resource_uniq, **kw)`
  - `delete_member(dataset_uniq, resource_uniq, **kw)`

- **`TableProxy`** (`service('table')`)
  - `load_array(table_uniq, path, slices=[])`
  - `store_array(array, name)`

- **`ImageProxy`** (`service('image_service')`)
  - `get_thumbnail(image_uniq, **kw)`

All proxies inherit from **`BaseServiceProxy`** providing:
- `get(path=None, params=None, render=None, **kw)`
- `post(path=None, params=None, render=None, **kw)`
- `put(path=None, params=None, render=None, **kw)`
- `delete(path=None, params=None, render=None, **kw)`

### Examples

- Upload a file and create a resource
```python
from bqapi.comm import BQSession

s = BQSession().init_local('https://<host>')
s.login('<user>', '<password>')
imp = s.service('import')
resp = imp.transfer('/path/to/file.tif')
print(resp.status_code)
```

- Create a dataset and add members
```python
from lxml import etree
from bqapi.comm import BQSession

s = BQSession().init_local('https://<host>')
s.login('<user>', '<password>')

# Create empty dataset via data_service
xml = etree.Element('dataset', name='My Dataset')
res = s.service('data_service').post('dataset', data=etree.tostring(xml))
uniq = res.headers['Location'].split('/')[-1]

# Append member via DatasetProxy
s.service('dataset_service').append_member(uniq, 'image/<image_uniq>')
```

- Download a table array as NumPy
```python
import numpy as np
from bqapi.comm import BQSession

s = BQSession().init_local('https://<host>')
s.login('<user>', '<password>')
arr = s.service('table').load_array('table/<table_uniq>', 'array')
print(arr.shape)
```

### Error handling

- `bqapi.exception.BQCommError`: request transport/HTTP errors
- `bqapi.exception.BQApiError`: client misuse/errors

### Tips

- Use `render='etree'` for XML parsing server-side in the client
- Use absolute uniq paths, e.g. `image/<uniq>`, when addressing resources via `data_service`
- Inspect available services via `session.service_map`