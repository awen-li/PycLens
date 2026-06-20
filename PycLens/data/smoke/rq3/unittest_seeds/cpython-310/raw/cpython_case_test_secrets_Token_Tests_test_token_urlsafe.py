# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Token_Tests_test_token_urlsafe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    legal = string.ascii_letters + string.digits + '-_'
    for n in (1, 11, 28, 76):
        with self.subTest(n=n):
            s = secrets.token_urlsafe(n)
            self.assertIsInstance(s, str)
            self.assertTrue(all((c in legal for c in s)))
