# pandas.Index.get_indexer_non_unique#

- 
Index.get_indexer_non_unique(*target* )[source]#
- Compute indexer and mask for new index given the current index. The indexer should be then used as an input to ndarray.take to align the current data to the new index. 
  - Parameters
    - **target** Index
  - Returns
    - **indexer** np.ndarray[np.intp]
    - Integers from 0 to n - 1 indicating that the index at these positions matches the corresponding target values. Missing values in the target are marked by -1.
    - **missing** np.ndarray[np.intp]
    - An indexer into the target of the values not found. These correspond to the -1 in the indexer array.