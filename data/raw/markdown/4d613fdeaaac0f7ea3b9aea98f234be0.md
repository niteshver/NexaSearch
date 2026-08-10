# pandas.Series.ewm#

- 
Series.ewm(*com=None* ,*span=None* ,*halflife=None* ,*alpha=None* ,*min_periods=0* ,*adjust=True* ,*ignore_na=False* ,*times=None* ,*method='single'* )[source]#
- Provide exponentially weighted (EW) calculations. Exactly one of `com` ,`span` ,`halflife` , or`alpha` must be
provided if`times` is not provided. If`times` is provided and`adjust=True` ,`halflife` and one of`com` ,`span` or`alpha` may be provided.
If`times` is provided and`adjust=False` ,`halflife` must be the only provided decay-specification parameter.
  - Parameters:
    - **com** float, optional
    - Specify decay in terms of center of mass     - **span** float, optional
    - Specify decay in terms of span     - **halflife** float, str, timedelta, optional
    - Specify decay in terms of half-life If `times` is specified, a timedelta convertible unit over which an
observation decays to half its value. Only applicable to`mean()` ,
and halflife value will not apply to the other functions.
    - **alpha** float, optional
    - Specify smoothing factor     - **min_periods** int, default 0
    - Minimum number of observations in window required to have a value; otherwise, result is `np.nan` .
    - **adjust** bool, default True
    - Divide by decaying adjustment factor in beginning periods to account for imbalance in relative weightings (viewing EWMA as a moving average). 
      - When `adjust=True` (default), the EW function is calculated
using weights
 
      - When `adjust=False` , the exponentially weighted function is calculated
recursively:
    - **ignore_na** bool, default False
    - Ignore missing values when calculating weights. 
      - When `ignore_na=False` (default), weights are based on absolute
positions.
For example, the weights of`adjust=True` , and`adjust=False` .
      - When `ignore_na=True` , weights are based
on relative positions. For example, the weights of`adjust=True` , and`adjust=False` .
    - **times** np.ndarray, Series, default None
    - Only applicable to `mean()` .Times corresponding to the observations. Must be monotonically increasing and `datetime64[ns]` dtype.If 1-D array like, a sequence with the same shape as the observations.
    - **method** str {‘single’, ‘table’}, default ‘single’
    - Execute the rolling operation per single column or row ( `'single'` )
or over the entire object (`'table'` ).This argument is only implemented when specifying `engine='numba'` in the method call.Only applicable to `mean()`
  - Returns:
    - pandas.api.typing.ExponentialMovingWindow
    - An instance of ExponentialMovingWindow for further exponentially weighted (EW) calculations, e.g. using the `mean` method.
 Notes See Windowing Operations for further usage details and examples. Examples >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]}) >>> df B 0 0.0 1 1.0 2 2.0 3 NaN 4 4.0 >>> df.ewm(com=0.5).mean() B 0 0.000000 1 0.750000 2 1.615385 3 1.615385 4 3.670213 >>> df.ewm(alpha=2 / 3).mean() B 0 0.000000 1 0.750000 2 1.615385 3 1.615385 4 3.670213 **adjust**>>> df.ewm(com=0.5, adjust=True).mean() B 0 0.000000 1 0.750000 2 1.615385 3 1.615385 4 3.670213 >>> df.ewm(com=0.5, adjust=False).mean() B 0 0.000000 1 0.666667 2 1.555556 3 1.555556 4 3.650794 **ignore_na**>>> df.ewm(com=0.5, ignore_na=True).mean() B 0 0.000000 1 0.750000 2 1.615385 3 1.615385 4 3.225000 >>> df.ewm(com=0.5, ignore_na=False).mean() B 0 0.000000 1 0.750000 2 1.615385 3 1.615385 4 3.670213 **times**Exponentially weighted mean with weights calculated with a timedelta `halflife` relative to`times` .>>> times = ['2020-01-01', '2020-01-03', '2020-01-10', '2020-01-15', ... '2020-01-17'] >>> df.ewm(halflife='4 days', times=pd.DatetimeIndex(times)).mean() B 0 0.000000 1 0.585786 2 1.523889 3 1.523889 4 3.233686