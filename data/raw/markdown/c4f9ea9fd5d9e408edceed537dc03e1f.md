# pandas.io.formats.style.Styler.set_sticky#

- 
Styler.set_sticky(*axis=0* ,*pixel_size=None* ,*levels=None* )[source]#
- Add CSS to permanently display the index or column headers in a scrolling frame. This method applies CSS `position: sticky` rules so that the index
or column headers remain visible while scrolling through large tables.
It supports both regular and MultiIndex axes, with configurable pixel
sizes for header cell dimensions.
  - Parameters:
    - **axis** {0 or ‘index’, 1 or ‘columns’}, default 0
    - Whether to make the index or column headers sticky.
    - **pixel_size** int, optional
    - Required to configure the width of index cells or the height of column header cells when sticking a MultiIndex (or with a named Index). Defaults to 75 and 25 respectively.
    - **levels** int, str, list, optional
    - If `axis` is a MultiIndex the specific levels to stick. If`None` will
stick all levels.
  - Returns:
    - Styler
      - Instance of class with CSS set for permanently displaying headers
      - in scrolling frame.
 See also 
  - `Styler.set_properties`
  - Set defined CSS-properties to each `<td>` HTML element for the given subset.
 Notes This method uses the CSS ‘position: sticky;’ property to display. It is designed to work with visible axes, therefore both: 
  - styler.set_sticky(axis=”index”).hide(axis=”index”)
  - styler.set_sticky(axis=”columns”).hide(axis=”columns”)
 may produce strange behaviour due to CSS controls with missing elements. Examples >>> df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}) >>> df.style.set_sticky(axis="index") Please see: Table Visualization for more examples.