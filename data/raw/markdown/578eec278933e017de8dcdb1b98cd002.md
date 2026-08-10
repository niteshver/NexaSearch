# pandas.Period.minute#

- Period.minute#
- Get minute of the hour component of the Period. For periods with a frequency shorter than an hour, this returns the minute portion of the time. For longer frequencies, it returns 0. 
  - Returns:
    - int
    - The minute as an integer, between 0 and 59.
 See also 
  - `Period.hour`
  - Get the hour component of the Period.
  - `Period.second`
  - Get the second component of the Period.
 Examples >>> p = pd.Period("2018-03-11 13:03:12.050000") >>> p.minute 3