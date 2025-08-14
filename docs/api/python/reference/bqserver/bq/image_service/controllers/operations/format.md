## Module `source/bqserver/bq/image_service/controllers/operations/format.py`

Provides an image in the requested format
       arg = format[,stream][,OPT1][,OPT2][,...]
       some formats are: tiff, jpeg, png, bmp, raw
       stream sets proper file name and forces browser to show save dialog
       any additional comma separated options are passed directly to the encoder

       for movie formats: fps,R,bitrate,B
       where R is a float number of frames per second and B is the integer bitrate

       for tiff: compression,C
       where C is the compression algorithm: none, packbits, lzw, fax

       for jpeg: quality,V
       where V is quality 0-100, 100 being best

       ex: format=jpeg

### Classes

#### `FormatOperation`

Provides an image in the requested format
arg = format[,stream][,OPT1][,OPT2][,...]
some formats are: tiff, jpeg, png, bmp, raw
stream sets proper file name and forces browser to show save dialog
any additional comma separated options are passed directly to the encoder

for movie formats: fps,R,bitrate,B
where R is a float number of frames per second and B is the integer bitrate

for tiff: compression,C
where C is the compression algorithm: none, packbits, lzw, fax

for jpeg: quality,V
where V is quality 0-100, 100 being best

ex: format=jpeg

Methods:
- `dryrun(token, arg)`
- `action(token, arg)`
