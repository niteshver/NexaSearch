# pandas.api.extensions.ExtensionArray.item#

- 
ExtensionArray.item(*index=None* )[source]#
- Return the array element at the specified position as a Python scalar. Analogous to `numpy.ndarray.item()` , this converts a single
element to a native Python object.
  - Parameters:
    - **index** int, optional
    - Position of the element. If not provided, the array must contain exactly one element.
  - Returns:
    - scalar
    - The element at the specified position.
  - Raises:
    - ValueError
    - If no index is provided and the array does not have exactly one element.
    - IndexError
    - If the specified position is out of bounds.
 See also 
  - `numpy.ndarray.item`
  - Return the item of an array as a scalar.
 Examples >>> arr = pd.array([1], dtype="Int64") >>> arr.item() np.int64(1) >>> arr = pd.array([1, 2, 3], dtype="Int64") >>> arr.item(0) np.int64(1) >>> arr.item(2) np.int64(3)