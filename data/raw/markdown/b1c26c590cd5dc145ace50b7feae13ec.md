# pandas.arrays.BooleanArray#

- 
class pandas.arrays.BooleanArray(*values* ,*mask* ,*copy=False* )[source]#
- Array of boolean (True/False) data with missing values. This is a pandas Extension array for boolean data, under the hood represented by 2 numpy arrays: a boolean array with the data and a boolean array with the mask (True indicating missing). BooleanArray implements Kleene logic (sometimes called three-value logic) for logical operations. See Kleene logical operations for more. To construct a BooleanArray from generic array-like input, use `pandas.array()` specifying`dtype="boolean"` (see examples
below).Warning BooleanArray is considered experimental. The implementation and parts of the API may change without warning. 
  - Parameters:
    - **values** numpy.ndarray
    - A 1-d boolean-dtype array with the data.
    - **mask** numpy.ndarray
    - A 1-d boolean-dtype array indicating missing values (True indicates missing).
    - **copy** bool, default False
    - Whether to copy the values and mask arrays.
  - Returns:
    - BooleanArray
 See also 
  - `array`
  - Create an array from data with the appropriate dtype.
  - `BooleanDtype`
  - Extension dtype for boolean data.
  - `Series`
  - One-dimensional ndarray with axis labels (including time series).
  - `DataFrame`
  - Two-dimensional, size-mutable, potentially heterogeneous tabular data.
 Examples Create a BooleanArray with `pandas.array()` :>>> pd.array([True, False, None], dtype="boolean") <BooleanArray> [True, False, <NA>] Length: 3, dtype: boolean