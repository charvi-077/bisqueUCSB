## Module `source/bqfeature/bq/features/controllers/extractors/Test/extractor.py`

Test library

### Classes

#### `SimpleTestFeature`

Test Feature
This extractor is completely useless to calculate any 
useful feature. 
Purpose: to test the reliability of the feature service

Methods:
- `calculate(resource)`

#### `UncachedTestFeature`

Uncached Test Feature 
This extractor is completely useless to calculate any 
useful feature. 
Purpose: to test the reliability of the feature service

#### `MultiVectorTestFeature`

Test Feature parameters
This extractor is completely useless to calculate any 
useful feature. 
Purpose: to test the reliability of the feature service

Methods:
- `calculate(resource)`

#### `UncachedMultiVectorTestFeature`

Test Feature parameters
This extractor is completely useless to calculate any 
useful feature. 
Purpose: to test the reliability of the feature service

#### `ParametersTestFeature`

Test Feature parameters
This extractor is completely useless to calculate any 
useful feature. 
Purpose: to test the reliability of the feature service

Methods:
- `cached_columns()`
- `workdir_columns()`
- `calculate(resource)`

#### `UncachedParametersTestFeature`

Test Feature parameters
This extractor is completely useless to calculate any 
useful feature. 
Purpose: to test the reliability of the feature service

#### `ExceptionTestFeature`

Exception Test Feature

This feature will produce an feature calculation
exceptions when asked to calculate.

Methods:
- `calculate(resource)`
