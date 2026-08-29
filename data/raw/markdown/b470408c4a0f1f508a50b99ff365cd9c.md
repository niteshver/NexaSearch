# pandas.DataFrame.to_feather#

- 
DataFrame.to_feather(*path* ,***kwargs* )[source]#
- Write a DataFrame to the binary Feather format. 
  - Parameters:
    - **path** str, path object, file-like object
    - String, path object (implementing `os.PathLike[str]` ), or file-like
object implementing a binary`write()` function. If a string or a path,
it will be used as Root Directory path when writing a partitioned dataset.
    - ****kwargs**
    - Additional keywords passed to `pyarrow.feather.write_feather()` .
This includes the compression, compression_level, chunksize
and version keywords.
 Notes This function writes the dataframe as a feather file. Requires a default index. For saving the DataFrame with your custom index use a method that supports custom indices e.g. to_parquet. Examples >>> df = pd.DataFrame([[1, 2, 3], [4, 5, 6]]) >>> df.to_feather("file.feather")