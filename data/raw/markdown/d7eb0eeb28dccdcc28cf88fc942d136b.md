# pandas.api.typing.SeriesGroupBy.apply#

- 
SeriesGroupBy.apply(*func* ,**args* ,***kwargs* )[source]#
- Apply function `func` group-wise and combine the results together.The function passed to `apply` must take a series as its first
argument and return a DataFrame, Series or scalar.`apply` will
then take care of combining the results back together into a single
dataframe or series.`apply` is therefore a highly flexible
grouping method.While `apply` is a very flexible method, its downside is that
using it can be quite a bit slower than using more specific methods
like`agg` or`transform` . Pandas offers a wide range of method that will
be much faster than using`apply` for their specific purposes, so try to
use them before reaching for`apply` .
  - Parameters:
    - **func** callable
    - A callable that takes a series as its first argument, and returns a dataframe, a series or a scalar. In addition the callable may take positional and keyword arguments.
    - ***args** tuple
    - Optional positional arguments to pass to `func` .
    - ****kwargs** dict
    - Optional keyword arguments to pass to `func` .
  - Returns:
    - Series or DataFrame
    - A pandas object with the result of applying `func` to each group.
 See also 
  - `pipe`
  - Apply function to the full GroupBy object instead of to each group.
  - `aggregate`
  - Apply aggregate function to the GroupBy object.
  - `transform`
  - Apply function column-by-column to the GroupBy object.
  - `Series.apply`
  - Apply a function to a Series.
  - `DataFrame.apply`
  - Apply a function to each row or column of a DataFrame.
 Notes See Flexible apply in the User Guide for more details and examples. The resulting dtype will reflect the return value of the passed `func` ,
see the examples below.Functions that mutate the passed object can produce unexpected behavior or errors and are not supported. See Mutating with User Defined Function (UDF) methods for more details. Each group passed to `func` has a`name` attribute set to the group
key (the value of the grouping for that group). This is useful for
identifying the current group, as in the examples below.Examples >>> s = pd.Series([0, 1, 2], index="a a b".split()) >>> g1 = s.groupby(s.index, group_keys=False) >>> g2 = s.groupby(s.index, group_keys=True) From `s` above we can see that`g` has two groups,`a` and`b` .
Notice that`g1` have`g2` have two groups,`a` and`b` , and only
differ in their`group_keys` argument. Calling apply in various ways,
we can get different grouping results:Example 1: The function passed to apply takes a Series as its argument and returns a Series. apply combines the result for each group together into a new Series. The resulting dtype will reflect the return value of the passed `func` .>>> g1.apply(lambda x: x * 2 if x.name == "a" else x / 2) a 0.0 a 2.0 b 1.0 dtype: float64 In the above, the groups are not part of the index. We can have them included by using `g2` where`group_keys=True` :>>> g2.apply(lambda x: x * 2 if x.name == "a" else x / 2) a a 0.0 a 2.0 b b 1.0 dtype: float64 Example 2: The function passed to apply takes a Series as its argument and returns a scalar. apply combines the result for each group together into a Series, including setting the index as appropriate: >>> g1.apply(lambda x: x.max() - x.min()) a 1 b 0 dtype: int64 The `group_keys` argument has no effect here because the result is not
like-indexed (i.e. a transform) when compared
to the input.>>> g2.apply(lambda x: x.max() - x.min()) a 1 b 0 dtype: int64