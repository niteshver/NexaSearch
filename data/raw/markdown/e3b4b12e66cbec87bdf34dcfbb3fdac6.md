# pandas.tseries.offsets.MonthBegin.nanos#

- MonthBegin.nanos#
- Return an integer of the total number of nanoseconds. This property computes the offset duration in nanoseconds. For fixed frequency offsets (like Hour, Minute, Second), this returns the exact number of nanoseconds. For non-fixed frequencies that depend on calendar context (like Week without a specified weekday), this raises an error. 
  - Raises:
    - ValueError
    - If the frequency is non-fixed.
 See also 
  - `tseries.offsets.Hour.nanos`
  - Returns an integer of the total number of nanoseconds.
  - `tseries.offsets.Day.nanos`
  - Returns an integer of the total number of nanoseconds.
 Examples >>> pd.offsets.Week(n=1).nanos ValueError: Week: weekday=None is a non-fixed frequency