# pandas.Float32Dtype#

- 
*class* pandas.Float32Dtype[source]#
- An ExtensionDtype for float32 data. This dtype uses `pd.NA` as missing value indicator.Examples For Float32Dtype: >>> ser = pd.Series([2.25, pd.NA], dtype=pd.Float32Dtype()) >>> ser.dtype Float32Dtype() For Float64Dtype: >>> ser = pd.Series([2.25, pd.NA], dtype=pd.Float64Dtype()) >>> ser.dtype Float64Dtype() Attributes **None**Methods **None**