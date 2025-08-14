## Module `source/bqapi/bqapi/util.py`

### Functions

#### `normalize_unicode(s)`

#### `safecopy(*largs)`

#### `parse_qs(query)`

parse a uri query string into a dict

#### `make_qs(pd)`

convert back from dict to qs

#### `save_blob(session, localfile, resource)`

put a local image on the server and return the URL
to the METADATA XML record

@param session: the local session
@param image: an BQImage object
@param localfile:  a file-like object or name of a localfile
@return XML content  when upload ok

@exceptions comm.BQCommError - if blob is failed to be posted

#### `fetch_blob(session, uri, dest, uselocalpath)`

fetch original image locally as tif
@param session: the bqsession
@param uri: resource image uri
@param dest: a destination directory
@param uselocalpath: true when routine is run on same host as server

#### `fetch_image_planes(session, uri, dest, uselocalpath)`

fetch all the image planes of an image locally
@param session: the bqsession
@param uri: resource image uri
@param dest: a destination directory
@param uselocalpath: true when routine is run on same host as server

#### `next_name(name)`

#### `fetch_image_pixels(session, uri, dest, uselocalpath)`

fetch original image locally as tif
@param session: the bqsession
@param uri: resource image uri
@param dest: a destination directory
@param uselocalpath: true when routine is run on same host as server

#### `fetch_dataset(session, uri, dest, uselocalpath)`

fetch elemens of dataset locally as tif

@param session: the bqsession
@param uri: resource image uri
@param dest: a destination directory
@param uselocalpath: true when routine is run on same host as server

@return:

#### `fetchImage(session, uri, dest, uselocalpath)`

@param: session -
@param: url -
@param: dest -
@param: uselocalpath- (default: False)

@return

#### `fetchDataset(session, uri, dest, uselocalpath)`

#### `save_image_pixels(session, localfile, image_tags)`

put a local image on the server and return the URL
to the METADATA XML record

@param: session - the local session
@param: image - an BQImage object
@param: localfile - a file-like object or name of a localfile

@return: XML content when upload ok

#### `as_flat_dict_tag_value(xmltree)`

#### `as_flat_dicts_node(xmltree)`

### Classes

#### `AttrDict`
