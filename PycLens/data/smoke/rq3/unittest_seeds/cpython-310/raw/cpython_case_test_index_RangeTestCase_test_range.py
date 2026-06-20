# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: RangeTestCase_test_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = newstyle()
    n.ind = 5
    self.assertEqual(range(1, 20)[n], 6)
    self.assertEqual(range(1, 20).__getitem__(n), 6)
