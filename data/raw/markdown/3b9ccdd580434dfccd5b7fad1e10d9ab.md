# pandas.TimedeltaIndex.to_pytimedelta#

- 
TimedeltaIndex.to_pytimedelta(**args* ,***kwargs* )[source]#
- Return an ndarray of datetime.timedelta objects. 
  - Returns:
    - numpy.ndarray
 Examples >>> tdelta_idx = pd.to_timedelta([1, 2, 3], unit='D') >>> tdelta_idx TimedeltaIndex(['1 days', '2 days', '3 days'], dtype='timedelta64[ns]', freq=None) >>> tdelta_idx.to_pytimedelta() array([datetime.timedelta(days=1), datetime.timedelta(days=2), datetime.timedelta(days=3)], dtype=object)