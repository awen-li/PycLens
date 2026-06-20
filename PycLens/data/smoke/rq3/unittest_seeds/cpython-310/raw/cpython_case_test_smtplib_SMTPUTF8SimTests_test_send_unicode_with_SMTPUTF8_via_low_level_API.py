# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPUTF8SimTests_test_send_unicode_with_SMTPUTF8_via_low_level_API

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = '¡a test message containing unicode!'.encode('utf-8')
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    smtp.ehlo()
    self.assertEqual(smtp.mail('Jő', options=['BODY=8BITMIME', 'SMTPUTF8']), (250, b'OK'))
    self.assertEqual(smtp.rcpt('János'), (250, b'OK'))
    self.assertEqual(smtp.data(m), (250, b'OK'))
    self.assertEqual(self.serv.last_mailfrom, 'Jő')
    self.assertEqual(self.serv.last_rcpttos, ['János'])
    self.assertEqual(self.serv.last_message, m)
    self.assertIn('BODY=8BITMIME', self.serv.last_mail_options)
    self.assertIn('SMTPUTF8', self.serv.last_mail_options)
    self.assertEqual(self.serv.last_rcpt_options, [])
