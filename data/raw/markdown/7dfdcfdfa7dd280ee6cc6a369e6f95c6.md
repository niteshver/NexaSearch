# pandas.tseries.holiday.USFederalHolidayCalendar#

- 
class pandas.tseries.holiday.USFederalHolidayCalendar(*name=''* ,*rules=None* )[source]#
- US Federal Government holiday calendar. The rules follow the federal holiday schedule published by the US Office of Personnel Management: https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/ Holidays that land on a weekend are observed on the nearest weekday. Pass an instance as the `calendar` argument of`CustomBusinessDay` to skip these dates
in business day arithmetic.
  - Parameters:
    - **name** str
    - Name of the holiday calendar, defaults to class name.
    - **rules** array of Holiday objects
    - A set of rules used to create the holidays.
 See also 
  - `tseries.holiday.AbstractHolidayCalendar`
  - Abstract interface to create holidays following certain rules.
  - `tseries.holiday.nearest_workday`
  - Move Saturday to Friday and Sunday to Monday.
  - `tseries.holiday.get_calendar`
  - Return an instance of a calendar based on its name.
 Examples >>> from pandas.tseries.holiday import USFederalHolidayCalendar >>> USFederalHolidayCalendar().holidays(start="2024-06-01", end="2024-07-31") DatetimeIndex(['2024-06-19', '2024-07-04'], dtype='datetime64[us]', freq=None) Attributes `end_date``rules``start_date`Methods `holidays` ([start, end, return_name])Return a curve with holidays between start_date and end_date. `merge` (other[, inplace])Merge holiday calendars together. `merge_class` (base, other)Merge holiday calendars together. `rule_from_name` (name)Return the rule for the holiday with the given name.