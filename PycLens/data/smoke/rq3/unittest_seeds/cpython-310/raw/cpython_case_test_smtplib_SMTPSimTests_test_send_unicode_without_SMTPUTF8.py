# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_send_unicode_without_SMTPUTF8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    self.assertRaises(UnicodeEncodeError, smtp.sendmail, 'Alice', 'Böb', '')
    self.assertRaises(UnicodeEncodeError, smtp.mail, 'Älice')
