# What’s new in 2.0.0 (April 3, 2023)#

These are the changes in pandas 2.0.0. See Release notes for a full changelog including other versions of pandas.

## Enhancements#

### Installing optional dependencies with pip extras#

When installing pandas using pip, sets of optional dependencies can also be installed by specifying extras.

```
pip install "pandas[performance, aws]>=2.0.0"
```
The available extras, found in the installation guide, are
```
[all, performance, computation, fss, aws, gcp, excel, parquet, feather, hdf5, spss, postgresql, mysql,
sql-other, html, xml, plot, output_formatting, clipboard, compression, test]
```
 (GH 39164).

### `Index` can now hold numpy numeric dtypes#

It is now possible to use any numpy numeric dtype in a `Index` (GH 42717).

Previously it was only possible to use `int64`, `uint64` & `float64` dtypes:

```
In [1]: pd.Index([1, 2, 3], dtype=np.int8)
Out[1]: Int64Index([1, 2, 3], dtype="int64")
In [2]: pd.Index([1, 2, 3], dtype=np.uint16)
Out[2]: UInt64Index([1, 2, 3], dtype="uint64")
In [3]: pd.Index([1, 2, 3], dtype=np.float32)
Out[3]: Float64Index([1.0, 2.0, 3.0], dtype="float64")
```
`Int64Index`, `UInt64Index` & `Float64Index` were deprecated in pandas
version 1.4 and have now been removed. Instead `Index` should be used directly, and
can it now take all numpy numeric dtypes, i.e.
`int8`/ `int16`/`int32`/`int64`/`uint8`/`uint16`/`uint32`/`uint64`/`float32`/`float64` dtypes:

```
In [1]: pd.Index([1, 2, 3], dtype=np.int8)
Out[1]: Index([1, 2, 3], dtype='int8')
In [2]: pd.Index([1, 2, 3], dtype=np.uint16)
Out[2]: Index([1, 2, 3], dtype='uint16')
In [3]: pd.Index([1, 2, 3], dtype=np.float32)
Out[3]: Index([1.0, 2.0, 3.0], dtype='float32')
```
The ability for `Index` to hold the numpy numeric dtypes has meant some changes in pandas
functionality. In particular, operations that previously were forced to create 64-bit indexes,
can now create indexes with lower bit sizes, e.g. 32-bit indexes.

Below is a possibly non-exhaustive list of changes:

1. Instantiating using a numpy numeric array now follows the dtype of the numpy array. Previously, all indexes created from numpy numeric arrays were forced to 64-bit. Now, for example, `Index(np.array([1, 2, 3]))` will be`int32` on 32-bit systems, where
it previously would have been`int64` even on 32-bit systems.
Instantiating`Index` using a list of numbers will still return 64bit dtypes,
e.g.`Index([1, 2, 3])` will have a`int64` dtype, which is the same as previously.
2. The various numeric datetime attributes of `DatetimeIndex` (`day` ,`month` ,`year` etc.) were previously in of
dtype`int64` , while they were`int32` for`arrays.DatetimeArray` . They are now`int32` on`DatetimeIndex` also:In [4]: idx = pd.date_range(start='1/1/2018', periods=3, freq='ME') In [5]: idx.array.year Out[5]: array([2018, 2018, 2018], dtype=int32) In [6]: idx.year Out[6]: Index([2018, 2018, 2018], dtype='int32')
3. Level dtypes on Indexes from `Series.sparse.from_coo()` are now of dtype`int32` ,
the same as they are on the`rows` /`cols` on a scipy sparse matrix. Previously they
were of dtype`int64` .In [7]: from scipy import sparse In [8]: A = sparse.coo_matrix( ...: ([3.0, 1.0, 2.0], ([1, 0, 0], [0, 2, 3])), shape=(3, 4) ...: ) ...: In [9]: ser = pd.Series.sparse.from_coo(A) In [10]: ser.index.dtypes Out[10]: level_0 int32 level_1 int32 dtype: object
4. `Index` cannot be instantiated using a float16 dtype. Previously instantiating
an`Index` using dtype`float16` resulted in a`Float64Index` with a`float64` dtype. It now raises a`NotImplementedError` :In [11]: pd.Index([1, 2, 3], dtype=np.float16) --------------------------------------------------------------------------- NotImplementedError Traceback (most recent call last) Cell In[11], line 1 ----> 1 pd.Index([1, 2, 3], dtype=np.float16) File ~/work/pandas/pandas/pandas/core/indexes/base.py:586, in Index.__new__(cls, data, dtype, copy, name, tupleize_cols) 582 arr = ensure_wrapped_if_datetimelike(arr) # type: ignore[no-untyped-call] 584 klass = cls._dtype_to_subclass(arr.dtype) --> 586 arr = klass._ensure_array(arr, arr.dtype, copy=False) 587 out = klass._simple_new(arr, name, refs=refs) 588 # Preserve freq when wrapping a DatetimeIndex/TimedeltaIndex input, 589 # since _simple_new doesn't copy Index-level attributes like _freq. File ~/work/pandas/pandas/pandas/core/indexes/base.py:606, in Index._ensure_array(cls, data, dtype, copy) 603 raise ValueError("Index data must be 1-dimensional") 604 elif dtype == np.float16: 605 # float16 not supported (no indexing engine) --> 606 raise NotImplementedError("float16 indexes are not supported") 608 if copy: 609 # asarray_tuplesafe does not always copy underlying data, 610 # so need to make sure that this happens 611 data = data.copy() NotImplementedError: float16 indexes are not supported

### Argument `dtype_backend`, to return pyarrow-backed or numpy-backed nullable dtypes#

The following functions gained a new keyword `dtype_backend` (GH 36712)

When this option is set to `"numpy_nullable"` it will return a `DataFrame` that is
backed by nullable dtypes.

When this keyword is set to `"pyarrow"`, then these functions will return pyarrow-backed nullable `ArrowDtype` DataFrames (GH 48957, GH 49997):

```
In [12]: import io
In [13]: data = io.StringIO("""a,b,c,d,e,f,g,h,i
   ....:     1,2.5,True,a,,,,,
   ....:     3,4.5,False,b,6,7.5,True,a,
   ....: """)
   ....: 
In [14]: df = pd.read_csv(data, dtype_backend="pyarrow")
In [15]: df.dtypes
Out[15]: 
a     int64[pyarrow]
b    double[pyarrow]
c      bool[pyarrow]
d    string[pyarrow]
e     int64[pyarrow]
f    double[pyarrow]
g      bool[pyarrow]
h    string[pyarrow]
i      null[pyarrow]
dtype: object
In [16]: data.seek(0)
Out[16]: 0
In [17]: df_pyarrow = pd.read_csv(data, dtype_backend="pyarrow", engine="pyarrow")
In [18]: df_pyarrow.dtypes
Out[18]: 
a     int64[pyarrow]
b    double[pyarrow]
c      bool[pyarrow]
d    string[pyarrow]
e     int64[pyarrow]
f    double[pyarrow]
g      bool[pyarrow]
h    string[pyarrow]
i      null[pyarrow]
dtype: object
```
### Copy-on-Write improvements#

- A new lazy copy mechanism that defers the copy until the object in question is modified was added to the methods listed in Copy-on-Write optimizations. These methods return views when Copy-on-Write is enabled, which provides a significant performance improvement compared to the regular execution (GH 49473).
- Accessing a single column of a DataFrame as a Series (e.g. `df["col"]` ) now always
returns a new object every time it is constructed when Copy-on-Write is enabled (not
returning multiple times an identical, cached Series object). This ensures that those
Series objects correctly follow the Copy-on-Write rules (GH 49450)
- The `Series` constructor will now create a lazy copy (deferring the copy until
a modification to the data happens) when constructing a Series from an existing
Series with the default of`copy=False` (GH 50471)
- The `DataFrame` constructor will now create a lazy copy (deferring the copy until
a modification to the data happens) when constructing from an existing`DataFrame` with the default of`copy=False` (GH 51239)
- The `DataFrame` constructor, when constructing a DataFrame from a dictionary
of Series objects and specifying`copy=False` , will now use a lazy copy
of those Series objects for the columns of the DataFrame (GH 50777)
- The `DataFrame` constructor, when constructing a DataFrame from a`Series` or`Index` and specifying`copy=False` , will
now respect Copy-on-Write.
- The `DataFrame` and`Series` constructors, when constructing from
a NumPy array, will now copy the array by default to avoid mutating
the`DataFrame` /`Series` when mutating the array. Specify`copy=False` to get the old behavior.
When setting`copy=False` pandas does not guarantee correct Copy-on-Write
behavior when the NumPy array is modified after creation of the`DataFrame` /`Series` .
- The `DataFrame.from_records()` will now respect Copy-on-Write when called
with a`DataFrame` .
- Trying to set values using chained assignment (for example, `df["a"][1:3] = 0` )
will now always raise a warning when Copy-on-Write is enabled. In this mode,
chained assignment can never work because we are always setting into a temporary
object that is the result of an indexing operation (getitem), which under
Copy-on-Write always behaves as a copy. Thus, assigning through a chain
can never update the original Series or DataFrame. Therefore, an informative
warning is raised to the user to avoid silently doing nothing (GH 49467)
- `DataFrame.replace()` will now respect the Copy-on-Write mechanism
when`inplace=True` .
- `DataFrame.transpose()` will now respect the Copy-on-Write mechanism.
- Arithmetic operations that can be inplace, e.g. `ser *= 2` will now respect the
Copy-on-Write mechanism.
- `DataFrame.__getitem__()` will now respect the Copy-on-Write mechanism when the`DataFrame` has`MultiIndex` columns.
  - `Series.__getitem__()` will now respect the Copy-on-Write mechanism when the
  - `Series` has a`MultiIndex` .
- `Series.view()` will now respect the Copy-on-Write mechanism.

Copy-on-Write can be enabled through one of

```
pd.set_option("mode.copy_on_write", True)
```
```
pd.options.mode.copy_on_write = True
```
Alternatively, copy on write can be enabled locally through:

```
with pd.option_context("mode.copy_on_write", True):
    ...
```
### Other enhancements#

- Added support for `str` accessor methods when using`ArrowDtype` with a`pyarrow.string` type (GH 50325)
- Added support for `dt` accessor methods when using`ArrowDtype` with a`pyarrow.timestamp` type (GH 50954)
- `read_sas()` now supports using`encoding='infer'` to correctly read and use the encoding specified by the sas file. (GH 48048)
- `DataFrameGroupBy.quantile()` ,`SeriesGroupBy.quantile()` and`DataFrameGroupBy.std()` now preserve nullable dtypes instead of casting to numpy dtypes (GH 37493)
- `DataFrameGroupBy.std()` ,`SeriesGroupBy.std()` now support datetime64, timedelta64, and`DatetimeTZDtype` dtypes (GH 48481)
- `Series.add_suffix()` ,`DataFrame.add_suffix()` ,`Series.add_prefix()` and`DataFrame.add_prefix()` support an`axis` argument. If`axis` is set, the default behaviour of which axis to consider can be overwritten (GH 47819)
- `testing.assert_frame_equal()` now shows the first element where the DataFrames differ, analogously to`pytest` ’s output (GH 47910)
- Added `index` parameter to`DataFrame.to_dict()` (GH 46398)
- Added support for extension array dtypes in `merge()` (GH 44240)
- Added metadata propagation for binary operators on `DataFrame` (GH 28283)
- Added `cumsum` ,`cumprod` ,`cummin` and`cummax` to the`ExtensionArray` interface via`_accumulate` (GH 28385)
- `CategoricalConversionWarning` ,`InvalidComparison` ,`InvalidVersion` ,`LossySetitemError` , and`NoBufferPresent` are now exposed in`pandas.errors` (GH 27656)
- Fix `test` optional_extra by adding missing test package`pytest-asyncio` (GH 48361)
- `DataFrame.astype()` exception message thrown improved to include column name when type conversion is not possible. (GH 47571)
- `date_range()` now supports a`unit` keyword (“s”, “ms”, “us”, or “ns”) to specify the desired resolution of the output index (GH 49106)
- `timedelta_range()` now supports a`unit` keyword (“s”, “ms”, “us”, or “ns”) to specify the desired resolution of the output index (GH 49824)
- `DataFrame.to_json()` now supports a`mode` keyword with supported inputs ‘w’ and ‘a’. Defaulting to ‘w’, ‘a’ can be used when lines=True and orient=’records’ to append record oriented json lines to an existing json file. (GH 35849)
- Added `name` parameter to`IntervalIndex.from_breaks()` ,`IntervalIndex.from_arrays()` and`IntervalIndex.from_tuples()` (GH 48911)
- Improve exception message when using `testing.assert_frame_equal()` on a`DataFrame` to include the column that is compared (GH 50323)
- Improved error message for `merge_asof()` when join-columns were duplicated (GH 50102)
- Added support for extension array dtypes to `get_dummies()` (GH 32430)
- Added `Index.infer_objects()` analogous to`Series.infer_objects()` (GH 50034)
- Added `copy` parameter to`Series.infer_objects()` and`DataFrame.infer_objects()` , passing`False` will avoid making copies for series or columns that are already non-object or where no better dtype can be inferred (GH 50096)
- `DataFrame.plot.hist()` now recognizes`xlabel` and`ylabel` arguments (GH 49793)
- `Series.drop_duplicates()` has gained`ignore_index` keyword to reset index (GH 48304)
- `Series.dropna()` and`DataFrame.dropna()` has gained`ignore_index` keyword to reset index (GH 31725)
- Improved error message in `to_datetime()` for non-ISO8601 formats, informing users about the position of the first error (GH 50361)
- Improved error message when trying to align `DataFrame` objects (for example, in`DataFrame.compare()` ) to clarify that “identically labelled” refers to both index and columns (GH 50083)
- Added support for `Index.min()` and`Index.max()` for pyarrow string dtypes (GH 51397)
- Added `DatetimeIndex.as_unit()` and`TimedeltaIndex.as_unit()` to convert to different resolutions; supported resolutions are “s”, “ms”, “us”, and “ns” (GH 50616)
- Added `Series.dt.unit()` and`Series.dt.as_unit()` to convert to different resolutions; supported resolutions are “s”, “ms”, “us”, and “ns” (GH 51223)
- Added new argument `dtype` to`read_sql()` to be consistent with`read_sql_query()` (GH 50797)
- `read_csv()` ,`read_table()` ,`read_fwf()` and`read_excel()` now accept`date_format` (GH 50601)
- `to_datetime()` now accepts`"ISO8601"` as an argument to`format` , which will match any ISO8601 string (but possibly not identically-formatted) (GH 50411)
- `to_datetime()` now accepts`"mixed"` as an argument to`format` , which will infer the format for each element individually (GH 50972)
- Added new argument `engine` to`read_json()` to support parsing JSON with pyarrow by specifying`engine="pyarrow"` (GH 48893)
- Added support for SQLAlchemy 2.0 (GH 40686)
- Added support for `decimal` parameter when`engine="pyarrow"` in`read_csv()` (GH 51302)
- `Index` set operations`Index.union()` ,`Index.intersection()` ,`Index.difference()` , and`Index.symmetric_difference()` now support`sort=True` , which will always return a sorted result, unlike the default`sort=None` which does not sort in some cases (GH 25151)
- Added new escape mode “latex-math” to avoid escaping “$” in formatter (GH 50040)

## Notable bug fixes#

These are bug fixes that might have notable behavior changes.

### `DataFrameGroupBy.cumsum()` and `DataFrameGroupBy.cumprod()` overflow instead of lossy casting to float#

In previous versions we cast to float when applying `cumsum` and `cumprod` which
lead to incorrect results even if the result could be hold by `int64` dtype.
Additionally, the aggregation overflows consistent with numpy and the regular
`DataFrame.cumprod()` and `DataFrame.cumsum()` methods when the limit of
`int64` is reached (GH 37493).

*Old Behavior*

```
In [1]: df = pd.DataFrame({"key": ["b"] * 7, "value": 625})
In [2]: df.groupby("key")["value"].cumprod()[5]
Out[2]: 5.960464477539062e+16
```
We return incorrect results with the 6th value.

*New Behavior*

```
In [19]: df = pd.DataFrame({"key": ["b"] * 7, "value": 625})
In [20]: df.groupby("key")["value"].cumprod()
Out[20]: 
0                   625
1                390625
2             244140625
3          152587890625
4        95367431640625
5     59604644775390625
6    359414837200037393
Name: value, dtype: int64
```
We overflow with the 7th value, but the 6th value is still correct.

### `DataFrameGroupBy.nth()` and `SeriesGroupBy.nth()` now behave as filtrations#

In previous versions of pandas, `DataFrameGroupBy.nth()` and
`SeriesGroupBy.nth()` acted as if they were aggregations. However, for most
inputs `n`, they may return either zero or multiple rows per group. This means
that they are filtrations, similar to e.g. `DataFrameGroupBy.head()`. pandas
now treats them as filtrations (GH 13666).

```
In [21]: df = pd.DataFrame({"a": [1, 1, 2, 1, 2], "b": [np.nan, 2.0, 3.0, 4.0, 5.0]})
In [22]: gb = df.groupby("a")
```
*Old Behavior*

```
In [5]: gb.nth(n=1)
Out[5]:
   A    B
1  1  2.0
4  2  5.0
```
*New Behavior*

```
In [23]: gb.nth(n=1)
Out[23]: 
   a    b
1  1  2.0
4  2  5.0
```
In particular, the index of the result is derived from the input by selecting
the appropriate rows. Also, when `n` is larger than the group, no rows instead of
`NaN` is returned.

*Old Behavior*

```
In [5]: gb.nth(n=3, dropna="any")
Out[5]:
    B
A
1 NaN
2 NaN
```
*New Behavior*

```
In [24]: gb.nth(n=3, dropna="any")
Out[24]: 
Empty DataFrame
Columns: [a, b]
Index: []
```
## Backwards incompatible API changes#

### Construction with datetime64 or timedelta64 dtype with unsupported resolution#

In past versions, when constructing a `Series` or `DataFrame` and
passing a “datetime64” or “timedelta64” dtype with unsupported resolution
(i.e. anything other than “ns”), pandas would silently replace the given dtype
with its nanosecond analogue:

*Previous behavior*:

```
In [5]: pd.Series(["2016-01-01"], dtype="datetime64[s]")
Out[5]:
0   2016-01-01
dtype: datetime64[ns]
In [6] pd.Series(["2016-01-01"], dtype="datetime64[D]")
Out[6]:
0   2016-01-01
dtype: datetime64[ns]
```
In pandas 2.0 we support resolutions “s”, “ms”, “us”, and “ns”. When passing a supported dtype (e.g. “datetime64[s]”), the result now has exactly the requested dtype:

*New behavior*:

```
In [25]: pd.Series(["2016-01-01"], dtype="datetime64[s]")
Out[25]: 
0   2016-01-01
dtype: datetime64[s]
```
With an un-supported dtype, pandas now raises instead of silently swapping in a supported dtype:

*New behavior*:

```
In [26]: pd.Series(["2016-01-01"], dtype="datetime64[D]")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[26], line 1
----> 1 pd.Series(["2016-01-01"], dtype="datetime64[D]")
File ~/work/pandas/pandas/pandas/core/series.py:497, in Series.__init__(self, data, index, dtype, name, copy)
    493                 data = data.astype(dtype=dtype)
    494             if copy:
    495                 data = data.copy(deep=True)
    496         else:
--> 497             data = sanitize_array(data, index, dtype, copy)
    498             data = SingleBlockManager.from_array(data, index, refs=refs)
    499 
    500         NDFrame.__init__(self, data)
File ~/work/pandas/pandas/pandas/core/construction.py:713, in sanitize_array(data, index, dtype, copy, allow_2d)
    710     subarr = np.array([], dtype=np.float64)
    712 elif dtype is not None:
--> 713     subarr = _try_cast(data, dtype, copy)
    715 else:
    716     subarr = construct_1d_object_array_from_listlike(data)
File ~/work/pandas/pandas/pandas/core/construction.py:884, in _try_cast(arr, dtype, copy)
    880         if arr.ndim == 2 and arr.shape[1] == 1:
    881             # GH#60081: DataFrame Constructor converts 1D data to array of
    882             # shape (N, 1), but maybe_cast_to_datetime assumes 1D input
    883             return maybe_cast_to_datetime(arr[:, 0], dtype).reshape(arr.shape)
--> 884     return maybe_cast_to_datetime(arr, dtype)
    886 # GH#15832: Check if we are requesting a numeric dtype and
    887 # that we can convert the data to the requested dtype.
    888 elif dtype.kind in "iu":
    889     # this will raise if we have e.g. floats
File ~/work/pandas/pandas/pandas/core/dtypes/cast.py:1092, in maybe_cast_to_datetime(value, dtype)
   1088     raise TypeError("value must be listlike")
   1090 # TODO: _from_sequence would raise ValueError in cases where
   1091 #  _ensure_nanosecond_dtype raises TypeError
-> 1092 _ensure_nanosecond_dtype(dtype)
   1094 if lib.is_np_dtype(dtype, "m"):
   1095     res = TimedeltaArray._from_sequence(value, dtype=dtype)
File ~/work/pandas/pandas/pandas/core/dtypes/cast.py:1149, in _ensure_nanosecond_dtype(dtype)
   1146     raise ValueError(msg)
   1147 # TODO: ValueError or TypeError? existing test
   1148 #  test_constructor_generic_timestamp_bad_frequency expects TypeError
-> 1149 raise TypeError(
   1150     f"dtype={dtype} is not supported. Supported resolutions are 's', "
   1151     "'ms', 'us', and 'ns'"
   1152 )
TypeError: dtype=datetime64[D] is not supported. Supported resolutions are 's', 'ms', 'us', and 'ns'
```
### Value counts sets the resulting name to `count`#

In past versions, when running `Series.value_counts()`, the result would inherit
the original object’s name, and the result index would be nameless. This would cause
confusion when resetting the index, and the column names would not correspond with the
column values.
Now, the result name will be `'count'` (or `'proportion'` if `normalize=True` was passed),
and the index will be named after the original object (GH 49497).

*Previous behavior*:

```
In [8]: pd.Series(['quetzal', 'quetzal', 'elk'], name='animal').value_counts()
Out[2]:
quetzal    2
elk        1
Name: animal, dtype: int64
```
*New behavior*:

```
In [27]: pd.Series(['quetzal', 'quetzal', 'elk'], name='animal').value_counts()
Out[27]: 
animal
quetzal    2
elk        1
Name: count, dtype: int64
```
Likewise for other `value_counts` methods (for example, `DataFrame.value_counts()`).

### Disallow astype conversion to non-supported datetime64/timedelta64 dtypes#

In previous versions, converting a `Series` or `DataFrame`
from `datetime64[ns]` to a different `datetime64[X]` dtype would return
with `datetime64[ns]` dtype instead of the requested dtype. In pandas 2.0,
support is added for “datetime64[s]”, “datetime64[ms]”, and “datetime64[us]” dtypes,
so converting to those dtypes gives exactly the requested dtype:

*Previous behavior*:

```
In [28]: idx = pd.date_range("2016-01-01", periods=3)
In [29]: ser = pd.Series(idx)
```
*Previous behavior*:

```
In [4]: ser.astype("datetime64[s]")
Out[4]:
0   2016-01-01
1   2016-01-02
2   2016-01-03
dtype: datetime64[ns]
```
With the new behavior, we get exactly the requested dtype:

*New behavior*:

```
In [30]: ser.astype("datetime64[s]")
Out[30]: 
0   2016-01-01
1   2016-01-02
2   2016-01-03
dtype: datetime64[s]
```
For non-supported resolutions e.g. “datetime64[D]”, we raise instead of silently ignoring the requested dtype:

*New behavior*:

```
In [31]: ser.astype("datetime64[D]")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[31], line 1
----> 1 ser.astype("datetime64[D]")
File ~/work/pandas/pandas/pandas/core/generic.py:6656, in NDFrame.astype(self, dtype, copy, errors)
   6652             results = [ser.astype(dtype, errors=errors) for _, ser in self.items()]
   6653 
   6654         else:
   6655             # else, only a single dtype is given
-> 6656             new_data = self._mgr.astype(dtype=dtype, errors=errors)
   6657             res = self._constructor_from_mgr(new_data, axes=new_data.axes)
   6658             return res.__finalize__(self, method="astype")
   6659 
File ~/work/pandas/pandas/pandas/core/internals/managers.py:632, in BaseBlockManager.astype(self, dtype, errors)
    631 def astype(self, dtype, errors: str = "raise") -> Self:
--> 632     return self.apply("astype", dtype=dtype, errors=errors)
File ~/work/pandas/pandas/pandas/core/internals/managers.py:450, in BaseBlockManager.apply(self, f, align_keys, **kwargs)
    448         applied = b.apply(f, **kwargs)
    449     else:
--> 450         applied = getattr(b, f)(**kwargs)
    451     result_blocks = extend_blocks(applied, result_blocks)
    453 out = type(self).from_blocks(result_blocks, [ax.view() for ax in self.axes])
File ~/work/pandas/pandas/pandas/core/internals/blocks.py:622, in Block.astype(self, dtype, errors, squeeze)
    619         raise ValueError("Can not squeeze with more than one column.")
    620     values = values[0, :]  # type: ignore[call-overload]
--> 622 new_values = astype_array_safe(values, dtype, errors=errors)
    624 new_values = maybe_coerce_values(new_values)
    626 refs = None
File ~/work/pandas/pandas/pandas/core/dtypes/astype.py:241, in astype_array_safe(values, dtype, copy, errors)
    238     dtype = dtype.numpy_dtype
    240 try:
--> 241     new_values = astype_array(values, dtype, copy=copy)
    242 except (ValueError, TypeError):
    243     # e.g. _astype_nansafe can fail on object-dtype of strings
    244     #  trying to convert to float
    245     if errors == "ignore":
File ~/work/pandas/pandas/pandas/core/dtypes/astype.py:183, in astype_array(values, dtype, copy)
    179     return values
    181 if not isinstance(values, np.ndarray):
    182     # i.e. ExtensionArray
--> 183     values = values.astype(dtype, copy=copy)
    185 else:
    186     values = _astype_nansafe(values, dtype, copy=copy)
File ~/work/pandas/pandas/pandas/core/arrays/datetimes.py:750, in DatetimeArray.astype(self, dtype, copy)
    748 elif isinstance(dtype, PeriodDtype):
    749     return self.to_period(freq=dtype.freq)
--> 750 return dtl.DatetimeLikeArrayMixin.astype(self, dtype, copy)
File ~/work/pandas/pandas/pandas/core/arrays/datetimelike.py:466, in DatetimeLikeArrayMixin.astype(self, dtype, copy)
    462 elif (dtype.kind in "mM" and self.dtype != dtype) or dtype.kind == "f":
    463     # disallow conversion between datetime/timedelta,
    464     # and conversions for any datetimelike to float
    465     msg = f"Cannot cast {type(self).__name__} to dtype {dtype}"
--> 466     raise TypeError(msg)
    467 else:
    468     return np.asarray(self, dtype=dtype)
TypeError: Cannot cast DatetimeArray to dtype datetime64[D]
```
For conversion from `timedelta64[ns]` dtypes, the old behavior converted
to a floating point format.

*Previous behavior*:

```
In [32]: idx = pd.timedelta_range("1 Day", periods=3)
In [33]: ser = pd.Series(idx)
```
*Previous behavior*:

```
In [7]: ser.astype("timedelta64[s]")
Out[7]:
0     86400.0
1    172800.0
2    259200.0
dtype: float64
In [8]: ser.astype("timedelta64[D]")
Out[8]:
0    1.0
1    2.0
2    3.0
dtype: float64
```
The new behavior, as for datetime64, either gives exactly the requested dtype or raises:

*New behavior*:

```
In [34]: ser.astype("timedelta64[s]")
Out[34]: 
0   1 days
1   2 days
2   3 days
dtype: timedelta64[s]
In [35]: ser.astype("timedelta64[D]")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[35], line 1
----> 1 ser.astype("timedelta64[D]")
File ~/work/pandas/pandas/pandas/core/generic.py:6656, in NDFrame.astype(self, dtype, copy, errors)
   6652             results = [ser.astype(dtype, errors=errors) for _, ser in self.items()]
   6653 
   6654         else:
   6655             # else, only a single dtype is given
-> 6656             new_data = self._mgr.astype(dtype=dtype, errors=errors)
   6657             res = self._constructor_from_mgr(new_data, axes=new_data.axes)
   6658             return res.__finalize__(self, method="astype")
   6659 
File ~/work/pandas/pandas/pandas/core/internals/managers.py:632, in BaseBlockManager.astype(self, dtype, errors)
    631 def astype(self, dtype, errors: str = "raise") -> Self:
--> 632     return self.apply("astype", dtype=dtype, errors=errors)
File ~/work/pandas/pandas/pandas/core/internals/managers.py:450, in BaseBlockManager.apply(self, f, align_keys, **kwargs)
    448         applied = b.apply(f, **kwargs)
    449     else:
--> 450         applied = getattr(b, f)(**kwargs)
    451     result_blocks = extend_blocks(applied, result_blocks)
    453 out = type(self).from_blocks(result_blocks, [ax.view() for ax in self.axes])
File ~/work/pandas/pandas/pandas/core/internals/blocks.py:622, in Block.astype(self, dtype, errors, squeeze)
    619         raise ValueError("Can not squeeze with more than one column.")
    620     values = values[0, :]  # type: ignore[call-overload]
--> 622 new_values = astype_array_safe(values, dtype, errors=errors)
    624 new_values = maybe_coerce_values(new_values)
    626 refs = None
File ~/work/pandas/pandas/pandas/core/dtypes/astype.py:241, in astype_array_safe(values, dtype, copy, errors)
    238     dtype = dtype.numpy_dtype
    240 try:
--> 241     new_values = astype_array(values, dtype, copy=copy)
    242 except (ValueError, TypeError):
    243     # e.g. _astype_nansafe can fail on object-dtype of strings
    244     #  trying to convert to float
    245     if errors == "ignore":
File ~/work/pandas/pandas/pandas/core/dtypes/astype.py:183, in astype_array(values, dtype, copy)
    179     return values
    181 if not isinstance(values, np.ndarray):
    182     # i.e. ExtensionArray
--> 183     values = values.astype(dtype, copy=copy)
    185 else:
    186     values = _astype_nansafe(values, dtype, copy=copy)
File ~/work/pandas/pandas/pandas/core/arrays/timedeltas.py:365, in TimedeltaArray.astype(self, dtype, copy)
    363         return type(self)._simple_new(res_values, dtype=res_values.dtype)
    364     else:
--> 365         raise ValueError(
    366             f"Cannot convert from {self.dtype} to {dtype}. "
    367             "Supported resolutions are 's', 'ms', 'us', 'ns'"
    368         )
    370 return dtl.DatetimeLikeArrayMixin.astype(self, dtype, copy=copy)
ValueError: Cannot convert from timedelta64[us] to timedelta64[D]. Supported resolutions are 's', 'ms', 'us', 'ns'
```
### UTC and fixed-offset timezones default to standard-library tzinfo objects#

In previous versions, the default `tzinfo` object used to represent UTC
was `pytz.UTC`. In pandas 2.0, we default to `datetime.timezone.utc` instead.
Similarly, for timezones represent fixed UTC offsets, we use `datetime.timezone`
objects instead of `pytz.FixedOffset` objects. See (GH 34916)

*Previous behavior*:

```
In [2]: ts = pd.Timestamp("2016-01-01", tz="UTC")
In [3]: type(ts.tzinfo)
Out[3]: pytz.UTC
In [4]: ts2 = pd.Timestamp("2016-01-01 04:05:06-07:00")
In [3]: type(ts2.tzinfo)
Out[5]: pytz._FixedOffset
```
*New behavior*:

```
In [36]: ts = pd.Timestamp("2016-01-01", tz="UTC")
In [37]: type(ts.tzinfo)
Out[37]: datetime.timezone
In [38]: ts2 = pd.Timestamp("2016-01-01 04:05:06-07:00")
In [39]: type(ts2.tzinfo)
Out[39]: datetime.timezone
```
For timezones that are neither UTC nor fixed offsets, e.g. “US/Pacific”, we
continue to default to `pytz` objects.

### Empty DataFrames/Series will now default to have a `RangeIndex`#

Before, constructing an empty (where `data` is `None` or an empty list-like argument) `Series` or `DataFrame` without
specifying the axes (`index=None`, `columns=None`) would return the axes as empty `Index` with object dtype.

Now, the axes return an empty `RangeIndex` (GH 49572).

*Previous behavior*:

```
In [8]: pd.Series().index
Out[8]:
Index([], dtype='object')
In [9] pd.DataFrame().axes
Out[9]:
[Index([], dtype='object'), Index([], dtype='object')]
```
*New behavior*:

```
In [40]: pd.Series().index
Out[40]: RangeIndex(start=0, stop=0, step=1)
In [41]: pd.DataFrame().axes
Out[41]: [RangeIndex(start=0, stop=0, step=1), RangeIndex(start=0, stop=0, step=1)]
```
### DataFrame to LaTeX has a new render engine#

The existing `DataFrame.to_latex()` has been restructured to utilise the
extended implementation previously available under `Styler.to_latex()`.
The arguments signature is similar, albeit `col_space` has been removed since
it is ignored by LaTeX engines. This render engine also requires `jinja2` as a
dependency which needs to be installed, since rendering is based upon jinja2 templates.

The pandas latex options below are no longer used and have been removed. The generic max rows and columns arguments remain but for this functionality should be replaced by the Styler equivalents. The alternative options giving similar functionality are indicated below:

- `display.latex.escape` : replaced with`styler.format.escape` ,
- `display.latex.longtable` : replaced with`styler.latex.environment` ,
- `display.latex.multicolumn` ,`display.latex.multicolumn_format` and`display.latex.multirow` : replaced with`styler.sparse.rows` ,`styler.sparse.columns` ,`styler.latex.multirow_align` and`styler.latex.multicol_align` ,
- `display.latex.repr` : replaced with`styler.render.repr` ,
- `display.max_rows` and`display.max_columns` : replace with`styler.render.max_rows` ,`styler.render.max_columns` and`styler.render.max_elements` .

Note that due to this change some defaults have also changed:

- `multirow` now defaults to*True* .
- `multirow_align` defaults to*“r”* instead of*“l”* .
- `multicol_align` defaults to*“r”* instead of*“l”* .
- `escape` now defaults to*False* .

Note that the behaviour of `_repr_latex_` is also changed. Previously
setting `display.latex.repr` would generate LaTeX only when using nbconvert for a
JupyterNotebook, and not when the user is running the notebook. Now the
`styler.render.repr` option allows control of the specific output
within JupyterNotebooks for operations (not just on nbconvert). See GH 39911.

### Increased minimum versions for dependencies#

Some minimum supported versions of dependencies were updated. If installed, we now require:

| Package | Minimum Version | Required | Changed | 
|---|---|---|---|
| mypy (dev) | 1.0 |  | X | 
| pytest (dev) | 7.0.0 |  | X | 
| pytest-xdist (dev) | 2.2.0 |  | X | 
| hypothesis (dev) | 6.34.2 |  | X | 
| python-dateutil | 2.8.2 | X | X | 
| tzdata | 2022.1 | X | X | 

For optional libraries the general recommendation is to use the latest version. The following table lists the lowest version per library that is currently being tested throughout the development of pandas. Optional libraries below the lowest tested version may still work, but are not considered supported.

| Package | Minimum Version | Changed | 
|---|---|---|
| pyarrow | 7.0.0 | X | 
| matplotlib | 3.6.1 | X | 
| fastparquet | 0.6.3 | X | 
| xarray | 0.21.0 | X | 

See Dependencies and Optional dependencies for more.

### Datetimes are now parsed with a consistent format#

In the past, `to_datetime()` guessed the format for each element independently. This was appropriate for some cases where elements had mixed date formats - however, it would regularly cause problems when users expected a consistent format but the function would switch formats between elements. As of version 2.0.0, parsing will use a consistent format, determined by the first non-NA value (unless the user specifies a format, in which case that is used).

*Old behavior*:

```
In [1]: ser = pd.Series(['13-01-2000', '12-01-2000'])
In [2]: pd.to_datetime(ser)
Out[2]:
0   2000-01-13
1   2000-12-01
dtype: datetime64[ns]
```
*New behavior*:

```
In [42]: ser = pd.Series(['13-01-2000', '12-01-2000'])
In [43]: pd.to_datetime(ser)
Out[43]: 
0   2000-01-13
1   2000-01-12
dtype: datetime64[us]
```
Note that this affects `read_csv()` as well.

If you still need to parse dates with inconsistent formats, you can use
`format='mixed'` (possibly alongside `dayfirst`)

```
ser = pd.Series(['13-01-2000', '12 January 2000'])
pd.to_datetime(ser, format='mixed', dayfirst=True)
```
or, if your formats are all ISO8601 (but possibly not identically-formatted)

```
ser = pd.Series(['2020-01-01', '2020-01-01 03:00'])
pd.to_datetime(ser, format='ISO8601')
```
### Other API changes#

- The `tz` ,`nanosecond` , and`unit` keywords in the`Timestamp` constructor are now keyword-only (GH 45307, GH 32526)
- Passing `nanoseconds` greater than 999 or less than 0 in`Timestamp` now raises a`ValueError` (GH 48538, GH 48255)
- `read_csv()` : specifying an incorrect number of columns with`index_col` of now raises`ParserError` instead of`IndexError` when using the c parser.
- Default value of `dtype` in`get_dummies()` is changed to`bool` from`uint8` (GH 45848)
- `DataFrame.astype()` ,`Series.astype()` , and`DatetimeIndex.astype()` casting datetime64 data to any of “datetime64[s]”, “datetime64[ms]”, “datetime64[us]” will return an object with the given resolution instead of coercing back to “datetime64[ns]” (GH 48928)
- `DataFrame.astype()` ,`Series.astype()` , and`DatetimeIndex.astype()` casting timedelta64 data to any of “timedelta64[s]”, “timedelta64[ms]”, “timedelta64[us]” will return an object with the given resolution instead of coercing to “float64” dtype (GH 48963)
- `DatetimeIndex.astype()` ,`TimedeltaIndex.astype()` ,`PeriodIndex.astype()``Series.astype()` ,`DataFrame.astype()` with`datetime64` ,`timedelta64` or`PeriodDtype` dtypes no longer allow converting to integer dtypes other than “int64”, do`obj.astype('int64', copy=False).astype(dtype)` instead (GH 49715)
- `Index.astype()` now allows casting from`float64` dtype to datetime-like dtypes, matching`Series` behavior (GH 49660)
- Passing data with dtype of “timedelta64[s]”, “timedelta64[ms]”, or “timedelta64[us]” to `TimedeltaIndex` ,`Series` , or`DataFrame` constructors will now retain that dtype instead of casting to “timedelta64[ns]”; timedelta64 data with lower resolution will be cast to the lowest supported resolution “timedelta64[s]” (GH 49014)
- Passing `dtype` of “timedelta64[s]”, “timedelta64[ms]”, or “timedelta64[us]” to`TimedeltaIndex` ,`Series` , or`DataFrame` constructors will now retain that dtype instead of casting to “timedelta64[ns]”; passing a dtype with lower resolution for`Series` or`DataFrame` will be cast to the lowest supported resolution “timedelta64[s]” (GH 49014)
- Passing a `np.datetime64` object with non-nanosecond resolution to`Timestamp` will retain the input resolution if it is “s”, “ms”, “us”, or “ns”; otherwise it will be cast to the closest supported resolution (GH 49008)
- Passing `datetime64` values with resolution other than nanosecond to`to_datetime()` will retain the input resolution if it is “s”, “ms”, “us”, or “ns”; otherwise it will be cast to the closest supported resolution (GH 50369)
- Passing integer values and a non-nanosecond datetime64 dtype (e.g. “datetime64[s]”) `DataFrame` ,`Series` , or`Index` will treat the values as multiples of the dtype’s unit, matching the behavior of e.g.`Series(np.array(values, dtype="M8[s]"))` (GH 51092)
- Passing a string in ISO-8601 format to `Timestamp` will retain the resolution of the parsed input if it is “s”, “ms”, “us”, or “ns”; otherwise it will be cast to the closest supported resolution (GH 49737)
- The `other` argument in`DataFrame.mask()` and`Series.mask()` now defaults to`no_default` instead of`np.nan` consistent with`DataFrame.where()` and`Series.where()` . Entries will be filled with the corresponding NULL value (`np.nan` for numpy dtypes,`pd.NA` for extension dtypes). (GH 49111)
- Changed behavior of `Series.quantile()` and`DataFrame.quantile()` with`SparseDtype` to retain sparse dtype (GH 49583)
- When creating a `Series` with a object-dtype`Index` of datetime objects, pandas no longer silently converts the index to a`DatetimeIndex` (GH 39307, GH 23598)
- `pandas.testing.assert_index_equal()` with parameter`exact="equiv"` now considers two indexes equal when both are either a`RangeIndex` or`Index` with an`int64` dtype. Previously it meant either a`RangeIndex` or a`Int64Index` (GH 51098)
- `Series.unique()` with dtype “timedelta64[ns]” or “datetime64[ns]” now returns`TimedeltaArray` or`DatetimeArray` instead of`numpy.ndarray` (GH 49176)
- `to_datetime()` and`DatetimeIndex` now allow sequences containing both`datetime` objects and numeric entries, matching`Series` behavior (GH 49037, GH 50453)
- `pandas.api.types.is_string_dtype()` now only returns`True` for array-likes with`dtype=object` when the elements are inferred to be strings (GH 15585)
- Passing a sequence containing `datetime` objects and`date` objects to`Series` constructor will return with`object` dtype instead of`datetime64[ns]` dtype, consistent with`Index` behavior (GH 49341)
- Passing strings that cannot be parsed as datetimes to `Series` or`DataFrame` with`dtype="datetime64[ns]"` will raise instead of silently ignoring the keyword and returning`object` dtype (GH 24435)
- Passing a sequence containing a type that cannot be converted to `Timedelta` to`to_timedelta()` or to the`Series` or`DataFrame` constructor with`dtype="timedelta64[ns]"` or to`TimedeltaIndex` now raises`TypeError` instead of`ValueError` (GH 49525)
- Changed behavior of `Index` constructor with sequence containing at least one`NaT` and everything else either`None` or`NaN` to infer`datetime64[ns]` dtype instead of`object` , matching`Series` behavior (GH 49340)
- `read_stata()` with parameter`index_col` set to`None` (the default) will now set the index on the returned`DataFrame` to a`RangeIndex` instead of a`Int64Index` (GH 49745)
- Changed behavior of `Index` ,`Series` , and`DataFrame` arithmetic methods when working with object-dtypes, the results no longer do type inference on the result of the array operations, use`result.infer_objects(copy=False)` to do type inference on the result (GH 49999, GH 49714)
- Changed behavior of `Index` constructor with an object-dtype`numpy.ndarray` containing all-`bool` values or all-complex values, this will now retain object dtype, consistent with the`Series` behavior (GH 49594)
- Changed behavior of `Series.astype()` from object-dtype containing`bytes` objects to string dtypes; this now does`val.decode()` on bytes objects instead of`str(val)` , matching`Index.astype()` behavior (GH 45326)
- Added `"None"` to default`na_values` in`read_csv()` (GH 50286)
- Changed behavior of `Series` and`DataFrame` constructors when given an integer dtype and floating-point data that is not round numbers, this now raises`ValueError` instead of silently retaining the float dtype; do`Series(data)` or`DataFrame(data)` to get the old behavior, and`Series(data).astype(dtype)` or`DataFrame(data).astype(dtype)` to get the specified dtype (GH 49599)
- Changed behavior of `DataFrame.shift()` with`axis=1` , an integer`fill_value` , and homogeneous datetime-like dtype, this now fills new columns with integer dtypes instead of casting to datetimelike (GH 49842)
- Files are now closed when encountering an exception in `read_json()` (GH 49921)
- Changed behavior of `read_csv()` ,`read_json()` &`read_fwf()` , where the index will now always be a`RangeIndex` , when no index is specified. Previously the index would be a`Index` with dtype`object` if the new DataFrame/Series has length 0 (GH 49572)
- `DataFrame.values()` ,`DataFrame.to_numpy()` ,`DataFrame.xs()` ,`DataFrame.reindex()` ,`DataFrame.fillna()` , and`DataFrame.replace()` no longer silently consolidate the underlying arrays; do`df = df.copy()` to ensure consolidation (GH 49356)
- Creating a new DataFrame using a full slice on both axes with `loc` or`iloc` (thus,`df.loc[:, :]` or`df.iloc[:, :]` ) now returns a
new DataFrame (shallow copy) instead of the original DataFrame, consistent with other
methods to get a full slice (for example`df.loc[:]` or`df[:]` ) (GH 49469)
- The `Series` and`DataFrame` constructors will now return a shallow copy
(i.e. share data, but not attributes) when passed a Series and DataFrame,
respectively, and with the default of`copy=False` (and if no other keyword triggers
a copy). Previously, the new Series or DataFrame would share the index attribute (e.g.`df.index = ...` would also update the index of the parent or child) (GH 49523)
- Disallow computing `cumprod` for`Timedelta` object; previously this returned incorrect values (GH 50246)
- `DataFrame` objects read from a`HDFStore` file without an index now have a`RangeIndex` instead of an`int64` index (GH 51076)
- Instantiating an `Index` with an numeric numpy dtype with data containing`NA` and/or`NaT` now raises a`ValueError` . Previously a`TypeError` was raised (GH 51050)
- Loading a JSON file with duplicate columns using `read_json(orient='split')` renames columns to avoid duplicates, as`read_csv()` and the other readers do (GH 50370)
- The levels of the index of the `Series` returned from`Series.sparse.from_coo` now always have dtype`int32` . Previously they had dtype`int64` (GH 50926)
- `to_datetime()` with`unit` of either “Y” or “M” will now raise if a sequence contains a non-round`float` value, matching the`Timestamp` behavior (GH 50301)
- The methods `Series.round()` ,`DataFrame.__invert__()` ,`Series.__invert__()` ,`DataFrame.swapaxes()` ,`DataFrame.first()` ,`DataFrame.last()` ,`Series.first()` ,`Series.last()` and`DataFrame.align()` will now always return new objects (GH 51032)
- `DataFrame` and`DataFrameGroupBy` aggregations (e.g. “sum”) with object-dtype columns no longer infer non-object dtypes for their results, explicitly call`result.infer_objects(copy=False)` on the result to obtain the old behavior (GH 51205, GH 49603)
- Division by zero with `ArrowDtype` dtypes returns`-inf` ,`nan` , or`inf` depending on the numerator, instead of raising (GH 51541)
- Added `pandas.api.types.is_any_real_numeric_dtype()` to check for real numeric dtypes (GH 51152)
- `value_counts()` now returns data with`ArrowDtype` with`pyarrow.int64` type instead of`"Int64"` type (GH 51462)
- `factorize()` and`unique()` preserve the original dtype when passed numpy timedelta64 or datetime64 with non-nanosecond resolution (GH 48670)

Note

A current PDEP proposes the deprecation and removal of the keywords `inplace` and `copy`
for all but a small subset of methods from the pandas API. The current discussion takes place
at here. The keywords won’t be necessary
anymore in the context of Copy-on-Write. If this proposal is accepted, both
keywords would be deprecated in the next release of pandas and removed in pandas 3.0.

## Deprecations#

- Deprecated parsing datetime strings with system-local timezone to `tzlocal` , pass a`tz` keyword or explicitly call`tz_localize` instead (GH 50791)
- Deprecated argument `infer_datetime_format` in`to_datetime()` and`read_csv()` , as a strict version of it is now the default (GH 48621)
- Deprecated behavior of `to_datetime()` with`unit` when parsing strings, in a future version these will be parsed as datetimes (matching unit-less behavior) instead of cast to floats. To retain the old behavior, cast strings to numeric types before calling`to_datetime()` (GH 50735)
- Deprecated `pandas.io.sql.execute()` (GH 50185)
- `Index.is_boolean()` has been deprecated. Use`pandas.api.types.is_bool_dtype()` instead (GH 50042)
- `Index.is_integer()` has been deprecated. Use`pandas.api.types.is_integer_dtype()` instead (GH 50042)
- `Index.is_floating()` has been deprecated. Use`pandas.api.types.is_float_dtype()` instead (GH 50042)
- `Index.holds_integer()` has been deprecated. Use`pandas.api.types.infer_dtype()` instead (GH 50243)
- `Index.is_numeric()` has been deprecated. Use`pandas.api.types.is_any_real_numeric_dtype()` instead (GH 50042,:issue:51152)
- `Index.is_categorical()` has been deprecated. Use`pandas.api.types.is_categorical_dtype()` instead (GH 50042)
- `Index.is_object()` has been deprecated. Use`pandas.api.types.is_object_dtype()` instead (GH 50042)
- `Index.is_interval()` has been deprecated. Use`pandas.api.types.is_interval_dtype()` instead (GH 50042)
- Deprecated argument `date_parser` in`read_csv()` ,`read_table()` ,`read_fwf()` , and`read_excel()` in favour of`date_format` (GH 50601)
- Deprecated `all` and`any` reductions with`datetime64` and`DatetimeTZDtype` dtypes, use e.g.`(obj != pd.Timestamp(0), tz=obj.tz).all()` instead (GH 34479)
- Deprecated unused arguments `*args` and`**kwargs` in`Resampler` (GH 50977)
- Deprecated calling `float` or`int` on a single element`Series` to return a`float` or`int` respectively. Extract the element before calling`float` or`int` instead (GH 51101)
- Deprecated `Grouper.groups()` , use`Groupby.groups()` instead (GH 51182)
- Deprecated `Grouper.grouper()` , use`Groupby.grouper()` instead (GH 51182)
- Deprecated `Grouper.obj()` , use`Groupby.obj()` instead (GH 51206)
- Deprecated `Grouper.indexer()` , use`Resampler.indexer()` instead (GH 51206)
- Deprecated `Grouper.ax()` , use`Resampler.ax()` instead (GH 51206)
- Deprecated keyword `use_nullable_dtypes` in`read_parquet()` , use`dtype_backend` instead (GH 51853)
- Deprecated `Series.pad()` in favor of`Series.ffill()` (GH 33396)
- Deprecated `Series.backfill()` in favor of`Series.bfill()` (GH 33396)
- Deprecated `DataFrame.pad()` in favor of`DataFrame.ffill()` (GH 33396)
- Deprecated `DataFrame.backfill()` in favor of`DataFrame.bfill()` (GH 33396)
- Deprecated `close()` . Use`StataReader` as a context manager instead (GH 49228)
- Deprecated producing a scalar when iterating over a `DataFrameGroupBy` or a`SeriesGroupBy` that has been grouped by a`level` parameter that is a list of length 1; a tuple of length one will be returned instead (GH 51583)

## Removal of prior version deprecations/changes#

- Removed `Int64Index` ,`UInt64Index` and`Float64Index` . See also here for more information (GH 42717)
- Removed deprecated `Timestamp.freq` ,`Timestamp.freqstr` and argument`freq` from the`Timestamp` constructor and`Timestamp.fromordinal()` (GH 14146)
- Removed deprecated `CategoricalBlock` ,`Block.is_categorical()` , require datetime64 and timedelta64 values to be wrapped in`DatetimeArray` or`TimedeltaArray` before passing to`Block.make_block_same_class()` , require`DatetimeTZBlock.values` to have the correct ndim when passing to the`BlockManager` constructor, and removed the “fastpath” keyword from the`SingleBlockManager` constructor (GH 40226, GH 40571)
- Removed deprecated global option `use_inf_as_null` in favor of`use_inf_as_na` (GH 17126)
- Removed deprecated module `pandas.core.index` (GH 30193)
- Removed deprecated alias `pandas.core.tools.datetimes.to_time` , import the function directly from`pandas.core.tools.times` instead (GH 34145)
- Removed deprecated alias `pandas.io.json.json_normalize` , import the function directly from`pandas.json_normalize` instead (GH 27615)
- Removed deprecated `Categorical.to_dense()` , use`np.asarray(cat)` instead (GH 32639)
- Removed deprecated `Categorical.take_nd()` (GH 27745)
- Removed deprecated `Categorical.mode()` , use`Series(cat).mode()` instead (GH 45033)
- Removed deprecated `Categorical.is_dtype_equal()` and`CategoricalIndex.is_dtype_equal()` (GH 37545)
- Removed deprecated `CategoricalIndex.take_nd()` (GH 30702)
- Removed deprecated `Index.is_type_compatible()` (GH 42113)
- Removed deprecated `Index.is_mixed()` , check`index.inferred_type` directly instead (GH 32922)
- Removed deprecated `pandas.api.types.is_categorical()` ; use`pandas.api.types.is_categorical_dtype()` instead  (GH 33385)
- Removed deprecated `Index.asi8()` (GH 37877)
- Enforced deprecation changing behavior when passing `datetime64[ns]` dtype data and timezone-aware dtype to`Series` , interpreting the values as wall-times instead of UTC times, matching`DatetimeIndex` behavior (GH 41662)
- Enforced deprecation changing behavior when applying a numpy ufunc on multiple non-aligned (on the index or columns) `DataFrame` that will now align the inputs first (GH 39239)
- Removed deprecated `DataFrame._AXIS_NUMBERS()` ,`DataFrame._AXIS_NAMES()` ,`Series._AXIS_NUMBERS()` ,`Series._AXIS_NAMES()` (GH 33637)
- Removed deprecated `Index.to_native_types()` , use`obj.astype(str)` instead (GH 36418)
- Removed deprecated `Series.iteritems()` ,`DataFrame.iteritems()` , use`obj.items` instead (GH 45321)
- Removed deprecated `DataFrame.lookup()` (GH 35224)
- Removed deprecated `Series.append()` ,`DataFrame.append()` , use`concat()` instead (GH 35407)
- Removed deprecated `Series.iteritems()` ,`DataFrame.iteritems()` and`HDFStore.iteritems()` use`obj.items` instead (GH 45321)
- Removed deprecated `DatetimeIndex.union_many()` (GH 45018)
- Removed deprecated `weekofyear` and`week` attributes of`DatetimeArray` ,`DatetimeIndex` and`dt` accessor in favor of`isocalendar().week` (GH 33595)
- Removed deprecated `RangeIndex._start()` ,`RangeIndex._stop()` ,`RangeIndex._step()` , use`start` ,`stop` ,`step` instead (GH 30482)
- Removed deprecated `DatetimeIndex.to_perioddelta()` , Use`dtindex - dtindex.to_period(freq).to_timestamp()` instead (GH 34853)
- Removed deprecated `Styler.hide_index()` and`Styler.hide_columns()` (GH 49397)
- Removed deprecated `Styler.set_na_rep()` and`Styler.set_precision()` (GH 49397)
- Removed deprecated `Styler.where()` (GH 49397)
- Removed deprecated `Styler.render()` (GH 49397)
- Removed deprecated argument `col_space` in`DataFrame.to_latex()` (GH 47970)
- Removed deprecated argument `null_color` in`Styler.highlight_null()` (GH 49397)
- Removed deprecated argument `check_less_precise` in`testing.assert_frame_equal()` ,`testing.assert_extension_array_equal()` ,`testing.assert_series_equal()` ,`testing.assert_index_equal()` (GH 30562)
- Removed deprecated `null_counts` argument in`DataFrame.info()` . Use`show_counts` instead (GH 37999)
- Removed deprecated `Index.is_monotonic()` , and`Series.is_monotonic()` ; use`obj.is_monotonic_increasing` instead (GH 45422)
- Removed deprecated `Index.is_all_dates()` (GH 36697)
- Enforced deprecation disallowing passing a timezone-aware `Timestamp` and`dtype="datetime64[ns]"` to`Series` or`DataFrame` constructors (GH 41555)
- Enforced deprecation disallowing passing a sequence of timezone-aware values and `dtype="datetime64[ns]"` to`Series` or`DataFrame` constructors (GH 41555)
- Enforced deprecation disallowing `numpy.ma.mrecords.MaskedRecords` in the`DataFrame` constructor; pass`"{name: data[name] for name in data.dtype.names}` instead (GH 40363)
- Enforced deprecation disallowing unit-less “datetime64” dtype in `Series.astype()` and`DataFrame.astype()` (GH 47844)
- Enforced deprecation disallowing using `.astype` to convert a`datetime64[ns]``Series` ,`DataFrame` , or`DatetimeIndex` to timezone-aware dtype, use`obj.tz_localize` or`ser.dt.tz_localize` instead (GH 39258)
- Enforced deprecation disallowing using `.astype` to convert a timezone-aware`Series` ,`DataFrame` , or`DatetimeIndex` to timezone-naive`datetime64[ns]` dtype, use`obj.tz_localize(None)` or`obj.tz_convert("UTC").tz_localize(None)` instead (GH 39258)
- Enforced deprecation disallowing passing non boolean argument to sort in `concat()` (GH 44629)
- Removed Date parser functions `parse_date_time()` ,`parse_date_fields()` ,`parse_all_fields()` and`generic_parser()` (GH 24518)
- Removed argument `index` from the`core.arrays.SparseArray` constructor (GH 43523)
- Remove argument `squeeze` from`DataFrame.groupby()` and`Series.groupby()` (GH 32380)
- Removed deprecated `apply` ,`apply_index` ,`__call__` ,`onOffset` , and`isAnchored` attributes from`DateOffset` (GH 34171)
- Removed `keep_tz` argument in`DatetimeIndex.to_series()` (GH 29731)
- Remove arguments `names` and`dtype` from`Index.copy()` and`levels` and`codes` from`MultiIndex.copy()` (GH 35853, GH 36685)
- Remove argument `inplace` from`MultiIndex.set_levels()` and`MultiIndex.set_codes()` (GH 35626)
- Removed arguments `verbose` and`encoding` from`DataFrame.to_excel()` and`Series.to_excel()` (GH 47912)
- Removed argument `line_terminator` from`DataFrame.to_csv()` and`Series.to_csv()` , use`lineterminator` instead (GH 45302)
- Removed argument `inplace` from`DataFrame.set_axis()` and`Series.set_axis()` , use`obj = obj.set_axis(..., copy=False)` instead (GH 48130)
- Disallow passing positional arguments to `MultiIndex.set_levels()` and`MultiIndex.set_codes()` (GH 41485)
- Disallow parsing to Timedelta strings with components with units “Y”, “y”, or “M”, as these do not represent unambiguous durations (GH 36838)
- Removed `MultiIndex.is_lexsorted()` and`MultiIndex.lexsort_depth()` (GH 38701)
- Removed argument `how` from`PeriodIndex.astype()` , use`PeriodIndex.to_timestamp()` instead (GH 37982)
- Removed argument `try_cast` from`DataFrame.mask()` ,`DataFrame.where()` ,`Series.mask()` and`Series.where()` (GH 38836)
- Removed argument `tz` from`Period.to_timestamp()` , use`obj.to_timestamp(...).tz_localize(tz)` instead (GH 34522)
- Removed argument `sort_columns` in`DataFrame.plot()` and`Series.plot()` (GH 47563)
- Removed argument `is_copy` from`DataFrame.take()` and`Series.take()` (GH 30615)
- Removed argument `kind` from`Index.get_slice_bound()` ,`Index.slice_indexer()` and`Index.slice_locs()` (GH 41378)
- Removed arguments `prefix` ,`squeeze` ,`error_bad_lines` and`warn_bad_lines` from`read_csv()` (GH 40413, GH 43427)
- Removed arguments `squeeze` from`read_excel()` (GH 43427)
- Removed argument `datetime_is_numeric` from`DataFrame.describe()` and`Series.describe()` as datetime data will always be summarized as numeric data (GH 34798)
- Disallow passing list `key` to`Series.xs()` and`DataFrame.xs()` , pass a tuple instead (GH 41789)
- Disallow subclass-specific keywords (e.g. “freq”, “tz”, “names”, “closed”) in the `Index` constructor (GH 38597)
- Removed argument `inplace` from`Categorical.remove_unused_categories()` (GH 37918)
- Disallow passing non-round floats to `Timestamp` with`unit="M"` or`unit="Y"` (GH 47266)
- Remove keywords `convert_float` and`mangle_dupe_cols` from`read_excel()` (GH 41176)
- Remove keyword `mangle_dupe_cols` from`read_csv()` and`read_table()` (GH 48137)
- Removed `errors` keyword from`DataFrame.where()` ,`Series.where()` ,`DataFrame.mask()` and`Series.mask()` (GH 47728)
- Disallow passing non-keyword arguments to `read_excel()` except`io` and`sheet_name` (GH 34418)
- Disallow passing non-keyword arguments to `DataFrame.drop()` and`Series.drop()` except`labels` (GH 41486)
- Disallow passing non-keyword arguments to `DataFrame.fillna()` and`Series.fillna()` except`value` (GH 41485)
- Disallow passing non-keyword arguments to `StringMethods.split()` and`StringMethods.rsplit()` except for`pat` (GH 47448)
- Disallow passing non-keyword arguments to `DataFrame.set_index()` except`keys` (GH 41495)
- Disallow passing non-keyword arguments to `Resampler.interpolate()` except`method` (GH 41699)
- Disallow passing non-keyword arguments to `DataFrame.reset_index()` and`Series.reset_index()` except`level` (GH 41496)
- Disallow passing non-keyword arguments to `DataFrame.dropna()` and`Series.dropna()` (GH 41504)
- Disallow passing non-keyword arguments to `ExtensionArray.argsort()` (GH 46134)
- Disallow passing non-keyword arguments to `Categorical.sort_values()` (GH 47618)
- Disallow passing non-keyword arguments to `Index.drop_duplicates()` and`Series.drop_duplicates()` (GH 41485)
- Disallow passing non-keyword arguments to `DataFrame.drop_duplicates()` except for`subset` (GH 41485)
- Disallow passing non-keyword arguments to `DataFrame.sort_index()` and`Series.sort_index()` (GH 41506)
- Disallow passing non-keyword arguments to `DataFrame.interpolate()` and`Series.interpolate()` except for`method` (GH 41510)
- Disallow passing non-keyword arguments to `DataFrame.any()` and`Series.any()` (GH 44896)
- Disallow passing non-keyword arguments to `Index.set_names()` except for`names` (GH 41551)
- Disallow passing non-keyword arguments to `Index.join()` except for`other` (GH 46518)
- Disallow passing non-keyword arguments to `concat()` except for`objs` (GH 41485)
- Disallow passing non-keyword arguments to `pivot()` except for`data` (GH 48301)
- Disallow passing non-keyword arguments to `DataFrame.pivot()` (GH 48301)
- Disallow passing non-keyword arguments to `read_html()` except for`io` (GH 27573)
- Disallow passing non-keyword arguments to `read_json()` except for`path_or_buf` (GH 27573)
- Disallow passing non-keyword arguments to `read_sas()` except for`filepath_or_buffer` (GH 47154)
- Disallow passing non-keyword arguments to `read_stata()` except for`filepath_or_buffer` (GH 48128)
- Disallow passing non-keyword arguments to `read_csv()` except`filepath_or_buffer` (GH 41485)
- Disallow passing non-keyword arguments to `read_table()` except`filepath_or_buffer` (GH 41485)
- Disallow passing non-keyword arguments to `read_fwf()` except`filepath_or_buffer` (GH 44710)
- Disallow passing non-keyword arguments to `read_xml()` except for`path_or_buffer` (GH 45133)
- Disallow passing non-keyword arguments to `Series.mask()` and`DataFrame.mask()` except`cond` and`other` (GH 41580)
- Disallow passing non-keyword arguments to `DataFrame.to_stata()` except for`path` (GH 48128)
- Disallow passing non-keyword arguments to `DataFrame.where()` and`Series.where()` except for`cond` and`other` (GH 41523)
- Disallow passing non-keyword arguments to `Series.set_axis()` and`DataFrame.set_axis()` except for`labels` (GH 41491)
- Disallow passing non-keyword arguments to `Series.rename_axis()` and`DataFrame.rename_axis()` except for`mapper` (GH 47587)
- Disallow passing non-keyword arguments to `Series.clip()` and`DataFrame.clip()` except`lower` and`upper` (GH 41511)
- Disallow passing non-keyword arguments to `Series.bfill()` ,`Series.ffill()` ,`DataFrame.bfill()` and`DataFrame.ffill()` (GH 41508)
- Disallow passing non-keyword arguments to `DataFrame.replace()` ,`Series.replace()` except for`to_replace` and`value` (GH 47587)
- Disallow passing non-keyword arguments to `DataFrame.sort_values()` except for`by` (GH 41505)
- Disallow passing non-keyword arguments to `Series.sort_values()` (GH 41505)
- Disallow passing non-keyword arguments to `DataFrame.reindex()` except for`labels` (GH 17966)
- Disallow `Index.reindex()` with non-unique`Index` objects (GH 42568)
- Disallowed constructing `Categorical` with scalar`data` (GH 38433)
- Disallowed constructing `CategoricalIndex` without passing`data` (GH 38944)
- Removed `Rolling.validate()` ,`Expanding.validate()` , and`ExponentialMovingWindow.validate()` (GH 43665)
- Removed `Rolling.win_type` returning`"freq"` (GH 38963)
- Removed `Rolling.is_datetimelike` (GH 38963)
- Removed the `level` keyword in`DataFrame` and`Series` aggregations; use`groupby` instead (GH 39983)
- Removed deprecated `Timedelta.delta()` ,`Timedelta.is_populated()` , and`Timedelta.freq` (GH 46430, GH 46476)
- Removed deprecated `NaT.freq` (GH 45071)
- Removed deprecated `Categorical.replace()` , use`Series.replace()` instead (GH 44929)
- Removed the `numeric_only` keyword from`Categorical.min()` and`Categorical.max()` in favor of`skipna` (GH 48821)
- Changed behavior of `DataFrame.median()` and`DataFrame.mean()` with`numeric_only=None` to not exclude datetime-like columns THIS NOTE WILL BE IRRELEVANT ONCE`numeric_only=None` DEPRECATION IS ENFORCED (GH 29941)
- Removed `is_extension_type()` in favor of`is_extension_array_dtype()` (GH 29457)
- Removed `.ExponentialMovingWindow.vol` (GH 39220)
- Removed `Index.get_value()` and`Index.set_value()` (GH 33907, GH 28621)
- Removed `Series.slice_shift()` and`DataFrame.slice_shift()` (GH 37601)
- Remove `DataFrameGroupBy.pad()` and`DataFrameGroupBy.backfill()` (GH 45076)
- Remove `numpy` argument from`read_json()` (GH 30636)
- Disallow passing abbreviations for `orient` in`DataFrame.to_dict()` (GH 32516)
- Disallow partial slicing on an non-monotonic `DatetimeIndex` with keys which are not in Index. This now raises a`KeyError` (GH 18531)
- Removed `get_offset` in favor of`to_offset()` (GH 30340)
- Removed the `warn` keyword in`infer_freq()` (GH 45947)
- Removed the `include_start` and`include_end` arguments in`DataFrame.between_time()` in favor of`inclusive` (GH 43248)
- Removed the `closed` argument in`date_range()` and`bdate_range()` in favor of`inclusive` argument (GH 40245)
- Removed the `center` keyword in`DataFrame.expanding()` (GH 20647)
- Removed the `truediv` keyword from`eval()` (GH 29812)
- Removed the `method` and`tolerance` arguments in`Index.get_loc()` . Use`index.get_indexer([label], method=..., tolerance=...)` instead (GH 42269)
- Removed the `pandas.datetime` submodule (GH 30489)
- Removed the `pandas.np` submodule (GH 30296)
- Removed `pandas.util.testing` in favor of`pandas.testing` (GH 30745)
- Removed `Series.str.__iter__()` (GH 28277)
- Removed `pandas.SparseArray` in favor of`arrays.SparseArray` (GH 30642)
- Removed `pandas.SparseSeries` and`pandas.SparseDataFrame` , including pickle support. (GH 30642)
- Enforced disallowing passing an integer `fill_value` to`DataFrame.shift()` and`Series.shift()` with datetime64, timedelta64, or period dtypes (GH 32591)
- Enforced disallowing a string column label into `times` in`DataFrame.ewm()` (GH 43265)
- Enforced disallowing passing `True` and`False` into`inclusive` in`Series.between()` in favor of`"both"` and`"neither"` respectively (GH 40628)
- Enforced disallowing using `usecols` with out of bounds indices for`read_csv` with`engine="c"` (GH 25623)
- Enforced disallowing the use of `**kwargs` in`ExcelWriter` ; use the keyword argument`engine_kwargs` instead (GH 40430)
- Enforced disallowing a tuple of column labels into `DataFrameGroupBy.__getitem__()` (GH 30546)
- Enforced disallowing missing labels when indexing with a sequence of labels on a level of a `MultiIndex` . This now raises a`KeyError` (GH 42351)
- Enforced disallowing setting values with `.loc` using a positional slice. Use`.loc` with labels or`.iloc` with positions instead (GH 31840)
- Enforced disallowing positional indexing with a `float` key even if that key is a round number, manually cast to integer instead (GH 34193)
- Enforced disallowing using a `DataFrame` indexer with`.iloc` , use`.loc` instead for automatic alignment (GH 39022)
- Enforced disallowing `set` or`dict` indexers in`__getitem__` and`__setitem__` methods (GH 42825)
- Enforced disallowing indexing on a `Index` or positional indexing on a`Series` producing multi-dimensional objects e.g.`obj[:, None]` , convert to numpy before indexing instead (GH 35141)
- Enforced disallowing `dict` or`set` objects in`suffixes` in`merge()` (GH 34810)
- Enforced disallowing `merge()` to produce duplicated columns through the`suffixes` keyword and already existing columns (GH 22818)
- Enforced disallowing using `merge()` or`join()` on a different number of levels (GH 34862)
- Enforced disallowing `value_name` argument in`DataFrame.melt()` to match an element in the`DataFrame` columns (GH 35003)
- Enforced disallowing passing `showindex` into`**kwargs` in`DataFrame.to_markdown()` and`Series.to_markdown()` in favor of`index` (GH 33091)
- Removed setting Categorical._codes directly (GH 41429)
- Removed setting Categorical.categories directly (GH 47834)
- Removed argument `inplace` from`Categorical.add_categories()` ,`Categorical.remove_categories()` ,`Categorical.set_categories()` ,`Categorical.rename_categories()` ,`Categorical.reorder_categories()` ,`Categorical.set_ordered()` ,`Categorical.as_ordered()` ,`Categorical.as_unordered()` (GH 37981, GH 41118, GH 41133, GH 47834)
- Enforced `Rolling.count()` with`min_periods=None` to default to the size of the window (GH 31302)
- Renamed `fname` to`path` in`DataFrame.to_parquet()` ,`DataFrame.to_stata()` and`DataFrame.to_feather()` (GH 30338)
- Enforced disallowing indexing a `Series` with a single item list with a slice (e.g.`ser[[slice(0, 2)]]` ). Either convert the list to tuple, or pass the slice directly instead (GH 31333)
- Changed behavior indexing on a `DataFrame` with a`DatetimeIndex` index using a string indexer, previously this operated as a slice on rows, now it operates like any other column key; use`frame.loc[key]` for the old behavior (GH 36179)
- Enforced the `display.max_colwidth` option to not accept negative integers (GH 31569)
- Removed the `display.column_space` option in favor of`df.to_string(col_space=...)` (GH 47280)
- Removed the deprecated method `mad` from pandas classes (GH 11787)
- Removed the deprecated method `tshift` from pandas classes (GH 11631)
- Changed behavior of empty data passed into `Series` ; the default dtype will be`object` instead of`float64` (GH 29405)
- Changed the behavior of `DatetimeIndex.union()` ,`DatetimeIndex.intersection()` , and`DatetimeIndex.symmetric_difference()` with mismatched timezones to convert to UTC instead of casting to object dtype (GH 39328)
- Changed the behavior of `to_datetime()` with argument “now” with`utc=False` to match`Timestamp("now")` (GH 18705)
- Changed the behavior of indexing on a timezone-aware `DatetimeIndex` with a timezone-naive`datetime` object or vice-versa; these now behave like any other non-comparable type by raising`KeyError` (GH 36148)
- Changed the behavior of `Index.reindex()` ,`Series.reindex()` , and`DataFrame.reindex()` with a`datetime64` dtype and a`datetime.date` object for`fill_value` ; these are no longer considered equivalent to`datetime.datetime` objects so the reindex casts to object dtype (GH 39767)
- Changed behavior of `SparseArray.astype()` when given a dtype that is not explicitly`SparseDtype` , cast to the exact requested dtype rather than silently using a`SparseDtype` instead (GH 34457)
- Changed behavior of `Index.ravel()` to return a view on the original`Index` instead of a`np.ndarray` (GH 36900)
- Changed behavior of `Series.to_frame()` and`Index.to_frame()` with explicit`name=None` to use`None` for the column name instead of the index’s name or default`0` (GH 45523)
- Changed behavior of `concat()` with one array of`bool` -dtype and another of integer dtype, this now returns`object` dtype instead of integer dtype; explicitly cast the bool object to integer before concatenating to get the old behavior (GH 45101)
- Changed behavior of `DataFrame` constructor given floating-point`data` and an integer`dtype` , when the data cannot be cast losslessly, the floating point dtype is retained, matching`Series` behavior (GH 41170)
- Changed behavior of `Index` constructor when given a`np.ndarray` with object-dtype containing numeric entries; this now retains object dtype rather than inferring a numeric dtype, consistent with`Series` behavior (GH 42870)
- Changed behavior of `Index.__and__()` ,`Index.__or__()` and`Index.__xor__()` to behave as logical operations (matching`Series` behavior) instead of aliases for set operations (GH 37374)
- Changed behavior of `DataFrame` constructor when passed a list whose first element is a`Categorical` , this now treats the elements as rows casting to`object` dtype, consistent with behavior for other types (GH 38845)
- Changed behavior of `DataFrame` constructor when passed a`dtype` (other than int) that the data cannot be cast to; it now raises instead of silently ignoring the dtype (GH 41733)
- Changed the behavior of `Series` constructor, it will no longer infer a datetime64 or timedelta64 dtype from string entries (GH 41731)
- Changed behavior of `Timestamp` constructor with a`np.datetime64` object and a`tz` passed to interpret the input as a wall-time as opposed to a UTC time (GH 42288)
- Changed behavior of `Timestamp.utcfromtimestamp()` to return a timezone-aware object satisfying`Timestamp.utcfromtimestamp(val).timestamp() == val` (GH 45083)
- Changed behavior of `Index` constructor when passed a`SparseArray` or`SparseDtype` to retain that dtype instead of casting to`numpy.ndarray` (GH 43930)
- Changed behavior of setitem-like operations ( `__setitem__` ,`fillna` ,`where` ,`mask` ,`replace` ,`insert` , fill_value for`shift` ) on an object with`DatetimeTZDtype` when using a value with a non-matching timezone, the value will be cast to the object’s timezone instead of casting both to object-dtype (GH 44243)
- Changed behavior of `Index` ,`Series` ,`DataFrame` constructors with floating-dtype data and a`DatetimeTZDtype` , the data are now interpreted as UTC-times instead of wall-times, consistent with how integer-dtype data are treated (GH 45573)
- Changed behavior of `Series` and`DataFrame` constructors with integer dtype and floating-point data containing`NaN` , this now raises`IntCastingNaNError` (GH 40110)
- Changed behavior of `Series` and`DataFrame` constructors with an integer`dtype` and values that are too large to losslessly cast to this dtype, this now raises`ValueError` (GH 41734)
- Changed behavior of `Series` and`DataFrame` constructors with an integer`dtype` and values having either`datetime64` or`timedelta64` dtypes, this now raises`TypeError` , use`values.view("int64")` instead (GH 41770)
- Removed the deprecated `base` and`loffset` arguments from`pandas.DataFrame.resample()` ,`pandas.Series.resample()` and`pandas.Grouper` . Use`offset` or`origin` instead (GH 31809)
- Changed behavior of `Series.fillna()` and`DataFrame.fillna()` with`timedelta64[ns]` dtype and an incompatible`fill_value` ; this now casts to`object` dtype instead of raising, consistent with the behavior with other dtypes (GH 45746)
- Change the default argument of `regex` for`Series.str.replace()` from`True` to`False` . Additionally, a single character`pat` with`regex=True` is now treated as a regular expression instead of a string literal. (GH 36695, GH 24804)
- Changed behavior of `DataFrame.any()` and`DataFrame.all()` with`bool_only=True` ; object-dtype columns with all-bool values will no longer be included, manually cast to`bool` dtype first (GH 46188)
- Changed behavior of `DataFrame.max()` ,`DataFrame.min` ,`DataFrame.mean` ,`DataFrame.median` ,`DataFrame.skew` ,`DataFrame.kurt` with`axis=None` to return a scalar applying the aggregation across both axes (GH 45072)
- Changed behavior of comparison of a `Timestamp` with a`datetime.date` object; these now compare as un-equal and raise on inequality comparisons, matching the`datetime.datetime` behavior (GH 36131)
- Changed behavior of comparison of `NaT` with a`datetime.date` object; these now raise on inequality comparisons (GH 39196)
- Enforced deprecation of silently dropping columns that raised a `TypeError` in`Series.transform` and`DataFrame.transform` when used with a list or dictionary (GH 43740)
- Changed behavior of `DataFrame.apply()` with list-like so that any partial failure will raise an error (GH 43740)
- Changed behaviour of `DataFrame.to_latex()` to now use the Styler implementation via`Styler.to_latex()` (GH 47970)
- Changed behavior of `Series.__setitem__()` with an integer key and a`Float64Index` when the key is not present in the index; previously we treated the key as positional (behaving like`series.iloc[key] = val` ), now we treat it is a label (behaving like`series.loc[key] = val` ), consistent with`Series.__getitem__()` behavior (GH 33469)
- Removed `na_sentinel` argument from`factorize()` ,`Index.factorize()` , and`ExtensionArray.factorize()` (GH 47157)
- Changed behavior of `Series.diff()` and`DataFrame.diff()` with`ExtensionDtype` dtypes whose arrays do not implement`diff` , these now raise`TypeError` rather than casting to numpy (GH 31025)
- Enforced deprecation of calling numpy “ufunc”s on `DataFrame` with`method="outer"` ; this now raises`NotImplementedError` (GH 36955)
- Enforced deprecation disallowing passing `numeric_only=True` to`Series` reductions (`rank` ,`any` ,`all` , …) with non-numeric dtype (GH 47500)
- Changed behavior of `DataFrameGroupBy.apply()` and`SeriesGroupBy.apply()` so that`group_keys` is respected even if a transformer is detected (GH 34998)
- Comparisons between a `DataFrame` and a`Series` where the frame’s columns do not match the series’s index raise`ValueError` instead of automatically aligning, do`left, right = left.align(right, axis=1, copy=False)` before comparing (GH 36795)
- Enforced deprecation `numeric_only=None` (the default) in DataFrame reductions that would silently drop columns that raised;`numeric_only` now defaults to`False` (GH 41480)
- Changed default of `numeric_only` to`False` in all DataFrame methods with that argument (GH 46096, GH 46906)
- Changed default of `numeric_only` to`False` in`Series.rank()` (GH 47561)
- Enforced deprecation of silently dropping nuisance columns in groupby and resample operations when `numeric_only=False` (GH 41475)
- Enforced deprecation of silently dropping nuisance columns in `Rolling` ,`Expanding` , and`ExponentialMovingWindow` ops. This will now raise a`errors.DataError` (GH 42834)
- Changed behavior in setting values with `df.loc[:, foo] = bar` or`df.iloc[:, foo] = bar` , these now always attempt to set values inplace before falling back to casting (GH 45333)
- Changed default of `numeric_only` in various`DataFrameGroupBy` methods; all methods now default to`numeric_only=False` (GH 46072)
- Changed default of `numeric_only` to`False` in`Resampler` methods (GH 47177)
- Using the method `DataFrameGroupBy.transform()` with a callable that returns DataFrames will align to the input’s index (GH 47244)
- When providing a list of columns of length one to `DataFrame.groupby()` , the keys that are returned by iterating over the resulting`DataFrameGroupBy` object will now be tuples of length one (GH 47761)
- Removed deprecated methods `ExcelWriter.write_cells()` ,`ExcelWriter.save()` ,`ExcelWriter.cur_sheet()` ,`ExcelWriter.handles()` ,`ExcelWriter.path()` (GH 45795)
- The `ExcelWriter` attribute`book` can no longer be set; it is still available to be accessed and mutated (GH 48943)
- Removed unused `*args` and`**kwargs` in`Rolling` ,`Expanding` , and`ExponentialMovingWindow` ops (GH 47851)
- Removed the deprecated argument `line_terminator` from`DataFrame.to_csv()` (GH 45302)
- Removed the deprecated argument `label` from`lreshape()` (GH 30219)
- Arguments after `expr` in`DataFrame.eval()` and`DataFrame.query()` are keyword-only (GH 47587)
- Removed `Index._get_attributes_dict()` (GH 50648)
- Removed `Series.__array_wrap__()` (GH 50648)
- Changed behavior of `DataFrame.value_counts()` to return a`Series` with`MultiIndex` for any list-like(one element or not) but an`Index` for a single label (GH 50829)

## Performance improvements#

- Performance improvement in `DataFrameGroupBy.median()` and`SeriesGroupBy.median()` and`DataFrameGroupBy.cumprod()` for nullable dtypes (GH 37493)
- Performance improvement in `DataFrameGroupBy.all()` ,`DataFrameGroupBy.any()` ,`SeriesGroupBy.all()` , and`SeriesGroupBy.any()` for object dtype (GH 50623)
- Performance improvement in `MultiIndex.argsort()` and`MultiIndex.sort_values()` (GH 48406)
- Performance improvement in `MultiIndex.size()` (GH 48723)
- Performance improvement in `MultiIndex.union()` without missing values and without duplicates (GH 48505, GH 48752)
- Performance improvement in `MultiIndex.difference()` (GH 48606)
- Performance improvement in `MultiIndex` set operations with sort=None (GH 49010)
- Performance improvement in `DataFrameGroupBy.mean()` ,`SeriesGroupBy.mean()` ,`DataFrameGroupBy.var()` , and`SeriesGroupBy.var()` for extension array dtypes (GH 37493)
- Performance improvement in `MultiIndex.isin()` when`level=None` (GH 48622, GH 49577)
- Performance improvement in `MultiIndex.putmask()` (GH 49830)
- Performance improvement in `Index.union()` and`MultiIndex.union()` when index contains duplicates (GH 48900)
- Performance improvement in `Series.rank()` for pyarrow-backed dtypes (GH 50264)
- Performance improvement in `Series.searchsorted()` for pyarrow-backed dtypes (GH 50447)
- Performance improvement in `Series.fillna()` for extension array dtypes (GH 49722, GH 50078)
- Performance improvement in `Index.join()` ,`Index.intersection()` and`Index.union()` for masked and arrow dtypes when`Index` is monotonic (GH 50310, GH 51365)
- Performance improvement for `Series.value_counts()` with nullable dtype (GH 48338)
- Performance improvement for `Series` constructor passing integer numpy array with nullable dtype (GH 48338)
- Performance improvement for `DatetimeIndex` constructor passing a list (GH 48609)
- Performance improvement in `merge()` and`DataFrame.join()` when joining on a sorted`MultiIndex` (GH 48504)
- Performance improvement in `to_datetime()` when parsing strings with timezone offsets (GH 50107)
- Performance improvement in `DataFrame.loc()` and`Series.loc()` for tuple-based indexing of a`MultiIndex` (GH 48384)
- Performance improvement for `Series.replace()` with categorical dtype (GH 49404)
- Performance improvement for `MultiIndex.unique()` (GH 48335)
- Performance improvement for indexing operations with nullable and arrow dtypes (GH 49420, GH 51316)
- Performance improvement for `concat()` with extension array backed indexes (GH 49128, GH 49178)
- Performance improvement for `api.types.infer_dtype()` (GH 51054)
- Reduce memory usage of `DataFrame.to_pickle()` /`Series.to_pickle()` when using BZ2 or LZMA (GH 49068)
- Performance improvement for `StringArray` constructor passing a numpy array with type`np.str_` (GH 49109)
- Performance improvement in `from_tuples()` (GH 50620)
- Performance improvement in `factorize()` (GH 49177)
- Performance improvement in `__setitem__()` (GH 50248, GH 50632)
- Performance improvement in `ArrowExtensionArray` comparison methods when array contains NA (GH 50524)
- Performance improvement in `to_numpy()` (GH 49973, GH 51227)
- Performance improvement when parsing strings to `BooleanDtype` (GH 50613)
- Performance improvement in `DataFrame.join()` when joining on a subset of a`MultiIndex` (GH 48611)
- Performance improvement for `MultiIndex.intersection()` (GH 48604)
- Performance improvement in `DataFrame.__setitem__()` (GH 46267)
- Performance improvement in `var` and`std` for nullable dtypes (GH 48379).
- Performance improvement when iterating over pyarrow and nullable dtypes (GH 49825, GH 49851)
- Performance improvements to `read_sas()` (GH 47403, GH 47405, GH 47656, GH 48502)
- Memory improvement in `RangeIndex.sort_values()` (GH 48801)
- Performance improvement in `Series.to_numpy()` if`copy=True` by avoiding copying twice (GH 24345)
- Performance improvement in `Series.rename()` with`MultiIndex` (GH 21055)
- Performance improvement in `DataFrameGroupBy` and`SeriesGroupBy` when`by` is a categorical type and`sort=False` (GH 48976)
- Performance improvement in `DataFrameGroupBy` and`SeriesGroupBy` when`by` is a categorical type and`observed=False` (GH 49596)
- Performance improvement in `read_stata()` with parameter`index_col` set to`None` (the default). Now the index will be a`RangeIndex` instead of`Int64Index` (GH 49745)
- Performance improvement in `merge()` when not merging on the index - the new index will now be`RangeIndex` instead of`Int64Index` (GH 49478)
- Performance improvement in `DataFrame.to_dict()` and`Series.to_dict()` when using any non-object dtypes (GH 46470)
- Performance improvement in `read_html()` when there are multiple tables (GH 49929)
- Performance improvement in `Period` constructor when constructing from a string or integer (GH 38312)
- Performance improvement in `to_datetime()` when using`'%Y%m%d'` format (GH 17410)
- Performance improvement in `to_datetime()` when format is given or can be inferred (GH 50465)
- Performance improvement in `Series.median()` for nullable dtypes (GH 50838)
- Performance improvement in `read_csv()` when passing`to_datetime()` lambda-function to`date_parser` and inputs have mixed timezone offsets (GH 35296)
- Performance improvement in `isna()` and`isnull()` (GH 50658)
- Performance improvement in `SeriesGroupBy.value_counts()` with categorical dtype (GH 46202)
- Fixed a reference leak in `read_hdf()` (GH 37441)
- Fixed a memory leak in `DataFrame.to_json()` and`Series.to_json()` when serializing datetimes and timedeltas (GH 40443)
- Decreased memory usage in many `DataFrameGroupBy` methods (GH 51090)
- Performance improvement in `DataFrame.round()` for an integer`decimal` parameter (GH 17254)
- Performance improvement in `DataFrame.replace()` and`Series.replace()` when using a large dict for`to_replace` (GH 6697)
- Memory improvement in `StataReader` when reading seekable files (GH 48922)

## Bug fixes#

### Categorical#

- Bug in `Categorical.set_categories()` losing dtype information (GH 48812)
- Bug in `Series.replace()` with categorical dtype when`to_replace` values overlap with new values (GH 49404)
- Bug in `Series.replace()` with categorical dtype losing nullable dtypes of underlying categories (GH 49404)
- Bug in `DataFrame.groupby()` and`Series.groupby()` would reorder categories when used as a grouper (GH 48749)
- Bug in `Categorical` constructor when constructing from a`Categorical` object and`dtype="category"` losing ordered-ness (GH 49309)
- Bug in `SeriesGroupBy.min()` ,`SeriesGroupBy.max()` ,`DataFrameGroupBy.min()` , and`DataFrameGroupBy.max()` with unordered`CategoricalDtype` with no groups failing to raise`TypeError` (GH 51034)

### Datetimelike#

- Bug in `pandas.infer_freq()` , raising`TypeError` when inferred on`RangeIndex` (GH 47084)
- Bug in `to_datetime()` incorrectly raising`OverflowError` with string arguments corresponding to large integers (GH 50533)
- Bug in `to_datetime()` was raising on invalid offsets with`errors='coerce'` and`infer_datetime_format=True` (GH 48633)
- Bug in `DatetimeIndex` constructor failing to raise when`tz=None` is explicitly specified in conjunction with timezone-aware`dtype` or data (GH 48659)
- Bug in subtracting a `datetime` scalar from`DatetimeIndex` failing to retain the original`freq` attribute (GH 48818)
- Bug in `pandas.tseries.holiday.Holiday` where a half-open date interval causes inconsistent return types from`USFederalHolidayCalendar.holidays()` (GH 49075)
- Bug in rendering `DatetimeIndex` and`Series` and`DataFrame` with timezone-aware dtypes with`dateutil` or`zoneinfo` timezones near daylight-savings transitions (GH 49684)
- Bug in `to_datetime()` was raising`ValueError` when parsing`Timestamp` ,`datetime.datetime` ,`datetime.date` , or`np.datetime64` objects when non-ISO8601`format` was passed (GH 49298, GH 50036)
- Bug in `to_datetime()` was raising`ValueError` when parsing empty string and non-ISO8601 format was passed. Now, empty strings will be parsed as`NaT` , for compatibility with how is done for ISO8601 formats (GH 50251)
- Bug in `Timestamp` was showing`UserWarning` , which was not actionable by users, when parsing non-ISO8601 delimited date strings (GH 50232)
- Bug in `to_datetime()` was showing misleading`ValueError` when parsing dates with format containing ISO week directive and ISO weekday directive (GH 50308)
- Bug in `Timestamp.round()` when the`freq` argument has zero-duration (e.g. “0ns”) returning incorrect results instead of raising (GH 49737)
- Bug in `to_datetime()` was not raising`ValueError` when invalid format was passed and`errors` was`'ignore'` or`'coerce'` (GH 50266)
- Bug in `DateOffset` was throwing`TypeError` when constructing with milliseconds and another super-daily argument (GH 49897)
- Bug in `to_datetime()` was not raising`ValueError` when parsing string with decimal date with format`'%Y%m%d'` (GH 50051)
- Bug in `to_datetime()` was not converting`None` to`NaT` when parsing mixed-offset date strings with ISO8601 format (GH 50071)
- Bug in `to_datetime()` was not returning input when parsing out-of-bounds date string with`errors='ignore'` and`format='%Y%m%d'` (GH 14487)
- Bug in `to_datetime()` was converting timezone-naive`datetime.datetime` to timezone-aware when parsing with timezone-aware strings, ISO8601 format, and`utc=False` (GH 50254)
- Bug in `to_datetime()` was throwing`ValueError` when parsing dates with ISO8601 format where some values were not zero-padded (GH 21422)
- Bug in `to_datetime()` was giving incorrect results when using`format='%Y%m%d'` and`errors='ignore'` (GH 26493)
- Bug in `to_datetime()` was failing to parse date strings`'today'` and`'now'` if`format` was not ISO8601 (GH 50359)
- Bug in `Timestamp.utctimetuple()` raising a`TypeError` (GH 32174)
- Bug in `to_datetime()` was raising`ValueError` when parsing mixed-offset`Timestamp` with`errors='ignore'` (GH 50585)
- Bug in `to_datetime()` was incorrectly handling floating-point inputs within 1`unit` of the overflow boundaries (GH 50183)
- Bug in `to_datetime()` with unit of “Y” or “M” giving incorrect results, not matching pointwise`Timestamp` results (GH 50870)
- Bug in `Series.interpolate()` and`DataFrame.interpolate()` with datetime or timedelta dtypes incorrectly raising`ValueError` (GH 11312)
- Bug in `to_datetime()` was not returning input with`errors='ignore'` when input was out-of-bounds (GH 50587)
- Bug in `DataFrame.from_records()` when given a`DataFrame` input with timezone-aware datetime64 columns incorrectly dropping the timezone-awareness (GH 51162)
- Bug in `to_datetime()` was raising`decimal.InvalidOperation` when parsing date strings with`errors='coerce'` (GH 51084)
- Bug in `to_datetime()` with both`unit` and`origin` specified returning incorrect results (GH 42624)
- Bug in `Series.astype()` and`DataFrame.astype()` when converting an object-dtype object containing timezone-aware datetimes or strings to`datetime64[ns]` incorrectly localizing as UTC instead of raising`TypeError` (GH 50140)
- Bug in `DataFrameGroupBy.quantile()` and`SeriesGroupBy.quantile()` with datetime or timedelta dtypes giving incorrect results for groups containing`NaT` (GH 51373)
- Bug in `DataFrameGroupBy.quantile()` and`SeriesGroupBy.quantile()` incorrectly raising with`PeriodDtype` or`DatetimeTZDtype` (GH 51373)

### Timedelta#

- Bug in `to_timedelta()` raising error when input has nullable dtype`Float64` (GH 48796)
- Bug in `Timedelta` constructor incorrectly raising instead of returning`NaT` when given a`np.timedelta64("nat")` (GH 48898)
- Bug in `Timedelta` constructor failing to raise when passed both a`Timedelta` object and keywords (e.g. days, seconds) (GH 48898)
- Bug in `Timedelta` comparisons with very large`datetime.timedelta` objects incorrect raising`OutOfBoundsTimedelta` (GH 49021)

### Timezones#

- Bug in `Series.astype()` and`DataFrame.astype()` with object-dtype containing multiple timezone-aware`datetime` objects with heterogeneous timezones to a`DatetimeTZDtype` incorrectly raising (GH 32581)
- Bug in `to_datetime()` was failing to parse date strings with timezone name when`format` was specified with`%Z` (GH 49748)
- Better error message when passing invalid values to `ambiguous` parameter in`Timestamp.tz_localize()` (GH 49565)
- Bug in string parsing incorrectly allowing a `Timestamp` to be constructed with an invalid timezone, which would raise when trying to print (GH 50668)
- Corrected TypeError message in `objects_to_datetime64ns()` to inform that DatetimeIndex has mixed timezones (GH 50974)

### Numeric#

- Bug in `DataFrame.add()` cannot apply ufunc when inputs contain mixed DataFrame type and Series type (GH 39853)
- Bug in arithmetic operations on `Series` not propagating mask when combining masked dtypes and numpy dtypes (GH 45810, GH 42630)
- Bug in `DataFrame.sem()` and`Series.sem()` where an erroneous`TypeError` would always raise when using data backed by an`ArrowDtype` (GH 49759)
- Bug in `Series.__add__()` casting to object for list and masked`Series` (GH 22962)
- Bug in `mode()` where`dropna=False` was not respected when there was`NA` values (GH 50982)
- Bug in `DataFrame.query()` with`engine="numexpr"` and column names are`min` or`max` would raise a`TypeError` (GH 50937)
- Bug in `DataFrame.min()` and`DataFrame.max()` with tz-aware data containing`pd.NaT` and`axis=1` would return incorrect results (GH 51242)

### Conversion#

- Bug in constructing `Series` with`int64` dtype from a string list raising instead of casting (GH 44923)
- Bug in constructing `Series` with masked dtype and boolean values with`NA` raising (GH 42137)
- Bug in `DataFrame.eval()` incorrectly raising an`AttributeError` when there are negative values in function call (GH 46471)
- Bug in `Series.convert_dtypes()` not converting dtype to nullable dtype when`Series` contains`NA` and has dtype`object` (GH 48791)
- Bug where any `ExtensionDtype` subclass with`kind="M"` would be interpreted as a timezone type (GH 34986)
- Bug in `arrays.ArrowExtensionArray` that would raise`NotImplementedError` when passed a sequence of strings or binary (GH 49172)
- Bug in `Series.astype()` raising`pyarrow.ArrowInvalid` when converting from a non-pyarrow string dtype to a pyarrow numeric type (GH 50430)
- Bug in `DataFrame.astype()` modifying input array inplace when converting to`string` and`copy=False` (GH 51073)
- Bug in `Series.to_numpy()` converting to NumPy array before applying`na_value` (GH 48951)
- Bug in `DataFrame.astype()` not copying data when converting to pyarrow dtype (GH 50984)
- Bug in `to_datetime()` was not respecting`exact` argument when`format` was an ISO8601 format (GH 12649)
- Bug in `TimedeltaArray.astype()` raising`TypeError` when converting to a pyarrow duration type (GH 49795)
- Bug in `DataFrame.eval()` and`DataFrame.query()` raising for extension array dtypes (GH 29618, GH 50261, GH 31913)
- Bug in `Series()` not copying data when created from`Index` and`dtype` is equal to`dtype` from`Index` (GH 52008)

### Strings#

- Bug in `pandas.api.types.is_string_dtype()` that would not return`True` for`StringDtype` or`ArrowDtype` with`pyarrow.string()` (GH 15585)
- Bug in converting string dtypes to “datetime64[ns]” or “timedelta64[ns]” incorrectly raising `TypeError` (GH 36153)
- Bug in setting values in a string-dtype column with an array, mutating the array as side effect when it contains missing values (GH 51299)

### Interval#

- Bug in `IntervalIndex.is_overlapping()` incorrect output if interval has duplicate left boundaries (GH 49581)
- Bug in `Series.infer_objects()` failing to infer`IntervalDtype` for an object series of`Interval` objects (GH 50090)
- Bug in `Series.shift()` with`IntervalDtype` and invalid null`fill_value` failing to raise`TypeError` (GH 51258)

### Indexing#

- Bug in `DataFrame.__setitem__()` raising when indexer is a`DataFrame` with`boolean` dtype (GH 47125)
- Bug in `DataFrame.reindex()` filling with wrong values when indexing columns and index for`uint` dtypes (GH 48184)
- Bug in `DataFrame.loc()` when setting`DataFrame` with different dtypes coercing values to single dtype (GH 50467)
- Bug in `DataFrame.sort_values()` where`None` was not returned when`by` is empty list and`inplace=True` (GH 50643)
- Bug in `DataFrame.loc()` coercing dtypes when setting values with a list indexer (GH 49159)
- Bug in `Series.loc()` raising error for out of bounds end of slice indexer (GH 50161)
- Bug in `DataFrame.loc()` raising`ValueError` with all`False``bool` indexer and empty object (GH 51450)
- Bug in `DataFrame.loc()` raising`ValueError` with`bool` indexer and`MultiIndex` (GH 47687)
- Bug in `DataFrame.loc()` raising`IndexError` when setting values for a pyarrow-backed column with a non-scalar indexer (GH 50085)
- Bug in `DataFrame.__getitem__()` ,`Series.__getitem__()` ,`DataFrame.__setitem__()` and`Series.__setitem__()` when indexing on indexes with extension float dtypes (`Float64` &`Float64` ) or complex dtypes using integers (GH 51053)
- Bug in `DataFrame.loc()` modifying object when setting incompatible value with an empty indexer (GH 45981)
- Bug in `DataFrame.__setitem__()` raising`ValueError` when right hand side is`DataFrame` with`MultiIndex` columns (GH 49121)
- Bug in `DataFrame.reindex()` casting dtype to`object` when`DataFrame` has single extension array column when re-indexing`columns` and`index` (GH 48190)
- Bug in `DataFrame.iloc()` raising`IndexError` when indexer is a`Series` with numeric extension array dtype (GH 49521)
- Bug in `describe()` when formatting percentiles in the resulting index showed more decimals than needed (GH 46362)
- Bug in `DataFrame.compare()` does not recognize differences when comparing`NA` with value in nullable dtypes (GH 48939)
- Bug in `Series.rename()` with`MultiIndex` losing extension array dtypes (GH 21055)
- Bug in `DataFrame.isetitem()` coercing extension array dtypes in`DataFrame` to object (GH 49922)
- Bug in `Series.__getitem__()` returning corrupt object when selecting from an empty pyarrow backed object (GH 51734)
- Bug in `BusinessHour` would cause creation of`DatetimeIndex` to fail when no opening hour was included in the index (GH 49835)

### Missing#

- Bug in `Index.equals()` raising`TypeError` when`Index` consists of tuples that contain`NA` (GH 48446)
- Bug in `Series.map()` caused incorrect result when data has NaNs and defaultdict mapping was used (GH 48813)
- Bug in `NA` raising a`TypeError` instead of return`NA` when performing a binary operation with a`bytes` object (GH 49108)
- Bug in `DataFrame.update()` with`overwrite=False` raising`TypeError` when`self` has column with`NaT` values and column not present in`other` (GH 16713)
- Bug in `Series.replace()` raising`RecursionError` when replacing value in object-dtype`Series` containing`NA` (GH 47480)
- Bug in `Series.replace()` raising`RecursionError` when replacing value in numeric`Series` with`NA` (GH 50758)

### MultiIndex#

- Bug in `MultiIndex.get_indexer()` not matching`NaN` values (GH 29252, GH 37222, GH 38623, GH 42883, GH 43222, GH 46173, GH 48905)
- Bug in `MultiIndex.argsort()` raising`TypeError` when index contains`NA` (GH 48495)
- Bug in `MultiIndex.difference()` losing extension array dtype (GH 48606)
- Bug in `MultiIndex.set_levels` raising`IndexError` when setting empty level (GH 48636)
- Bug in `MultiIndex.unique()` losing extension array dtype (GH 48335)
- Bug in `MultiIndex.intersection()` losing extension array (GH 48604)
- Bug in `MultiIndex.union()` losing extension array (GH 48498, GH 48505, GH 48900)
- Bug in `MultiIndex.union()` not sorting when sort=None and index contains missing values (GH 49010)
- Bug in `MultiIndex.append()` not checking names for equality (GH 48288)
- Bug in `MultiIndex.symmetric_difference()` losing extension array (GH 48607)
- Bug in `MultiIndex.join()` losing dtypes when`MultiIndex` has duplicates (GH 49830)
- Bug in `MultiIndex.putmask()` losing extension array (GH 49830)
- Bug in `MultiIndex.value_counts()` returning a`Series` indexed by flat index of tuples instead of a`MultiIndex` (GH 49558)

### I/O#

- Bug in `read_sas()` caused fragmentation of`DataFrame` and raised`errors.PerformanceWarning` (GH 48595)
- Improved error message in `read_excel()` by including the offending sheet name when an exception is raised while reading a file (GH 48706)
- Bug when a pickling a subset PyArrow-backed data that would serialize the entire data instead of the subset (GH 42600)
- Bug in `read_sql_query()` ignoring`dtype` argument when`chunksize` is specified and result is empty (GH 50245)
- Bug in `read_csv()` for a single-line csv with fewer columns than`names` raised`errors.ParserError` with`engine="c"` (GH 47566)
- Bug in `read_json()` raising with`orient="table"` and`NA` value (GH 40255)
- Bug in displaying `string` dtypes not showing storage option (GH 50099)
- Bug in `DataFrame.to_string()` with`header=False` that printed the index name on the same line as the first row of the data (GH 49230)
- Bug in `DataFrame.to_string()` ignoring float formatter for extension arrays (GH 39336)
- Fixed memory leak which stemmed from the initialization of the internal JSON module (GH 49222)
- Fixed issue where `json_normalize()` would incorrectly remove leading characters from column names that matched the`sep` argument (GH 49861)
- Bug in `read_csv()` unnecessarily overflowing for extension array dtype when containing`NA` (GH 32134)
- Bug in `DataFrame.to_dict()` not converting`NA` to`None` (GH 50795)
- Bug in `DataFrame.to_json()` where it would segfault when failing to encode a string (GH 50307)
- Bug in `DataFrame.to_html()` with`na_rep` set when the`DataFrame` contains non-scalar data (GH 47103)
- Bug in `read_xml()` where file-like objects failed when iterparse is used (GH 50641)
- Bug in `read_csv()` when`engine="pyarrow"` where`encoding` parameter was not handled correctly (GH 51302)
- Bug in `read_xml()` ignored repeated elements when iterparse is used (GH 51183)
- Bug in `ExcelWriter` leaving file handles open if an exception occurred during instantiation (GH 51443)
- Bug in `DataFrame.to_parquet()` where non-string index or columns were raising a`ValueError` when`engine="pyarrow"` (GH 52036)

### Period#

- Bug in `Period.strftime()` and`PeriodIndex.strftime()` , raising`UnicodeDecodeError` when a locale-specific directive was passed (GH 46319)
- Bug in adding a `Period` object to an array of`DateOffset` objects incorrectly raising`TypeError` (GH 50162)
- Bug in `Period` where passing a string with finer resolution than nanosecond would result in a`KeyError` instead of dropping the extra precision (GH 50417)
- Bug in parsing strings representing Week-periods e.g. “2017-01-23/2017-01-29” as minute-frequency instead of week-frequency (GH 50803)
- Bug in `DataFrameGroupBy.sum()` ,`DataFrameGroupByGroupBy.cumsum()` ,`DataFrameGroupByGroupBy.prod()` ,`DataFrameGroupByGroupBy.cumprod()` with`PeriodDtype` failing to raise`TypeError` (GH 51040)
- Bug in parsing empty string with `Period` incorrectly raising`ValueError` instead of returning`NaT` (GH 51349)

### Plotting#

- Bug in `DataFrame.plot.hist()` , not dropping elements of`weights` corresponding to`NaN` values in`data` (GH 48884)
- `ax.set_xlim` was sometimes raising`UserWarning` which users couldn’t address due to`set_xlim` not accepting parsing arguments - the converter now uses`Timestamp()` instead (GH 49148)

### Groupby/resample/rolling#

- Bug in `ExponentialMovingWindow` with`online` not raising a`NotImplementedError` for unsupported operations (GH 48834)
- Bug in `DataFrameGroupBy.sample()` raises`ValueError` when the object is empty (GH 48459)
- Bug in `Series.groupby()` raises`ValueError` when an entry of the index is equal to the name of the index (GH 48567)
- Bug in `DataFrameGroupBy.resample()` produces inconsistent results when passing empty DataFrame (GH 47705)
- Bug in `DataFrameGroupBy` and`SeriesGroupBy` would not include unobserved categories in result when grouping by categorical indexes (GH 49354)
- Bug in `DataFrameGroupBy` and`SeriesGroupBy` would change result order depending on the input index when grouping by categoricals (GH 49223)
- Bug in `DataFrameGroupBy` and`SeriesGroupBy` when grouping on categorical data would sort result values even when used with`sort=False` (GH 42482)
- Bug in `DataFrameGroupBy.apply()` and`SeriesGroupBy.apply` with`as_index=False` would not attempt the computation without using the grouping keys when using them failed with a`TypeError` (GH 49256)
- Bug in `DataFrameGroupBy.describe()` would describe the group keys (GH 49256)
- Bug in `SeriesGroupBy.describe()` with`as_index=False` would have the incorrect shape (GH 49256)
- Bug in `DataFrameGroupBy` and`SeriesGroupBy` with`dropna=False` would drop NA values when the grouper was categorical (GH 36327)
- Bug in `SeriesGroupBy.nunique()` would incorrectly raise when the grouper was an empty categorical and`observed=True` (GH 21334)
- Bug in `SeriesGroupBy.nth()` would raise when grouper contained NA values after subsetting from a`DataFrameGroupBy` (GH 26454)
- Bug in `DataFrame.groupby()` would not include a`Grouper` specified by`key` in the result when`as_index=False` (GH 50413)
- Bug in `DataFrameGroupBy.value_counts()` would raise when used with a`TimeGrouper` (GH 50486)
- Bug in `Resampler.size()` caused a wide`DataFrame` to be returned instead of a`Series` with`MultiIndex` (GH 46826)
- Bug in `DataFrameGroupBy.transform()` and`SeriesGroupBy.transform()` would raise incorrectly when grouper had`axis=1` for`"idxmin"` and`"idxmax"` arguments (GH 45986)
- Bug in `DataFrameGroupBy` would raise when used with an empty DataFrame, categorical grouper, and`dropna=False` (GH 50634)
- Bug in `SeriesGroupBy.value_counts()` did not respect`sort=False` (GH 50482)
- Bug in `DataFrameGroupBy.resample()` raises`KeyError` when getting the result from a key list when resampling on time index (GH 50840)
- Bug in `DataFrameGroupBy.transform()` and`SeriesGroupBy.transform()` would raise incorrectly when grouper had`axis=1` for`"ngroup"` argument (GH 45986)
- Bug in `DataFrameGroupBy.describe()` produced incorrect results when data had duplicate columns (GH 50806)
- Bug in `DataFrameGroupBy.agg()` with`engine="numba"` failing to respect`as_index=False` (GH 51228)
- Bug in `DataFrameGroupBy.agg()` ,`SeriesGroupBy.agg()` , and`Resampler.agg()` would ignore arguments when passed a list of functions (GH 50863)
- Bug in `DataFrameGroupBy.ohlc()` ignoring`as_index=False` (GH 51413)
- Bug in `DataFrameGroupBy.agg()` after subsetting columns (e.g.`.groupby(...)[["a", "b"]]` ) would not include groupings in the result (GH 51186)

### Reshaping#

- Bug in `DataFrame.pivot_table()` raising`TypeError` for nullable dtype and`margins=True` (GH 48681)
- Bug in `DataFrame.unstack()` and`Series.unstack()` unstacking wrong level of`MultiIndex` when`MultiIndex` has mixed names (GH 48763)
- Bug in `DataFrame.melt()` losing extension array dtype (GH 41570)
- Bug in `DataFrame.pivot()` not respecting`None` as column name (GH 48293)
- Bug in `DataFrame.join()` when`left_on` or`right_on` is or includes a`CategoricalIndex` incorrectly raising`AttributeError` (GH 48464)
- Bug in `DataFrame.pivot_table()` raising`ValueError` with parameter`margins=True` when result is an empty`DataFrame` (GH 49240)
- Clarified error message in `merge()` when passing invalid`validate` option (GH 49417)
- Bug in `DataFrame.explode()` raising`ValueError` on multiple columns with`NaN` values or empty lists (GH 46084)
- Bug in `DataFrame.transpose()` with`IntervalDtype` column with`timedelta64[ns]` endpoints (GH 44917)
- Bug in `DataFrame.agg()` and`Series.agg()` would ignore arguments when passed a list of functions (GH 50863)

### Sparse#

- Bug in `Series.astype()` when converting a`SparseDtype` with`datetime64[ns]` subtype to`int64` dtype raising, inconsistent with the non-sparse behavior (GH 49631,:issue:50087)
- Bug in `Series.astype()` when converting a from`datetime64[ns]` to`Sparse[datetime64[ns]]` incorrectly raising (GH 50082)
- Bug in `Series.sparse.to_coo()` raising`SystemError` when`MultiIndex` contains a`ExtensionArray` (GH 50996)

### ExtensionArray#

- Bug in `Series.mean()` overflowing unnecessarily with nullable integers (GH 48378)
- Bug in `Series.tolist()` for nullable dtypes returning numpy scalars instead of python scalars (GH 49890)
- Bug in `Series.round()` for pyarrow-backed dtypes raising`AttributeError` (GH 50437)
- Bug when concatenating an empty DataFrame with an ExtensionDtype to another DataFrame with the same ExtensionDtype, the resulting dtype turned into object (GH 48510)
- Bug in `array.PandasArray.to_numpy()` raising with`NA` value when`na_value` is specified (GH 40638)
- Bug in `api.types.is_numeric_dtype()` where a custom`ExtensionDtype` would not return`True` if`_is_numeric` returned`True` (GH 50563)
- Bug in `api.types.is_integer_dtype()` ,`api.types.is_unsigned_integer_dtype()` ,`api.types.is_signed_integer_dtype()` ,`api.types.is_float_dtype()` where a custom`ExtensionDtype` would not return`True` if`kind` returned the corresponding NumPy type (GH 50667)
- Bug in `Series` constructor unnecessarily overflowing for nullable unsigned integer dtypes (GH 38798, GH 25880)
- Bug in setting non-string value into `StringArray` raising`ValueError` instead of`TypeError` (GH 49632)
- Bug in `DataFrame.reindex()` not honoring the default`copy=True` keyword in case of columns with ExtensionDtype (and as a result also selecting multiple columns with getitem (`[]` ) didn’t correctly result in a copy) (GH 51197)
- Bug in `ArrowExtensionArray` logical operations`&` and`|` raising`KeyError` (GH 51688)

### Styler#

- Fix `background_gradient()` for nullable dtype`Series` with`NA` values (GH 50712)

### Metadata#

- Fixed metadata propagation in `DataFrame.corr()` and`DataFrame.cov()` (GH 28283)

### Other#

## Contributors#

A total of 260 people contributed patches to this release. People with a “+” by their names contributed a patch for the first time.

- 5j9 +
- ABCPAN-rank +
- Aarni Koskela +
- Aashish KC +
- Abubeker Mohammed +
- Adam Mróz +
- Adam Ormondroyd +
- Aditya Anulekh +
- Ahmed Ibrahim
- Akshay Babbar +
- Aleksa Radojicic +
- Alex +
- Alex Buzenet +
- Alex Kirko
- Allison Kwan +
- Amay Patel +
- Ambuj Pawar +
- Amotz +
- Andreas Schwab +
- Andrew Chen +
- Anton Shevtsov
- Antonio Ossa Guerra +
- Antonio Ossa-Guerra +
- Anushka Bishnoi +
- Arda Kosar
- Armin Berres
- Asadullah Naeem +
- Asish Mahapatra
- Bailey Lissington +
- BarkotBeyene
- Ben Beasley
- Bhavesh Rajendra Patil +
- Bibek Jha +
- Bill +
- Bishwas +
- CarlosGDCJ +
- Carlotta Fabian +
- Chris Roth +
- Chuck Cadman +
- Corralien +
- DG +
- Dan Hendry +
- Daniel Isaac
- David Kleindienst +
- David Poznik +
- David Rudel +
- DavidKleindienst +
- Dea María Léon +
- Deepak Sirohiwal +
- Dennis Chukwunta
- Douglas Lohmann +
- Dries Schaumont
- Dustin K +
- Edoardo Abati +
- Eduardo Chaves +
- Ege Özgüroğlu +
- Ekaterina Borovikova +
- Eli Schwartz +
- Elvis Lim +
- Emily Taylor +
- Emma Carballal Haire +
- Erik Welch +
- Fangchen Li
- Florian Hofstetter +
- Flynn Owen +
- Fredrik Erlandsson +
- Gaurav Sheni
- Georeth Chow +
- George Munyoro +
- Guilherme Beltramini
- Gulnur Baimukhambetova +
- H L +
- Hans
- Hatim Zahid +
- HighYoda +
- Hiki +
- Himanshu Wagh +
- Hugo van Kemenade +
- Idil Ismiguzel +
- Irv Lustig
- Isaac Chung
- Isaac Virshup
- JHM Darbyshire
- JHM Darbyshire (iMac)
- JMBurley
- Jaime Di Cristina
- Jan Koch
- JanVHII +
- Janosh Riebesell
- JasmandeepKaur +
- Jeremy Tuloup
- Jessica M +
- Jonas Haag
- Joris Van den Bossche
- João Meirelles +
- Julia Aoun +
- Justus Magin +
- Kang Su Min +
- Kevin Sheppard
- Khor Chean Wei
- Kian Eliasi
- Kostya Farber +
- KotlinIsland +
- Lakmal Pinnaduwage +
- Lakshya A Agrawal +
- Lawrence Mitchell +
- Levi Ob +
- Loic Diridollou
- Lorenzo Vainigli +
- Luca Pizzini +
- Lucas Damo +
- Luke Manley
- Madhuri Patil +
- Marc Garcia
- Marco Edward Gorelli
- Marco Gorelli
- MarcoGorelli
- Maren Westermann +
- Maria Stazherova +
- Marie K +
- Marielle +
- Mark Harfouche +
- Marko Pacak +
- Martin +
- Matheus Cerqueira +
- Matheus Pedroni +
- Matteo Raso +
- Matthew Roeschke
- MeeseeksMachine +
- Mehdi Mohammadi +
- Michael Harris +
- Michael Mior +
- Natalia Mokeeva +
- Neal Muppidi +
- Nick Crews
- Nishu Choudhary +
- Noa Tamir
- Noritada Kobayashi
- Omkar Yadav +
- P. Talley +
- Pablo +
- Pandas Development Team
- Parfait Gasana
- Patrick Hoefler
- Pedro Nacht +
- Philip +
- Pietro Battiston
- Pooja Subramaniam +
- Pranav Saibhushan Ravuri +
- Pranav. P. A +
- Ralf Gommers +
- RaphSku +
- Richard Shadrach
- Robsdedude +
- Roger
- Roger Thomas
- RogerThomas +
- SFuller4 +
- Salahuddin +
- Sam Rao
- Sean Patrick Malloy +
- Sebastian Roll +
- Shantanu
- Shashwat +
- Shashwat Agrawal +
- Shiko Wamwea +
- Shoham Debnath
- Shubhankar Lohani +
- Siddhartha Gandhi +
- Simon Hawkins
- Soumik Dutta +
- Sowrov Talukder +
- Stefanie Molin
- Stefanie Senger +
- Stepfen Shawn +
- Steven Rotondo
- Stijn Van Hoey
- Sudhansu +
- Sven
- Sylvain MARIE
- Sylvain Marié
- Tabea Kossen +
- Taylor Packard
- Terji Petersen
- Thierry Moisan
- Thomas H +
- Thomas Li
- Torsten Wörtwein
- Tsvika S +
- Tsvika Shapira +
- Vamsi Verma +
- Vinicius Akira +
- William Andrea
- William Ayd
- William Blum +
- Wilson Xing +
- Xiao Yuan +
- Xnot +
- Yasin Tatar +
- Yuanhao Geng
- Yvan Cywan +
- Zachary Moon +
- Zhengbo Wang +
- abonte +
- adrienpacifico +
- alm
- amotzop +
- andyjessen +
- anonmouse1 +
- bang128 +
- bishwas jha +
- calhockemeyer +
- carla-alves-24 +
- carlotta +
- casadipietra +
- catmar22 +
- cfabian +
- codamuse +
- dataxerik
- davidleon123 +
- dependabot[bot] +
- fdrocha +
- github-actions[bot]
- himanshu_wagh +
- iofall +
- jakirkham +
- jbrockmendel
- jnclt +
- joelchen +
- joelsonoda +
- joshuabello2550
- joycewamwea +
- kathleenhang +
- krasch +
- ltoniazzi +
- luke396 +
- milosz-martynow +
- minat-hub +
- mliu08 +
- monosans +
- nealxm
- nikitaved +
- paradox-lab +
- partev
- raisadz +
- ram vikram singh +
- rebecca-palmer
- sarvaSanjay +
- seljaks +
- silviaovo +
- smij720 +
- soumilbaldota +
- stellalin7 +
- strawberry beach sandals +
- tmoschou +
- uzzell +
- yqyqyq-W +
- yun +
- Ádám Lippai
- 김동현 (Daniel Donghyun Kim) +