# pandas.Series.unique#

- Series.unique()[source]#
- Return unique values of Series object. Uniques are returned in order of appearance. Hash table-based unique, therefore does NOT sort. 
  - Returns:
    - ndarray or ExtensionArray
    - The unique values returned as a NumPy array. See Notes.
 See also 
  - `Series.drop_duplicates`
  - Return Series with duplicate values removed.
  - `unique`
  - Top-level unique method for any 1-d array-like object.
  - `Index.unique`
  - Return Index with unique values from an Index object.
 Notes Returns the unique values as a NumPy array. In case of an extension-array backed Series, a new `ExtensionArray` of that type with just
the unique values is returned. This includes
  - Categorical
  - Period
  - Datetime with Timezone
  - Datetime without Timezone
  - Timedelta
  - Interval
  - Sparse
  - IntegerNA
  - String
 See Examples section. Examples >>> pd.Series([2, 1, 3, 3], name="A").unique() array([2, 1, 3]) >>> pd.Series([pd.Timestamp("2016-01-01") for _ in range(3)]).unique() <DatetimeArray> ['2016-01-01 00:00:00'] Length: 1, dtype: datetime64[us] >>> pd.Series( ... [pd.Timestamp("2016-01-01", tz="US/Eastern") for _ in range(3)] ... ).unique() <DatetimeArray> ['2016-01-01 00:00:00-05:00'] Length: 1, dtype: datetime64[us, US/Eastern] A Categorical will return categories in the order of appearance and with the same dtype. >>> pd.Series(pd.Categorical(list("baabc"))).unique() ['b', 'a', 'c'] Categories (3, str): ['a', 'b', 'c'] >>> pd.Series( ... pd.Categorical(list("baabc"), categories=list("abc"), ordered=True) ... ).unique() ['b', 'a', 'c'] Categories (3, str): ['a' < 'b' < 'c']