# pandas.Timedelta.asm8#

- Timedelta.asm8#
- Return a numpy timedelta64 array scalar view. Provides access to the array scalar view (i.e. a combination of the value and the units) associated with the numpy.timedelta64().view(), including a 64-bit integer representation of the timedelta in nanoseconds (Python int compatible). 
  - Returns:
    - numpy timedelta64 array scalar view
    - Array scalar view of the timedelta in nanoseconds.
 See also 
  - `Timedelta.total_seconds`
  - Return the total seconds in the duration.
  - `Timedelta.components`
  - Return a namedtuple of the Timedelta’s components.
  - `Timedelta.to_timedelta64`
  - Convert the Timedelta to a numpy.timedelta64.
 Examples >>> td = pd.Timedelta('1 days 2 min 3 us 42 ns') >>> td.asm8 np.timedelta64(86520000003042,'ns') >>> td = pd.Timedelta('2 min 3 s') >>> td.asm8 np.timedelta64(123000000,'us') >>> td = pd.Timedelta('3 ms 5 us') >>> td.asm8 np.timedelta64(3005,'us') >>> td = pd.Timedelta(42, unit='ns') >>> td.asm8 np.timedelta64(42,'ns')