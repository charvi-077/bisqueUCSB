## Module `source/bqfeature/bq/features/controllers/utils.py`

Utils for feature service

### Functions

#### `calculation_lock(calc)`

Some feature calculation functions are not thread-safe.
This decorator will force calculations to be run concurrently
in threads. Place on calculation functions in Feature classes.

#### `request_externally(url)`

Makes a request on the give url externally. If it finds url without errors the content
of the body is returned else None is returned

@param url - the url that is requested externally

@return requests response object

#### `check_access(ident)`

Checks for element in the database. If found returns True else returns
False

@param ident  - resource uniq or resource id
@param action - resource action on the database (default: RESOURCE_READ)

@return bool

#### `mex_validation(resource)`

First checks the access of the token if the url is image_service or data_service.
If the token is not found on the url an internal request is made to check the
response status. If a 302 is returned the redirect url is added to the resource.
If an internal request fails an external request is made in the same way as the
internal request. If all fails an InvalidResourceError is returned.

@param: resource - a feature_resource namedtuple

@return: resource - feature_resource namedtuple with redirected urls added

@exception: InvalidResourceError - if the resource could not be found

#### `except_image_only(resource)`

Returns only if the resource contains an image url else a FeatureExtractorError
is raised.

@param: resource

@exception: FeatureExtractionError

#### `fetch_resource(uri)`

Attempts to make a request first internally and then externally.
If one request returns a 200 the content is return else an
InvalidResourceError is raised.
@param: url - the url the request is made with

@return: body of the request

@exception: InvalidResourceError

#### `image2numpy(uri, **kw)`

Converts image url to numpy array.
For bisque image_service it changes the format
to ome-tiff and reads in the tiff with pylibtiff
If the uri does not return a tiff file
and then the pillow reader is used instead.

@param: takes in an image_url
@param: query parameters added to only image service urls

@return numpy image

#### `convert_image2numpy(image_path)`

Converts the image at the given path to a numpy array.
First attempts to read the image with pylibtiff. If
the image is not a tiff file, Pillow is used to try
to read the file. IF all fails an InvalidResourceError
is returned.

@param: image_path

@return: image numpy array

@exception InvalidResourceError

#### `gobject2mask(uri, im)`

Converts a gobject with a shape into
a binary mask

@param: uri - gobject uris
@param: im - image matrix

@return: mask

#### `gobject2keypoint(uri)`

Given a gobject data_service url which is either
a circle or point. The vertices are extracted
and parameters for an opencv keypoint.
@param: uri - circle or point gobject url

@return: circle (x,y,r), point (x,y,1)

@exception FeatureExtractionError - if the xml is
not complete or not correctly formatted
