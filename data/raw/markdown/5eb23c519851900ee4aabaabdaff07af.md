# pandas.PeriodIndex.week#

- property PeriodIndex.week[source]#
- The week ordinal of the year. See also 
  - `PeriodIndex.day_of_week`
  - The day of the week with Monday=0, Sunday=6.
  - `PeriodIndex.dayofweek`
  - The day of the week with Monday=0, Sunday=6.
  - `PeriodIndex.week`
  - The week ordinal of the year.
  - `PeriodIndex.weekday`
  - The day of the week with Monday=0, Sunday=6.
  - `PeriodIndex.year`
  - The year of the period.
 Examples >>> idx = pd.PeriodIndex(["2023-01", "2023-02", "2023-03"], freq="M") >>> idx.week # It can be written `weekofyear` Index([5, 9, 13], dtype='int64')