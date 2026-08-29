# pandas.Categorical.from_codes#

- 
*classmethod* Categorical.from_codes(*codes* ,*categories=None* ,*ordered=None* ,*dtype=None* ,*validate=True* )[source]#
- Make a Categorical type from codes and categories or dtype. This constructor is useful if you already have codes and categories/dtype and so do not need the (computation intensive) factorization step, which is usually done on the constructor. If your data does not follow this convention, please use the normal constructor. 
  - Parameters:
    - **codes** array-like of int
    - An integer array, where each integer points to a category in categories or dtype.categories, or else is -1 for NaN.
    - **categories** index-like, optional
    - The categories for the categorical. Items need to be unique. If the categories are not given here, then they must be provided in dtype.
    - **ordered** bool, optional
    - Whether or not this categorical is treated as an ordered categorical. If not given here or in dtype, the resulting categorical will be unordered.
    - **dtype** CategoricalDtype or “category”, optional
    - If `CategoricalDtype` , cannot be used together with
categories or ordered.
    - **validate** bool, default True
    - If True, validate that the codes are valid for the dtype. If False, don’t validate that the codes are valid. Be careful about skipping validation, as invalid codes can lead to severe problems, such as segfaults. Added in version 2.1.0.
  - Returns:
    - Categorical
 Examples >>> dtype = pd.CategoricalDtype(['a', 'b'], ordered=True) >>> pd.Categorical.from_codes(codes=[0, 1, 0, 1], dtype=dtype) ['a', 'b', 'a', 'b'] Categories (2, object): ['a' < 'b']