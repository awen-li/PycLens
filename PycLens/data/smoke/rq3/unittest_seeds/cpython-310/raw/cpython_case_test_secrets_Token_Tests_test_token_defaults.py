# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_secrets.py
# case: Token_Tests_test_token_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for func in (secrets.token_bytes, secrets.token_hex, secrets.token_urlsafe):
        with self.subTest(func=func):
            name = func.__name__
            try:
                func()
            except TypeError:
                self.fail('%s cannot be called with no argument' % name)
            try:
                func(None)
            except TypeError:
                self.fail('%s cannot be called with None' % name)
    size = secrets.DEFAULT_ENTROPY
    self.assertEqual(len(secrets.token_bytes(None)), size)
    self.assertEqual(len(secrets.token_hex(None)), 2 * size)
