# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: CopyTestCase_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h1 = hmac.HMAC(b'key', digestmod='sha256')
    h1.update(b'some random text')
    h2 = h1.copy()
    self.assertEqual(h1.digest(), h2.digest(), "Digest of copy doesn't match original digest.")
    self.assertEqual(h1.hexdigest(), h2.hexdigest(), "Hexdigest of copy doesn't match original hexdigest.")
