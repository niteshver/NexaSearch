# pandas.io.formats.style.Styler.pipe#

- 
Styler.pipe(*func* ,**args* ,***kwargs* )[source]#
- Apply `func(self, *args, **kwargs)` , and return the result.This is useful for chaining multiple user-defined styling operations in a readable manner, rather than nesting function calls. 
  - Parameters:
    - **func** function
    - Function to apply to the Styler. Alternatively, a `(callable, keyword)` tuple where`keyword` is a string
indicating the keyword of`callable` that expects the Styler.
    - ***args** optional
    - Arguments passed to func.
    - ****kwargs** optional
    - A dictionary of keyword arguments passed into `func` .
  - Returns:
    - object
    - The value returned by `func` .
 See also 
  - `DataFrame.pipe`
  - Analogous method for DataFrame.
  - `Styler.apply`
  - Apply a CSS-styling function column-wise, row-wise, or table-wise.
 Notes Like `DataFrame.pipe()` , this method can simplify the
application of several user-defined functions to a styler.  Instead
of writing:f(g(df.style.format(precision=3), arg1=a), arg2=b, arg3=c) users can write: (df.style.format(precision=3).pipe(g, arg1=a).pipe(f, arg2=b, arg3=c)) In particular, this allows users to define functions that take a styler object, along with other parameters, and return the styler after making styling changes (such as calling `Styler.apply()` or`Styler.set_properties()` ).Examples **Common Use**A common usage pattern is to pre-define styling operations which can be easily applied to a generic styler in a single `pipe` call.>>> def some_highlights(styler, min_color="red", max_color="blue"): ... styler.highlight_min(color=min_color, axis=None) ... styler.highlight_max(color=max_color, axis=None) ... styler.highlight_null() ... return styler >>> df = pd.DataFrame([[1, 2, 3, pd.NA], [pd.NA, 4, 5, 6]], dtype="Int64") >>> df.style.pipe(some_highlights, min_color="green") Since the method returns a `Styler` object it can be chained with other
methods as if applying the underlying highlighters directly.>>> ( ... df.style.format("{:.1f}") ... .pipe(some_highlights, min_color="green") ... .highlight_between(left=2, right=5) ... ) **Advanced Use**Sometimes it may be necessary to pre-define styling functions, but in the case where those functions rely on the styler, data or context. Since `Styler.use` and`Styler.export` are designed to be non-data dependent,
they cannot be used for this purpose. Additionally the`Styler.apply` and`Styler.format` type methods are not context aware, so a solution
is to use`pipe` to dynamically wrap this functionality.Suppose we want to code a generic styling function that highlights the final level of a MultiIndex. The number of levels in the Index is dynamic so we need the `Styler` context to define the level.>>> def highlight_last_level(styler): ... return styler.apply_index( ... lambda v: "background-color: pink; color: yellow", ... axis="columns", ... level=styler.columns.nlevels - 1, ... ) >>> df.columns = pd.MultiIndex.from_product([["A", "B"], ["X", "Y"]]) >>> df.style.pipe(highlight_last_level) Additionally suppose we want to highlight a column header if there is any missing data in that column. In this case we need the data object itself to determine the effect on the column headers. >>> def highlight_header_missing(styler, level): ... def dynamic_highlight(s): ... return np.where( ... styler.data.isna().any(), "background-color: red;", "" ... ) ... ... return styler.apply_index(dynamic_highlight, axis=1, level=level) >>> df.style.pipe(highlight_header_missing, level=1)