# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_key_with_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(-2, 2))
    dup = data[:]
    self.assertRaises(ZeroDivisionError, data.sort, key=lambda x: 1 / x)
    self.assertEqual(data, dup)
