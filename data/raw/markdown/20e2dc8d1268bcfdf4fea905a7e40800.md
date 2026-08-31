# pandas.Index.is_monotonic_decreasing#

- property Index.is_monotonic_decreasing[source]#
- Return a boolean if the values are equal or decreasing. A monotonically decreasing index has values that are equal to or less than the preceding value. This is useful for checking if an index is sorted in non-increasing order. 
  - Returns:
    - bool
 See also 
  - `Index.is_monotonic_increasing`
  - Check if the values are equal or increasing.
 Examples >>> pd.Index([3, 2, 1]).is_monotonic_decreasing True >>> pd.Index([3, 2, 2]).is_monotonic_decreasing True >>> pd.Index([3, 1, 2]).is_monotonic_decreasing False