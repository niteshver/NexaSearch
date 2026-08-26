# pandas.api.extensions.ExtensionArray._concat_same_type#

- 
classmethod ExtensionArray._concat_same_type(*to_concat* )[source]#
- Concatenate multiple arrays of this dtype. This method joins a sequence of ExtensionArrays of the same dtype into a single ExtensionArray. All arrays in the sequence must have the same dtype. 
  - Parameters:
    - **to_concat** sequence of this type
    - An array of the same dtype to concatenate.
  - Returns:
    - ExtensionArray
 See also 
  - `api.extensions.ExtensionArray._explode`
  - Transform each element of list-like to a row.
  - `api.extensions.ExtensionArray._formatter`
  - Formatting function for scalar values.
  - `api.extensions.ExtensionArray._from_factorized`
  - Reconstruct an ExtensionArray after factorization.
 Examples >>> arr1 = pd.array([1, 2, 3]) >>> arr2 = pd.array([4, 5, 6]) >>> pd.arrays.IntegerArray._concat_same_type([arr1, arr2]) <IntegerArray> [1, 2, 3, 4, 5, 6] Length: 6, dtype: Int64