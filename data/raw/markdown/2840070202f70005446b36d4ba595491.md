# Getting started#

## Installation#

## Intro to pandas#

When working with tabular data, such as data stored in spreadsheets or databases, pandas is the right tool for you. pandas will help you
to explore, clean, and process your data. In pandas, a data table is called a `DataFrame`.

pandas supports the integration with many file formats or data sources out of the box (csv, excel, sql, json, parquet,…). Importing data from each of these
data sources is provided by function with the prefix `read_*`. Similarly, the `to_*` methods are used to store data.

Selecting or filtering specific rows and/or columns? Filtering the data on a condition? Methods for slicing, selecting, and extracting the data you need are available in pandas.

pandas provides plotting your data out of the box, using the power of Matplotlib. You can pick the plot type (scatter, bar, boxplot,…) corresponding to your data.

There is no need to loop over all rows of your data table to do calculations. Data manipulations on a column work elementwise.
Adding a column to a `DataFrame` based on existing data in other columns is straightforward.

Basic statistics (mean, median, min, max, counts…) are easily calculable. These or custom aggregations can be applied on the entire data set, a sliding window of the data, or grouped by categories. The latter is also known as the split-apply-combine approach.

Multiple tables can be concatenated both column wise and row wise as database-like join/merge operations are provided to combine multiple tables of data.

pandas has great support for time series and has an extensive set of tools for working with dates, times, and time-indexed data.

Data sets do not only contain numerical data. pandas provides a wide range of functions to clean textual data and extract useful information from it.

## Coming from…#

Are you familiar with other software for manipulating tabular data? Learn the pandas-equivalent operations compared to software you already know:

The R programming language provides the
`data.frame` data structure and multiple packages, such as
tidyverse use and extend `data.frame`
for convenient data handling functionalities similar to pandas.

Already familiar to `SELECT`, `GROUP BY`, `JOIN`, etc.?
Most of these SQL manipulations do have equivalents in pandas.

The `data set` included in the STATA
statistical software suite corresponds to the pandas `DataFrame`.
Many of the operations known from STATA have an equivalent in pandas.

Users of Excel or other spreadsheet programs will find that many of the concepts are transferrable to pandas.

The SAS statistical software suite
also provides the `data set` corresponding to the pandas `DataFrame`.
Also SAS vectorized operations, filtering, string processing operations,
and more have similar functions in pandas.

## Tutorials#

For a quick overview of pandas functionality, see 10 Minutes to pandas.

You can also reference the pandas cheat sheet for a succinct guide for manipulating data with pandas.

The community produces a wide variety of tutorials available online. Some of the material is enlisted in the community contributed Community tutorials.