# pandas.Index.argmax#

- 
Index.argmax(*axis=None* ,*skipna=True* ,**args* ,***kwargs* )[source]#
- Return int position of the largest value in the Index. If the maximum is achieved in multiple locations, the first row position is returned. 
  - Parameters:
    - **axis** None
    - Unused. Parameter needed for compatibility with DataFrame.
    - **skipna** bool, default True
    - Exclude NA/null values. If the entire Series is NA, or if `skipna=False` and there is an NA value, this method will raise a`ValueError` .
    - ***args, **kwargs**
    - Additional arguments and keywords for compatibility with NumPy.
  - Returns:
    - int
    - Row position of the maximum value.
 See also 
  - `Series.argmax`
  - Return position of the maximum value.
  - `Series.argmin`
  - Return position of the minimum value.
  - `numpy.ndarray.argmax`
  - Equivalent method for numpy arrays.
  - `Series.idxmax`
  - Return index label of the maximum values.
  - `Series.idxmin`
  - Return index label of the minimum values.
 Examples Consider dataset containing cereal calories >>> idx = pd.Index([100.0, 110.0, 120.0, 110.0]) >>> idx Index([100.0, 110.0, 120.0, 110.0], dtype='float64') >>> idx.argmax() np.int64(2) >>> idx.argmin() np.int64(0) The maximum cereal calories is the third element and the minimum cereal calories is the first element, since index is zero-indexed.