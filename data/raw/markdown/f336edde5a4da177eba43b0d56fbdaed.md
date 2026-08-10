# pandas.Series.str.repeat#

- 
Series.str.repeat(*repeats* )[source]#
- Duplicate each string in the Series or Index. Duplicates each string in the Series or Index, either by applying the same repeat count to all elements or by using different repeat values for each element. 
  - Parameters:
    - **repeats** int or sequence of int
    - Same value for all (int) or different value per (sequence).
  - Returns:
    - Series or pandas.Index
    - Series or Index of repeated string objects specified by input parameter repeats.
 See also 
  - `Series.str.lower`
  - Convert all characters in each string to lowercase.
  - `Series.str.upper`
  - Convert all characters in each string to uppercase.
  - `Series.str.title`
  - Convert each string to title case (capitalizing the first letter of each word).
  - `Series.str.strip`
  - Remove leading and trailing whitespace from each string.
  - `Series.str.replace`
  - Replace occurrences of a substring with another substring in each string.
  - `Series.str.ljust`
  - Left-justify each string in the Series/Index by padding with a specified character.
  - `Series.str.rjust`
  - Right-justify each string in the Series/Index by padding with a specified character.
 Examples >>> s = pd.Series(["a", "b", "c"]) >>> s 0 a 1 b 2 c dtype: str Single int repeats string in Series >>> s.str.repeat(repeats=2) 0 aa 1 bb 2 cc dtype: str Sequence of int repeats corresponding string in Series >>> s.str.repeat(repeats=[1, 2, 3]) 0 a 1 bb 2 ccc dtype: str