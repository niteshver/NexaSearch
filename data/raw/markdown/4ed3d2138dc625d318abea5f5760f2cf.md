# User Guide#

The User Guide covers all of pandas by topic area. Each of the subsections introduces a topic (such as “working with missing data”), and discusses how pandas approaches the problem, with many examples throughout.

Users brand-new to pandas should start with 10 minutes to pandas.

For a high level summary of the pandas fundamentals, see Intro to data structures and Essential basic functionality.

Further information on any specific method can be obtained in the API reference.

## How to read these guides#

In these guides you will see input code inside code blocks such as:

```
import pandas as pd
pd.DataFrame({'A': [1, 2, 3]})
```
or:

```
In [1]: import pandas as pd
In [2]: pd.DataFrame({'A': [1, 2, 3]})
Out[2]: 
   A
0  1
1  2
2  3
```
The first block is a standard python input, while in the second the `In [1]:` indicates the input is inside a notebook. In Jupyter Notebooks the last line is printed and plots are shown inline.

For example:

```
In [3]: a = 1
In [4]: a
Out[4]: 1
```
is equivalent to:

```
a = 1
print(a)
```