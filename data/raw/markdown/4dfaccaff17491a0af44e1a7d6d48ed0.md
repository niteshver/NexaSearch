# pandas.api.extensions.ExtensionArray._values_for_factorize#

- ExtensionArray._values_for_factorize()[source]#
- Return an array and missing value suitable for factorization. This method provides the values and NA sentinel to use in the factorization process. Subclasses may override this to customize the factorization behavior. 
  - Returns:
    - **values** ndarray
    - An array suitable for factorization. This should maintain order and be a supported dtype (Float64, Int64, UInt64, String, Object). By default, the extension array is cast to object dtype.
    - **na_value** object
    - The value in values to consider missing. This will be treated as NA in the factorization routines, so it will be coded as -1 and not included in uniques. By default, `np.nan` is used.
 See also 
  - `util.hash_pandas_object`
  - Hash the pandas object.
 Notes The values returned by this method are also used in `pandas.util.hash_pandas_object()` . If needed, this can be
overridden in the`self._hash_pandas_object()` method.Examples >>> pd.array([1, 2, 3])._values_for_factorize() (array([1, 2, 3], dtype=object), nan)