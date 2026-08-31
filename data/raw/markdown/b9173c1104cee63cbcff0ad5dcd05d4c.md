# pandas.Index.is_#

- 
*final* Index.is_(*other* )[source]#
- More flexible, faster check like `is` but that works through views.Note: this is *not* the same as`Index.identical()` , which checks
that metadata is also the same.
  - Parameters:
    - **other** object
    - Other object to compare against.
  - Returns:
    - bool
    - True if both have same underlying data, False otherwise.
 See also 
  - `Index.identical`
  - Works like `Index.is_` but also checks metadata.
 Examples >>> idx1 = pd.Index(['1', '2', '3']) >>> idx1.is_(idx1.view()) True >>> idx1.is_(idx1.copy()) False