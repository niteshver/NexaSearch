# pandas.IntervalIndex.length#

- property IntervalIndex.length[source]#
- Calculate the length of each interval in the IntervalIndex. This method returns a new Index containing the lengths of each interval in the IntervalIndex. The length of an interval is defined as the difference between its end and its start. 
  - Returns:
    - Index
    - An Index containing the lengths of each interval.
 See also 
  - `Interval.length`
  - Return the length of the Interval.
 Examples >>> intervals = pd.IntervalIndex.from_arrays( ... [1, 2, 3], [4, 5, 6], closed="right" ... ) >>> intervals.length Index([3, 3, 3], dtype='int64') >>> intervals = pd.IntervalIndex.from_tuples([(1, 5), (6, 10), (11, 15)]) >>> intervals.length Index([4, 4, 4], dtype='int64')