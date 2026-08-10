# pandas.Series.case_when#

- 
Series.case_when(*caselist* )[source]#
- Replace values where the conditions are True. Replacement is performed in order; for each element, the first condition that evaluates to True determines the value used. This mirrors the semantics of a SQL `CASE WHEN` expression. If no condition matches, the original
value is kept.Added in version 2.2.0. 
  - Parameters:
    - **caselist** A list of tuples of conditions and expected replacements
    - Takes the form: `(condition0, replacement0)` ,`(condition1, replacement1)` , … .`condition` should be a 1-D boolean array-like object
or a callable. If`condition` is a callable,
it is computed on the Series
and should return a boolean Series or array.
The callable must not change the input Series
(though pandas doesn`t check it).`replacement` should be a
1-D array-like object, a scalar or a callable.
If`replacement` is a callable, it is computed on the Series
and should return a scalar or Series. The callable
must not change the input Series
(though pandas doesn`t check it).
  - Returns:
    - Series
    - A new Series with values replaced based on the provided conditions.
 See also 
  - `Series.mask`
  - Replace values where the condition is True.
 Examples >>> c = pd.Series([6, 7, 8, 9], name="c") >>> a = pd.Series([0, 0, 1, 2]) >>> b = pd.Series([0, 3, 4, 5]) >>> c.case_when( ... caselist=[ ... (a.gt(0), a), # condition, replacement ... (b.gt(0), b), ... ] ... ) 0 6 1 3 2 1 3 2 Name: c, dtype: int64