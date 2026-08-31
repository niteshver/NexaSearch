# `sklearn.preprocessing`.PolynomialFeatures¶

- 
*class* `sklearn.preprocessing.``PolynomialFeatures` (*degree=2* ,*interaction_only=False* ,*include_bias=True* )[source]¶
- Generate polynomial and interaction features. Generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree. For example, if an input sample is two dimensional and of the form [a, b], the degree-2 polynomial features are [1, a, b, a^2, ab, b^2]. Parameters: **degree** : integerThe degree of the polynomial features. Default = 2. **interaction_only** : boolean, default = FalseIf true, only interaction features are produced: features that are products of at most `degree`*distinct* input features (so not`x[1] ** 2` ,`x[0] * x[2] ** 3` , etc.).**include_bias** : booleanIf True (default), then include a bias column, the feature in which all polynomial powers are zero (i.e. a column of ones - acts as an intercept term in a linear model). Attributes: **powers_** : array, shape (n_input_features, n_output_features)powers_[i, j] is the exponent of the jth input in the ith output. **n_input_features_** : intThe total number of input features. **n_output_features_** : intThe total number of polynomial output features. The number of output features is computed by iterating over all suitably sized combinations of input features. Notes Be aware that the number of features in the output array scales polynomially in the number of features of the input array, and exponentially in the degree. High degrees can cause overfitting. See *examples/linear_model/plot_polynomial_interpolation.py*Examples >>> X = np.arange(6).reshape(3, 2) >>> X array([[0, 1], [2, 3], [4, 5]]) >>> poly = PolynomialFeatures(2) >>> poly.fit_transform(X) array([[ 1, 0, 1, 0, 0, 1], [ 1, 2, 3, 4, 6, 9], [ 1, 4, 5, 16, 20, 25]]) >>> poly = PolynomialFeatures(interaction_only=True) >>> poly.fit_transform(X) array([[ 1, 0, 1, 0], [ 1, 2, 3, 6], [ 1, 4, 5, 20]]) Methods `fit` (X[, y])Compute number of output features. `fit_transform` (X[, y])Fit to data, then transform it. `get_params` ([deep])Get parameters for this estimator. `set_params` (**params)Set the parameters of this estimator. `transform` (X[, y])Transform data to polynomial features 
  - 
`fit_transform` (*X* ,*y=None* ,***fit_params* )[source]¶
  - Fit to data, then transform it. Fits transformer to X and y with optional parameters fit_params and returns a transformed version of X. Parameters: **X** : numpy array of shape [n_samples, n_features]Training set. **y** : numpy array of shape [n_samples]Target values. Returns: **X_new** : numpy array of shape [n_samples, n_features_new]Transformed array.
 
  - 
`get_params` (*deep=True* )[source]¶
  - Get parameters for this estimator. Parameters: **deep: boolean, optional** :If True, will return the parameters for this estimator and contained subobjects that are estimators. Returns: **params** : mapping of string to anyParameter names mapped to their values.
 
  - 
`set_params` (***params* )[source]¶
  - Set the parameters of this estimator. The method works on simple estimators as well as on nested objects (such as pipelines). The former have parameters of the form `<component>__<parameter>` so that it’s possible to update each
component of a nested object.Returns: **self** :
 
  - 
`transform` (*X* ,*y=None* )[source]¶
  - Transform data to polynomial features Parameters: **X** : array with shape [n_samples, n_features]The data to transform, row by row. Returns: **XP** : np.ndarray shape [n_samples, NP]The matrix of features, where NP is the number of polynomial features generated from the combination of inputs.
-