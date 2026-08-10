# pandas.DatetimeIndex.second#

- 
*property* DatetimeIndex.second[source]#
- The seconds of the datetime. Examples >>> datetime_series = pd.Series( ... pd.date_range("2000-01-01", periods=3, freq="s") ... ) >>> datetime_series 0 2000-01-01 00:00:00 1 2000-01-01 00:00:01 2 2000-01-01 00:00:02 dtype: datetime64[ns] >>> datetime_series.dt.second 0 0 1 1 2 2 dtype: int32