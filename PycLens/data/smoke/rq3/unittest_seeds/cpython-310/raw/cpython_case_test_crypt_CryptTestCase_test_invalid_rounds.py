# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_crypt.py
# case: CryptTestCase_test_invalid_rounds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for method in (crypt.METHOD_SHA256, crypt.METHOD_SHA512, crypt.METHOD_BLOWFISH):
        with self.assertRaises(TypeError):
            crypt.mksalt(method, rounds='4096')
        with self.assertRaises(TypeError):
            crypt.mksalt(method, rounds=4096.0)
        for rounds in (0, 1, -1, 1 << 999):
            with self.assertRaises(ValueError):
                crypt.mksalt(method, rounds=rounds)
    with self.assertRaises(ValueError):
        crypt.mksalt(crypt.METHOD_BLOWFISH, rounds=1000)
    for method in (crypt.METHOD_CRYPT, crypt.METHOD_MD5):
        with self.assertRaisesRegex(ValueError, 'support'):
            crypt.mksalt(method, rounds=4096)
