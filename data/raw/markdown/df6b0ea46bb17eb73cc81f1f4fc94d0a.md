# pandas.errors.ClosedFileError#

- exception pandas.errors.ClosedFileError[source]#
- Exception is raised when trying to perform an operation on a closed HDFStore file. `ClosedFileError` is specific to operations on`HDFStore` objects. Once an
HDFStore is closed, its resources are no longer available, and any further attempt
to access data or perform file operations will raise this exception.See also 
  - `HDFStore.close`
  - Closes the PyTables file handle.
  - `HDFStore.open`
  - Opens the file in the specified mode.
  - `HDFStore.is_open`
  - Returns a boolean indicating whether the file is open.
 Examples >>> store = pd.HDFStore("my-store", "a") >>> store.close() >>> store.keys() ... # ClosedFileError: my-store file is not open!