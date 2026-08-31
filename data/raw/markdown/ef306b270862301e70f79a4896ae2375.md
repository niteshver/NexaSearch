# pandas.Period.month#

- Period.month#
- Return the month this Period falls on. Months are numbered from 1 (January) through 12 (December). 
  - Returns:
    - int
 See also 
  - `period.week`
  - Get the week of the year on the given Period.
  - `Period.year`
  - Return the year this Period falls on.
  - `Period.day`
  - Return the day of the month this Period falls on.
 Notes The month is based on the ordinal and base attributes of the Period. Examples Create a Period object for January 2022 and get the month: >>> period = pd.Period('2022-01', 'M') >>> period.month 1 Period object with no specified frequency, resulting in a default frequency: >>> period = pd.Period('2022', 'Y') >>> period.month 12 Create a Period object with a specified frequency but an incomplete date string: >>> period = pd.Period('2022', 'M') >>> period.month 1 Handle a case where the Period object is empty, which results in NaN: >>> period = pd.Period('nan', 'M') >>> period.month nan