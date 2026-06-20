# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestTLS_FTPClass_test_context

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.quit()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    self.assertRaises(ValueError, ftplib.FTP_TLS, keyfile=CERTFILE, context=ctx)
    self.assertRaises(ValueError, ftplib.FTP_TLS, certfile=CERTFILE, context=ctx)
    self.assertRaises(ValueError, ftplib.FTP_TLS, certfile=CERTFILE, keyfile=CERTFILE, context=ctx)
    self.client = ftplib.FTP_TLS(context=ctx, timeout=TIMEOUT)
    self.client.connect(self.server.host, self.server.port)
    self.assertNotIsInstance(self.client.sock, ssl.SSLSocket)
    self.client.auth()
    self.assertIs(self.client.sock.context, ctx)
    self.assertIsInstance(self.client.sock, ssl.SSLSocket)
    self.client.prot_p()
    with self.client.transfercmd('list') as sock:
        self.assertIs(sock.context, ctx)
        self.assertIsInstance(sock, ssl.SSLSocket)
