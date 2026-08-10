# pandas.Series.update#

- 
Series.update(*other* )[source]#
- Modify Series in place using values from passed Series. Uses non-NA values from passed Series to make updates. Aligns on index. 
  - Parameters:
    - **other** Series, or object coercible into Series
    - Other Series that provides values to update the current Series.
 See also 
  - `Series.combine`
  - Perform element-wise operation on two Series using a given function.
  - `Series.transform`
  - Modify a Series using a function.
 Examples >>> s = pd.Series([1, 2, 3]) >>> s.update(pd.Series([4, 5, 6])) >>> s 0 4 1 5 2 6 dtype: int64 >>> s = pd.Series(["a", "b", "c"]) >>> s.update(pd.Series(["d", "e"], index=[0, 2])) >>> s 0 d 1 b 2 e dtype: str >>> s = pd.Series([1, 2, 3]) >>> s.update(pd.Series([4, 5, 6, 7, 8])) >>> s 0 4 1 5 2 6 dtype: int64 If `other` contains NaNs the corresponding values are not updated
in the original Series.>>> s = pd.Series([1, 2, 3]) >>> s.update(pd.Series([4, np.nan, 6])) >>> s 0 4 1 2 2 6 dtype: int64 `other` can also be a non-Series object type
that is coercible into a Series>>> s = pd.Series([1, 2, 3]) >>> s.update([4, np.nan, 6]) >>> s 0 4 1 2 2 6 dtype: int64 >>> s = pd.Series([1, 2, 3]) >>> s.update({1: 9}) >>> s 0 1 1 9 2 3 dtype: int64