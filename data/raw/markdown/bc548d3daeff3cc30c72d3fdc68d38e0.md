# pandas.DatetimeIndex.microsecond#

- property DatetimeIndex.microsecond[source]#
- The microseconds of the datetime. See also 
  - `DatetimeIndex.second`
  - The seconds of the datetime.
  - `DatetimeIndex.nanosecond`
  - The nanoseconds of the datetime.
 Examples >>> datetime_series = pd.Series( ... pd.date_range("2000-01-01", periods=3, freq="us") ... ) >>> datetime_series 0 2000-01-01 00:00:00.000000 1 2000-01-01 00:00:00.000001 2 2000-01-01 00:00:00.000002 dtype: datetime64[us] >>> datetime_series.dt.microsecond 0 0 1 1 2 2 dtype: int32