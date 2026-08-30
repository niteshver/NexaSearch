# What’s new in 1.0.1 (February 5, 2020)#

These are the changes in pandas 1.0.1. See Release notes for a full changelog including other versions of pandas.

## Fixed regressions#

- Fixed regression in `DataFrame` setting values with a slice (e.g.`df[-4:] = 1` ) indexing by label instead of position (GH 31469)
- Fixed regression when indexing a `Series` or`DataFrame` indexed by`DatetimeIndex` with a slice containing a`datetime.date` (GH 31501)
- Fixed regression in `DataFrame.__setitem__` raising an`AttributeError` with a`MultiIndex` and a non-monotonic indexer (GH 31449)
- Fixed regression in `Series` multiplication when multiplying a numeric`Series` with >10000 elements with a timedelta-like scalar (GH 31457)
- Fixed regression in `.groupby().agg()` raising an`AssertionError` for some reductions like`min` on object-dtype columns (GH 31522)
- Fixed regression in `.groupby()` aggregations with categorical dtype using Cythonized reduction functions (e.g.`first` ) (GH 31450)
- Fixed regression in `DataFrameGroupBy.apply()` and`SeriesGroupBy.apply()` if called with a function which returned a non-pandas non-scalar object (e.g. a list or numpy array) (GH 31441)
- Fixed regression in `DataFrame.groupby()` whereby taking the minimum or maximum of a column with period dtype would raise a`TypeError` . (GH 31471)
- Fixed regression in `DataFrame.groupby()` with an empty DataFrame grouping by a level of a MultiIndex (GH 31670).
- Fixed regression in `DataFrame.apply()` with object dtype and non-reducing function (GH 31505)
- Fixed regression in `to_datetime()` when parsing non-nanosecond resolution datetimes (GH 31491)
- Fixed regression in `to_csv()` where specifying an`na_rep` might truncate the values written (GH 31447)
- Fixed regression in `Categorical` construction with`numpy.str_` categories (GH 31499)
- Fixed regression in `DataFrame.loc()` and`DataFrame.iloc()` when selecting a row containing a single`datetime64` or`timedelta64` column (GH 31649)
- Fixed regression where setting `pd.options.display.max_colwidth` was not accepting negative integer. In addition, this behavior has been deprecated in favor of using`None` (GH 31532)
- Fixed regression in objTOJSON.c fix return-type warning (GH 31463)
- Fixed regression in `qcut()` when passed a nullable integer. (GH 31389)
- Fixed regression in assigning to a `Series` using a nullable integer dtype (GH 31446)
- Fixed performance regression when indexing a `DataFrame` or`Series` with a`MultiIndex` for the index using a list of labels (GH 31648)
- Fixed regression in `read_csv()` used in file like object`RawIOBase` is not recognize`encoding` option (GH 31575)

## Deprecations#

- Support for negative integer for `pd.options.display.max_colwidth` is deprecated in favor of using`None` (GH 31532)

## Bug fixes#

**Datetimelike**

- Fixed bug in `to_datetime()` raising when`cache=True` and out-of-bound values are present (GH 31491)

**Numeric**

- Bug in dtypes being lost in `DataFrame.__invert__` (`~` operator) with mixed dtypes (GH 31183)
and for extension-array backed`Series` and`DataFrame` (GH 23087)

**Plotting**

- Plotting tz-aware timeseries no longer gives UserWarning (GH 31205)

**Interval**

- Bug in `Series.shift()` with`interval` dtype raising a`TypeError` when shifting an interval array of integers or datetimes (GH 34195)

## Contributors#

A total of 15 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- Daniel Saxton
- Guillaume Lemaitre
- Jeff Reback
- Joris Van den Bossche
- Kaiqi Dong
- Marco Gorelli
- MeeseeksMachine
- Pandas Development Team
- Sebastián Vanrell +
- Tom Augspurger
- William Ayd
- alimcmaster1
- jbrockmendel
- paihu +
- proost