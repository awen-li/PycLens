# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_python_ciphers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ciphers = ctx.get_ciphers()
    for suite in ciphers:
        name = suite['name']
        self.assertNotIn('PSK', name)
        self.assertNotIn('SRP', name)
        self.assertNotIn('MD5', name)
        self.assertNotIn('RC4', name)
        self.assertNotIn('3DES', name)
