# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_no_HELO_MAIL

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'MAIL from:<foo@example.com>')
    self.assertEqual(self.channel.socket.last, b'503 Error: send HELO first\r\n')
