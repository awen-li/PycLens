# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_salt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(len(crypt._saltchars), 64)
    for method in crypt.methods:
        salt = crypt.mksalt(method)
        self.assertIn(len(salt) - method.salt_chars, {0, 1, 3, 4, 6, 7})
        if method.ident:
            self.assertIn(method.ident, salt[:len(salt) - method.salt_chars])
