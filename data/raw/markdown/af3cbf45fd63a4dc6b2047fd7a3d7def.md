# pandas.api.typing.ExponentialMovingWindow.corr#

- 
ExponentialMovingWindow.corr(*other=None* ,*pairwise=None* ,*numeric_only=False* )[source]#
- Calculate the ewm (exponential weighted moment) sample correlation. The weighting is controlled by the `com` ,`span` ,`halflife` , or`alpha` parameter specified when calling`DataFrame.ewm()` or`Series.ewm()` .
  - Parameters:
    - **other** Series or DataFrame, optional
    - If not supplied then will default to self and produce pairwise output.
    - **pairwise** bool, default None
    - If False then only matching columns between self and other will be used and the output will be a DataFrame. If True then all pairwise combinations will be calculated and the output will be a MultiIndex DataFrame in the case of DataFrame inputs. In the case of missing elements, only complete pairwise observations will be used.
    - **numeric_only** bool, default False
    - Include only float, int, boolean columns.
  - Returns:
    - Series or DataFrame
    - Return type is the same as the original object with `np.float64` dtype.
 See also 
  - `Series.ewm`
  - Calling ewm with Series data.
  - `DataFrame.ewm`
  - Calling ewm with DataFrames.
  - `Series.corr`
  - Aggregating corr for Series.
  - `DataFrame.corr`
  - Aggregating corr for DataFrame.
 Examples >>> ser1 = pd.Series([1, 2, 3, 4]) >>> ser2 = pd.Series([10, 11, 13, 16]) >>> ser1.ewm(alpha=0.2).corr(ser2) 0 NaN 1 1.000000 2 0.982821 3 0.977802 dtype: float64