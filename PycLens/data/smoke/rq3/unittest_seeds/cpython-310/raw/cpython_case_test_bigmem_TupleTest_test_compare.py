# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: TupleTest_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = ('',) * size
    t2 = ('',) * size
    self.assertTrue(t1 == t2)
    del t2
    t2 = ('',) * (size + 1)
    self.assertFalse(t1 == t2)
    del t2
    t2 = (1,) * size
    self.assertFalse(t1 == t2)
