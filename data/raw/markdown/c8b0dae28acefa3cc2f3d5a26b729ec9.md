# pandas.api.typing.DataFrameGroupBy.corr#

- 
DataFrameGroupBy.corr(*method='pearson'* ,*min_periods=1* ,*numeric_only=False* )[source]#
- Compute pairwise correlation of columns, excluding NA/null values. Computes a correlation matrix for each group, measuring the linear or rank-based relationship between columns. 
  - Parameters:
    - **method** {‘pearson’, ‘kendall’, ‘spearman’} or callable
    - Method of correlation: 
      - pearson : standard correlation coefficient
      - kendall : Kendall Tau correlation coefficient
      - spearman : Spearman rank correlation
        - callable: callable with input two 1d ndarrays
        - and returning a float. Note that the returned matrix from corr will have 1 along the diagonals and will be symmetric regardless of the callable’s behavior.
    - **min_periods** int, optional
    - Minimum number of observations required per pair of columns to have a valid result. Currently only available for Pearson and Spearman correlation.
    - **numeric_only** bool, default False
    - Include only float, int or boolean data. Changed in version 2.0.0: The default value of `numeric_only` is now`False` .
  - Returns:
    - DataFrame
    - Correlation matrix.
 See also 
  - `DataFrame.corrwith`
  - Compute pairwise correlation with another DataFrame or Series.
  - `Series.corr`
  - Compute the correlation between two Series.
 Notes Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations. 
  - Pearson correlation coefficient
  - Kendall rank correlation coefficient
  - Spearman’s rank correlation coefficient
 Examples >>> df = pd.DataFrame( ... { ... "age": [2, 3, 4, 6, 6, 1, 2, 1], ... "weight": [2.1, 3.2, 4.1, 6.5, 3.3, 2.1, 4.1, 1.9], ... "pet": ["dog", "cat", "dog", "cat", "dog", "cat", "dog", "cat"], ... } ... ) >>> df age weight pet 0 2 2.1 dog 1 3 3.2 cat 2 4 4.1 dog 3 6 6.5 cat 4 6 3.3 dog 5 1 2.1 cat 6 2 4.1 dog 7 1 1.9 cat >>> df.groupby("pet").corr() age weight pet cat age 1.000000 0.989321 weight 0.989321 1.000000 dog age 1.000000 0.184177 weight 0.184177 1.000000