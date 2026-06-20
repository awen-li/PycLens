# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTestWithEnableSMTPUTF8True_test_MAIL_command_limit_extended_with_SIZE_and_SMTPUTF8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'ehlo example')
    fill_len = 512 + 26 + 10 - len('mail from:<@example>')
    self.write_line(b'MAIL from:<' + b'a' * (fill_len + 1) + b'@example>')
    self.assertEqual(self.channel.socket.last, b'500 Error: line too long\r\n')
    self.write_line(b'MAIL from:<' + b'a' * fill_len + b'@example>')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
