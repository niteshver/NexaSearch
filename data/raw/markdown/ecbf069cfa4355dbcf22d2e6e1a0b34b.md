# pandas.tseries.holiday.nearest_workday#

- 
pandas.tseries.holiday.nearest_workday(*dt* )[source]#
- Move Saturday to Friday and Sunday to Monday. Most US federal holidays follow this rule. 
  - Parameters:
    - **dt** datetime
    - The date the holiday falls on.
  - Returns:
    - datetime
    - The date the holiday is observed on.
 See also 
  - `tseries.holiday.before_nearest_workday`
  - Move to the workday before the nearest workday.
  - `tseries.holiday.after_nearest_workday`
  - Move to the workday after the nearest workday.
  - `tseries.holiday.USFederalHolidayCalendar`
  - US Federal Government holiday calendar.
 Examples >>> from datetime import datetime >>> from pandas.tseries.holiday import nearest_workday >>> nearest_workday(datetime(2022, 1, 1)) # Saturday datetime.datetime(2021, 12, 31, 0, 0) >>> nearest_workday(datetime(2022, 1, 2)) # Sunday datetime.datetime(2022, 1, 3, 0, 0)