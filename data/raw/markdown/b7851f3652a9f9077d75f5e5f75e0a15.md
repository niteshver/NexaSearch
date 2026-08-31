# pandas.CategoricalIndex.equals#

- 
CategoricalIndex.equals(*other* )[source]#
- Determine if two CategoricalIndex objects contain the same elements. 
  - Returns:
    - bool
    - `True` if two`pandas.CategoricalIndex` objects have equal
elements,`False` otherwise.
 Examples >>> ci = pd.CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c']) >>> ci2 = pd.CategoricalIndex(pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])) >>> ci.equals(ci2) True The order of elements matters. >>> ci3 = pd.CategoricalIndex(['c', 'b', 'a', 'a', 'b', 'c']) >>> ci.equals(ci3) False The orderedness also matters. >>> ci4 = ci.as_ordered() >>> ci.equals(ci4) False The categories matter, but the order of the categories matters only when `ordered=True` .>>> ci5 = ci.set_categories(['a', 'b', 'c', 'd']) >>> ci.equals(ci5) False >>> ci6 = ci.set_categories(['b', 'c', 'a']) >>> ci.equals(ci6) True >>> ci_ordered = pd.CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c'], ... ordered=True) >>> ci2_ordered = ci_ordered.set_categories(['b', 'c', 'a']) >>> ci_ordered.equals(ci2_ordered) False