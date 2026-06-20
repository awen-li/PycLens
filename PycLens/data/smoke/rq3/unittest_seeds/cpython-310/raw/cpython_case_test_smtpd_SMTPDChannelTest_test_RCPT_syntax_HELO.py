# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_RCPT_syntax_HELO

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'HELO example')
    self.write_line(b'MAIL From: eggs@example')
    self.write_line(b'RCPT to eggs@example')
    self.assertEqual(self.channel.socket.last, b'501 Syntax: RCPT TO: <address>\r\n')
