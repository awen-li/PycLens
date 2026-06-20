# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPUTF8SimTests_test_send_unicode_with_SMTPUTF8_via_sendmail

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = '¡a test message containing unicode!'.encode('utf-8')
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    smtp.sendmail('Jőhn', 'Sálly', m, mail_options=['BODY=8BITMIME', 'SMTPUTF8'])
    self.assertEqual(self.serv.last_mailfrom, 'Jőhn')
    self.assertEqual(self.serv.last_rcpttos, ['Sálly'])
    self.assertEqual(self.serv.last_message, m)
    self.assertIn('BODY=8BITMIME', self.serv.last_mail_options)
    self.assertIn('SMTPUTF8', self.serv.last_mail_options)
    self.assertEqual(self.serv.last_rcpt_options, [])
