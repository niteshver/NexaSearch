# pandas.errors.IncompatibleFrequency#

- exception pandas.errors.IncompatibleFrequency#
- Raised when trying to compare or operate between Periods with different frequencies. This error occurs when performing operations between Period objects or PeriodArrays that have different frequencies that cannot be aligned, such as comparing or doing arithmetic on periods with mismatched frequencies. See also 
  - `Period`
  - Represents a period of time.
  - `PeriodIndex`
  - Immutable ndarray holding ordinal values.
  - `PeriodDtype`
  - An ExtensionDtype for Period data.
 Examples Trying to compare Period objects with different frequencies: >>> pd.Period("2024-01", freq="M") - pd.Period("2024-01-01", freq="D") Traceback (most recent call last): IncompatibleFrequency: Input has different freq=D from Period(freq=M)