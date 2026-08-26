# pandas.api.extensions.ExtensionArray.unique#

- ExtensionArray.unique()[source]#
- Compute the ExtensionArray of unique values. This method returns a new ExtensionArray containing the distinct values from the original array, preserving the order of first appearance. 
  - Returns:
    - pandas.api.extensions.ExtensionArray
    - With unique values from the input array.
 See also 
  - `Index.unique`
  - Return unique values in the index.
  - `Series.unique`
  - Return unique values of Series object.
  - `unique`
  - Return unique values based on a hash table.
 Examples >>> arr = pd.array([1, 2, 3, 1, 2, 3]) >>> arr.unique() <IntegerArray> [1, 2, 3] Length: 3, dtype: Int64