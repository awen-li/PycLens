# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: ConstructorTestCase_test_with_sha256_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = hmac.HMAC(b'key', b'hash this!', digestmod=sha256_module.sha256)
    self.assertEqual(h.hexdigest(), self.expected)
    self.assertEqual(h.name, 'hmac-sha256')
    digest = hmac.digest(b'key', b'hash this!', sha256_module.sha256)
    self.assertEqual(digest, binascii.unhexlify(self.expected))
