# pandas.Series.values#

- property Series.values[source]#
- Return Series as ndarray or ndarray-like depending on the dtype. Warning We recommend using `Series.array` or`Series.to_numpy()` , depending on whether you need
a reference to the underlying data or a NumPy array.
The return type of`.values` depends on the dtype: it is a`numpy.ndarray` for some dtypes (for example`int64` or`float64` ) and an`ExtensionArray` for others (for
example`category` , nullable`Int64` , or string dtypes),
which makes it harder to write code that works across dtypes.`.values` also converts timezone-aware datetimes to UTC and
drops the timezone.`Series.array` always returns
the underlying array as an`ExtensionArray` , and`Series.to_numpy()` always returns a`numpy.ndarray` and accepts`dtype` ,`copy` , and`na_value` arguments to
control the conversion.
  - Returns:
    - numpy.ndarray or ndarray-like
 See also 
  - `Series.array`
  - Reference to the underlying data.
  - `Series.to_numpy`
  - A NumPy array representing the underlying data.
 Examples For a Series backed by a NumPy dtype such as `int64` ,`.values` returns a`numpy.ndarray` :>>> pd.Series([1, 2, 3]).values array([1, 2, 3]) For extension dtypes such as the default string dtype or `category` ,`.values` returns an`ExtensionArray` instead, while`Series.to_numpy()` always returns a`numpy.ndarray` :>>> pd.Series(list("aabc")).values <ArrowStringArray> ['a', 'a', 'b', 'c'] Length: 4, dtype: str >>> pd.Series(list("aabc")).to_numpy() array(['a', 'a', 'b', 'c'], dtype=object) >>> pd.Series(list("aabc")).astype("category").values ['a', 'a', 'b', 'c'] Categories (3, str): ['a', 'b', 'c'] Timezone aware datetime data is converted to UTC and the timezone is dropped, while `Series.array` preserves the timezone:>>> pd.Series( ... pd.date_range("20130101", periods=3, tz="US/Eastern") ... ).values array(['2013-01-01T05:00:00.000000', '2013-01-02T05:00:00.000000', '2013-01-03T05:00:00.000000'], dtype='datetime64[us]') >>> pd.Series(pd.date_range("20130101", periods=3, tz="US/Eastern")).array <DatetimeArray> ['2013-01-01 00:00:00-05:00', '2013-01-02 00:00:00-05:00', '2013-01-03 00:00:00-05:00'] Length: 3, dtype: datetime64[us, US/Eastern] Deprecated since version 3.0.0: For `DatetimeTZDtype` ,`PeriodDtype` , and`IntervalDtype` dtypes, the behavior of`.values` returning
a lossy or object-dtype result is deprecated. In a future version,`.values` will return the underlying ExtensionArray. Use`Series.to_numpy()` or`Series.array` instead.