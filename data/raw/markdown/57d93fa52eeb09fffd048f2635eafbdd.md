# pandas.errors.CSSWarning#

- exception pandas.errors.CSSWarning[source]#
- Warning is raised when converting css styling fails. This can be due to the styling not having an equivalent value or because the styling isn’t properly formatted. See also 
  - `DataFrame.style`
  - Returns a Styler object for applying CSS-like styles.
  - `io.formats.style.Styler`
  - Helps style a DataFrame or Series according to the data with HTML and CSS.
  - `io.formats.style.Styler.to_excel`
  - Export styled DataFrame to Excel.
  - `io.formats.style.Styler.to_html`
  - Export styled DataFrame to HTML.
 Examples >>> df = pd.DataFrame({"A": [1, 1, 1]}) >>> df.style.map(lambda x: "background-color: blueGreenRed;").to_excel( ... "styled.xlsx" ... ) CSSWarning: Unhandled color format: 'blueGreenRed' >>> df.style.map(lambda x: "border: 1px solid red red;").to_excel( ... "styled.xlsx" ... ) CSSWarning: Unhandled color format: 'blueGreenRed'