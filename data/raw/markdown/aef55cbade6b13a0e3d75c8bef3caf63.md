# pandas.TimedeltaIndex.to_pytimedelta#

- TimedeltaIndex.to_pytimedelta()[source]#
- Return an ndarray of datetime.timedelta objects. Each element of the `TimedeltaIndex` is converted to the
corresponding native Python`datetime.timedelta` object.
  - Returns:
    - numpy.ndarray
    - A NumPy `timedelta64` object representing the same duration as the
original pandas`Timedelta` object. The precision of the resulting
object is in nanoseconds, which is the default
time resolution used by pandas for`Timedelta` objects, ensuring
high precision for time-based calculations.
 See also 
  - `to_timedelta`
  - Convert argument to timedelta format.
  - `Timedelta`
  - Represents a duration between two dates or times.
  - `DatetimeIndex`
  - Index of datetime64 data.
  - `Timedelta.components`
  - Return a components namedtuple-like of a single timedelta.
 Examples >>> tdelta_idx = pd.to_timedelta([1, 2, 3], unit="D") >>> tdelta_idx TimedeltaIndex(['1 days', '2 days', '3 days'], dtype='timedelta64[s]', freq=None) >>> tdelta_idx.to_pytimedelta() array([datetime.timedelta(days=1), datetime.timedelta(days=2), datetime.timedelta(days=3)], dtype=object) >>> tidx = pd.TimedeltaIndex(data=["1 days 02:30:45", "3 days 04:15:10"]) >>> tidx TimedeltaIndex(['1 days 02:30:45', '3 days 04:15:10'], dtype='timedelta64[us]', freq=None) >>> tidx.to_pytimedelta() array([datetime.timedelta(days=1, seconds=9045), datetime.timedelta(days=3, seconds=15310)], dtype=object)