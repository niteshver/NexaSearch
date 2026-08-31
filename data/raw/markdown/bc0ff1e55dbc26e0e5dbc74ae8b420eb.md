# What’s new in 0.23.4 (August 3, 2018)#

This is a minor bug-fix release in the 0.23.x series and includes some small regression fixes and bug fixes. We recommend that all users upgrade to this version.

Warning

Starting January 1, 2019, pandas feature releases will support Python 3 only. See Dropping Python 2.7 for more.

## Fixed regressions#

- Python 3.7 with Windows gave all missing values for rolling variance calculations (GH 21813)

## Bug fixes#

**Groupby/resample/rolling**

- Bug where calling `DataFrameGroupBy.agg()` with a list of functions including`ohlc` as the non-initial element would raise a`ValueError` (GH 21716)
- Bug in `roll_quantile` caused a memory leak when calling`.rolling(...).quantile(q)` with`q` in (0,1) (GH 21965)

**Missing**

- Bug in `Series.clip()` and`DataFrame.clip()` cannot accept list-like threshold containing`NaN` (GH 19992)

## Contributors#

A total of 6 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- Jeff Reback
- MeeseeksMachine +
- Tom Augspurger
- chris-b1
- h-vetinari
- meeseeksdev[bot]