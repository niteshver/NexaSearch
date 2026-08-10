# pandas.Index.intersection#

- 
*final* Index.intersection(*other* ,*sort=False* )[source]#
- Form the intersection of two Index objects. This returns a new Index with elements common to the index and other. 
  - Parameters:
    - **other** Index or array-like
    - **sort** True, False or None, default False
    - Whether to sort the resulting index. 
      - None : sort the result, except when self and other are equal or when the values cannot be compared.
      - False : do not sort the result.
      - True : Sort the result (which may raise TypeError).
  - Returns:
    - Index
 Examples >>> idx1 = pd.Index([1, 2, 3, 4]) >>> idx2 = pd.Index([3, 4, 5, 6]) >>> idx1.intersection(idx2) Index([3, 4], dtype='int64')