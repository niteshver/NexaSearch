# What’s new in 1.3.4 (October 17, 2021)#

These are the changes in pandas 1.3.4. See Release notes for a full changelog including other versions of pandas.

## Fixed regressions#

- Fixed regression in `DataFrame.convert_dtypes()` incorrectly converts byte strings to strings (GH 43183)
- Fixed regression in `DataFrameGroupBy.agg()` and`SeriesGroupBy.agg()` were failing silently with mixed data types along`axis=1` and`MultiIndex` (GH 43209)
- Fixed regression in `merge()` with integer and`NaN` keys failing with`outer` merge (GH 43550)
- Fixed regression in `DataFrame.corr()` raising`ValueError` with`method="spearman"` on 32-bit platforms (GH 43588)
- Fixed performance regression in `MultiIndex.equals()` (GH 43549)
- Fixed performance regression in `DataFrameGroupBy.first()` ,`SeriesGroupBy.first()` ,`DataFrameGroupBy.last()` , and`SeriesGroupBy.last()` with`StringDtype` (GH 41596)
- Fixed regression in `Series.cat.reorder_categories()` failing to update the categories on the`Series` (GH 43232)
- Fixed regression in `Series.cat.categories()` setter failing to update the categories on the`Series` (GH 43334)
- Fixed regression in `read_csv()` raising`UnicodeDecodeError` exception when`memory_map=True` (GH 43540)
- Fixed regression in `DataFrame.explode()` raising`AssertionError` when`column` is any scalar which is not a string (GH 43314)
- Fixed regression in `Series.aggregate()` attempting to pass`args` and`kwargs` multiple times to the user supplied`func` in certain cases (GH 43357)
- Fixed regression when iterating over a `DataFrame.groupby.rolling` object causing the resulting DataFrames to have an incorrect index if the input groupings were not sorted (GH 43386)
- Fixed regression in `DataFrame.groupby.rolling.cov()` and`DataFrame.groupby.rolling.corr()` computing incorrect results if the input groupings were not sorted (GH 43386)

## Bug fixes#

- Fixed bug in `pandas.DataFrame.groupby.rolling()` and`pandas.api.indexers.FixedForwardWindowIndexer` leading to segfaults and window endpoints being mixed across groups (GH 43267)
- Fixed bug in `DataFrameGroupBy.mean()` and`SeriesGroupBy.mean()` with datetimelike values including`NaT` values returning incorrect results (GH 43132)
- Fixed bug in `Series.aggregate()` not passing the first`args` to the user supplied`func` in certain cases (GH 43357)
- Fixed memory leaks in `Series.rolling.quantile()` and`Series.rolling.median()` (GH 43339)

## Other#

- The minimum version of Cython needed to compile pandas is now `0.29.24` (GH 43729)

## Contributors#

A total of 17 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- Alexey Györi +
- DSM
- Irv Lustig
- Jeff Reback
- Julien de la Bruère-T +
- Matthew Zeitlin
- MeeseeksMachine
- Pandas Development Team
- Patrick Hoefler
- Richard Shadrach
- Shoham Debnath
- Simon Hawkins
- Thomas Li
- aptalca +
- jbrockmendel
- michal-gh +
- realead