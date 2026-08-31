# pandas.Period.freqstr#

- Period.freqstr#
- Return a string representation of the frequency. This property provides the frequency string associated with the Period object. The frequency string describes the granularity of the time span represented by the Period. Common frequency strings include ‘D’ for daily, ‘M’ for monthly, ‘Y’ for yearly, etc. See also 
  - `Period.asfreq`
  - Convert Period to desired frequency, at the start or end of the interval.
  - `period_range`
  - Return a fixed frequency PeriodIndex.
 Examples >>> pd.Period('2020-01', 'D').freqstr 'D'