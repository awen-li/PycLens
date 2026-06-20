# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_421_from_mail_cmd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    smtp.noop()
    self.serv._SMTPchannel.mail_response = '421 closing connection'
    with self.assertRaises(smtplib.SMTPSenderRefused):
        smtp.sendmail('John', 'Sally', 'test message')
    self.assertIsNone(smtp.sock)
    self.assertEqual(self.serv._SMTPchannel.rset_count, 0)
