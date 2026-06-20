# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test__create_stdlib_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl._create_stdlib_context()
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    self.assertFalse(ctx.check_hostname)
    self._assert_context_options(ctx)
    if has_tls_protocol(ssl.PROTOCOL_TLSv1):
        with warnings_helper.check_warnings():
            ctx = ssl._create_stdlib_context(ssl.PROTOCOL_TLSv1)
        self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLSv1)
        self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
        self._assert_context_options(ctx)
    with warnings_helper.check_warnings():
        ctx = ssl._create_stdlib_context(ssl.PROTOCOL_TLSv1_2, cert_reqs=ssl.CERT_REQUIRED, check_hostname=True)
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLSv1_2)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    self.assertTrue(ctx.check_hostname)
    self._assert_context_options(ctx)
    ctx = ssl._create_stdlib_context(purpose=ssl.Purpose.CLIENT_AUTH)
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLS_SERVER)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    self._assert_context_options(ctx)
