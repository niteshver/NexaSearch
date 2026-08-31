# pandas.Index.astype#

- 
Index.astype(*dtype* ,*copy=True* )[source]#
- Create an Index with values cast to dtypes. The class of a new Index is determined by dtype. When conversion is impossible, a TypeError exception is raised. 
  - Parameters:
    - **dtype** numpy dtype or pandas type
    - Note that any signed integer dtype is treated as `'int64'` ,
and any unsigned integer dtype is treated as`'uint64'` ,
regardless of the size.
    - **copy** bool, default True
    - By default, astype always returns a newly allocated object. If copy is set to False and internal requirements on dtype are satisfied, the original data is used to create a new Index or the original Index is returned.
  - Returns:
    - Index
    - Index with values cast to specified dtype.
 Examples >>> idx = pd.Index([1, 2, 3]) >>> idx Index([1, 2, 3], dtype='int64') >>> idx.astype('float') Index([1.0, 2.0, 3.0], dtype='float64')