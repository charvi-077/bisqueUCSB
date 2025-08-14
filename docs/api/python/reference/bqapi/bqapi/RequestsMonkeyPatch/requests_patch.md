## Module `source/bqapi/bqapi/RequestsMonkeyPatch/requests_patch.py`

A patch to format_header_param in urllib3

If a value has unicode the header will be returned
as 'name="value"; name*=utf-8''value' else
'name="value"'
