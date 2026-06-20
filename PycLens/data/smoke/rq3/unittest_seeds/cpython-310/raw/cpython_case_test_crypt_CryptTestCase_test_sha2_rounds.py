# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_sha2_rounds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for method in (crypt.METHOD_SHA256, crypt.METHOD_SHA512):
        for rounds in (1000, 10000, 100000):
            salt = crypt.mksalt(method, rounds=rounds)
            self.assertIn('$rounds=%d$' % rounds, salt)
            self.assertEqual(len(salt) - method.salt_chars, 11 + len(str(rounds)))
            cr = crypt.crypt('mypassword', salt)
            self.assertTrue(cr)
            cr2 = crypt.crypt('mypassword', cr)
            self.assertEqual(cr2, cr)
