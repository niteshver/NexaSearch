# pandas.Index.is_unique#

- Index.is_unique[source]#
- Return if the index has unique values. The uniqueness check is based on exact equality of values. An index with no repeated values returns `True` , otherwise`False` .
  - Returns:
    - bool
 See also 
  - `Index.has_duplicates`
  - Inverse method that checks if it has duplicate values.
 Examples >>> idx = pd.Index([1, 5, 7, 7]) >>> idx.is_unique False >>> idx = pd.Index([1, 5, 7]) >>> idx.is_unique True >>> idx = pd.Index(["Watermelon", "Orange", "Apple", "Watermelon"]).astype( ... "category" ... ) >>> idx.is_unique False >>> idx = pd.Index(["Orange", "Apple", "Watermelon"]).astype("category") >>> idx.is_unique True