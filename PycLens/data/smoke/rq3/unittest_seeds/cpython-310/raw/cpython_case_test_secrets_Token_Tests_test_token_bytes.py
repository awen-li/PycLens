# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Token_Tests_test_token_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in (1, 8, 17, 100):
        with self.subTest(n=n):
            self.assertIsInstance(secrets.token_bytes(n), bytes)
            self.assertEqual(len(secrets.token_bytes(n)), n)
