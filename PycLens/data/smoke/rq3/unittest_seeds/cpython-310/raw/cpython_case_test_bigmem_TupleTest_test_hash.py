# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: TupleTest_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t1 = (0,) * size
    h1 = hash(t1)
    del t1
    t2 = (0,) * (size + 1)
    self.assertFalse(h1 == hash(t2))
