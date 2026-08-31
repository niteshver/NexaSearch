# pandas.DatetimeIndex.to_series#

- 
DatetimeIndex.to_series(*index=None* ,*name=None* )[source]#
- Create a Series with both index and values equal to the index keys. Useful with map for returning an indexer based on an index. 
  - Parameters:
    - **index** Index, optional
    - Index of resulting Series. If None, defaults to original index.
    - **name** str, optional
    - Name of resulting Series. If None, defaults to name of original index.
  - Returns:
    - Series
    - The dtype will be based on the type of the Index values.
 See also 
  - `Index.to_frame`
  - Convert an Index to a DataFrame.
  - `Series.to_frame`
  - Convert Series to DataFrame.
 Examples >>> idx = pd.Index(['Ant', 'Bear', 'Cow'], name='animal') By default, the original index and original name is reused. >>> idx.to_series() animal Ant Ant Bear Bear Cow Cow Name: animal, dtype: object To enforce a new index, specify new labels to `index` :>>> idx.to_series(index=[0, 1, 2]) 0 Ant 1 Bear 2 Cow Name: animal, dtype: object To override the name of the resulting column, specify `name` :>>> idx.to_series(name='zoo') animal Ant Ant Bear Bear Cow Cow Name: zoo, dtype: object