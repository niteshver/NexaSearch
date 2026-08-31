# Version 0.7.1 (February 29, 2012)#

This release includes a few new features and addresses over a dozen bugs in 0.7.0.

## New features#


Add `to_clipboard` function to pandas namespace for writing objects to
the system clipboard (GH 774)

Add `itertuples` method to DataFrame for iterating through the rows of a
dataframe as tuples (GH 818)

Add ability to pass fill_value and method to DataFrame and Series align method (GH 806, GH 807)

Add fill_value option to reindex, align methods (GH 784)

Enable concat to produce DataFrame from Series (GH 787)

Add `between` method to Series (GH 802)

Add HTML representation hook to DataFrame for the IPython HTML notebook (GH 773)

Support for reading Excel 2007 XML documents using openpyxl


## Performance improvements#


Improve performance and memory usage of fillna on DataFrame

Can concatenate a list of Series along axis=1 to obtain a DataFrame (GH 787)


## Contributors#

A total of 9 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- Adam Klein
- Brian Granger +
- Chang She
- Dieter Vandenbussche
- Josh Klein
- Steve +
- Wes McKinney
- Wouter Overmeire
- Yaroslav Halchenko