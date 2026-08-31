# pandas.Index.value_counts#

- 
Index.value_counts(*normalize=False* ,*sort=True* ,*ascending=False* ,*bins=None* ,*dropna=True* )[source]#
- Return a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default. 
  - Parameters:
    - **normalize** bool, default False
    - If True then the object returned will contain the relative frequencies of the unique values.
    - **sort** bool, default True
    - Stable sort by frequencies when True. Preserve the order of the data when False. Changed in version 3.0.0: Prior to 3.0.0, the sort was unstable.
    - **ascending** bool, default False
    - Sort in ascending order.
    - **bins** int, optional
    - Rather than count values, group them into half-open bins, a convenience for `pd.cut` , only works with numeric data.
    - **dropna** bool, default True
    - Don’t include counts of NaN.
  - Returns:
    - Series
    - Series containing counts of unique values.
 See also 
  - `Series.count`
  - Number of non-NA elements in a Series.
  - `DataFrame.count`
  - Number of non-NA elements in a DataFrame.
  - `DataFrame.value_counts`
  - Equivalent method on DataFrames.
 Examples >>> index = pd.Index([3, 1, 2, 3, 4, np.nan]) >>> index.value_counts() 3.0 2 1.0 1 2.0 1 4.0 1 Name: count, dtype: int64 With normalize set to True, returns the relative frequency by dividing all values by the sum of values. >>> s = pd.Series([3, 1, 2, 3, 4, np.nan]) >>> s.value_counts(normalize=True) 3.0 0.4 1.0 0.2 2.0 0.2 4.0 0.2 Name: proportion, dtype: float64 **bins**Bins can be useful for going from a continuous variable to a categorical variable; instead of counting unique apparitions of values, divide the index in the specified number of half-open bins. >>> s.value_counts(bins=3) (0.996, 2.0] 2 (2.0, 3.0] 2 (3.0, 4.0] 1 Name: count, dtype: int64 **dropna**With dropna set to False we can also see NaN index values. >>> s.value_counts(dropna=False) 3.0 2 1.0 1 2.0 1 4.0 1 NaN 1 Name: count, dtype: int64 **Categorical Dtypes**Rows with categorical type will be counted as one group if they have same categories and order. In the example below, even though `a` ,`c` , and`d` all have the same data types of`category` ,
only`c` and`d` will be counted as one group
since`a` doesn’t have the same categories.>>> df = pd.DataFrame({"a": [1], "b": ["2"], "c": [3], "d": [3]}) >>> df = df.astype({"a": "category", "c": "category", "d": "category"}) >>> df a b c d 0 1 2 3 3 >>> df.dtypes a category b str c category d category dtype: object >>> df.dtypes.value_counts() category 2 category 1 str 1 Name: count, dtype: int64