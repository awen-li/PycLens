# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_blowfish_rounds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for log_rounds in range(4, 11):
        salt = crypt.mksalt(crypt.METHOD_BLOWFISH, rounds=1 << log_rounds)
        self.assertIn('$%02d$' % log_rounds, salt)
        self.assertIn(len(salt) - crypt.METHOD_BLOWFISH.salt_chars, {6, 7})
        cr = crypt.crypt('mypassword', salt)
        self.assertTrue(cr)
        cr2 = crypt.crypt('mypassword', cr)
        self.assertEqual(cr2, cr)
