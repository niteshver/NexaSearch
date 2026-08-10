# pandas.tseries.offsets.HalfYearEnd.is_year_start#

- 
HalfYearEnd.is_year_start(*ts* )#
- Return boolean whether a timestamp occurs on the year start. This method checks if the given timestamp falls on January 1st, which marks the beginning of a calendar year. 
  - Parameters:
    - **ts** Timestamp
    - The timestamp to check.
 See also 
  - `is_year_end`
  - Return boolean whether a timestamp occurs on the year end.
 Examples >>> ts = pd.Timestamp(2022, 1, 1) >>> freq = pd.offsets.Hour(5) >>> freq.is_year_start(ts) True