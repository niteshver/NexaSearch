# pandas.DatetimeIndex.unit#

- property DatetimeIndex.unit[source]#
- The precision unit of the datetime data. Returns the precision unit for the dtype of the index. This is the smallest time frame that can be stored within this dtype. 
  - Returns:
    - str
    - Unit string representation (e.g. `"ns"` ).
 See also 
  - `DatetimeIndex.as_unit`
  - Convert to the given unit.
  - `TimedeltaIndex.as_unit`
  - Convert to the given unit.
 Examples For a DatetimeIndex: >>> idx = pd.DatetimeIndex(["2020-01-02 01:02:03.004005006"]) >>> idx.unit 'ns' >>> idx_s = pd.DatetimeIndex(["2020-01-02 01:02:03"], dtype="datetime64[s]") >>> idx_s.unit 's' For a TimedeltaIndex: >>> tdidx = pd.TimedeltaIndex(["1 day 3 min 2 us 42 ns"]) >>> tdidx.unit 'ns' >>> tdidx_s = pd.TimedeltaIndex(["1 day 3 min"], dtype="timedelta64[s]") >>> tdidx_s.unit 's'