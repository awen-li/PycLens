# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_set_ecdh_curve

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.set_ecdh_curve('prime256v1')
    ctx.set_ecdh_curve(b'prime256v1')
    self.assertRaises(TypeError, ctx.set_ecdh_curve)
    self.assertRaises(TypeError, ctx.set_ecdh_curve, None)
    self.assertRaises(ValueError, ctx.set_ecdh_curve, 'foo')
    self.assertRaises(ValueError, ctx.set_ecdh_curve, b'foo')
