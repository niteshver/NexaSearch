# pandas.Series.str.count#

- 
Series.str.count(*pat* ,*flags=0* )[source]#
- Count occurrences of pattern in each string of the Series/Index. This function is used to count the number of times a particular regex pattern is repeated in each of the string elements of the `Series` .
  - Parameters:
    - **pat** str
    - Valid regular expression.
    - **flags** int, default 0, meaning no flags
    - Flags for the re module. For a complete list, see here.
  - Returns:
    - Series or Index
    - Same type as the calling object containing the integer counts.
 See also Notes Some characters need to be escaped when passing in pat. eg. `'$'` has a special meaning in regex and must be escaped when
finding this literal character.Examples >>> s = pd.Series(["A", "B", "Aaba", "Baca", np.nan, "CABA", "cat"]) >>> s.str.count("a") 0 0.0 1 0.0 2 2.0 3 2.0 4 NaN 5 0.0 6 1.0 dtype: float64 Escape `'$'` to find the literal dollar sign.>>> s = pd.Series(["$", "B", "Aab$", "$$ca", "C$B$", "cat"]) >>> s.str.count("\\$") 0 1 1 0 2 1 3 2 4 2 5 0 dtype: int64 This is also available on Index >>> pd.Index(["A", "A", "Aaba", "cat"]).str.count("a") Index([0, 0, 2, 1], dtype='int64')