# pandas.Timestamp.timestamp#

- Timestamp.timestamp()#
- Return POSIX timestamp as float. This method converts the Timestamp object to a POSIX timestamp, which is the number of seconds since the Unix epoch (January 1, 1970). The returned value is a floating-point number, where the integer part represents the seconds, and the fractional part represents the microseconds. 
  - Returns:
    - float
    - The POSIX timestamp representation of the Timestamp object.
 See also 
  - `Timestamp.fromtimestamp`
  - Construct a Timestamp from a POSIX timestamp.
  - `datetime.datetime.timestamp`
  - Equivalent method from the datetime module.
  - `Timestamp.to_pydatetime`
  - Convert the Timestamp to a datetime object.
  - `Timestamp.to_datetime64`
  - Converts Timestamp to numpy.datetime64.
 Examples >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548') >>> ts.timestamp() 1584199972.192548