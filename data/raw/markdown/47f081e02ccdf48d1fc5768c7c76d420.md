# pandas.CategoricalIndex.add_categories#

- 
CategoricalIndex.add_categories(*new_categories* )[source]#
- Add new categories. new_categories will be included at the last/highest place in the categories and will be unused directly after this call. 
  - Parameters:
    - **new_categories** category or list-like of category
    - The new categories to be included.
  - Returns:
    - Categorical
    - Categorical with new categories added.
  - Raises:
    - ValueError
    - If the new categories include old categories or do not validate as categories
 See also 
  - `rename_categories`
  - Rename categories.
  - `reorder_categories`
  - Reorder categories.
  - `remove_categories`
  - Remove the specified categories.
  - `remove_unused_categories`
  - Remove categories which are not used.
  - `set_categories`
  - Set the categories to the specified ones.
 Examples >>> c = pd.Categorical(["c", "b", "c"]) >>> c ['c', 'b', 'c'] Categories (2, str): ['b', 'c'] >>> c.add_categories(["d", "a"]) ['c', 'b', 'c'] Categories (4, str): ['b', 'c', 'd', 'a']