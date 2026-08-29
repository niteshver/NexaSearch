# pandas.Series.le#

- 
Series.le(*other* ,*level=None* ,*fill_value=None* ,*axis=0* )[source]#
- Return Less than or equal to of series and other, element-wise (binary operator le). Equivalent to `series <= other` , but with support to substitute a fill_value for
missing data in either one of the inputs.
  - Parameters:
    - **other** Series or scalar value
    - **level** int or name
    - Broadcast across a level, matching Index values on the passed MultiIndex level.
    - **fill_value** None or float value, default None (NaN)
    - Fill existing missing (NaN) values, and any new element needed for successful Series alignment, with this value before computation. If data in both corresponding Series locations is missing the result of filling (at that location) will be missing.
    - **axis** {0 or ‘index’}
    - Unused. Parameter needed for compatibility with DataFrame.
  - Returns:
    - Series
    - The result of the operation.
 Examples >>> a = pd.Series([1, 1, 1, np.nan, 1], index=['a', 'b', 'c', 'd', 'e']) >>> a a 1.0 b 1.0 c 1.0 d NaN e 1.0 dtype: float64 >>> b = pd.Series([0, 1, 2, np.nan, 1], index=['a', 'b', 'c', 'd', 'f']) >>> b a 0.0 b 1.0 c 2.0 d NaN f 1.0 dtype: float64 >>> a.le(b, fill_value=0) a False b True c True d False e False f True dtype: bool