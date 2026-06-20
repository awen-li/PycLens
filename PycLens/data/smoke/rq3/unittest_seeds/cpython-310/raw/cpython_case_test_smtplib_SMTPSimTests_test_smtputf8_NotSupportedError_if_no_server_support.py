# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_smtputf8_NotSupportedError_if_no_server_support

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    smtp.ehlo()
    self.assertTrue(smtp.does_esmtp)
    self.assertFalse(smtp.has_extn('smtputf8'))
    self.assertRaises(smtplib.SMTPNotSupportedError, smtp.sendmail, 'John', 'Sally', '', mail_options=['BODY=8BITMIME', 'SMTPUTF8'])
    self.assertRaises(smtplib.SMTPNotSupportedError, smtp.mail, 'John', options=['BODY=8BITMIME', 'SMTPUTF8'])
