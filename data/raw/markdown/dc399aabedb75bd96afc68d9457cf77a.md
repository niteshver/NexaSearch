# pandas.Series.sparse.sp_values#

- Series.sparse.sp_values[source]#
- An ndarray containing the non- `fill_value` values.This property returns the actual data values stored in the sparse representation, excluding the values that are equal to the `fill_value` .
The result is an ndarray of the underlying values, preserving the sparse
structure by omitting the default`fill_value` entries.See also 
  - `Series.sparse.to_dense`
  - Convert a Series from sparse values to dense.
  - `Series.sparse.fill_value`
  - Elements in data that are fill_value are not stored.
  - `Series.sparse.density`
  - The percent of non- `fill_value` points, as decimal.
 Examples >>> from pandas.arrays import SparseArray >>> s = SparseArray([0, 0, 1, 0, 2], fill_value=0) >>> s.sp_values array([1, 2])