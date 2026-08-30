# pandas.tseries.offsets.BusinessDay.is_on_offset#

- 
BusinessDay.is_on_offset(*dt* )#
- Return boolean whether a timestamp intersects with this frequency. This method determines if a given timestamp falls on a business day (Monday through Friday). If `normalize` is True, it also checks that
the time component is midnight.
  - Parameters:
    - **dt** datetime
    - Timestamp to check intersection with frequency.
  - Returns:
    - bool
    - True if the timestamp is on a business day, False otherwise.
 See also 
  - `tseries.offsets.BusinessDay`
  - Represents business day offset.
  - `tseries.offsets.CustomBusinessDay`
  - Represents custom business day offset.
 Examples >>> ts = pd.Timestamp(2022, 8, 5) >>> ts.day_name() 'Friday' >>> pd.offsets.BusinessDay().is_on_offset(ts) True >>> ts = pd.Timestamp(2022, 8, 6) >>> ts.day_name() 'Saturday' >>> pd.offsets.BusinessDay().is_on_offset(ts) False With `normalize=True` , the timestamp must also be at midnight:>>> ts = pd.Timestamp(2022, 8, 5, 12, 0) >>> pd.offsets.BusinessDay(normalize=True).is_on_offset(ts) False >>> ts = pd.Timestamp(2022, 8, 5, 0, 0) >>> pd.offsets.BusinessDay(normalize=True).is_on_offset(ts) True