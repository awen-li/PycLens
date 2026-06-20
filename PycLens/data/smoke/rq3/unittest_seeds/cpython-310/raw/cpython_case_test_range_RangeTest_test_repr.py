# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(range(1)), 'range(0, 1)')
    self.assertEqual(repr(range(1, 2)), 'range(1, 2)')
    self.assertEqual(repr(range(1, 2, 3)), 'range(1, 2, 3)')
