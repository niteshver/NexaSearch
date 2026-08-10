# pandas.Index.is_monotonic_increasing#

- 
*property* Index.is_monotonic_increasing[source]#
- Return a boolean if the values are equal or increasing. 
  - Returns
    - bool
 See also 
  - `Index.is_monotonic_decreasing`
  - Check if the values are equal or decreasing.
 Examples >>> pd.Index([1, 2, 3]).is_monotonic_increasing True >>> pd.Index([1, 2, 2]).is_monotonic_increasing True >>> pd.Index([1, 3, 2]).is_monotonic_increasing False