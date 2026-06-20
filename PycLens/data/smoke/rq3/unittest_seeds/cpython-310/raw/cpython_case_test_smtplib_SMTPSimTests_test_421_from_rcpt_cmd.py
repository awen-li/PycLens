# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_421_from_rcpt_cmd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    smtp.noop()
    self.serv._SMTPchannel.rcpt_response = ['250 accepted', '421 closing']
    with self.assertRaises(smtplib.SMTPRecipientsRefused) as r:
        smtp.sendmail('John', ['Sally', 'Frank', 'George'], 'test message')
    self.assertIsNone(smtp.sock)
    self.assertEqual(self.serv._SMTPchannel.rset_count, 0)
    self.assertDictEqual(r.exception.args[0], {'Frank': (421, b'closing')})
