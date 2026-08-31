# GroupBy#

GroupBy objects are returned by groupby calls: `pandas.DataFrame.groupby()`, `pandas.Series.groupby()`, etc.

## Indexing, iteration#

| `DataFrameGroupBy.__iter__` () | Groupby iterator. | 
| `SeriesGroupBy.__iter__` () | Groupby iterator. | 
| `DataFrameGroupBy.groups` | Dict {group name -> group labels}. | 
| `SeriesGroupBy.groups` | Dict {group name -> group labels}. | 
| `DataFrameGroupBy.indices` | Dict {group name -> group indices}. | 
| `SeriesGroupBy.indices` | Dict {group name -> group indices}. | 
| `DataFrameGroupBy.get_group` (name[, obj]) | Construct DataFrame from group with provided name. | 
| `SeriesGroupBy.get_group` (name[, obj]) | Construct DataFrame from group with provided name. | 

| `Grouper` (*args, **kwargs) | A Grouper allows the user to specify a groupby instruction for an object. | 

## Function application helper#

| `NamedAgg` (column, aggfunc) | Helper for column specific aggregation with control over output column names. | 

## Function application#

| `SeriesGroupBy.apply` (func, *args, **kwargs) | Apply function `func` group-wise and combine the results together. | 
| `DataFrameGroupBy.apply` (func, *args, **kwargs) | Apply function `func` group-wise and combine the results together. | 
| `SeriesGroupBy.agg` ([func, engine, engine_kwargs]) | Aggregate using one or more operations over the specified axis. | 
| `DataFrameGroupBy.agg` ([func, engine, ...]) | Aggregate using one or more operations over the specified axis. | 
| `SeriesGroupBy.aggregate` ([func, engine, ...]) | Aggregate using one or more operations over the specified axis. | 
| `DataFrameGroupBy.aggregate` ([func, engine, ...]) | Aggregate using one or more operations over the specified axis. | 
| `SeriesGroupBy.transform` (func, *args[, ...]) | Call function producing a same-indexed Series on each group. | 
| `DataFrameGroupBy.transform` (func, *args[, ...]) | Call function producing a same-indexed DataFrame on each group. | 
| `SeriesGroupBy.pipe` (func, *args, **kwargs) | Apply a `func` with arguments to this GroupBy object and return its result. | 
| `DataFrameGroupBy.pipe` (func, *args, **kwargs) | Apply a `func` with arguments to this GroupBy object and return its result. | 
| `DataFrameGroupBy.filter` (func[, dropna]) | Filter elements from groups that don't satisfy a criterion. | 
| `SeriesGroupBy.filter` (func[, dropna]) | Filter elements from groups that don't satisfy a criterion. | 

## `DataFrameGroupBy` computations / descriptive stats#

| `DataFrameGroupBy.all` ([skipna]) | Return True if all values in the group are truthful, else False. | 
| `DataFrameGroupBy.any` ([skipna]) | Return True if any value in the group is truthful, else False. | 
| `DataFrameGroupBy.bfill` ([limit]) | Backward fill the values. | 
| `DataFrameGroupBy.corr` ([method, min_periods, ...]) | Compute pairwise correlation of columns, excluding NA/null values. | 
| `DataFrameGroupBy.corrwith` (other[, axis, ...]) | Compute pairwise correlation. | 
| `DataFrameGroupBy.count` () | Compute count of group, excluding missing values. | 
| `DataFrameGroupBy.cov` ([min_periods, ddof, ...]) | Compute pairwise covariance of columns, excluding NA/null values. | 
| `DataFrameGroupBy.cumcount` ([ascending]) | Number each item in each group from 0 to the length of that group - 1. | 
| `DataFrameGroupBy.cummax` ([axis, numeric_only]) | Cumulative max for each group. | 
| `DataFrameGroupBy.cummin` ([axis, numeric_only]) | Cumulative min for each group. | 
| `DataFrameGroupBy.cumprod` ([axis]) | Cumulative product for each group. | 
| `DataFrameGroupBy.cumsum` ([axis]) | Cumulative sum for each group. | 
| `DataFrameGroupBy.describe` ([percentiles, ...]) | Generate descriptive statistics. | 
| `DataFrameGroupBy.diff` ([periods, axis]) | First discrete difference of element. | 
| `DataFrameGroupBy.ffill` ([limit]) | Forward fill the values. | 
| `DataFrameGroupBy.fillna` ([value, method, ...]) | Fill NA/NaN values using the specified method within groups. | 
| `DataFrameGroupBy.first` ([numeric_only, min_count]) | Compute the first non-null entry of each column. | 
| `DataFrameGroupBy.head` ([n]) | Return first n rows of each group. | 
| `DataFrameGroupBy.idxmax` ([axis, skipna, ...]) | Return index of first occurrence of maximum over requested axis. | 
| `DataFrameGroupBy.idxmin` ([axis, skipna, ...]) | Return index of first occurrence of minimum over requested axis. | 
| `DataFrameGroupBy.last` ([numeric_only, min_count]) | Compute the last non-null entry of each column. | 
| `DataFrameGroupBy.max` ([numeric_only, ...]) | Compute max of group values. | 
| `DataFrameGroupBy.mean` ([numeric_only, ...]) | Compute mean of groups, excluding missing values. | 
| `DataFrameGroupBy.median` ([numeric_only]) | Compute median of groups, excluding missing values. | 
| `DataFrameGroupBy.min` ([numeric_only, ...]) | Compute min of group values. | 
| `DataFrameGroupBy.ngroup` ([ascending]) | Number each group from 0 to the number of groups - 1. | 
| `DataFrameGroupBy.nth` | Take the nth row from each group if n is an int, otherwise a subset of rows. | 
| `DataFrameGroupBy.nunique` ([dropna]) | Return DataFrame with counts of unique elements in each position. | 
| `DataFrameGroupBy.ohlc` () | Compute open, high, low and close values of a group, excluding missing values. | 
| `DataFrameGroupBy.pct_change` ([periods, ...]) | Calculate pct_change of each value to previous entry in group. | 
| `DataFrameGroupBy.prod` ([numeric_only, min_count]) | Compute prod of group values. | 
| `DataFrameGroupBy.quantile` ([q, ...]) | Return group values at the given quantile, a la numpy.percentile. | 
| `DataFrameGroupBy.rank` ([method, ascending, ...]) | Provide the rank of values within each group. | 
| `DataFrameGroupBy.resample` (rule, *args, **kwargs) | Provide resampling when using a TimeGrouper. | 
| `DataFrameGroupBy.rolling` (*args, **kwargs) | Return a rolling grouper, providing rolling functionality per group. | 
| `DataFrameGroupBy.sample` ([n, frac, replace, ...]) | Return a random sample of items from each group. | 
| `DataFrameGroupBy.sem` ([ddof, numeric_only]) | Compute standard error of the mean of groups, excluding missing values. | 
| `DataFrameGroupBy.shift` ([periods, freq, ...]) | Shift each group by periods observations. | 
| `DataFrameGroupBy.size` () | Compute group sizes. | 
| `DataFrameGroupBy.skew` ([axis, skipna, ...]) | Return unbiased skew within groups. | 
| `DataFrameGroupBy.std` ([ddof, engine, ...]) | Compute standard deviation of groups, excluding missing values. | 
| `DataFrameGroupBy.sum` ([numeric_only, ...]) | Compute sum of group values. | 
| `DataFrameGroupBy.var` ([ddof, engine, ...]) | Compute variance of groups, excluding missing values. | 
| `DataFrameGroupBy.tail` ([n]) | Return last n rows of each group. | 
| `DataFrameGroupBy.take` (indices[, axis]) | Return the elements in the given *positional* indices in each group. | 
| `DataFrameGroupBy.value_counts` ([subset, ...]) | Return a Series or DataFrame containing counts of unique rows. | 

## `SeriesGroupBy` computations / descriptive stats#

| `SeriesGroupBy.all` ([skipna]) | Return True if all values in the group are truthful, else False. | 
| `SeriesGroupBy.any` ([skipna]) | Return True if any value in the group is truthful, else False. | 
| `SeriesGroupBy.bfill` ([limit]) | Backward fill the values. | 
| `SeriesGroupBy.corr` (other[, method, min_periods]) | Compute correlation with other Series, excluding missing values. | 
| `SeriesGroupBy.count` () | Compute count of group, excluding missing values. | 
| `SeriesGroupBy.cov` (other[, min_periods, ddof]) | Compute covariance with Series, excluding missing values. | 
| `SeriesGroupBy.cumcount` ([ascending]) | Number each item in each group from 0 to the length of that group - 1. | 
| `SeriesGroupBy.cummax` ([axis, numeric_only]) | Cumulative max for each group. | 
| `SeriesGroupBy.cummin` ([axis, numeric_only]) | Cumulative min for each group. | 
| `SeriesGroupBy.cumprod` ([axis]) | Cumulative product for each group. | 
| `SeriesGroupBy.cumsum` ([axis]) | Cumulative sum for each group. | 
| `SeriesGroupBy.describe` (**kwargs) | Generate descriptive statistics. | 
| `SeriesGroupBy.diff` ([periods, axis]) | First discrete difference of element. | 
| `SeriesGroupBy.ffill` ([limit]) | Forward fill the values. | 
| `SeriesGroupBy.fillna` ([value, method, axis, ...]) | Fill NA/NaN values using the specified method within groups. | 
| `SeriesGroupBy.first` ([numeric_only, min_count]) | Compute the first non-null entry of each column. | 
| `SeriesGroupBy.head` ([n]) | Return first n rows of each group. | 
| `SeriesGroupBy.last` ([numeric_only, min_count]) | Compute the last non-null entry of each column. | 
| `SeriesGroupBy.idxmax` ([axis, skipna]) | Return the row label of the maximum value. | 
| `SeriesGroupBy.idxmin` ([axis, skipna]) | Return the row label of the minimum value. | 
| `SeriesGroupBy.is_monotonic_increasing` | Return boolean if values in the object are monotonically increasing. | 
| `SeriesGroupBy.is_monotonic_decreasing` | Return boolean if values in the object are monotonically decreasing. | 
| `SeriesGroupBy.max` ([numeric_only, min_count, ...]) | Compute max of group values. | 
| `SeriesGroupBy.mean` ([numeric_only, engine, ...]) | Compute mean of groups, excluding missing values. | 
| `SeriesGroupBy.median` ([numeric_only]) | Compute median of groups, excluding missing values. | 
| `SeriesGroupBy.min` ([numeric_only, min_count, ...]) | Compute min of group values. | 
| `SeriesGroupBy.ngroup` ([ascending]) | Number each group from 0 to the number of groups - 1. | 
| `SeriesGroupBy.nlargest` ([n, keep]) | Return the largest n elements. | 
| `SeriesGroupBy.nsmallest` ([n, keep]) | Return the smallest n elements. | 
| `SeriesGroupBy.nth` | Take the nth row from each group if n is an int, otherwise a subset of rows. | 
| `SeriesGroupBy.nunique` ([dropna]) | Return number of unique elements in the group. | 
| `SeriesGroupBy.unique` () | Return unique values of Series object. | 
| `SeriesGroupBy.ohlc` () | Compute open, high, low and close values of a group, excluding missing values. | 
| `SeriesGroupBy.pct_change` ([periods, ...]) | Calculate pct_change of each value to previous entry in group. | 
| `SeriesGroupBy.prod` ([numeric_only, min_count]) | Compute prod of group values. | 
| `SeriesGroupBy.quantile` ([q, interpolation, ...]) | Return group values at the given quantile, a la numpy.percentile. | 
| `SeriesGroupBy.rank` ([method, ascending, ...]) | Provide the rank of values within each group. | 
| `SeriesGroupBy.resample` (rule, *args, **kwargs) | Provide resampling when using a TimeGrouper. | 
| `SeriesGroupBy.rolling` (*args, **kwargs) | Return a rolling grouper, providing rolling functionality per group. | 
| `SeriesGroupBy.sample` ([n, frac, replace, ...]) | Return a random sample of items from each group. | 
| `SeriesGroupBy.sem` ([ddof, numeric_only]) | Compute standard error of the mean of groups, excluding missing values. | 
| `SeriesGroupBy.shift` ([periods, freq, axis, ...]) | Shift each group by periods observations. | 
| `SeriesGroupBy.size` () | Compute group sizes. | 
| `SeriesGroupBy.skew` ([axis, skipna, numeric_only]) | Return unbiased skew within groups. | 
| `SeriesGroupBy.std` ([ddof, engine, ...]) | Compute standard deviation of groups, excluding missing values. | 
| `SeriesGroupBy.sum` ([numeric_only, min_count, ...]) | Compute sum of group values. | 
| `SeriesGroupBy.var` ([ddof, engine, ...]) | Compute variance of groups, excluding missing values. | 
| `SeriesGroupBy.tail` ([n]) | Return last n rows of each group. | 
| `SeriesGroupBy.take` (indices[, axis]) | Return the elements in the given *positional* indices in each group. | 
| `SeriesGroupBy.value_counts` ([normalize, ...]) |  | 

## Plotting and visualization#

| `DataFrameGroupBy.boxplot` ([subplots, column, ...]) | Make box plots from DataFrameGroupBy data. | 
| `DataFrameGroupBy.hist` ([column, by, grid, ...]) | Make a histogram of the DataFrame's columns. | 
| `SeriesGroupBy.hist` ([by, ax, grid, ...]) | Draw histogram of the input series using matplotlib. | 
| `DataFrameGroupBy.plot` | Make plots of Series or DataFrame. | 
| `SeriesGroupBy.plot` | Make plots of Series or DataFrame. |