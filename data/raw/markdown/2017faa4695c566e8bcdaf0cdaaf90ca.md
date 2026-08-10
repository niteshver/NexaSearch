# pandas.testing.assert_series_equal#

- 
pandas.testing.assert_series_equal(*left* ,*right* ,*check_dtype=True* ,*check_index_type='equiv'* ,*check_series_type=True* ,*check_names=True* ,*check_exact=<no_default>* ,*check_datetimelike_compat=False* ,*check_categorical=True* ,*check_category_order=True* ,*check_freq=True* ,*check_flags=True* ,*rtol=<no_default>* ,*atol=<no_default>* ,*obj='Series'* ,*** ,*check_index=True* ,*check_like=False* )[source]#
- Check that left and right Series are equal. This function compares two Series and raises an `AssertionError` if they
are not equal. It provides fine-grained control over which attributes to
check, including dtype, index, names, and categorical properties.
  - Parameters:
    - **left** Series
    - First Series to compare.
    - **right** Series
    - Second Series to compare.
    - **check_dtype** bool, default True
    - Whether to check the Series dtype is identical.
    - **check_index_type** bool or {‘equiv’}, default ‘equiv’
    - Whether to check the Index class, dtype and inferred_type are identical.
    - **check_series_type** bool, default True
    - Whether to check the Series class is identical.
    - **check_names** bool, default True
    - Whether to check the Series and Index names attribute.
    - **check_exact** bool, default False
    - Whether to compare number exactly. This also applies when checking Index equivalence. Changed in version 2.2.0: Defaults to True for integer dtypes if none of `check_exact` ,`rtol` and`atol` are specified.Changed in version 3.0.0: check_exact for comparing the Indexes defaults to True by checking if an Index is of integer dtypes. When `check_exact=True` , the comparison of object-dtype values
containing nested`numpy.ndarray` objects takes the type of
the nested object into account. In particular, a nested`numpy.ndarray` is not considered equivalent to a Python`list` , Python`tuple` , or a pandas`ExtensionArray` merely because the
contained values are the same.
    - **check_datetimelike_compat** bool, default False
    - Compare datetime-like which is comparable ignoring dtype. Deprecated since version 3.0.
    - **check_categorical** bool, default True
    - Whether to compare internal Categorical exactly.
    - **check_category_order** bool, default True
    - Whether to compare category order of internal Categoricals.
    - **check_freq** bool, default True
    - Whether to check the freq attribute on a DatetimeIndex or TimedeltaIndex. This check is skipped if `check_index=False` or`check_like=True` .
    - **check_flags** bool, default True
    - Whether to check the flags attribute.
    - **rtol** float, default 1e-5
    - Relative tolerance. Only used when check_exact is False.
    - **atol** float, default 1e-8
    - Absolute tolerance. Only used when check_exact is False.
    - **obj** str, default ‘Series’
    - Specify object name being compared, internally used to show appropriate assertion message.
    - **check_index** bool, default True
    - Whether to check index equivalence. If False, then compare only values.
    - **check_like** bool, default False
    - If True, ignore the order of the index. Must be False if check_index is False. Note: same labels must be with the same data.
 See also 
  - `testing.assert_index_equal`
  - Check that two Indexes are equal.
  - `testing.assert_frame_equal`
  - Check that two DataFrames are equal.
 Examples >>> from pandas import testing as tm >>> a = pd.Series([1, 2, 3, 4]) >>> b = pd.Series([1, 2, 3, 4]) >>> tm.assert_series_equal(a, b)