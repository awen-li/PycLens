# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_verify_mode_protocol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings():
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    ctx.verify_mode = ssl.CERT_OPTIONAL
    self.assertEqual(ctx.verify_mode, ssl.CERT_OPTIONAL)
    ctx.verify_mode = ssl.CERT_REQUIRED
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    ctx.verify_mode = ssl.CERT_NONE
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    with self.assertRaises(TypeError):
        ctx.verify_mode = None
    with self.assertRaises(ValueError):
        ctx.verify_mode = 42
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    self.assertFalse(ctx.check_hostname)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    self.assertTrue(ctx.check_hostname)
