# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_MAIL_RCPT_unknown_parameters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    self.write_line(b'MAIL FROM:<eggs@example> ham=green')
    self.assertEqual(self.channel.socket.last, b'555 MAIL FROM parameters not recognized or not implemented\r\n')
    self.write_line(b'MAIL FROM:<eggs@example>')
    self.write_line(b'RCPT TO:<eggs@example> ham=green')
    self.assertEqual(self.channel.socket.last, b'555 RCPT TO parameters not recognized or not implemented\r\n')
