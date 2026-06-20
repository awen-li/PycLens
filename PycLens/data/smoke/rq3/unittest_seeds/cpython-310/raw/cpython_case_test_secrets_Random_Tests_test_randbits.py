# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Random_Tests_test_randbits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    errmsg = 'randbits(%d) returned %d'
    for numbits in (3, 12, 30):
        for i in range(6):
            n = secrets.randbits(numbits)
            self.assertTrue(0 <= n < 2 ** numbits, errmsg % (numbits, n))
