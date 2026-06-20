# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_sni_callback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    self.assertRaises(TypeError, ctx.set_servername_callback)
    self.assertRaises(TypeError, ctx.set_servername_callback, 4)
    self.assertRaises(TypeError, ctx.set_servername_callback, '')
    self.assertRaises(TypeError, ctx.set_servername_callback, ctx)

    def dummycallback(sock, servername, ctx):
        pass
    ctx.set_servername_callback(None)
    ctx.set_servername_callback(dummycallback)
