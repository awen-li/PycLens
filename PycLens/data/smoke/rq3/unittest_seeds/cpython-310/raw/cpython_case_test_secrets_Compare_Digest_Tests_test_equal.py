# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Compare_Digest_Tests_test_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('a', 'bcd', 'xyz123'):
        a = s * 100
        b = s * 100
        self.assertTrue(secrets.compare_digest(a, b))
        self.assertTrue(secrets.compare_digest(a.encode('utf-8'), b.encode('utf-8')))
