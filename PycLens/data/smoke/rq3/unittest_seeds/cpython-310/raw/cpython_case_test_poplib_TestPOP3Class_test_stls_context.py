# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3Class_test_stls_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = b'+OK Begin TLS negotiation'
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.load_verify_locations(CAFILE)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    self.assertEqual(ctx.check_hostname, True)
    with self.assertRaises(ssl.CertificateError):
        resp = self.client.stls(context=ctx)
    self.client = poplib.POP3('localhost', self.server.port, timeout=test_support.LOOPBACK_TIMEOUT)
    resp = self.client.stls(context=ctx)
    self.assertEqual(resp, expected)
