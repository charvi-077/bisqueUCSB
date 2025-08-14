## Module `source/bqserver/bq/preference/controllers/service.py`

SYNOPSIS
========


DESCRIPTION
===========

### Functions

#### `mergeDocuments(current, new, **attrib)`

Merges two xml documents. Current document elements are replace with new document elements.


@param: current - preference etree document
@param: new - preference etree document
@param: attrib - top level attribute for the new merged document

#### `to_dict(tree)`

@param: etree
@return: preference dictionary structure

#### `to_etree(dictionary, **attrib)`

@param: preference dictionary stucture (TagNameNode)
@return: etree

#### `update_level(new_doc, current_doc, **attrib)`

prepares the new elements to be place in the preference resource

#### `initialize(url)`

Initialize the top level server for this microapp

### Classes

#### `PreferenceController`

The preference controller is a central point for
a special resource that cascades all the resource levels
meant as guidance for the bisque UI
(System -> User -> all other Resource) providing


General Format of <preference> resource

<preference>
    <tag name="UI Component"/>
        <tag name="UI preference name 1" value="preference value"/>
            <template>
                <tag name="template parameter name" value="template parameter value"/>
                ...
            </template>
        <tag name="sub UI component"/>
            <tag name="sub UI preference name 1" value="preference value"/>
        ...
    ...
</preference>

Methods:
- `user(*arg, **kw)`
- `reset(*arg, **kw)`
- `ensure_admin()`
- `log_start()`
- `log_finish()`
- `get(resource_uniq, xpath, level, **kw)`
- `get_current_user(**kw)`
- `get_current_user_annotation(resource_uniq, **kw)`
- `strip_attributes(xml, save_attrib)`
- `system_post(body, xpath, **kw)`
- `system_put(body, xpath, **kw)`
- `system_reset(xpath, **kw)`
- `system_delete(xpath, **kw)`
- `user_post(body, xpath, **kw)`
- `user_put(body, xpath, **kw)`
- `user_delete(xpath, **kw)`
- `resource_post(resource_uniq, body, xpath, **kw)`
- `resource_put(resource_uniq, xpath, body, **kw)`
- `resource_delete(resource_uniq, xpath, **kw)`
- `post(resource, resource_preference_list, preference_doc, xpath)`
- `put()`
- `delete(preference_uri, xpath)`
