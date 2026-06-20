# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_deepcopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = slice(1, 10)
    c = copy.deepcopy(s)
    self.assertEqual(s, c)
    s = slice(1, 10, 2)
    c = copy.deepcopy(s)
    self.assertEqual(s, c)
    s = slice([1, 2], [3, 4], [5, 6])
    c = copy.deepcopy(s)
    self.assertIsNot(s, c)
    self.assertEqual(s, c)
    self.assertIsNot(s.start, c.start)
    self.assertIsNot(s.stop, c.stop)
    self.assertIsNot(s.step, c.step)
