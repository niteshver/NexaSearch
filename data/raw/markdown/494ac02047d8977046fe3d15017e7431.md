# What’s new in 1.3.2 (August 15, 2021)#

These are the changes in pandas 1.3.2. See Release notes for a full changelog including other versions of pandas.

## Fixed regressions#

- Performance regression in `DataFrame.isin()` and`Series.isin()` for nullable data types (GH 42714)
- Regression in updating values of `Series` using boolean index, created by using`DataFrame.pop()` (GH 42530)
- Regression in `DataFrame.from_records()` with empty records (GH 42456)
- Fixed regression in `DataFrame.shift()` where`TypeError` occurred when shifting DataFrame created by concatenation of slices and fills with values (GH 42719)
- Regression in `DataFrame.agg()` when the`func` argument returned lists and`axis=1` (GH 42727)
- Regression in `DataFrame.drop()` does nothing if`MultiIndex` has duplicates and indexer is a tuple or list of tuples (GH 42771)
- Fixed regression where `read_csv()` raised a`ValueError` when parameters`names` and`prefix` were both set to`None` (GH 42387)
- Fixed regression in comparisons between `Timestamp` object and`datetime64` objects outside the implementation bounds for nanosecond`datetime64` (GH 42794)
- Fixed regression in `Styler.highlight_min()` and`Styler.highlight_max()` where`pandas.NA` was not successfully ignored (GH 42650)
- Fixed regression in `concat()` where`copy=False` was not honored in`axis=1` Series concatenation (GH 42501)
- Regression in `Series.nlargest()` and`Series.nsmallest()` with nullable integer or float dtype (GH 42816)
- Fixed regression in `Series.quantile()` with`Int64Dtype` (GH 42626)
- Fixed regression in `Series.groupby()` and`DataFrame.groupby()` where supplying the`by` argument with a Series named with a tuple would incorrectly raise (GH 42731)

## Bug fixes#

- Bug in `read_excel()` modifies the dtypes dictionary when reading a file with duplicate columns (GH 42462)
- 1D slices over extension types turn into N-dimensional slices over ExtensionArrays (GH 42430)
- Fixed bug in `Series.rolling()` and`DataFrame.rolling()` not calculating window bounds correctly for the first row when`center=True` and`window` is an offset that covers all the rows (GH 42753)
- `Styler.hide_columns()` now hides the index name header row as well as column headers (GH 42101)
- `Styler.set_sticky()` has amended CSS to control the column/index names and ensure the correct sticky positions (GH 42537)
- Bug in de-serializing datetime indexes in PYTHONOPTIMIZED mode (GH 42866)

## Contributors#

A total of 16 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- Alexander Gorodetsky +
- Fangchen Li
- Fred Reiss
- Justin McOmie +
- Matthew Zeitlin
- MeeseeksMachine
- Pandas Development Team
- Patrick Hoefler
- Richard Shadrach
- Shoham Debnath
- Simon Hawkins
- Thomas Li
- Wenjun Si
- attack68
- dicristina +
- jbrockmendel