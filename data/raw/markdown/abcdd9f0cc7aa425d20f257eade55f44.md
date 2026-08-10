# pandas.errors.SpecificationError#

- exception pandas.errors.SpecificationError[source]#
- Exception raised by `agg` when the functions are ill-specified.The exception raised in two scenarios. The first way is calling `agg` on a
Dataframe or Series using a nested renamer (dict-of-dict).The second way is calling `agg` on a Dataframe with duplicated functions
names without assigning column name.See also 
  - `DataFrame.agg`
  - Aggregate using one or more operations over the specified axis.
  - `Series.agg`
  - Aggregate using one or more operations over the specified axis.
 Examples >>> df = pd.DataFrame({"A": [1, 1, 1, 2, 2], "B": range(5), "C": range(5)}) >>> df.groupby("A").B.agg({"foo": "count"}) ... # SpecificationError: nested renamer is not supported >>> df.groupby("A").agg({"B": {"foo": ["sum", "max"]}}) ... # SpecificationError: nested renamer is not supported >>> df.groupby("A").agg(["min", "min"]) ... # SpecificationError: nested renamer is not supported