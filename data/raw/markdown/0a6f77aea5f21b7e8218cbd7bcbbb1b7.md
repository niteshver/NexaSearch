# pandas.Index.slice_locs#

- 
Index.slice_locs(*start=None* ,*end=None* ,*step=None* )[source]#
- Compute slice locations for input labels. This method determines the integer start and end positions for a label-based slice, which is useful for translating label-based slicing into positional slicing on the underlying data. 
  - Parameters:
    - **start** label, default None
    - If None, defaults to the beginning.
    - **end** label, default None
    - If None, defaults to the end.
    - **step** int, defaults None
    - If None, defaults to 1.
  - Returns:
    - tuple[int, int]
    - Returns a tuple of two integers representing the slice locations for the input labels within the index.
 See also 
  - `Index.get_loc`
  - Get location for a single label.
  - `Index.get_slice_bound`
  - Calculate the slice bound for a single label; used internally by `slice_locs` for each of`start` and`end` .
 Notes This method only works if the index is monotonic or unique. If `start` or`end` is not present in a monotonic index, the
returned position is the insertion point that preserves ordering
(analogous to`numpy.searchsorted()` ); no error is raised. If the
index is not monotonic and the label is missing, a`KeyError` is
raised.Examples >>> idx = pd.Index(list("abcd")) >>> idx.slice_locs(start="b", end="c") (1, 3) `start` and`end` need not be present in the index; for a
monotonic index they are mapped to the appropriate insertion
positions:>>> idx = pd.Index(list("bcde")) >>> idx.slice_locs(start="a", end="c") (0, 2)