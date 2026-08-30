# pandas.Series.dt.as_unit#

- 
Series.dt.as_unit(*unit* ,*round_ok=True* )[source]#
- Convert to a dtype with the given unit resolution. The limits of timestamp representation depend on the chosen resolution. Different resolutions can be converted to each other through as_unit. 
  - Parameters:
    - **unit** {‘s’, ‘ms’, ‘us’, ‘ns’}
    - **round_ok** bool, default True
    - If False and the conversion requires rounding, raise ValueError.
  - Returns:
    - same type as self
    - Converted to the specified unit.
 See also 
  - `Timestamp.as_unit`
  - Convert to the given unit.
 Examples For `pandas.DatetimeIndex` :>>> idx = pd.DatetimeIndex(["2020-01-02 01:02:03.004005006"]) >>> idx DatetimeIndex(['2020-01-02 01:02:03.004005006'], dtype='datetime64[ns]', freq=None) >>> idx.as_unit("s") DatetimeIndex(['2020-01-02 01:02:03'], dtype='datetime64[s]', freq=None) For `pandas.TimedeltaIndex` :>>> tdelta_idx = pd.to_timedelta(["1 day 3 min 2 us 42 ns"]) >>> tdelta_idx TimedeltaIndex(['1 days 00:03:00.000002042'], dtype='timedelta64[ns]', freq=None) >>> tdelta_idx.as_unit("s") TimedeltaIndex(['1 days 00:03:00'], dtype='timedelta64[s]', freq=None)