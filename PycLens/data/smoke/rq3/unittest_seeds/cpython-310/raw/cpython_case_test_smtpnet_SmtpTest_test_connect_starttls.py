# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpnet.py
# case: SmtpTest_test_connect_starttls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.get_attribute(smtplib, 'SMTP_SSL')
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with socket_helper.transient_internet(self.testServer):
        server = smtplib.SMTP(self.testServer, self.remotePort)
        try:
            server.starttls(context=context)
        except smtplib.SMTPException as e:
            if e.args[0] == 'STARTTLS extension not supported by server.':
                unittest.skip(e.args[0])
            else:
                raise
        server.ehlo()
        server.quit()
