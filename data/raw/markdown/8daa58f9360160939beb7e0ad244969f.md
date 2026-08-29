# pandas.DataFrame.attrs#

- property DataFrame.attrs[source]#
- Dictionary of global attributes of this dataset. Warning attrs is experimental and may change without warning. See also 
  - `DataFrame.flags`
  - Global flags applying to this object.
 Notes Many operations that create new datasets will copy `attrs` . Copies
are always deep so that changing`attrs` will only affect the
present dataset.`pandas.concat()` and`pandas.merge()` will
only copy`attrs` if all input datasets have the same`attrs` .`attrs` is a property of a`Series` or`DataFrame` as a
whole, not of an individual column. The`DataFrame` constructor
does not extract`attrs` from a`Series` it is built from, and
assigning a`Series` as a column of an existing`DataFrame` (e.g.`df[col] = ser` ) does not modify`DataFrame.attrs` . Methods that build a new`DataFrame` from a single`Series` (such as`Series.to_frame()` ) do
propagate the source`attrs` .Examples For Series: >>> ser = pd.Series([1, 2, 3]) >>> ser.attrs = {"A": [10, 20, 30]} >>> ser.attrs {'A': [10, 20, 30]} For DataFrame: >>> df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}) >>> df.attrs = {"A": [10, 20, 30]} >>> df.attrs {'A': [10, 20, 30]}