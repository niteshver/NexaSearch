# pandas.DataFrame.set_axis#

- 
DataFrame.set_axis(*labels* ,*** ,*axis=0* ,*copy=<no_default>* )[source]#
- Assign desired index to given axis. Indexes for column or row labels can be changed by assigning a list-like or Index. 
  - Parameters:
    - **labels** list-like, Index
    - The values for the new index.
    - **axis** {0 or ‘index’, 1 or ‘columns’}, default 0
    - The axis to update. The value 0 identifies the rows. For Series this parameter is unused and defaults to 0.
    - **copy** bool, default False
    - This keyword is now ignored; changing its value will have no impact on the method. Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the user guide on Copy-on-Write for more details.
  - Returns:
    - DataFrame
    - An object of type DataFrame.
 See also 
  - `DataFrame.rename_axis`
  - Alter the name of the index or columns.
 Examples >>> df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]}) Change the row labels. >>> df.set_axis(["a", "b", "c"], axis="index") A B a 1 4 b 2 5 c 3 6 Change the column labels. >>> df.set_axis(["I", "II"], axis="columns") I II 0 1 4 1 2 5 2 3 6