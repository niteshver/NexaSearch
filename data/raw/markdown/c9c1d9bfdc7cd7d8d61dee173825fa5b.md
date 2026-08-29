# pandas.DataFrame.ndim#

- property DataFrame.ndim[source]#
- Return an int representing the number of axes / array dimensions. Return 1 if Series. Otherwise return 2 if DataFrame. See also 
  - `numpy.ndarray.ndim`
  - Number of array dimensions.
 Examples >>> s = pd.Series({"a": 1, "b": 2, "c": 3}) >>> s.ndim 1 >>> df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}) >>> df.ndim 2