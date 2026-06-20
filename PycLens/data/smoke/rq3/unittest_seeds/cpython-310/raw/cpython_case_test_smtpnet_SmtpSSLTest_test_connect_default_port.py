# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpnet.py
# case: SmtpSSLTest_test_connect_default_port

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.get_attribute(smtplib, 'SMTP_SSL')
    with socket_helper.transient_internet(self.testServer):
        server = smtplib.SMTP_SSL(self.testServer)
        server.ehlo()
        server.quit()
