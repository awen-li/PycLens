# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_context_client_server

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertTrue(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    self.assertFalse(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
