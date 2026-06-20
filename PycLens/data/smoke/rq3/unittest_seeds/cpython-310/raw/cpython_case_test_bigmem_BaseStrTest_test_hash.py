# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    s = _('\x00') * size
    h1 = hash(s)
    del s
    s = _('\x00') * (size + 1)
    self.assertNotEqual(h1, hash(s))
