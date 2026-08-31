# pandas.CategoricalIndex.reorder_categories#

- 
CategoricalIndex.reorder_categories(**args* ,***kwargs* )[source]#
- Reorder categories as specified in new_categories. `new_categories` need to include all old categories and no new category
items.
  - Parameters:
    - **new_categories** Index-like
    - The categories in new order.
    - **ordered** bool, optional
    - Whether or not the categorical is treated as a ordered categorical. If not given, do not change the ordered information.
  - Returns:
    - Categorical
    - Categorical with reordered categories.
  - Raises:
    - ValueError
    - If the new categories do not contain all old category items or any new ones
 See also 
  - `rename_categories`
  - Rename categories.
  - `add_categories`
  - Add new categories.
  - `remove_categories`
  - Remove the specified categories.
  - `remove_unused_categories`
  - Remove categories which are not used.
  - `set_categories`
  - Set the categories to the specified ones.
 Examples For `pandas.Series` :>>> ser = pd.Series(['a', 'b', 'c', 'a'], dtype='category') >>> ser = ser.cat.reorder_categories(['c', 'b', 'a'], ordered=True) >>> ser 0 a 1 b 2 c 3 a dtype: category Categories (3, object): ['c' < 'b' < 'a'] >>> ser.sort_values() 2 c 1 b 0 a 3 a dtype: category Categories (3, object): ['c' < 'b' < 'a'] For `pandas.CategoricalIndex` :>>> ci = pd.CategoricalIndex(['a', 'b', 'c', 'a']) >>> ci CategoricalIndex(['a', 'b', 'c', 'a'], categories=['a', 'b', 'c'], ordered=False, dtype='category') >>> ci.reorder_categories(['c', 'b', 'a'], ordered=True) CategoricalIndex(['a', 'b', 'c', 'a'], categories=['c', 'b', 'a'], ordered=True, dtype='category')