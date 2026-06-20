# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Compare_Digest_Tests_test_bad_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 'abcde'
    b = a.encode('utf-8')
    assert isinstance(a, str)
    assert isinstance(b, bytes)
    self.assertRaises(TypeError, secrets.compare_digest, a, b)
    self.assertRaises(TypeError, secrets.compare_digest, b, a)
