# Comparison with SPSS#

For potential users coming from SPSS, this page is meant to demonstrate how various SPSS operations would be performed using pandas.

If you’re new to pandas, you might want to first read through 10 Minutes to pandas to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

```
In [1]: import pandas as pd
In [2]: import numpy as np
```
## Data structures#

### General terminology translation#

| pandas | SPSS | 
|---|---|
| `DataFrame` | data file | 
| column | variable | 
| row | case | 
| groupby | split file | 
| `NaN` | system-missing | 

### `DataFrame`#

A `DataFrame` in pandas is analogous to an SPSS data file - a two-dimensional
data source with labeled columns that can be of different types. As will be shown in this
document, almost any operation that can be performed in SPSS can also be accomplished in pandas.

### `Series`#

A `Series` is the data structure that represents one column of a `DataFrame`. SPSS doesn’t have a
separate data structure for a single variable, but in general, working with a `Series` is analogous
to working with a variable in SPSS.

### `Index`#

Every `DataFrame` and `Series` has an `Index` – labels on the *rows* of the data. SPSS does not
have an exact analogue, as cases are simply numbered sequentially from 1. In pandas, if no index is
specified, a `RangeIndex` is used by default (first row = 0, second row = 1, and so on).

While using a labeled `Index` or `MultiIndex` can enable sophisticated analyses and is ultimately an
important part of pandas to understand, for this comparison we will essentially ignore the `Index` and
just treat the `DataFrame` as a collection of columns. Please see the indexing documentation
for much more on how to use an `Index` effectively.

## Copies vs. in place operations#

Most pandas operations return copies of the `Series`/`DataFrame`. To make the changes “stick”,
you’ll need to either assign to a new variable:

sorted_df = df.sort_values("col1")

or overwrite the original one:

df = df.sort_values("col1")

Note

You will see an `inplace=True` or `copy=False` keyword argument available for
some methods:

```
df.replace(5, inplace=True)
```
There is an active discussion about deprecating and removing `inplace` and `copy` for
most methods (e.g. `dropna`) except for a very small subset of methods
(including `replace`). Both keywords won’t be
necessary anymore in the context of Copy-on-Write. The proposal can be found
here.

## Data input / output#

### Reading external data#

Like SPSS, pandas provides utilities for reading in data from many formats. The `tips` dataset, found within
the pandas tests (csv)
will be used in many of the following examples.

In SPSS, you would use File > Open > Data to import a CSV file:

```
FILE > OPEN > DATA
/TYPE=CSV
/FILE='tips.csv'
/DELIMITERS=","
/FIRSTCASE=2
/VARIABLES=col1 col2 col3.
```
The pandas equivalent would use `read_csv()`:

```
url = (
    "https://raw.githubusercontent.com/pandas-dev"
    "/pandas/main/pandas/tests/io/data/csv/tips.csv"
)
tips = pd.read_csv(url)
tips
```
Like SPSS’s data import wizard, `read_csv` can take a number of parameters to specify how the data should be parsed.
For example, if the data was instead tab delimited, and did not have column names, the pandas command would be:

```
tips = pd.read_csv("tips.csv", sep="\t", header=None)
# alternatively, read_table is an alias to read_csv with tab delimiter
tips = pd.read_table("tips.csv", header=None)
```
## Data operations#

### Filtering#

In SPSS, filtering is done through Data > Select Cases:

```
SELECT IF (total_bill > 10).
EXECUTE.
```
In pandas, boolean indexing can be used:

```
tips[tips["total_bill"] > 10]
```
### Sorting#

In SPSS, sorting is done through Data > Sort Cases:

```
SORT CASES BY sex total_bill.
EXECUTE.
```
In pandas, this would be written as:

```
tips.sort_values(["sex", "total_bill"])
```
## String processing#

### Finding length of string#

In SPSS:

```
COMPUTE length = LENGTH(time).
EXECUTE.
```
You can find the length of a character string with `Series.str.len()`.
In Python 3, all strings are Unicode strings. `len` includes trailing blanks.
Use `len` and `rstrip` to exclude trailing blanks.

```
In [3]: tips["time"].str.len()
Out[3]: 
67     6
92     6
111    6
145    5
135    5
      ..
182    6
156    6
59     6
212    6
170    6
Name: time, Length: 244, dtype: int64
In [4]: tips["time"].str.rstrip().str.len()
Out[4]: 
67     6
92     6
111    6
145    5
135    5
      ..
182    6
156    6
59     6
212    6
170    6
Name: time, Length: 244, dtype: int64
```
### Changing case#

In SPSS:

```
COMPUTE upper = UPCASE(time).
COMPUTE lower = LOWER(time).
EXECUTE.
```
The equivalent pandas methods are `Series.str.upper()`, `Series.str.lower()`, and
`Series.str.title()`.

```
In [5]: firstlast = pd.DataFrame({"string": ["John Smith", "Jane Cook"]})
In [6]: firstlast["upper"] = firstlast["string"].str.upper()
In [7]: firstlast["lower"] = firstlast["string"].str.lower()
In [8]: firstlast["title"] = firstlast["string"].str.title()
In [9]: firstlast
Out[9]: 
       string       upper       lower       title
0  John Smith  JOHN SMITH  john smith  John Smith
1   Jane Cook   JANE COOK   jane cook   Jane Cook
```
## Merging#

In SPSS, merging data files is done through Data > Merge Files.

The following tables will be used in the merge examples:

```
In [10]: df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
In [11]: df1
Out[11]: 
  key     value
0   A  0.469112
1   B -0.282863
2   C -1.509059
3   D -1.135632
In [12]: df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})
In [13]: df2
Out[13]: 
  key     value
0   B  1.212112
1   D -0.173215
2   D  0.119209
3   E -1.044236
```
pandas DataFrames have a `merge()` method, which provides similar functionality. The
data does not have to be sorted ahead of time, and different join types are accomplished via the
`how` keyword.

```
In [14]: inner_join = df1.merge(df2, on=["key"], how="inner")
In [15]: inner_join
Out[15]: 
  key   value_x   value_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209
In [16]: left_join = df1.merge(df2, on=["key"], how="left")
In [17]: left_join
Out[17]: 
  key   value_x   value_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
In [18]: right_join = df1.merge(df2, on=["key"], how="right")
In [19]: right_join
Out[19]: 
  key   value_x   value_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209
3   E       NaN -1.044236
In [20]: outer_join = df1.merge(df2, on=["key"], how="outer")
In [21]: outer_join
Out[21]: 
  key   value_x   value_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E       NaN -1.044236
```
## GroupBy operations#

### Split-file processing#

In SPSS, split-file analysis is done through Data > Split File:

```
SORT CASES BY sex.
SPLIT FILE BY sex.
DESCRIPTIVES VARIABLES=total_bill tip
  /STATISTICS=MEAN STDDEV MIN MAX.
```
The pandas equivalent would be:

```
tips.groupby("sex")[["total_bill", "tip"]].agg(["mean", "std", "min", "max"])
```
## Missing data#

SPSS uses the period (`.`) for numeric missing values and blank spaces for string missing values.
pandas uses `NaN` (Not a Number) for numeric missing values and `None` or `NaN` for string
missing values.

In pandas, `Series.isna()` and `Series.notna()` can be used to filter the rows.

```
In [22]: outer_join[outer_join["value_x"].isna()]
Out[22]: 
  key  value_x   value_y
5   E      NaN -1.044236
In [23]: outer_join[outer_join["value_x"].notna()]
Out[23]: 
  key   value_x   value_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
```
pandas provides a variety of methods to work with missing data. Here are some examples:

### Drop rows with missing values#

```
In [24]: outer_join.dropna()
Out[24]: 
  key   value_x   value_y
1   B -0.282863  1.212112
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
```
### Forward fill from previous rows#

```
In [25]: outer_join.ffill()
Out[25]: 
  key   value_x   value_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059  1.212112
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E -1.135632 -1.044236
```
### Replace missing values with a specified value#

Using the mean:

```
In [26]: outer_join["value_x"].fillna(outer_join["value_x"].mean())
Out[26]: 
0    0.469112
1   -0.282863
2   -1.509059
3   -1.135632
4   -1.135632
5   -0.718815
Name: value_x, dtype: float64
```
## Other considerations#

## Output management#

While pandas does not have a direct equivalent to SPSS’s Output Management System (OMS), you can capture and export results in various ways:

```
# Save summary statistics to CSV
tips.groupby('sex')[['total_bill', 'tip']].mean().to_csv('summary.csv')
# Save multiple results to Excel sheets
with pd.ExcelWriter('results.xlsx') as writer:
    tips.describe().to_excel(writer, sheet_name='Descriptives')
    tips.groupby('sex').mean().to_excel(writer, sheet_name='Means by Gender')
```