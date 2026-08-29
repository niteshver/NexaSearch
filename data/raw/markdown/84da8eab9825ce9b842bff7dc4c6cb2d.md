# pandas.Period.to_timestamp#

- 
Period.to_timestamp(*freq=None* ,*how='start'* )#
- Return the Timestamp representation of the Period. Uses the target frequency specified at the part of the period specified by how, which is either Start or Finish. 
  - Parameters:
    - **freq** str or DateOffset
    - Target frequency. Default is ‘D’ if self.freq is week or longer and ‘S’ otherwise.
    - **how** str, default ‘S’ (start)
    - One of ‘S’, ‘E’. Can be aliased as case insensitive ‘Start’, ‘Finish’, ‘Begin’, ‘End’.
  - Returns:
    - Timestamp
 Examples >>> period = pd.Period('2023-1-1', freq='D') >>> timestamp = period.to_timestamp() >>> timestamp Timestamp('2023-01-01 00:00:00')