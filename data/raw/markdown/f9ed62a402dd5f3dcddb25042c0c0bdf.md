# pandas.Series.head#

- 
Series.head(*n=5* )[source]#
- Return the first n rows. This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it. For negative values of n, this function returns all rows except the last |n| rows, equivalent to `df[:n]` .If n is larger than the number of rows, this function returns all rows. 
  - Parameters
    - **n** int, default 5
    - Number of rows to select.
  - Returns
    - same type as caller
    - The first n rows of the caller object.
 See also 
  - `DataFrame.tail`
  - Returns the last n rows.
 Examples >>> df = pd.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion', ... 'monkey', 'parrot', 'shark', 'whale', 'zebra']}) >>> df animal 0 alligator 1 bee 2 falcon 3 lion 4 monkey 5 parrot 6 shark 7 whale 8 zebra Viewing the first 5 lines >>> df.head() animal 0 alligator 1 bee 2 falcon 3 lion 4 monkey Viewing the first n lines (three in this case) >>> df.head(3) animal 0 alligator 1 bee 2 falcon For negative values of n >>> df.head(-3) animal 0 alligator 1 bee 2 falcon 3 lion 4 monkey 5 parrot