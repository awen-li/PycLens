# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: SMTPSimTests_test_421_from_data_cmd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySimSMTPChannel(SimSMTPChannel):

        def found_terminator(self):
            if self.smtp_state == self.DATA:
                self.push('421 closing')
            else:
                super().found_terminator()
    self.serv.channel_class = MySimSMTPChannel
    smtp = smtplib.SMTP(HOST, self.port, local_hostname='localhost', timeout=support.LOOPBACK_TIMEOUT)
    smtp.noop()
    with self.assertRaises(smtplib.SMTPDataError):
        smtp.sendmail('John@foo.org', ['Sally@foo.org'], 'test message')
    self.assertIsNone(smtp.sock)
    self.assertEqual(self.serv._SMTPchannel.rcpt_count, 0)
