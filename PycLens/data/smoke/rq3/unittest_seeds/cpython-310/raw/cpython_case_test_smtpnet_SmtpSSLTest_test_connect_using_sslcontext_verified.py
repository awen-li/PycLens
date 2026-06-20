# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpnet.py
# case: SmtpSSLTest_test_connect_using_sslcontext_verified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket_helper.transient_internet(self.testServer):
        can_verify = check_ssl_verifiy(self.testServer, self.remotePort)
        if not can_verify:
            self.skipTest("SSL certificate can't be verified")
    support.get_attribute(smtplib, 'SMTP_SSL')
    context = ssl.create_default_context()
    with socket_helper.transient_internet(self.testServer):
        server = smtplib.SMTP_SSL(self.testServer, self.remotePort, context=context)
        server.ehlo()
        server.quit()
