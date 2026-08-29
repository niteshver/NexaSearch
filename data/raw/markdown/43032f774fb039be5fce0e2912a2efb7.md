# What’s new in 2.2.0 (January 19, 2024)#

These are the changes in pandas 2.2.0. See Release notes for a full changelog including other versions of pandas.

## Upcoming changes in pandas 3.0#

pandas 3.0 will bring two bigger changes to the default behavior of pandas.

### Copy-on-Write#

The currently optional mode Copy-on-Write will be enabled by default in pandas 3.0. There won’t be an option to keep the current behavior enabled. The new behavioral semantics are explained in the user guide about Copy-on-Write.

The new behavior can be enabled since pandas 2.0 with the following option:

```
pd.options.mode.copy_on_write = True
```
This change brings different changes in behavior in how pandas operates with respect to copies and views. Some of these changes allow a clear deprecation, like the changes in chained assignment. Other changes are more subtle and thus, the warnings are hidden behind an option that can be enabled in pandas 2.2.

```
pd.options.mode.copy_on_write = "warn"
```
This mode will warn in many different scenarios that aren’t actually relevant to most queries. We recommend exploring this mode, but it is not necessary to get rid of all of these warnings. The migration guide explains the upgrade process in more detail.

### Dedicated string data type (backed by Arrow) by default#

Historically, pandas represented string columns with NumPy object data type. This
representation has numerous problems, including slow performance and a large memory
footprint. This will change in pandas 3.0. pandas will start inferring string columns
as a new `string` data type, backed by Arrow, which represents strings contiguous in memory. This brings
a huge performance and memory improvement.

Old behavior:

```
In [1]: ser = pd.Series(["a", "b"])
Out[1]:
0    a
1    b
dtype: object
```
New behavior:

```
In [1]: ser = pd.Series(["a", "b"])
Out[1]:
0    a
1    b
dtype: string
```
The string data type that is used in these scenarios will mostly behave as NumPy object would, including missing value semantics and general operations on these columns.

This change includes a few additional changes across the API:

- Currently, specifying `dtype="string"` creates a dtype that is backed by Python strings
which are stored in a NumPy array. This will change in pandas 3.0, this dtype
will create an Arrow backed string column.
- The column names and the Index will also be backed by Arrow strings.
- PyArrow will become a required dependency with pandas 3.0 to accommodate this change.

This future dtype inference logic can be enabled with:

```
pd.options.future.infer_string = True
```
## Enhancements#

### ADBC Driver support in to_sql and read_sql#

`read_sql()` and `to_sql()` now work with Apache Arrow ADBC drivers. Compared to
traditional drivers used via SQLAlchemy, ADBC drivers should provide
significant performance improvements, better type support and cleaner
nullability handling.

```
import adbc_driver_postgresql.dbapi as pg_dbapi
df = pd.DataFrame(
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    columns=['a', 'b', 'c']
)
uri = "postgresql://postgres:postgres@localhost/postgres"
with pg_dbapi.connect(uri) as conn:
    df.to_sql("pandas_table", conn, index=False)
# for round-tripping
with pg_dbapi.connect(uri) as conn:
    df2 = pd.read_sql("pandas_table", conn)
```
The Arrow type system offers a wider array of types that can more closely match what databases like PostgreSQL can offer. To illustrate, note this (non-exhaustive) listing of types available in different databases and pandas backends:

| numpy/pandas | arrow | postgres | sqlite | 
|---|---|---|---|
| int16/Int16 | int16 | SMALLINT | INTEGER | 
| int32/Int32 | int32 | INTEGER | INTEGER | 
| int64/Int64 | int64 | BIGINT | INTEGER | 
| float32 | float32 | REAL | REAL | 
| float64 | float64 | DOUBLE PRECISION | REAL | 
| object | string | TEXT | TEXT | 
| bool | `bool_` | BOOLEAN |  | 
| datetime64[ns] | timestamp(us) | TIMESTAMP |  | 
| datetime64[ns,tz] | timestamp(us,tz) | TIMESTAMPTZ |  | 
|  | date32 | DATE |  | 
|  | month_day_nano_interval | INTERVAL |  | 
|  | binary | BINARY | BLOB | 
|  | decimal128 | DECIMAL [1] |  | 
|  | list | ARRAY [1] |  | 
|  | struct |  |  | 

Footnotes

If you are interested in preserving database types as best as possible
throughout the lifecycle of your DataFrame, users are encouraged to
leverage the `dtype_backend="pyarrow"` argument of `read_sql()`

```
# for round-tripping
with pg_dbapi.connect(uri) as conn:
    df2 = pd.read_sql("pandas_table", conn, dtype_backend="pyarrow")
```
This will prevent your data from being converted to the traditional pandas/NumPy type system, which often converts SQL types in ways that make them impossible to round-trip.

For a full list of ADBC drivers and their development status, see the ADBC Driver Implementation Status documentation.

### Create a pandas Series based on one or more conditions#

The `Series.case_when()` function has been added to create a Series object based on one or more conditions. (GH 39154)

```
In [1]: import pandas as pd
In [2]: df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]))
In [3]: default=pd.Series('default', index=df.index)
In [4]: default.case_when(
   ...:      caselist=[
   ...:          (df.a == 1, 'first'),                              # condition, replacement
   ...:          (df.a.gt(1) & df.b.eq(5), 'second'),  # condition, replacement
   ...:      ],
   ...: )
   ...: 
Out[4]: 
0      first
1     second
2    default
dtype: str
```
### `to_numpy` for NumPy nullable and Arrow types converts to suitable NumPy dtype#

`to_numpy` for NumPy nullable and Arrow types will now convert to a
suitable NumPy dtype instead of `object` dtype for nullable and PyArrow backed extension dtypes.

*Old behavior:*

```
In [1]: ser = pd.Series([1, 2, 3], dtype="Int64")
In [2]: ser.to_numpy()
Out[2]: array([1, 2, 3], dtype=object)
```
*New behavior:*

```
In [5]: ser = pd.Series([1, 2, 3], dtype="Int64")
In [6]: ser.to_numpy()
Out[6]: array([1, 2, 3])
In [7]: ser = pd.Series([1, 2, 3], dtype="timestamp[ns][pyarrow]")
In [8]: ser.to_numpy()
Out[8]: 
array(['1970-01-01T00:00:00.000000001', '1970-01-01T00:00:00.000000002',
       '1970-01-01T00:00:00.000000003'], dtype='datetime64[ns]')
```
The default NumPy dtype (without any arguments) is determined as follows:

- float dtypes are cast to NumPy floats
- integer dtypes without missing values are cast to NumPy integer dtypes
- integer dtypes with missing values are cast to NumPy float dtypes and `NaN` is used as missing value indicator
- boolean dtypes without missing values are cast to NumPy bool dtype
- boolean dtypes with missing values keep object dtype
- datetime and timedelta types are cast to Numpy datetime64 and timedelta64 types respectively and `NaT` is used as missing value indicator

### Series.struct accessor for PyArrow structured data#

The `Series.struct` accessor provides attributes and methods for processing
data with `struct[pyarrow]` dtype Series. For example,
`Series.struct.explode()` converts PyArrow structured data to a pandas
DataFrame. (GH 54938)

```
In [9]: import pyarrow as pa
In [10]: series = pd.Series(
   ....:     [
   ....:         {"project": "pandas", "version": "2.2.0"},
   ....:         {"project": "numpy", "version": "1.25.2"},
   ....:         {"project": "pyarrow", "version": "13.0.0"},
   ....:     ],
   ....:     dtype=pd.ArrowDtype(
   ....:         pa.struct([
   ....:             ("project", pa.string()),
   ....:             ("version", pa.string()),
   ....:         ])
   ....:     ),
   ....: )
   ....: 
In [11]: series.struct.explode()
Out[11]: 
   project version
0   pandas   2.2.0
1    numpy  1.25.2
2  pyarrow  13.0.0
```
Use `Series.struct.field()` to index into a (possible nested)
struct field.

```
In [12]: series.struct.field("project")
Out[12]: 
0     pandas
1      numpy
2    pyarrow
Name: project, dtype: string[pyarrow]
```
### Series.list accessor for PyArrow list data#

The `Series.list` accessor provides attributes and methods for processing
data with `list[pyarrow]` dtype Series. For example,
`Series.list.__getitem__()` allows indexing pyarrow lists in
a Series. (GH 55323)

```
In [13]: import pyarrow as pa
In [14]: series = pd.Series(
   ....:     [
   ....:         [1, 2, 3],
   ....:         [4, 5],
   ....:         [6],
   ....:     ],
   ....:     dtype=pd.ArrowDtype(
   ....:         pa.list_(pa.int64())
   ....:     ),
   ....: )
   ....: 
In [15]: series.list[0]
Out[15]: 
0    1
1    4
2    6
dtype: int64[pyarrow]
```
### Calamine engine for `read_excel()`#

The `calamine` engine was added to `read_excel()`.
It uses `python-calamine`, which provides Python bindings for the Rust library calamine.
This engine supports Excel files (`.xlsx`, `.xlsm`, `.xls`, `.xlsb`) and OpenDocument spreadsheets (`.ods`) (GH 50395).

There are two advantages of this engine:

1. Calamine is often faster than other engines, some benchmarks show results up to 5x faster than ‘openpyxl’, 20x - ‘odf’, 4x - ‘pyxlsb’, and 1.5x - ‘xlrd’. But, ‘openpyxl’ and ‘pyxlsb’ are faster in reading a few rows from large files because of lazy iteration over rows.
2. Calamine supports the recognition of datetime in `.xlsb` files, unlike ‘pyxlsb’ which is the only other engine in pandas that can read`.xlsb` files.

```
pd.read_excel("path_to_file.xlsb", engine="calamine")
```
For more, see Calamine (Excel and ODS files) in the user guide on IO tools.

### Other enhancements#

- `to_sql()` with method parameter set to`multi` works with Oracle on the backend
- `Series.attrs` /`DataFrame.attrs` now uses a deepcopy for propagating`attrs` (GH 54134).
- `get_dummies()` now returning  extension dtypes`boolean` or`bool[pyarrow]` that are compatible with the input dtype (GH 56273)
- `read_csv()` now supports`on_bad_lines` parameter with`engine="pyarrow"` (GH 54480)
- `read_sas()` returns`datetime64` dtypes with resolutions better matching those stored natively in SAS, and avoids returning object-dtype in cases that cannot be stored with`datetime64[ns]` dtype (GH 56127)
- `read_spss()` now returns a`DataFrame` that stores the metadata in`DataFrame.attrs` (GH 54264)
- `tseries.api.guess_datetime_format()` is now part of the public API (GH 54727)
- `DataFrame.apply()` now allows the usage of numba (via`engine="numba"` ) to JIT compile the passed function, allowing for potential speedups (GH 54666)
- `ExtensionArray._explode()` interface method added to allow extension type implementations of the`explode` method (GH 54833)
- `ExtensionArray.duplicated()` added to allow extension type implementations of the`duplicated` method (GH 55255)
- `Series.ffill()` ,`Series.bfill()` ,`DataFrame.ffill()` , and`DataFrame.bfill()` have gained the argument`limit_area` ; 3rd party`ExtensionArray` authors need to add this argument to the method`_pad_or_backfill` (GH 56492)
- Allow passing `read_only` ,`data_only` and`keep_links` arguments to openpyxl using`engine_kwargs` of`read_excel()` (GH 55027)
- Implement `Series.interpolate()` and`DataFrame.interpolate()` for`ArrowDtype` and masked dtypes (GH 56267)
- Implement masked algorithms for `Series.value_counts()` (GH 54984)
- Implemented `Series.dt()` methods and attributes for`ArrowDtype` with`pyarrow.duration` type (GH 52284)
- Implemented `Series.str.extract()` for`ArrowDtype` (GH 56268)
- Improved error message that appears in `DatetimeIndex.to_period()` with frequencies which are not supported as period frequencies, such as`"BMS"` (GH 56243)
- Improved error message when constructing `Period` with invalid offsets such as`"QS"` (GH 55785)
- The dtypes `string[pyarrow]` and`string[pyarrow_numpy]` now both utilize the`large_string` type from PyArrow to avoid overflow for long columns (GH 56259)

## Notable bug fixes#

These are bug fixes that might have notable behavior changes.

### `merge()` and `DataFrame.join()` now consistently follow documented sort behavior#

In previous versions of pandas, `merge()` and `DataFrame.join()` did not
always return a result that followed the documented sort behavior. pandas now
follows the documented sort behavior in merge and join operations (GH 54611, GH 56426, GH 56443).

As documented, `sort=True` sorts the join keys lexicographically in the resulting
`DataFrame`. With `sort=False`, the order of the join keys depends on the
join type (`how` keyword):

- `how="left"` : preserve the order of the left keys
- `how="right"` : preserve the order of the right keys
- `how="inner"` : preserve the order of the left keys
- `how="outer"` : sort keys lexicographically

One example with changing behavior is inner joins with non-unique left join keys
and `sort=False`:

```
In [16]: left = pd.DataFrame({"a": [1, 2, 1]})
In [17]: right = pd.DataFrame({"a": [1, 2]})
In [18]: result = pd.merge(left, right, how="inner", on="a", sort=False)
```
*Old Behavior*

```
In [5]: result
Out[5]:
   a
0  1
1  1
2  2
```
*New Behavior*

```
In [19]: result
Out[19]: 
   a
0  1
1  2
2  1
```
### `merge()` and `DataFrame.join()` no longer reorder levels when levels differ#

In previous versions of pandas, `merge()` and `DataFrame.join()` would reorder
index levels when joining on two indexes with different levels (GH 34133).

```
In [20]: left = pd.DataFrame({"left": 1}, index=pd.MultiIndex.from_tuples([("x", 1), ("x", 2)], names=["A", "B"]))
In [21]: right = pd.DataFrame({"right": 2}, index=pd.MultiIndex.from_tuples([(1, 1), (2, 2)], names=["B", "C"]))
In [22]: left
Out[22]: 
     left
A B      
x 1     1
  2     1
In [23]: right
Out[23]: 
     right
B C       
1 1      2
2 2      2
In [24]: result = left.join(right)
```
*Old Behavior*

```
In [5]: result
Out[5]:
       left  right
B A C
1 x 1     1      2
2 x 2     1      2
```
*New Behavior*

```
In [25]: result
Out[25]: 
       left  right
A B C             
x 1 1     1      2
  2 2     1      2
```
### Increased minimum versions for dependencies#

For optional dependencies the general recommendation is to use the latest version. Optional dependencies below the lowest tested version may still work but are not considered supported. The following table lists the optional dependencies that have had their minimum tested version increased.

| Package | New Minimum Version | 
|---|---|
| beautifulsoup4 | 4.11.2 | 
| blosc | 1.21.3 | 
| bottleneck | 1.3.6 | 
| fastparquet | 2022.12.0 | 
| fsspec | 2022.11.0 | 
| gcsfs | 2022.11.0 | 
| lxml | 4.9.2 | 
| matplotlib | 3.6.3 | 
| numba | 0.56.4 | 
| numexpr | 2.8.4 | 
| qtpy | 2.3.0 | 
| openpyxl | 3.1.0 | 
| psycopg2 | 2.9.6 | 
| pyreadstat | 1.2.0 | 
| pytables | 3.8.0 | 
| pyxlsb | 1.0.10 | 
| s3fs | 2022.11.0 | 
| scipy | 1.10.0 | 
| sqlalchemy | 2.0.0 | 
| tabulate | 0.9.0 | 
| xarray | 2022.12.0 | 
| xlsxwriter | 3.0.5 | 
| zstandard | 0.19.0 | 
| pyqt5 | 5.15.8 | 
| tzdata | 2022.7 | 

See Dependencies and Optional dependencies for more.

### Other API changes#

- The hash values of nullable extension dtypes changed to improve the performance of the hashing operation (GH 56507)
- `check_exact` now only takes effect for floating-point dtypes in`testing.assert_frame_equal()` and`testing.assert_series_equal()` . In particular, integer dtypes are always checked exactly (GH 55882)

## Deprecations#

### Chained assignment#

In preparation of larger upcoming changes to the copy / view behaviour in pandas 3.0
(Copy-on-Write (CoW), PDEP-7), we started deprecating *chained assignment*.

Chained assignment occurs when you try to update a pandas DataFrame or Series through two subsequent indexing operations. Depending on the type and order of those operations this currently does or does not work.

A typical example is as follows:

```
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
# first selecting rows with a mask, then assigning values to a column
# -> this has never worked and raises a SettingWithCopyWarning
df[df["bar"] > 5]["foo"] = 100
# first selecting the column, and then assigning to a subset of that column
# -> this currently works
df["foo"][df["bar"] > 5] = 100
```
This second example of chained assignment currently works to update the original `df`.
This will no longer work in pandas 3.0, and therefore we started deprecating this:

```
>>> df["foo"][df["bar"] > 5] = 100
FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:
df["col"][row_indexer] = value
Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.
See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
```
You can fix this warning and ensure your code is ready for pandas 3.0 by removing
the usage of chained assignment. Typically, this can be done by doing the assignment
in a single step using for example `.loc`. For the example above, we can do:

```
df.loc[df["bar"] > 5, "foo"] = 100
```
The same deprecation applies to inplace methods that are done in a chained manner, such as:

```
>>> df["foo"].fillna(0, inplace=True)
FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
```
When the goal is to update the column in the DataFrame `df`, the alternative here is
to call the method on `df` itself, such as `df.fillna({"foo": 0}, inplace=True)`.

See more details in the migration guide.

### Deprecate aliases `M`, `Q`, `Y`, etc. in favour of `ME`, `QE`, `YE`, etc. for offsets#

Deprecated the following frequency aliases (GH 9586):

| offsets | deprecated aliases | new aliases | 
|---|---|---|
| `MonthEnd` | `M` | `ME` | 
| `BusinessMonthEnd` | `BM` | `BME` | 
| `SemiMonthEnd` | `SM` | `SME` | 
| `CustomBusinessMonthEnd` | `CBM` | `CBME` | 
| `QuarterEnd` | `Q` | `QE` | 
| `BQuarterEnd` | `BQ` | `BQE` | 
| `YearEnd` | `Y` | `YE` | 
| `BYearEnd` | `BY` | `BYE` | 

For example:

*Previous behavior*:

```
In [8]: pd.date_range('2020-01-01', periods=3, freq='Q-NOV')
Out[8]:
DatetimeIndex(['2020-02-29', '2020-05-31', '2020-08-31'],
              dtype='datetime64[ns]', freq='Q-NOV')
```
*Future behavior*:

```
In [26]: pd.date_range('2020-01-01', periods=3, freq='QE-NOV')
Out[26]: DatetimeIndex(['2020-02-29', '2020-05-31', '2020-08-31'], dtype='datetime64[us]', freq='QE-NOV')
```
### Deprecated automatic downcasting#

Deprecated the automatic downcasting of object dtype results in a number of methods. These would silently change the dtype in a hard to predict manner since the behavior was value dependent. Additionally, pandas is moving away from silent dtype changes (GH 54710, GH 54261).

These methods are:

Explicitly call `DataFrame.infer_objects()` to replicate the current behavior in the future.

```
result = result.infer_objects(copy=False)
```
Or explicitly cast all-round floats to ints using `astype`.

Set the following option to opt into the future behavior:

```
In [9]: pd.set_option("future.no_silent_downcasting", True)
```
### Other Deprecations#

- Changed `Timedelta.resolution_string()` to return`h` ,`min` ,`s` ,`ms` ,`us` , and`ns` instead of`H` ,`T` ,`S` ,`L` ,`U` , and`N` , for compatibility with respective deprecations in frequency aliases (GH 52536)
- Deprecated `offsets.Day.delta` ,`offsets.Hour.delta` ,`offsets.Minute.delta` ,`offsets.Second.delta` ,`offsets.Milli.delta` ,`offsets.Micro.delta` ,`offsets.Nano.delta` , use`pd.Timedelta(obj)` instead (GH 55498)
- Deprecated `pandas.api.types.is_interval()` and`pandas.api.types.is_period()` , use`isinstance(obj, pd.Interval)` and`isinstance(obj, pd.Period)` instead (GH 55264)
- Deprecated `read_gbq()` and`DataFrame.to_gbq()` . Use`pandas_gbq.read_gbq` and`pandas_gbq.to_gbq` instead https://pandas-gbq.readthedocs.io/en/latest/api.html (GH 55525)
- Deprecated `DataFrameGroupBy.fillna()` and`SeriesGroupBy.fillna()` ; use`DataFrameGroupBy.ffill()` ,`DataFrameGroupBy.bfill()` for forward and backward filling or`DataFrame.fillna()` to fill with a single value (or the Series equivalents) (GH 55718)
- Deprecated `DateOffset.is_anchored()` , use`obj.n == 1` for non-Tick subclasses (for Tick this was always False) (GH 55388)
- Deprecated `DatetimeArray.__init__()` and`TimedeltaArray.__init__()` , use`array()` instead (GH 55623)
- Deprecated `Index.format()` , use`index.astype(str)` or`index.map(formatter)` instead (GH 55413)
- Deprecated `Series.ravel()` , the underlying array is already 1D, so ravel is not necessary (GH 52511)
- Deprecated `Series.resample()` and`DataFrame.resample()` with a`PeriodIndex` (and the ‘convention’ keyword), convert to`DatetimeIndex` (with`.to_timestamp()` ) before resampling instead (GH 53481). Note: this deprecation was later undone in pandas 2.3.3 (GH 57033)
- Deprecated `Series.view()` , use`Series.astype()` instead to change the dtype (GH 20251)
- Deprecated `offsets.Tick.is_anchored()` , use`False` instead (GH 55388)
- Deprecated `core.internals` members`Block` ,`ExtensionBlock` , and`DatetimeTZBlock` , use public APIs instead (GH 55139)
- Deprecated `year` ,`month` ,`quarter` ,`day` ,`hour` ,`minute` , and`second` keywords in the`PeriodIndex` constructor, use`PeriodIndex.from_fields()` instead (GH 55960)
- Deprecated accepting a type as an argument in `Index.view()` , call without any arguments instead (GH 55709)
- Deprecated allowing non-integer `periods` argument in`date_range()` ,`timedelta_range()` ,`period_range()` , and`interval_range()` (GH 56036)
- Deprecated allowing non-keyword arguments in `DataFrame.to_clipboard()` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_csv()` except`path_or_buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_dict()` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_excel()` except`excel_writer` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_gbq()` except`destination_table` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_hdf()` except`path_or_buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_html()` except`buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_json()` except`path_or_buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_latex()` except`buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_markdown()` except`buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_parquet()` except`path` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_pickle()` except`path` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_string()` except`buf` (GH 54229)
- Deprecated allowing non-keyword arguments in `DataFrame.to_xml()` except`path_or_buffer` (GH 54229)
- Deprecated allowing passing `BlockManager` objects to`DataFrame` or`SingleBlockManager` objects to`Series` (GH 52419)
- Deprecated behavior of `Index.insert()` with an object-dtype index silently performing type inference on the result, explicitly call`result.infer_objects(copy=False)` for the old behavior instead (GH 51363)
- Deprecated casting non-datetimelike values (mainly strings) in `Series.isin()` and`Index.isin()` with`datetime64` ,`timedelta64` , and`PeriodDtype` dtypes (GH 53111)
- Deprecated dtype inference in `Index` ,`Series` and`DataFrame` constructors when giving a pandas input, call`.infer_objects` on the input to keep the current behavior (GH 56012)
- Deprecated dtype inference when setting a `Index` into a`DataFrame` , cast explicitly instead (GH 56102)
- Deprecated including the groups in computations when using `DataFrameGroupBy.apply()` and`DataFrameGroupBy.resample()` ; pass`include_groups=False` to exclude the groups (GH 7155)
- Deprecated indexing an `Index` with a boolean indexer of length zero (GH 55820)
- Deprecated not passing a tuple to `DataFrameGroupBy.get_group` or`SeriesGroupBy.get_group` when grouping by a length-1 list-like (GH 25971)
- Deprecated string `AS` denoting frequency in`YearBegin` and strings`AS-DEC` ,`AS-JAN` , etc. denoting annual frequencies with various fiscal year starts (GH 54275)
- Deprecated string `A` denoting frequency in`YearEnd` and strings`A-DEC` ,`A-JAN` , etc. denoting annual frequencies with various fiscal year ends (GH 54275)
- Deprecated string `BAS` denoting frequency in`BYearBegin` and strings`BAS-DEC` ,`BAS-JAN` , etc. denoting annual frequencies with various fiscal year starts (GH 54275)
- Deprecated string `BA` denoting frequency in`BYearEnd` and strings`BA-DEC` ,`BA-JAN` , etc. denoting annual frequencies with various fiscal year ends (GH 54275)
- Deprecated strings `H` ,`BH` , and`CBH` denoting frequencies in`Hour` ,`BusinessHour` ,`CustomBusinessHour` (GH 52536)
- Deprecated strings `H` ,`S` ,`U` , and`N` denoting units in`to_timedelta()` (GH 52536)
- Deprecated strings `H` ,`T` ,`S` ,`L` ,`U` , and`N` denoting units in`Timedelta` (GH 52536)
- Deprecated strings `T` ,`S` ,`L` ,`U` , and`N` denoting frequencies in`Minute` ,`Second` ,`Milli` ,`Micro` ,`Nano` (GH 52536)
- Deprecated support for combining parsed datetime columns in `read_csv()` along with the`keep_date_col` keyword (GH 55569)
- Deprecated the `DataFrameGroupBy.grouper` and`SeriesGroupBy.grouper` ; these attributes will be removed in a future version of pandas (GH 56521)
- Deprecated the `Grouping` attributes`group_index` ,`result_index` , and`group_arraylike` ; these will be removed in a future version of pandas (GH 56148)
- Deprecated the `delim_whitespace` keyword in`read_csv()` and`read_table()` , use`sep="\\s+"` instead (GH 55569)
- Deprecated the `errors="ignore"` option in`to_datetime()` ,`to_timedelta()` , and`to_numeric()` ; explicitly catch exceptions instead (GH 54467)
- Deprecated the `fastpath` keyword in the`Series` constructor (GH 20110)
- Deprecated the `kind` keyword in`Series.resample()` and`DataFrame.resample()` , explicitly cast the object’s`index` instead (GH 55895)
- Deprecated the `ordinal` keyword in`PeriodIndex` , use`PeriodIndex.from_ordinals()` instead (GH 55960)
- Deprecated the `unit` keyword in`TimedeltaIndex` construction, use`to_timedelta()` instead (GH 55499)
- Deprecated the `verbose` keyword in`read_csv()` and`read_table()` (GH 55569)
- Deprecated the behavior of `DataFrame.replace()` and`Series.replace()` with`CategoricalDtype` ; in a future version replace will change the values while preserving the categories. To change the categories, use`ser.cat.rename_categories` instead (GH 55147)
- Deprecated the behavior of `Series.value_counts()` and`Index.value_counts()` with object dtype; in a future version these will not perform dtype inference on the resulting`Index` , do`result.index = result.index.infer_objects()` to retain the old behavior (GH 56161)
- Deprecated the default of `observed=False` in`DataFrame.pivot_table()` ; will be`True` in a future version (GH 56236)
- Deprecated the extension test classes `BaseNoReduceTests` ,`BaseBooleanReduceTests` , and`BaseNumericReduceTests` , use`BaseReduceTests` instead (GH 54663)
- Deprecated the option `mode.data_manager` and the`ArrayManager` ; only the`BlockManager` will be available in future versions (GH 55043)
- Deprecated the previous implementation of `DataFrame.stack` ; specify`future_stack=True` to adopt the future version (GH 53515)

## Performance improvements#

- Performance improvement in `testing.assert_frame_equal()` and`testing.assert_series_equal()` (GH 55949, GH 55971)
- Performance improvement in `concat()` with`axis=1` and objects with unaligned indexes (GH 55084)
- Performance improvement in `get_dummies()` (GH 56089)
- Performance improvement in `merge()` and`merge_ordered()` when joining on sorted ascending keys (GH 56115)
- Performance improvement in `merge_asof()` when`by` is not`None` (GH 55580, GH 55678)
- Performance improvement in `read_stata()` for files with many variables (GH 55515)
- Performance improvement in `DataFrame.groupby()` when aggregating pyarrow timestamp and duration dtypes (GH 55031)
- Performance improvement in `DataFrame.join()` when joining on unordered categorical indexes (GH 56345)
- Performance improvement in `DataFrame.loc()` and`Series.loc()` when indexing with a`MultiIndex` (GH 56062)
- Performance improvement in `DataFrame.sort_index()` and`Series.sort_index()` when indexed by a`MultiIndex` (GH 54835)
- Performance improvement in `DataFrame.to_dict()` on converting DataFrame to dictionary (GH 50990)
- Performance improvement in `Index.difference()` (GH 55108)
- Performance improvement in `Index.sort_values()` when index is already sorted (GH 56128)
- Performance improvement in `MultiIndex.get_indexer()` when`method` is not`None` (GH 55839)
- Performance improvement in `Series.duplicated()` for pyarrow dtypes (GH 55255)
- Performance improvement in `Series.str.get_dummies()` when dtype is`"string[pyarrow]"` or`"string[pyarrow_numpy]"` (GH 56110)
- Performance improvement in `Series.str()` methods (GH 55736)
- Performance improvement in `Series.value_counts()` and`Series.mode()` for masked dtypes (GH 54984, GH 55340)
- Performance improvement in `DataFrameGroupBy.nunique()` and`SeriesGroupBy.nunique()` (GH 55972)
- Performance improvement in `SeriesGroupBy.idxmax()` ,`SeriesGroupBy.idxmin()` ,`DataFrameGroupBy.idxmax()` ,`DataFrameGroupBy.idxmin()` (GH 54234)
- Performance improvement when hashing a nullable extension array (GH 56507)
- Performance improvement when indexing into a non-unique index (GH 55816)
- Performance improvement when indexing with more than 4 keys (GH 54550)
- Performance improvement when localizing time to UTC (GH 55241)

## Bug fixes#

### Categorical#

- `Categorical.isin()` raising`InvalidIndexError` for categorical containing overlapping`Interval` values (GH 34974)
- Bug in `CategoricalDtype.__eq__()` returning`False` for unordered categorical data with mixed types (GH 55468)
- Bug when casting `pa.dictionary` to`CategoricalDtype` using a`pa.DictionaryArray` as categories (GH 56672)

### Datetimelike#

- Bug in `DatetimeIndex` construction when passing both a`tz` and either`dayfirst` or`yearfirst` ignoring dayfirst/yearfirst (GH 55813)
- Bug in `DatetimeIndex` when passing an object-dtype ndarray of float objects and a`tz` incorrectly localizing the result (GH 55780)
- Bug in `Series.isin()` with`DatetimeTZDtype` dtype and comparison values that are all`NaT` incorrectly returning all-`False` even if the series contains`NaT` entries (GH 56427)
- Bug in `concat()` raising`AttributeError` when concatenating all-NA DataFrame with`DatetimeTZDtype` dtype DataFrame (GH 52093)
- Bug in `testing.assert_extension_array_equal()` that could use the wrong unit when comparing resolutions (GH 55730)
- Bug in `to_datetime()` and`DatetimeIndex` when passing a list of mixed-string-and-numeric types incorrectly raising (GH 55780)
- Bug in `to_datetime()` and`DatetimeIndex` when passing mixed-type objects with a mix of timezones or mix of timezone-awareness failing to raise`ValueError` (GH 55693)
- Bug in `Tick.delta()` with very large ticks raising`OverflowError` instead of`OutOfBoundsTimedelta` (GH 55503)
- Bug in `DatetimeIndex.shift()` with non-nanosecond resolution incorrectly returning with nanosecond resolution (GH 56117)
- Bug in `DatetimeIndex.union()` returning object dtype for tz-aware indexes with the same timezone but different units (GH 55238)
- Bug in `Index.is_monotonic_increasing()` and`Index.is_monotonic_decreasing()` always caching`Index.is_unique()` as`True` when first value in index is`NaT` (GH 55755)
- Bug in `Index.view()` to a datetime64 dtype with non-supported resolution incorrectly raising (GH 55710)
- Bug in `Series.dt.round()` with non-nanosecond resolution and`NaT` entries incorrectly raising`OverflowError` (GH 56158)
- Bug in `Series.fillna()` with non-nanosecond resolution dtypes and higher-resolution vector values returning incorrect (internally-corrupted) results (GH 56410)
- Bug in `Timestamp.unit()` being inferred incorrectly from an ISO8601 format string with minute or hour resolution and a timezone offset (GH 56208)
- Bug in `.astype` converting from a higher-resolution`datetime64` dtype to a lower-resolution`datetime64` dtype (e.g.`datetime64[us]->datetime64[ms]` ) silently overflowing with values near the lower implementation bound (GH 55979)
- Bug in adding or subtracting a `Week` offset to a`datetime64``Series` ,`Index` , or`DataFrame` column with non-nanosecond resolution returning incorrect results (GH 55583)
- Bug in addition or subtraction of `BusinessDay` offset with`offset` attribute to non-nanosecond`Index` ,`Series` , or`DataFrame` column giving incorrect results (GH 55608)
- Bug in addition or subtraction of `DateOffset` objects with microsecond components to`datetime64``Index` ,`Series` , or`DataFrame` columns with non-nanosecond resolution (GH 55595)
- Bug in addition or subtraction of very large `Tick` objects with`Timestamp` or`Timedelta` objects raising`OverflowError` instead of`OutOfBoundsTimedelta` (GH 55503)
- Bug in creating a `Index` ,`Series` , or`DataFrame` with a non-nanosecond`DatetimeTZDtype` and inputs that would be out of bounds with nanosecond resolution incorrectly raising`OutOfBoundsDatetime` (GH 54620)
- Bug in creating a `Index` ,`Series` , or`DataFrame` with a non-nanosecond`datetime64` (or`DatetimeTZDtype` ) from mixed-numeric inputs treating those as nanoseconds instead of as multiples of the dtype’s unit (which would happen with non-mixed numeric inputs) (GH 56004)
- Bug in creating a `Index` ,`Series` , or`DataFrame` with a non-nanosecond`datetime64` dtype and inputs that would be out of bounds for a`datetime64[ns]` incorrectly raising`OutOfBoundsDatetime` (GH 55756)
- Bug in parsing datetime strings with nanosecond resolution with non-ISO8601 formats incorrectly truncating sub-microsecond components (GH 56051)
- Bug in parsing datetime strings with sub-second resolution and trailing zeros incorrectly inferring second or millisecond resolution (GH 55737)
- Bug in the results of `to_datetime()` with an floating-dtype argument with`unit` not matching the pointwise results of`Timestamp` (GH 56037)
- Fixed regression where `concat()` would raise an error when concatenating`datetime64` columns with differing resolutions (GH 53641)

### Timedelta#

- Bug in `Timedelta` construction raising`OverflowError` instead of`OutOfBoundsTimedelta` (GH 55503)
- Bug in rendering ( `__repr__` ) of`TimedeltaIndex` and`Series` with timedelta64 values with non-nanosecond resolution entries that are all multiples of 24 hours failing to use the compact representation used in the nanosecond cases (GH 55405)

### Timezones#

- Bug in `AbstractHolidayCalendar` where timezone data was not propagated when computing holiday observances (GH 54580)
- Bug in `Timestamp` construction with an ambiguous value and a`pytz` timezone failing to raise`pytz.AmbiguousTimeError` (GH 55657)
- Bug in `Timestamp.tz_localize()` with`nonexistent="shift_forward` around UTC+0 during DST (GH 51501)

### Numeric#

- Bug in `read_csv()` with`engine="pyarrow"` causing rounding errors for large integers (GH 52505)
- Bug in `Series.__floordiv__()` and`Series.__truediv__()` for`ArrowDtype` with integral dtypes raising for large divisors (GH 56706)
- Bug in `Series.__floordiv__()` for`ArrowDtype` with integral dtypes raising for large values (GH 56645)
- Bug in `Series.pow()` not filling missing values correctly (GH 55512)
- Bug in `Series.replace()` and`DataFrame.replace()` matching float`0.0` with`False` and vice versa (GH 55398)
- Bug in `Series.round()` raising for nullable boolean dtype (GH 55936)

### Conversion#

- Bug in `DataFrame.astype()` when called with`str` on unpickled array - the array might change in-place (GH 54654)
- Bug in `DataFrame.astype()` where`errors="ignore"` had no effect for extension types (GH 54654)
- Bug in `DataFrame.loc()` was not throwing “incompatible dtype warning” (see PDEP6) when assigning a`Series` with a different dtype using a full column setter (e.g.`df.loc[:, 'a'] = incompatible_value` ) (GH 39584)
- Bug in `Series.convert_dtypes()` not converting all NA column to`null[pyarrow]` (GH 55346)

### Strings#

- Bug in `pandas.api.types.is_string_dtype()` while checking object array with no elements is of the string dtype (GH 54661)
- Bug in `DataFrame.apply()` failing when`engine="numba"` and columns or index have`StringDtype` (GH 56189)
- Bug in `DataFrame.reindex()` not matching`Index` with`string[pyarrow_numpy]` dtype (GH 56106)
- Bug in `Index.str.cat()` always casting result to object dtype (GH 56157)
- Bug in `Series.__mul__()` for`ArrowDtype` with`pyarrow.string` dtype and`string[pyarrow]` for the pyarrow backend (GH 51970)
- Bug in `Series.str.find()` when`start < 0` for`ArrowDtype` with`pyarrow.string` (GH 56411)
- Bug in `Series.str.fullmatch()` when`dtype=pandas.ArrowDtype(pyarrow.string())` allows partial matches when regex ends in literal //$ (GH 56652)
- Bug in `Series.str.replace()` when`n < 0` for`ArrowDtype` with`pyarrow.string` (GH 56404)
- Bug in `Series.str.startswith()` and`Series.str.endswith()` with arguments of type`tuple[str, ...]` for`ArrowDtype` with`pyarrow.string` dtype (GH 56579)
- Bug in `Series.str.startswith()` and`Series.str.endswith()` with arguments of type`tuple[str, ...]` for`string[pyarrow]` (GH 54942)
- Bug in comparison operations for `dtype="string[pyarrow_numpy]"` raising if dtypes can’t be compared (GH 56008)

### Interval#

- Bug in `Interval``__repr__` not displaying UTC offsets for`Timestamp` bounds. Additionally the hour, minute and second components will now be shown (GH 55015)
- Bug in `IntervalIndex.factorize()` and`Series.factorize()` with`IntervalDtype` with datetime64 or timedelta64 intervals not preserving non-nanosecond units (GH 56099)
- Bug in `IntervalIndex.from_arrays()` when passed`datetime64` or`timedelta64` arrays with mismatched resolutions constructing an invalid`IntervalArray` object (GH 55714)
- Bug in `IntervalIndex.from_tuples()` raising if subtype is a nullable extension dtype (GH 56765)
- Bug in `IntervalIndex.get_indexer()` with datetime or timedelta intervals incorrectly matching on integer targets (GH 47772)
- Bug in `IntervalIndex.get_indexer()` with timezone-aware datetime intervals incorrectly matching on a sequence of timezone-naive targets (GH 47772)
- Bug in setting values on a `Series` with an`IntervalIndex` using a slice incorrectly raising (GH 54722)

### Indexing#

- Bug in `DataFrame.loc()` mutating a boolean indexer when`DataFrame` has a`MultiIndex` (GH 56635)
- Bug in `DataFrame.loc()` when setting`Series` with extension dtype into NumPy dtype (GH 55604)
- Bug in `Index.difference()` not returning a unique set of values when`other` is empty or`other` is considered non-comparable (GH 55113)
- Bug in setting `Categorical` values into a`DataFrame` with numpy dtypes raising`RecursionError` (GH 52927)
- Fixed bug when creating new column with missing values when setting a single string value (GH 56204)

### Missing#

- Bug in `DataFrame.update()` wasn’t updating in-place for tz-aware datetime64 dtypes (GH 56227)

### MultiIndex#

- Bug in `MultiIndex.get_indexer()` not raising`ValueError` when`method` provided and index is non-monotonic (GH 53452)

### I/O#

- Bug in `read_csv()` where`engine="python"` did not respect`chunksize` arg when`skiprows` was specified (GH 56323)
- Bug in `read_csv()` where`engine="python"` was causing a`TypeError` when a callable`skiprows` and a chunk size was specified (GH 55677)
- Bug in `read_csv()` where`on_bad_lines="warn"` would write to`stderr` instead of raising a Python warning; this now yields a`errors.ParserWarning` (GH 54296)
- Bug in `read_csv()` with`engine="pyarrow"` where`quotechar` was ignored (GH 52266)
- Bug in `read_csv()` with`engine="pyarrow"` where`usecols` wasn’t working with a CSV with no headers (GH 54459)
- Bug in `read_excel()` , with`engine="xlrd"` (`xls` files) erroring when the file contains`NaN` or`Inf` (GH 54564)
- Bug in `read_json()` not handling dtype conversion properly if`infer_string` is set (GH 56195)
- Bug in `DataFrame.to_excel()` , with`OdsWriter` (`ods` files) writing Boolean/string value (GH 54994)
- Bug in `DataFrame.to_hdf()` and`read_hdf()` with`datetime64` dtypes with non-nanosecond resolution failing to round-trip correctly (GH 55622)
- Bug in `DataFrame.to_stata()` raising for extension dtypes (GH 54671)
- Bug in `read_excel()` with`engine="odf"` (`ods` files) when a string cell contains an annotation (GH 55200)
- Bug in `read_excel()` with an ODS file without cached formatted cell for float values (GH 55219)
- Bug where `DataFrame.to_json()` would raise an`OverflowError` instead of a`TypeError` with unsupported NumPy types (GH 55403)

### Period#

- Bug in `PeriodIndex` construction when more than one of`data` ,`ordinal` and`**fields` are passed failing to raise`ValueError` (GH 55961)
- Bug in `Period` addition silently wrapping around instead of raising`OverflowError` (GH 55503)
- Bug in casting from `PeriodDtype` with`astype` to`datetime64` or`DatetimeTZDtype` with non-nanosecond unit incorrectly returning with nanosecond unit (GH 55958)

### Plotting#

- Bug in `DataFrame.plot.box()` with`vert=False` and a Matplotlib`Axes` created with`sharey=True` (GH 54941)
- Bug in `DataFrame.plot.scatter()` discarding string columns (GH 56142)
- Bug in `Series.plot()` when reusing an`ax` object failing to raise when a`how` keyword is passed (GH 55953)

### Groupby/resample/rolling#

- Bug in `DataFrameGroupBy.idxmin()` ,`DataFrameGroupBy.idxmax()` ,`SeriesGroupBy.idxmin()` , and`SeriesGroupBy.idxmax()` would not retain`Categorical` dtype when the index was a`CategoricalIndex` that contained NA values (GH 54234)
- Bug in `DataFrameGroupBy.transform()` and`SeriesGroupBy.transform()` when`observed=False` and`f="idxmin"` or`f="idxmax"` would incorrectly raise on unobserved categories (GH 54234)
- Bug in `DataFrameGroupBy.value_counts()` and`SeriesGroupBy.value_counts()` could result in incorrect sorting if the columns of the DataFrame or name of the Series are integers (GH 55951)
- Bug in `DataFrameGroupBy.value_counts()` and`SeriesGroupBy.value_counts()` would not respect`sort=False` in`DataFrame.groupby()` and`Series.groupby()` (GH 55951)
- Bug in `DataFrameGroupBy.value_counts()` and`SeriesGroupBy.value_counts()` would sort by proportions rather than frequencies when`sort=True` and`normalize=True` (GH 55951)
- Bug in `DataFrame.asfreq()` and`Series.asfreq()` with a`DatetimeIndex` with non-nanosecond resolution incorrectly converting to nanosecond resolution (GH 55958)
- Bug in `DataFrame.ewm()` when passed`times` with non-nanosecond`datetime64` or`DatetimeTZDtype` dtype (GH 56262)
- Bug in `DataFrame.groupby()` and`Series.groupby()` where grouping by a combination of`Decimal` and NA values would fail when`sort=True` (GH 54847)
- Bug in `DataFrame.groupby()` for DataFrame subclasses when selecting a subset of columns to apply the function to (GH 56761)
- Bug in `DataFrame.resample()` not respecting`closed` and`label` arguments for`BusinessDay` (GH 55282)
- Bug in `DataFrame.resample()` when resampling on a`ArrowDtype` of`pyarrow.timestamp` or`pyarrow.duration` type (GH 55989)
- Bug in `DataFrame.resample()` where bin edges were not correct for`BusinessDay` (GH 55281)
- Bug in `DataFrame.resample()` where bin edges were not correct for`MonthBegin` (GH 55271)
- Bug in `DataFrame.rolling()` and`Series.rolling()` where duplicate datetimelike indexes are treated as consecutive rather than equal with`closed='left'` and`closed='neither'` (GH 20712)
- Bug in `DataFrame.rolling()` and`Series.rolling()` where either the`index` or`on` column was`ArrowDtype` with`pyarrow.timestamp` type (GH 55849)

### Reshaping#

- Bug in `concat()` ignoring`sort` parameter when passed`DatetimeIndex` indexes (GH 54769)
- Bug in `concat()` renaming`Series` when`ignore_index=False` (GH 15047)
- Bug in `merge_asof()` raising`TypeError` when`by` dtype is not`object` ,`int64` , or`uint64` (GH 22794)
- Bug in `merge_asof()` raising incorrect error for string dtype (GH 56444)
- Bug in `merge_asof()` when using a`Timedelta` tolerance on a`ArrowDtype` column (GH 56486)
- Bug in `merge()` not raising when merging datetime columns with timedelta columns (GH 56455)
- Bug in `merge()` not raising when merging string columns with numeric columns (GH 56441)
- Bug in `merge()` not sorting for new string dtype (GH 56442)
- Bug in `merge()` returning columns in incorrect order when left and/or right is empty (GH 51929)
- Bug in `DataFrame.melt()` where an exception was raised if`var_name` was not a string (GH 55948)
- Bug in `DataFrame.melt()` where it would not preserve the datetime (GH 55254)
- Bug in `DataFrame.pivot_table()` where the row margin is incorrect when the columns have numeric names (GH 26568)
- Bug in `DataFrame.pivot()` with numeric columns and extension dtype for data (GH 56528)
- Bug in `DataFrame.stack()` with`future_stack=True` would not preserve NA values in the index (GH 56573)

### Sparse#

- Bug in `arrays.SparseArray.take()` when using a different fill value than the array’s fill value (GH 55181)

### Other#

- `DataFrame.__dataframe__()` did not support pyarrow large strings (GH 56702)
- Bug in `DataFrame.describe()` when formatting percentiles in the resulting percentile 99.999% is rounded to 100% (GH 55765)
- Bug in `api.interchange.from_dataframe()` where it raised`NotImplementedError` when handling empty string columns (GH 56703)
- Bug in `cut()` and`qcut()` with`datetime64` dtype values with non-nanosecond units incorrectly returning nanosecond-unit bins (GH 56101)
- Bug in `cut()` incorrectly allowing cutting of timezone-aware datetimes with timezone-naive bins (GH 54964)
- Bug in `infer_freq()` and`DatetimeIndex.inferred_freq()` with weekly frequencies and non-nanosecond resolutions (GH 55609)
- Bug in `DataFrame.apply()` where passing`raw=True` ignored`args` passed to the applied function (GH 55009)
- Bug in `DataFrame.from_dict()` which would always sort the rows of the created`DataFrame` .  (GH 55683)
- Bug in `DataFrame.sort_index()` when passing`axis="columns"` and`ignore_index=True` raising a`ValueError` (GH 56478)
- Bug in rendering `inf` values inside a`DataFrame` with the`use_inf_as_na` option enabled (GH 55483)
- Bug in rendering a `Series` with a`MultiIndex` when one of the index level’s names is 0 not having that name displayed (GH 55415)
- Bug in the error message when assigning an empty `DataFrame` to a column (GH 55956)
- Bug when time-like strings were being cast to `ArrowDtype` with`pyarrow.time64` type (GH 56463)
- Fixed a spurious deprecation warning from `numba` >= 0.58.0 when passing a numpy ufunc in`core.window.Rolling.apply` with`engine="numba"` (GH 55247)

## Contributors#

A total of 162 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- AG
- Aaron Rahman +
- Abdullah Ihsan Secer +
- Abhijit Deo +
- Adrian D’Alessandro
- Ahmad Mustafa Anis +
- Amanda Bizzinotto
- Amith KK +
- Aniket Patil +
- Antonio Fonseca +
- Artur Barseghyan
- Ben Greiner
- Bill Blum +
- Boyd Kane
- Damian Kula
- Dan King +
- Daniel Weindl +
- Daniele Nicolodi
- David Poznik
- David Toneian +
- Dea María Léon
- Deepak George +
- Dmitriy +
- Dominique Garmier +
- Donald Thevalingam +
- Doug Davis +
- Dukastlik +
- Elahe Sharifi +
- Eric Han +
- Fangchen Li
- Francisco Alfaro +
- Gadea Autric +
- Guillaume Lemaitre
- Hadi Abdi Khojasteh
- Hedeer El Showk +
- Huanghz2001 +
- Isaac Virshup
- Issam +
- Itay Azolay +
- Itayazolay +
- Jaca +
- Jack McIvor +
- JackCollins91 +
- James Spencer +
- Jay
- Jessica Greene
- Jirka Borovec +
- JohannaTrost +
- John C +
- Joris Van den Bossche
- José Lucas Mayer +
- José Lucas Silva Mayer +
- João Andrade +
- Kai Mühlbauer
- Katharina Tielking, MD +
- Kazuto Haruguchi +
- Kevin
- Lawrence Mitchell
- Linus +
- Linus Sommer +
- Louis-Émile Robitaille +
- Luke Manley
- Lumberbot (aka Jack)
- Maggie Liu +
- MainHanzo +
- Marc Garcia
- Marco Edward Gorelli
- MarcoGorelli
- Martin Šícho +
- Mateusz Sokół
- Matheus Felipe +
- Matthew Roeschke
- Matthias Bussonnier
- Maxwell Bileschi +
- Michael Tiemann
- Michał Górny
- Molly Bowers +
- Moritz Schubert +
- NNLNR +
- Natalia Mokeeva
- Nils Müller-Wendt +
- Omar Elbaz
- Pandas Development Team
- Paras Gupta +
- Parthi
- Patrick Hoefler
- Paul Pellissier +
- Paul Uhlenbruck +
- Philip Meier
- Philippe THOMY +
- Quang Nguyễn
- Raghav
- Rajat Subhra Mukherjee
- Ralf Gommers
- Randolf Scholz +
- Richard Shadrach
- Rob +
- Rohan Jain +
- Ryan Gibson +
- Sai-Suraj-27 +
- Samuel Oranyeli +
- Sara Bonati +
- Sebastian Berg
- Sergey Zakharov +
- Shyamala Venkatakrishnan +
- StEmGeo +
- Stefanie Molin
- Stijn de Gooijer +
- Thiago Gariani +
- Thomas A Caswell
- Thomas Baumann +
- Thomas Guillet +
- Thomas Lazarus +
- Thomas Li
- Tim Hoffmann
- Tim Swast
- Tom Augspurger
- Toro +
- Torsten Wörtwein
- Ville Aikas +
- Vinita Parasrampuria +
- Vyas Ramasubramani +
- William Andrea
- William Ayd
- Willian Wang +
- Xiao Yuan
- Yao Xiao
- Yves Delley
- Zemux1613 +
- Ziad Kermadi +
- aaron-robeson-8451 +
- aram-cinnamon +
- caneff +
- ccccjone +
- chris-caballero +
- cobalt
- color455nm +
- denisrei +
- dependabot[bot]
- jbrockmendel
- jfadia +
- johanna.trost +
- kgmuzungu +
- mecopur +
- mhb143 +
- morotti +
- mvirts +
- omar-elbaz
- paulreece
- pre-commit-ci[bot]
- raj-thapa
- rebecca-palmer
- rmhowe425
- rohanjain101
- shiersansi +
- smij720
- srkds +
- taytzehao
- torext
- vboxuser +
- xzmeng +
- yashb +