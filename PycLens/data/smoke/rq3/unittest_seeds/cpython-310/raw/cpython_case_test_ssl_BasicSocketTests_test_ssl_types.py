# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_ssl_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ssl_types = [_ssl._SSLContext, _ssl._SSLSocket, _ssl.MemoryBIO, _ssl.Certificate, _ssl.SSLSession, _ssl.SSLError]
    for ssl_type in ssl_types:
        with self.subTest(ssl_type=ssl_type):
            with self.assertRaisesRegex(TypeError, 'immutable type'):
                ssl_type.value = None
    support.check_disallow_instantiation(self, _ssl.Certificate)
