# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_preallocation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iterable = [0] * 10
    iter_size = sys.getsizeof(iterable)
    self.assertEqual(iter_size, sys.getsizeof(list([0] * 10)))
    self.assertEqual(iter_size, sys.getsizeof(list(range(10))))
