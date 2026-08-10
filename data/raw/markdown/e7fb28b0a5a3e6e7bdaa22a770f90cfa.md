# pandas.Index.memory_usage#

- 
Index.memory_usage(*deep=False* )[source]#
- Memory usage of the values. Returns the number of bytes consumed by the Index. When `deep=True` ,
the memory consumption of underlying objects referencing this Index
(e.g., the characters of object-dtype values) is included.
  - Parameters:
    - **deep** bool, default False
    - Introspect the data deeply, interrogate object dtypes for system-level memory consumption.
  - Returns:
    - bytes used
    - Returns memory usage of the values in the Index in bytes.
 See also 
  - `numpy.ndarray.nbytes`
  - Total bytes consumed by the elements of the array.
 Notes Memory usage does not include memory consumed by elements that are not components of the array if deep=False or if used on PyPy Examples >>> idx = pd.Index([1, 2, 3]) >>> idx.memory_usage() 24