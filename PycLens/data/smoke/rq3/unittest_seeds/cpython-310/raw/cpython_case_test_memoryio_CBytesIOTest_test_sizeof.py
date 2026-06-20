# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: CBytesIOTest_test_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    basesize = support.calcobjsize('P2n2Pn')
    check = self.check_sizeof
    self.assertEqual(object.__sizeof__(io.BytesIO()), basesize)
    check(io.BytesIO(), basesize)
    n = 1000
    check(io.BytesIO(b'a' * n), basesize + sys.getsizeof(b'a' * n))
