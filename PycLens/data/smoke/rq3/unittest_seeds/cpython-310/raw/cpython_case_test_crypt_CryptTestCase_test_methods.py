# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(len(crypt.methods) >= 1)
    if sys.platform.startswith('openbsd'):
        self.assertEqual(crypt.methods, [crypt.METHOD_BLOWFISH])
    else:
        self.assertEqual(crypt.methods[-1], crypt.METHOD_CRYPT)
