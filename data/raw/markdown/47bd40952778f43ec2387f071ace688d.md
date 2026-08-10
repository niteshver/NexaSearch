# pandas.Series.dt.is_year_start#

- Series.dt.is_year_start[source]#
- Indicate whether the date is the first day of a year. This boolean attribute evaluates to True if the date is January 1st, and False otherwise. 
  - Returns:
    - Series or DatetimeIndex
    - The same type as the original data with boolean values. Series will have the same name and index. DatetimeIndex will have the same name.
 See also 
  - `is_year_end`
  - Similar property indicating the last day of the year.
 Examples This method is available on Series with datetime values under the `.dt` accessor, and directly on DatetimeIndex.>>> dates = pd.Series(pd.date_range("2017-12-30", periods=3)) >>> dates 0 2017-12-30 1 2017-12-31 2 2018-01-01 dtype: datetime64[us] >>> dates.dt.is_year_start 0 False 1 False 2 True dtype: bool >>> idx = pd.date_range("2017-12-30", periods=3) >>> idx DatetimeIndex(['2017-12-30', '2017-12-31', '2018-01-01'], dtype='datetime64[us]', freq='D') >>> idx.is_year_start array([False, False, True]) This method, when applied to Series with datetime values under the `.dt` accessor, will lose information about Business offsets.>>> dates = pd.Series(pd.date_range("2020-10-30", periods=4, freq="BYS")) >>> dates 0 2021-01-01 1 2022-01-03 2 2023-01-02 3 2024-01-01 dtype: datetime64[us] >>> dates.dt.is_year_start 0 True 1 False 2 False 3 True dtype: bool >>> idx = pd.date_range("2020-10-30", periods=4, freq="BYS") >>> idx DatetimeIndex(['2021-01-01', '2022-01-03', '2023-01-02', '2024-01-01'], dtype='datetime64[us]', freq='BYS-JAN') >>> idx.is_year_start array([ True, True, True, True])