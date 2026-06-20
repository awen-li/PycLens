# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: TestVectorsTestCase_test_legacy_block_size_warnings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MockCrazyHash(object):
        """Ain't no block_size attribute here."""

        def __init__(self, *args):
            self._x = hashlib.sha256(*args)
            self.digest_size = self._x.digest_size

        def update(self, v):
            self._x.update(v)

        def digest(self):
            return self._x.digest()
    with warnings.catch_warnings():
        warnings.simplefilter('error', RuntimeWarning)
        with self.assertRaises(RuntimeWarning):
            hmac.HMAC(b'a', b'b', digestmod=MockCrazyHash)
            self.fail('Expected warning about missing block_size')
        MockCrazyHash.block_size = 1
        with self.assertRaises(RuntimeWarning):
            hmac.HMAC(b'a', b'b', digestmod=MockCrazyHash)
            self.fail('Expected warning about small block_size')
