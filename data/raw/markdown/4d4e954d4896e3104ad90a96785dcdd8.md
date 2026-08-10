# pandas.DataFrame.rename_axis#

- 
DataFrame.rename_axis(*mapper=<no_default>* ,*** ,*index=<no_default>* ,*columns=<no_default>* ,*axis=0* ,*copy=<no_default>* ,*inplace=False* )[source]#
- Set the name of the axis for the index or columns. This method is useful for labeling the axes in a MultiIndex or for providing descriptive names to axes. 
  - Parameters:
    - **mapper** scalar, list-like, optional
    - Value to set the axis name attribute. Use either `mapper` and`axis` to
specify the axis to target with`mapper` , or`index` and/or`columns` .
    - **index** scalar, list-like, dict-like or function, optional
    - A scalar, list-like, dict-like or functions transformations to apply to that axis’ values.
    - **columns** scalar, list-like, dict-like or function, optional
    - A scalar, list-like, dict-like or functions transformations to apply to that axis’ values.
    - **axis** {0 or ‘index’, 1 or ‘columns’}, default 0
    - The axis to rename.
    - **copy** bool, default False
    - This keyword is now ignored; changing its value will have no impact on the method. Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the user guide on Copy-on-Write for more details.
    - **inplace** bool, default False
    - Modifies the object directly, instead of creating a new Series or DataFrame.
  - Returns:
    - DataFrame, or None
    - The same type as the caller or None if `inplace=True` .
 See also 
  - `Series.rename`
  - Alter Series index labels or name.
  - `DataFrame.rename`
  - Alter DataFrame index labels or name.
  - `Index.rename`
  - Set new names on index.
 Notes `DataFrame.rename_axis` supports two calling conventions
  - `(index=index_mapper, columns=columns_mapper, ...)`
  - `(mapper, axis={'index', 'columns'}, ...)`
 The first calling convention will only modify the names of the index and/or the names of the Index object that is the columns. In this case, the parameter `copy` is ignored.The second calling convention will modify the names of the corresponding index if mapper is a list or a scalar. However, if mapper is dict-like or a function, it will use the deprecated behavior of modifying the axis *labels* .We *highly* recommend using keyword arguments to clarify your
intent.Examples **DataFrame**>>> df = pd.DataFrame( ... {"num_legs": [4, 4, 2], "num_arms": [0, 0, 2]}, ["dog", "cat", "monkey"] ... ) >>> df num_legs num_arms dog 4 0 cat 4 0 monkey 2 2 >>> df = df.rename_axis("animal") >>> df num_legs num_arms animal dog 4 0 cat 4 0 monkey 2 2 >>> df = df.rename_axis("limbs", axis="columns") >>> df limbs num_legs num_arms animal dog 4 0 cat 4 0 monkey 2 2 **MultiIndex**>>> df.index = pd.MultiIndex.from_product( ... [["mammal"], ["dog", "cat", "monkey"]], names=["type", "name"] ... ) >>> df limbs num_legs num_arms type name mammal dog 4 0 cat 4 0 monkey 2 2 >>> df.rename_axis(index={"type": "class"}) limbs num_legs num_arms class name mammal dog 4 0 cat 4 0 monkey 2 2 >>> df.rename_axis(columns=str.upper) LIMBS num_legs num_arms type name mammal dog 4 0 cat 4 0 monkey 2 2