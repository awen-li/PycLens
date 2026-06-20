# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Token_Tests_test_token_hex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in (1, 12, 25, 90):
        with self.subTest(n=n):
            s = secrets.token_hex(n)
            self.assertIsInstance(s, str)
            self.assertEqual(len(s), 2 * n)
            self.assertTrue(all((c in string.hexdigits for c in s)))
