# pandas.tseries.api.guess_datetime_format#

- 
pandas.tseries.api.guess_datetime_format(*dt_str* ,*dayfirst=False* )#
- Guess the datetime format of a given datetime string. This function attempts to deduce the format of a given datetime string. It is useful for situations where the datetime format is unknown and needs to be determined for proper parsing. The function is not guaranteed to return a format. 
  - Parameters:
    - **dt_str** str
    - Datetime string to guess the format of.
    - **dayfirst** bool, default False
    - If True parses dates with the day first, eg 20/01/2005 Warning dayfirst=True is not strict, but will prefer to parse with day first (this is a known bug).
  - Returns:
    - **str or None** ret
    - datetime format string (for strftime or strptime), or None if it can’t be guessed.
 See also 
  - `to_datetime`
  - Convert argument to datetime.
  - `Timestamp`
  - Pandas replacement for python datetime.datetime object.
  - `DatetimeIndex`
  - Immutable ndarray-like of datetime64 data.
 Examples >>> from pandas.tseries.api import guess_datetime_format >>> guess_datetime_format('09/13/2023') '%m/%d/%Y' >>> guess_datetime_format('2023|September|13')