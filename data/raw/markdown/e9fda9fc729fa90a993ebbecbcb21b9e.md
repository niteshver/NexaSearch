# Window#

Rolling objects are returned by `.rolling` calls: `pandas.DataFrame.rolling()`, `pandas.Series.rolling()`, etc.
Expanding objects are returned by `.expanding` calls: `pandas.DataFrame.expanding()`, `pandas.Series.expanding()`, etc.
ExponentialMovingWindow objects are returned by `.ewm` calls: `pandas.DataFrame.ewm()`, `pandas.Series.ewm()`, etc.

## Rolling window functions#

| `Rolling.count` ([numeric_only]) | Calculate the rolling count of non NaN observations. | 
| `Rolling.sum` ([numeric_only, engine, ...]) | Calculate the rolling sum. | 
| `Rolling.mean` ([numeric_only, engine, ...]) | Calculate the rolling mean. | 
| `Rolling.median` ([numeric_only, engine, ...]) | Calculate the rolling median. | 
| `Rolling.var` ([ddof, numeric_only, engine, ...]) | Calculate the rolling variance. | 
| `Rolling.std` ([ddof, numeric_only, engine, ...]) | Calculate the rolling standard deviation. | 
| `Rolling.min` ([numeric_only, engine, ...]) | Calculate the rolling minimum. | 
| `Rolling.max` ([numeric_only, engine, ...]) | Calculate the rolling maximum. | 
| `Rolling.corr` ([other, pairwise, ddof, ...]) | Calculate the rolling correlation. | 
| `Rolling.cov` ([other, pairwise, ddof, ...]) | Calculate the rolling sample covariance. | 
| `Rolling.skew` ([numeric_only]) | Calculate the rolling unbiased skewness. | 
| `Rolling.kurt` ([numeric_only]) | Calculate the rolling Fisher's definition of kurtosis without bias. | 
| `Rolling.apply` (func[, raw, engine, ...]) | Calculate the rolling custom aggregation function. | 
| `Rolling.aggregate` (func, *args, **kwargs) | Aggregate using one or more operations over the specified axis. | 
| `Rolling.quantile` (quantile[, interpolation, ...]) | Calculate the rolling quantile. | 
| `Rolling.sem` ([ddof, numeric_only]) | Calculate the rolling standard error of mean. | 
| `Rolling.rank` ([method, ascending, pct, ...]) | Calculate the rolling rank. | 

## Weighted window functions#

| `Window.mean` ([numeric_only]) | Calculate the rolling weighted window mean. | 
| `Window.sum` ([numeric_only]) | Calculate the rolling weighted window sum. | 
| `Window.var` ([ddof, numeric_only]) | Calculate the rolling weighted window variance. | 
| `Window.std` ([ddof, numeric_only]) | Calculate the rolling weighted window standard deviation. | 

## Expanding window functions#

| `Expanding.count` ([numeric_only]) | Calculate the expanding count of non NaN observations. | 
| `Expanding.sum` ([numeric_only, engine, ...]) | Calculate the expanding sum. | 
| `Expanding.mean` ([numeric_only, engine, ...]) | Calculate the expanding mean. | 
| `Expanding.median` ([numeric_only, engine, ...]) | Calculate the expanding median. | 
| `Expanding.var` ([ddof, numeric_only, engine, ...]) | Calculate the expanding variance. | 
| `Expanding.std` ([ddof, numeric_only, engine, ...]) | Calculate the expanding standard deviation. | 
| `Expanding.min` ([numeric_only, engine, ...]) | Calculate the expanding minimum. | 
| `Expanding.max` ([numeric_only, engine, ...]) | Calculate the expanding maximum. | 
| `Expanding.corr` ([other, pairwise, ddof, ...]) | Calculate the expanding correlation. | 
| `Expanding.cov` ([other, pairwise, ddof, ...]) | Calculate the expanding sample covariance. | 
| `Expanding.skew` ([numeric_only]) | Calculate the expanding unbiased skewness. | 
| `Expanding.kurt` ([numeric_only]) | Calculate the expanding Fisher's definition of kurtosis without bias. | 
| `Expanding.apply` (func[, raw, engine, ...]) | Calculate the expanding custom aggregation function. | 
| `Expanding.aggregate` (func, *args, **kwargs) | Aggregate using one or more operations over the specified axis. | 
| `Expanding.quantile` (quantile[, ...]) | Calculate the expanding quantile. | 
| `Expanding.sem` ([ddof, numeric_only]) | Calculate the expanding standard error of mean. | 
| `Expanding.rank` ([method, ascending, pct, ...]) | Calculate the expanding rank. | 

## Exponentially-weighted window functions#

| `ExponentialMovingWindow.mean` ([numeric_only, ...]) | Calculate the ewm (exponential weighted moment) mean. | 
| `ExponentialMovingWindow.sum` ([numeric_only, ...]) | Calculate the ewm (exponential weighted moment) sum. | 
| `ExponentialMovingWindow.std` ([bias, numeric_only]) | Calculate the ewm (exponential weighted moment) standard deviation. | 
| `ExponentialMovingWindow.var` ([bias, numeric_only]) | Calculate the ewm (exponential weighted moment) variance. | 
| `ExponentialMovingWindow.corr` ([other, ...]) | Calculate the ewm (exponential weighted moment) sample correlation. | 
| `ExponentialMovingWindow.cov` ([other, ...]) | Calculate the ewm (exponential weighted moment) sample covariance. | 

## Window indexer#

Base class for defining custom window boundaries.

| `api.indexers.BaseIndexer` ([index_array, ...]) | Base class for window bounds calculations. | 
| `api.indexers.FixedForwardWindowIndexer` ([...]) | Creates window boundaries for fixed-length windows that include the current row. | 
| `api.indexers.VariableOffsetWindowIndexer` ([...]) | Calculate window boundaries based on a non-fixed offset such as a BusinessDay. |