# pandas.DataFrame.keys#

- DataFrame.keys()[source]#
- Get the ‘info axis’ (see Indexing for more). This is index for Series, columns for DataFrame. 
  - Returns:
    - Index
    - Info axis.
 See also 
  - `DataFrame.index`
  - The index (row labels) of the DataFrame.
  - `DataFrame.columns`
  - The column labels of the DataFrame.
 Examples >>> d = pd.DataFrame( ... data={"A": [1, 2, 3], "B": [0, 4, 8]}, index=["a", "b", "c"] ... ) >>> d A B a 1 0 b 2 4 c 3 8 >>> d.keys() Index(['A', 'B'], dtype='str')