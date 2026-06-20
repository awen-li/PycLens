# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(range(3).count(-1), 0)
    self.assertEqual(range(3).count(0), 1)
    self.assertEqual(range(3).count(1), 1)
    self.assertEqual(range(3).count(2), 1)
    self.assertEqual(range(3).count(3), 0)
    self.assertIs(type(range(3).count(-1)), int)
    self.assertIs(type(range(3).count(1)), int)
    self.assertEqual(range(10 ** 20).count(1), 1)
    self.assertEqual(range(10 ** 20).count(10 ** 20), 0)
    self.assertEqual(range(3).index(1), 1)
    self.assertEqual(range(1, 2 ** 100, 2).count(2 ** 87), 0)
    self.assertEqual(range(1, 2 ** 100, 2).count(2 ** 87 + 1), 1)
    self.assertEqual(range(10).count(ALWAYS_EQ), 10)
    self.assertEqual(len(range(sys.maxsize, sys.maxsize + 10)), 10)
