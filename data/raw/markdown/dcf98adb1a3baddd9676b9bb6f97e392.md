# pandas.Series.idxmax#

- 
Series.idxmax(*axis=0* ,*skipna=True* ,**args* ,***kwargs* )[source]#
- Return the row label of the maximum value. If multiple values equal the maximum, the first row label with that value is returned. 
  - Parameters:
    - **axis** {0 or ‘index’}
    - Unused. Parameter needed for compatibility with DataFrame.
    - **skipna** bool, default True
    - Exclude NA/null values. If the entire Series is NA, or if `skipna=False` and there is an NA value, this method will raise a`ValueError` .
    - ***args, **kwargs**
    - Additional arguments and keywords have no effect but might be accepted for compatibility with NumPy. See NumPy compatibility kwargs for more.
  - Returns:
    - Index
    - Label of the maximum value.
  - Raises:
    - ValueError
    - If the Series is empty.
 See also 
  - `numpy.argmax`
  - Return indices of the maximum values along the given axis.
  - `DataFrame.idxmax`
  - Return index of first occurrence of maximum over requested axis.
  - `Series.idxmin`
  - Return index *label* of the first occurrence of minimum of values.
 Notes This method is the Series version of `ndarray.argmax` . This method
returns the label of the maximum, while`ndarray.argmax` returns
the position. To get the position, use`series.values.argmax()` .Examples >>> s = pd.Series(data=[1, None, 4, 3, 4], index=["A", "B", "C", "D", "E"]) >>> s A 1.0 B NaN C 4.0 D 3.0 E 4.0 dtype: float64 >>> s.idxmax() 'C'