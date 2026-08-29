# pandas.DataFrame.infer_objects#

- 
DataFrame.infer_objects(*copy=<no_default>* )[source]#
- Attempt to infer better dtypes for object columns. Attempts soft conversion of object-dtyped columns, leaving non-object and unconvertible columns unchanged. The inference rules are the same as during normal Series/DataFrame construction. 
  - Parameters:
    - **copy** bool, default False
    - This keyword is now ignored; changing its value will have no impact on the method. Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the user guide on Copy-on-Write for more details.
  - Returns:
    - same type as input object
    - Returns an object of the same type as the input object.
 See also 
  - `to_datetime`
  - Convert argument to datetime.
  - `to_timedelta`
  - Convert argument to timedelta.
  - `to_numeric`
  - Convert argument to numeric type.
  - `convert_dtypes`
  - Convert argument to best possible dtype.
 Examples >>> df = pd.DataFrame({"A": ["a", 1, 2, 3]}) >>> df = df.iloc[1:] >>> df A 1 1 2 2 3 3 >>> df.dtypes A object dtype: object >>> df.infer_objects().dtypes A int64 dtype: object