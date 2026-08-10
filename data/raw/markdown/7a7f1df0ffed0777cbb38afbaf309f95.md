# pandas.PeriodIndex.dayofyear#

- property PeriodIndex.dayofyear[source]#
- The ordinal day of the year. See also 
  - `PeriodIndex.day`
  - The days of the period.
  - `PeriodIndex.day_of_week`
  - The day of the week with Monday=0, Sunday=6.
  - `PeriodIndex.day_of_year`
  - The ordinal day of the year.
  - `PeriodIndex.dayofweek`
  - The day of the week with Monday=0, Sunday=6.
  - `PeriodIndex.dayofyear`
  - The ordinal day of the year.
  - `PeriodIndex.weekday`
  - The day of the week with Monday=0, Sunday=6.
  - `PeriodIndex.weekofyear`
  - The week ordinal of the year.
  - `PeriodIndex.year`
  - The year of the period.
 Examples >>> idx = pd.PeriodIndex(["2023-01-10", "2023-02-01", "2023-03-01"], freq="D") >>> idx.dayofyear Index([10, 32, 60], dtype='int64') >>> idx = pd.PeriodIndex(["2023", "2024", "2025"], freq="Y") >>> idx PeriodIndex(['2023', '2024', '2025'], dtype='period[Y-DEC]') >>> idx.dayofyear Index([365, 366, 365], dtype='int64')