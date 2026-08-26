# pandas.api.extensions.ExtensionArray.dtype#

- property ExtensionArray.dtype[source]#
- An instance of ExtensionDtype. This property returns the dtype object associated with this ExtensionArray. The dtype describes the type of data stored in the array. See also 
  - `api.extensions.ExtensionDtype`
  - Base class for extension dtypes.
  - `api.extensions.ExtensionArray`
  - Base class for extension array types.
  - `api.extensions.ExtensionArray.dtype`
  - The dtype of an ExtensionArray.
  - `Series.dtype`
  - The dtype of a Series.
  - `DataFrame.dtype`
  - The dtype of a DataFrame.
 Examples >>> pd.array([1, 2, 3]).dtype Int64Dtype()