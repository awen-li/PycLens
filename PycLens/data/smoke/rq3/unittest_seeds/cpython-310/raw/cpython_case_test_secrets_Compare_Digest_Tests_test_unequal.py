# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Compare_Digest_Tests_test_unequal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(secrets.compare_digest('abc', 'abcd'))
    self.assertFalse(secrets.compare_digest(b'abc', b'abcd'))
    for s in ('x', 'mn', 'a1b2c3'):
        a = s * 100 + 'q'
        b = s * 100 + 'k'
        self.assertFalse(secrets.compare_digest(a, b))
        self.assertFalse(secrets.compare_digest(a.encode('utf-8'), b.encode('utf-8')))
