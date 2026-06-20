# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_MAIL_command_limit_extended_with_SIZE

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    fill_len = self.channel.command_size_limit - len('MAIL from:<@example>')
    self.write_line(b'MAIL from:<' + b'a' * fill_len + b'@example> SIZE=1234')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
    self.write_line(b'MAIL from:<' + b'a' * (fill_len + 26) + b'@example> SIZE=1234')
    self.assertEqual(self.channel.socket.last, b'500 Error: line too long\r\n')
