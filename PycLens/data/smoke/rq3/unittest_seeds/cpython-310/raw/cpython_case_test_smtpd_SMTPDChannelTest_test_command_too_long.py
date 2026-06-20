# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_command_too_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'HELO example')
    self.write_line(b'MAIL from: ' + b'a' * self.channel.command_size_limit + b'@example')
    self.assertEqual(self.channel.socket.last, b'500 Error: line too long\r\n')
