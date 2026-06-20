# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestTLS_FTPClass_test_check_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.quit()
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    self.assertEqual(ctx.check_hostname, True)
    ctx.load_verify_locations(CAFILE)
    self.client = ftplib.FTP_TLS(context=ctx, timeout=TIMEOUT)
    self.client.connect(self.server.host, self.server.port)
    with self.assertRaises(ssl.CertificateError):
        self.client.auth()
    self.client.connect(self.server.host, self.server.port)
    self.client.prot_p()
    with self.assertRaises(ssl.CertificateError):
        with self.client.transfercmd('list') as sock:
            pass
    self.client.quit()
    self.client.connect('localhost', self.server.port)
    self.client.auth()
    self.client.quit()
    self.client.connect('localhost', self.server.port)
    self.client.prot_p()
    with self.client.transfercmd('list') as sock:
        pass
