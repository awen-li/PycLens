# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_load_default_certs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_default_certs()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_default_certs(ssl.Purpose.SERVER_AUTH)
    ctx.load_default_certs()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_default_certs(ssl.Purpose.CLIENT_AUTH)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertRaises(TypeError, ctx.load_default_certs, None)
    self.assertRaises(TypeError, ctx.load_default_certs, 'SERVER_AUTH')
