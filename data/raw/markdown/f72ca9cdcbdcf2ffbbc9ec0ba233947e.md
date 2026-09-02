# `sklearn.utils`.check_random_state¶

- 
`sklearn.utils.``check_random_state` (*seed* )[source]¶
- Turn seed into a np.random.RandomState instance If seed is None, return the RandomState singleton used by np.random. If seed is an int, return a new RandomState instance seeded with seed. If seed is already a RandomState instance, return it. Otherwise raise ValueError.