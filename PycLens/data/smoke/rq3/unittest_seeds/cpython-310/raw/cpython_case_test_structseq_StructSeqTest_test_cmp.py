# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_structseq.py
# case: StructSeqTest_test_cmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = time.gmtime()
    t2 = type(t1)(t1)
    self.assertEqual(t1, t2)
    self.assertTrue(not t1 < t2)
    self.assertTrue(t1 <= t2)
    self.assertTrue(not t1 > t2)
    self.assertTrue(t1 >= t2)
    self.assertTrue(not t1 != t2)
