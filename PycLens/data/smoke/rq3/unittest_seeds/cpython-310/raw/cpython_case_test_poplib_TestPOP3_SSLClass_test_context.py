# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3_SSLClass_test_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    self.assertRaises(ValueError, poplib.POP3_SSL, self.server.host, self.server.port, keyfile=CERTFILE, context=ctx)
    self.assertRaises(ValueError, poplib.POP3_SSL, self.server.host, self.server.port, certfile=CERTFILE, context=ctx)
    self.assertRaises(ValueError, poplib.POP3_SSL, self.server.host, self.server.port, keyfile=CERTFILE, certfile=CERTFILE, context=ctx)
    self.client.quit()
    self.client = poplib.POP3_SSL(self.server.host, self.server.port, context=ctx)
    self.assertIsInstance(self.client.sock, ssl.SSLSocket)
    self.assertIs(self.client.sock.context, ctx)
    self.assertTrue(self.client.noop().startswith(b'+OK'))
