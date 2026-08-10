# pandas.api.types.is_dtype_equal#

- 
pandas.api.types.is_dtype_equal(*source* ,*target* )[source]#
- Check if two dtypes are equal. This function compares two dtype specifications, handling both NumPy dtypes and pandas ExtensionDtypes. String representations of dtypes are also supported and will be resolved before comparison. 
  - Parameters:
    - **source** type or str
    - The first dtype to compare.
    - **target** type or str
    - The second dtype to compare.
  - Returns:
    - boolean
    - Whether or not the two dtypes are equal.
 See also 
  - `api.types.is_categorical_dtype`
  - Check whether the provided array or dtype is of the Categorical dtype.
  - `api.types.is_string_dtype`
  - Check whether the provided array or dtype is of the string dtype.
  - `api.types.is_object_dtype`
  - Check whether an array-like or dtype is of the object dtype.
 Examples >>> from pandas.api.types import is_dtype_equal >>> is_dtype_equal(int, float) False >>> is_dtype_equal("int", int) True >>> is_dtype_equal(object, "category") False >>> from pandas.api.types import CategoricalDtype >>> is_dtype_equal(CategoricalDtype(), "category") True >>> from pandas.api.types import DatetimeTZDtype >>> is_dtype_equal(DatetimeTZDtype(tz="UTC"), "datetime64") False