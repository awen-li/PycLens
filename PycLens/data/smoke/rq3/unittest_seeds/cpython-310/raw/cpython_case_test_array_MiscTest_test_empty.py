# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: MiscTest_test_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('B')
    a[:] = a
    self.assertEqual(len(a), 0)
    self.assertEqual(len(a + a), 0)
    self.assertEqual(len(a * 3), 0)
    a += a
    self.assertEqual(len(a), 0)
