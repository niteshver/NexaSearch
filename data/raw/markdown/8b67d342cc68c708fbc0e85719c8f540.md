# pandas.MultiIndex.drop#

- 
MultiIndex.drop(*codes* ,*level=None* ,*errors='raise'* )[source]#
- Make a new `pandas.MultiIndex` with the passed list of codes deleted.This method allows for the removal of specified labels from a MultiIndex. The labels to be removed can be provided as a list of tuples if no level is specified, or as a list of labels from a specific level if the level parameter is provided. This can be useful for refining the structure of a MultiIndex to fit specific requirements. 
  - Parameters:
    - **codes** array-like
    - Must be a list of tuples when `level` is not specified.
    - **level** int or level name, default None
    - Level from which the labels will be dropped.
    - **errors** str, default ‘raise’
    - If ‘ignore’, suppress error and existing labels are dropped.
  - Returns:
    - MultiIndex
    - A new MultiIndex with the specified labels removed.
 See also 
  - `MultiIndex.remove_unused_levels`
  - Create new MultiIndex from current that removes unused levels.
  - `MultiIndex.reorder_levels`
  - Rearrange levels using input order.
  - `MultiIndex.rename`
  - Rename levels in a MultiIndex.
 Examples >>> idx = pd.MultiIndex.from_product( ... [(0, 1, 2), ("green", "purple")], names=["number", "color"] ... ) >>> idx MultiIndex([(0, 'green'), (0, 'purple'), (1, 'green'), (1, 'purple'), (2, 'green'), (2, 'purple')], names=['number', 'color']) >>> idx.drop([(1, "green"), (2, "purple")]) MultiIndex([(0, 'green'), (0, 'purple'), (1, 'purple'), (2, 'green')], names=['number', 'color']) We can also drop from a specific level. >>> idx.drop("green", level="color") MultiIndex([(0, 'purple'), (1, 'purple'), (2, 'purple')], names=['number', 'color']) >>> idx.drop([1, 2], level=0) MultiIndex([(0, 'green'), (0, 'purple')], names=['number', 'color'])