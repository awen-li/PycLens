# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_create_default_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.create_default_context()
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    self.assertTrue(ctx.check_hostname)
    self._assert_context_options(ctx)
    with open(SIGNING_CA) as f:
        cadata = f.read()
    ctx = ssl.create_default_context(cafile=SIGNING_CA, capath=CAPATH, cadata=cadata)
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    self._assert_context_options(ctx)
    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLS_SERVER)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    self._assert_context_options(ctx)
