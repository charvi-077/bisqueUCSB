## Module `source/bqapi/bqapi/xmldict.py`

### Functions

#### `xml2d(e)`

Convert an etree into a dict structure

@type  e: etree.Element
@param e: the root of the tree
@return: The dictionary representation of the XML tree

#### `d2xml(d)`

convert dict to xml

   1. The top level d must contain a single entry i.e. the root element
   2.  Keys of the dictionary become sublements or attributes
   3.  If a value is a simple string, then the key is an attribute
   4.  if a value is dict then, then key is a subelement
   5.  if a value is list, then key is a set of sublements

   a  = { 'module' : {'tag' : [ { 'name': 'a', 'value': 'b'},
                                { 'name': 'c', 'value': 'd'},
                             ],
                      'gobject' : { 'name': 'g', 'type':'xx' },
                      'uri' : 'test',
                   }
       }
>>> d2xml(a)
<module uri="test">
   <gobject type="xx" name="g"/>
   <tag name="a" value="b"/>
   <tag name="c" value="d"/>
</module>

@type  d: dict
@param d: A dictionary formatted as an XML document
@return:  A etree Root element

#### `xml2nv(e)`

Convert an etree into a dict structure

@type  e: etree.Element
@param e: the root of the tree
@return: The dictionary representation of the XML tree
