# pandas.Series.str.replace#

- 
Series.str.replace(*pat* ,*repl=None* ,*n=-1* ,*case=None* ,*flags=0* ,*regex=False* )[source]#
- Replace each occurrence of pattern/regex in the Series/Index. Equivalent to `str.replace()` or`re.sub()` , depending on
the regex value.
  - Parameters:
    - **pat** str, compiled regex, or a dict
    - String can be a character sequence or regular expression. Dictionary contains <key : value> pairs of strings to be replaced along with the updated value.
    - **repl** str or callable
    - Replacement string or a callable. The callable is passed the regex match object and must return a replacement string to be used. Must have a value of None if pat is a dict See `re.sub()` .
    - **n** int, default -1 (all)
    - Number of replacements to make from start.
    - **case** bool, default None
    - Determines if replace is case sensitive: 
      - If True, case sensitive (the default if pat is a string)
      - Set to False for case insensitive
      - Cannot be set if pat is a compiled regex.
    - **flags** int, default 0 (no flags)
    - Regex module flags, e.g. re.IGNORECASE. Cannot be set if pat is a compiled regex.
    - **regex** bool, default False
    - Determines if the passed-in pattern is a regular expression: 
      - If True, assumes the passed-in pattern is a regular expression.
      - If False, treats the pattern as a literal string
      - Cannot be set to False if pat is a compiled regex or repl is a callable.
  - Returns:
    - Series or Index of object
    - A copy of the object with all matching occurrences of pat replaced by repl.
  - Raises:
    - ValueError
      - if regex is False and repl is a callable or pat is a compiled regex
      - if pat is a compiled regex and case or flags is set
      - if pat is a dictionary and repl is not None.
 See also 
  - `Series.str.replace`
  - Method to replace occurrences of a substring with another substring.
  - `Series.str.extract`
  - Extract substrings using a regular expression.
  - `Series.str.findall`
  - Find all occurrences of a pattern or regex in each string.
  - `Series.str.split`
  - Split each string by a specified delimiter or pattern.
 Notes When pat is a compiled regex, all flags should be included in the compiled regex. Use of case, flags, or regex=False with a compiled regex will raise an error. Examples When pat is a dictionary, every key in pat is replaced with its corresponding value: >>> pd.Series(["A", "B", np.nan]).str.replace(pat={"A": "a", "B": "b"}) 0 a 1 b 2 NaN dtype: str When pat is a string and regex is True, the given pat is compiled as a regex. When repl is a string, it replaces matching regex patterns as with `re.sub()` . NaN value(s) in the Series are
left as is:>>> pd.Series(["foo", "fuz", np.nan]).str.replace("f.", "ba", regex=True) 0 bao 1 baz 2 NaN dtype: str When pat is a string and regex is False, every pat is replaced with repl as with `str.replace()` :>>> pd.Series(["f.o", "fuz", np.nan]).str.replace("f.", "ba", regex=False) 0 bao 1 fuz 2 NaN dtype: str When repl is a callable, it is called on every pat using `re.sub()` . The callable should expect one positional argument
(a regex object) and return a string.To get the idea: >>> pd.Series(["foo", "fuz", np.nan]).str.replace("f", repr, regex=True) 0 <re.Match object; span=(0, 1), match='f'>oo 1 <re.Match object; span=(0, 1), match='f'>uz 2 NaN dtype: str Reverse every lowercase alphabetic word: >>> repl = lambda m: m.group(0)[::-1] >>> ser = pd.Series(["foo 123", "bar baz", np.nan]) >>> ser.str.replace(r"[a-z]+", repl, regex=True) 0 oof 123 1 rab zab 2 NaN dtype: str Using regex groups (extract second group and swap case): >>> pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)" >>> repl = lambda m: m.group("two").swapcase() >>> ser = pd.Series(["One Two Three", "Foo Bar Baz"]) >>> ser.str.replace(pat, repl, regex=True) 0 tWO 1 bAR dtype: str Using a compiled regex with flags >>> import re >>> regex_pat = re.compile(r"FUZ", flags=re.IGNORECASE) >>> pd.Series(["foo", "fuz", np.nan]).str.replace(regex_pat, "bar", regex=True) 0 foo 1 bar 2 NaN dtype: str