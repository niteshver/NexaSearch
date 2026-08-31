# pandas typing aliases#

## Typing aliases#

The typing declarations in `pandas/_typing.py` are considered private, and used
by pandas developers for type checking of the pandas code base.  For users, it is
highly recommended to use the `pandas-stubs` package that represents the officially
supported type declarations for users of pandas.
They are documented here for users who wish to use these declarations in their
own python code that calls pandas or expects certain results.

Warning

Note that the definitions and use cases of these aliases are subject to change without notice in any major, minor, or patch release of pandas.

Each of these aliases listed in the table below can be found by importing them from `pandas.api.typing.aliases`.

| Alias | Meaning | 
|---|---|
|  | Type of functions that can be passed to `DataFrame's` ,`Series'` , and`DataFrameGroupBy's``aggregate()` methods | 
|  | Argument type for `join` in`DataFrame's` and`Series'``align()` methods | 
|  | Argument type for `how` in`DataFrame's` and`Series'``dropna()` methods | 
|  | Used to represent `ExtensionArray` ,`numpy` arrays,`Index` and`Series` | 
|  | Used to represent `ExtensionArray` ,`numpy` arrays | 
|  | Argument type in `DataFrame's` and`Series'``astype()` methods | 
|  | `AnyArrayLike` plus sequences (not strings) and`range` | 
|  | Argument type for `axis` in many methods | 
|  | Argument type for `engine` in`pandas.read_csv()` | 
|  | Argument type for `colspace` in`pandas.DataFrame.to_html()` | 
|  | Argument type for `compression` in all I/O output methods except`pandas.DataFrame.to_parquet()` | 
|  | Argument type for `correlation` in`DataFrame's` and`Series'``corr()` methods | 
|  | Argument type for `keep` in`DataFrame's` and`Series'``drop_duplicates()` methods | 
|  | Types as objects that can be used to specify dtypes | 
|  | Argument type for `dtype` in various methods | 
|  | Argument type for `dtype_backend` in various methods | 
|  | Numpy dtypes and Extension dtypes | 
|  | Argument type for `if_sheet_exists` in`ExcelWriter` | 
|  | Argument type for `merge_cells` in`DataFrame's` and`Series'``to_excel()` methods | 
|  | Type of paths for files for I/O methods | 
|  | Argument type for `method` in various methods where NA values are filled | 
|  | Argument type for `float_format` in`DataFrame's` and`Series'``to_string()` methods | 
|  | Argument type for `formatters` in`DataFrame's` and`Series'``to_string()` methods | 
|  | Argument type for `orient` in`DataFrame.from_dict()` | 
|  | Argument type for `flavor` in`pandas.read_html()` | 
|  | Argument type for `errors` in multiple methods | 
|  | Argument type for `level` in multiple methods | 
|  | Argument type for `interpolate` in`DataFrame's` and`Series'``interpolate()` methods | 
|  | Argument type for `closed` in`Interval` ,`IntervalIndex` , and`inclusive` in various methods | 
|  | Restriction for `closed` to be`left` or`right` in`Interval` ,`IntervalIndex` , and`inclusive` in various methods | 
|  | Argument type for `engine` in`pandas.read_json()` | 
|  | Argument type for the return type of a callable for argument `default_handler` in`DataFrame's` and`Series'``to_json()` methods | 
|  | Argument type for `how` in`pandas.merge_ordered()` and for`join` in`Series.align()` | 
|  | Argument type for `validate` in`DataFrame.join()` | 
|  | Argument type for arguments that can be either a single value or a list of values in various methods | 
|  | Argument type for `how` in`pandas.merge()` | 
|  | Argument type for `validate` in`pandas.merge()` | 
|  | Argument type for `na_position` in`DataFrame's` and`Series'``sort_values()` methods | 
|  | Argument type for `keep` in`DataFrame's` and`Series'``nlargest()` ,`DataFrame's` and`Series'``nsmallest()` , and`SeriesGroupBy's``nlargest()` methods | 
|  | Argument type for `errors` in`DataFrame's` ,`Series'``to_hdf()` methods, and`DataFrame's` and`Series'``to_csv()` methods | 
|  | Return type for `ordered` in`pandas.CategoricalDtype` and`pandas.Categorical` | 
|  | Argument type for `compression` in`DataFrame.to_parquet()` | 
|  | Argument type for `interpolation` in`DataFrame's` and`Series'``quantile()` methods | 
|  | Additional argument type corresponding to buffers for various file reading methods | 
|  | Additional argument type corresponding to buffers for `pandas.read_csv()` | 
|  | Additional argument type corresponding to buffers for `pandas.read_pickle()` | 
|  | Argument type for `reindex` in`DataFrame's` and`Series'``reindex()` methods | 
|  | Types that can be stored in `Series` with non-object dtype | 
|  | Argument type used for scalar indexing operations, such as the `key` argument in`__getitem__()` methods | 
|  | Argument type used for sequence indexing operations, such as the `key` argument in`__getitem__()` methods | 
|  | Used for arguments that require sequences, but not plain strings | 
|  | Argument types for `start` and`end` in`Index.slice_locs()` | 
|  | Argument type for `kind` in`DataFrame's` and`Series'``sort_values()` methods | 
|  | Argument type for `storage_options` in various file output methods | 
|  | Argument type for `suffixes` in`pandas.merge()` ,`pandas.merge_ordered()` ,  and`DataFrame's` and`Series'``compare()` methods | 
|  | Argument type for `indexer` and`indices` in`DataFrame's` and`Series'``take()` methods | 
|  | Argument type for `ambiguous` in time operations | 
|  | Argument type for `origin` in`DataFrame's` ,`Series'``resample()` methods and for`Grouper` | 
|  | Argument type for `nonexistent` in time operations | 
|  | Time unit argument and return type for `pandas.Timedelta.unit` , arguments`unit` and`date_unit` | 
|  | Argument type for `offset` in various methods, such as`DataFrame's` and`Series'``resample()` ,`halflife` in`DataFrame's` ,`DataFrameGroupBy's` , and`Series'``ewm()` , and`start` and`end` in`pandas.timedelta_range()` | 
|  | Argument type for `origin` in`DataFrame's` and`Series'``resample()` , and in`pandas.to_datetime()` | 
|  | Argument type for `byteorder` in`DataFrame.to_stata()` | 
|  | Argument type for `how` in`DataFrame's` and`Series'``to_timestamp()` methods, and`convention` in`DataFrame's` and`Series'``resample()` methods | 
|  | Argument type for `join` in`DataFrame.update()` | 
|  | Argument type for `usecols` in`pandas.read_clipboard()` ,`pandas.read_csv()` and`pandas.read_excel()` | 
|  | Argument type for `method` in`Rolling's` and`Expanding's``rank()` methods, applicable in rolling and expanding window operations | 
|  | Additional argument type corresponding to buffers for various file output methods | 
|  | Additional argument type corresponding to buffers for `DataFrame's` ,`Series'` and`Styler's``to_excel()` methods | 
|  | Argument type for `parser` in`DataFrame.to_xml()` and`pandas.read_xml()` |