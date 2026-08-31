# pandas.api.typing.Rolling.skew#

- 
Rolling.skew(*numeric_only=False* )[source]#
- Calculate the rolling unbiased skewness. This is equivalent to applying `scipy.stats.skew` over each rolling
window. A minimum of three periods is required.
  - Parameters:
    - **numeric_only** bool, default False
    - Include only float, int, boolean columns.
  - Returns:
    - Series or DataFrame
    - Return type is the same as the original object with `np.float64` dtype.
 See also 
  - `scipy.stats.skew`
  - Third moment of a probability density.
  - `Series.rolling`
  - Calling rolling with Series data.
  - `DataFrame.rolling`
  - Calling rolling with DataFrames.
  - `Series.skew`
  - Aggregating skew for Series.
  - `DataFrame.skew`
  - Aggregating skew for DataFrame.
 Notes A minimum of three periods is required for the rolling calculation. Examples >>> ser = pd.Series([1, 5, 2, 7, 15, 6]) >>> ser.rolling(3).skew().round(6) 0 NaN 1 NaN 2 1.293343 3 -0.585583 4 0.670284 5 1.652317 dtype: float64