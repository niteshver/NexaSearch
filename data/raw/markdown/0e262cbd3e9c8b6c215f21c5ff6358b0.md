# pandas.TimedeltaIndex#

- 
class pandas.TimedeltaIndex(*data=None* ,*freq=<no_default>* ,*dtype=None* ,*copy=None* ,*name=None* )[source]#
- Immutable Index of timedelta64 data. Represented internally as int64, and scalars returned Timedelta objects. 
  - Parameters:
    - **data** array-like (1-dimensional), optional
    - Optional timedelta-like data to construct index with.
    - **freq** str or pandas offset object, optional
    - One of pandas date offset strings or corresponding objects. The string `'infer'` can be passed in order to set the frequency of the index as
the inferred frequency upon creation.
    - **dtype** numpy.dtype or str, default None
    - Valid `numpy` dtypes are`timedelta64[ns]` ,`timedelta64[us]` ,`timedelta64[ms]` , and`timedelta64[s]` .
    - **copy** bool, default None
    - Whether to copy input data, only relevant for array, Series, and Index inputs (for other input, e.g. a list, a new array is created anyway). Defaults to True for array input and False for Index/Series. Set to False to avoid copying array input at your own risk (if you know the input data won’t be modified elsewhere). Set to True to force copying Series/Index input up front.
    - **name** object
    - Name to be stored in the index.
 Attributes `days`Number of days for each element. `seconds`Number of seconds (>= 0 and less than 1 day) for each element. `microseconds`Number of microseconds (>= 0 and less than 1 second) for each element. `nanoseconds`Number of nanoseconds (>= 0 and less than 1 microsecond) for each element. `components`Return a DataFrame of the individual resolution components of the Timedeltas. `inferred_freq`(DEPRECATED) Return the inferred frequency of the index. Methods `to_pytimedelta` ()Return an ndarray of datetime.timedelta objects. `to_series` ([index, name])Create a Series with both index and values equal to the index keys. `round` (freq[, ambiguous, nonexistent])Perform round operation on the data to the specified freq. `floor` (freq[, ambiguous, nonexistent])Perform floor operation on the data to the specified freq. `ceil` (freq[, ambiguous, nonexistent])Perform ceil operation on the data to the specified freq. `to_frame` ([index, name])Create a DataFrame with a column containing the Index. `mean` (*[, skipna, axis])Return the mean value of the Array. See also 
  - `Index`
  - The base pandas Index type.
  - `Timedelta`
  - Represents a duration between two dates or times.
  - `DatetimeIndex`
  - Index of datetime64 data.
  - `PeriodIndex`
  - Index of Period data.
  - `timedelta_range`
  - Create a fixed-frequency TimedeltaIndex.
 Notes To learn more about the frequency strings, please see this link. Examples >>> pd.TimedeltaIndex(["0 days", "1 days", "2 days", "3 days", "4 days"]) TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'], dtype='timedelta64[us]', freq=None) We can also let pandas infer the frequency when possible. >>> pd.TimedeltaIndex(np.arange(5) * 24 * 3600 * 1e9, freq="infer") TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'], dtype='timedelta64[ns]', freq='D')