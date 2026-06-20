# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_name_field_not_included_in_envelop_addresses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    self.addCleanup(smtp.close)
    message = EmailMessage()
    message['From'] = email.utils.formataddr(('Michaël', 'michael@example.com'))
    message['To'] = email.utils.formataddr(('René', 'rene@example.com'))
    self.assertDictEqual(smtp.send_message(message), {})
    self.assertEqual(self.serv._addresses['from'], 'michael@example.com')
    self.assertEqual(self.serv._addresses['tos'], ['rene@example.com'])
