# pandas.DataFrame.map#

- 
DataFrame.map(*func* ,*na_action=None* ,***kwargs* )[source]#
- Apply a function to a Dataframe elementwise. New in version 2.1.0: DataFrame.applymap was deprecated and renamed to DataFrame.map. This method applies a function that accepts and returns a scalar to every element of a DataFrame. 
  - Parameters:
    - **func** callable
    - Python function, returns a single value from a single value.
    - **na_action** {None, ‘ignore’}, default None
    - If ‘ignore’, propagate NaN values, without passing them to func.
    - ****kwargs**
    - Additional keyword arguments to pass as keywords arguments to func.
  - Returns:
    - DataFrame
    - Transformed DataFrame.
 See also 
  - `DataFrame.apply`
  - Apply a function along input axis of DataFrame.
  - `DataFrame.replace`
  - Replace values given in to_replace with value.
  - `Series.map`
  - Apply a function elementwise on a Series.
 Examples >>> df = pd.DataFrame([[1, 2.12], [3.356, 4.567]]) >>> df 0 1 0 1.000 2.120 1 3.356 4.567 >>> df.map(lambda x: len(str(x))) 0 1 0 3 4 1 5 5 Like Series.map, NA values can be ignored: >>> df_copy = df.copy() >>> df_copy.iloc[0, 0] = pd.NA >>> df_copy.map(lambda x: len(str(x)), na_action='ignore') 0 1 0 NaN 4 1 5.0 5 Note that a vectorized version of func often exists, which will be much faster. You could square each number elementwise. >>> df.map(lambda x: x**2) 0 1 0 1.000000 4.494400 1 11.262736 20.857489 But it’s better to avoid map in that case. >>> df ** 2 0 1 0 1.000000 4.494400 1 11.262736 20.857489