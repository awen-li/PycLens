# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: RegressionTests_test_long_chain_of_empty_iterables

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = chain.from_iterable((() for unused in range(10000000)))
    with self.assertRaises(StopIteration):
        next(it)
