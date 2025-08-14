## Module `source/bqserver/bq/stats/controllers/stats_server.py`

Statistics server : provides tag documents with summarization of input data retreived from
   a given URL using a given XPath expression

DESCRIPTION
===========

 The idea for the statistics service is in the sequence of filter applied to the data
 URL specifies the documents URL, which can be: gobjects, tags or dataset
 1) QUERY: [etree -> vector of objects]
    Elements are extracted from the document into the vector using XPath expression
    at this stage the vector should only comntain:
        a) tags (where values could be either numeric or string), 
        b) primitive gobjects (only graphical elements like poits and polygones...)
        c) numerics as a result of operation in XPath
 2) MAP: [vector of objects -> uniform vector of numbers or strings]
    An operator is applied onto the vector of objects to produce a vector of numbers or strings
    The operator is specified by the user and can take specific elements and produces specific result
    for example: operator "area" could take polygon or rect and produce a number
                 operator "numeric-value" can take a "tag" and return tag's value as a number
                 possible operator functions should be extensible and maintained by the stat service
 3) REDUCE: [uniform vector of numbers or strings -> summary as XML]
    A summarizer function is applied to the vector of objects to produce some summary
    the summary is returned as an XML document
    for example: summary "vector" could simply pass the input vector for output
                 summary "histogram" could bin the values of the input vector and could work on both text and numbers 
                 summary "max" would return max value of the input vector

EXTENSIONS
===========

Operations and summarizers are added into the service by simply deriving them from
appropriate base classes and writng the code in appropriate files, just that...

### Functions

#### `dict2url(d, mykeys)`

#### `getNumberedArgs(d, basename)`

#### `guaranteeSize(l, n)`

#### `startWithEither(s, l)`

#### `initialize(uri)`

Initialize the top level server for this microapp

#### `get_static_dirs()`

Return the static directories for this server

### Classes

#### `statsController`

Methods:
- `maps(**kw)`
- `reduces(**kw)`
- `index(**kw)`
- `compute(**kw)`
- `xml(**kw)`
- `json(**kw)`
- `csv(**kw)`
- `get_request(url, setmode)`
- `compute_stats(**kw)`
