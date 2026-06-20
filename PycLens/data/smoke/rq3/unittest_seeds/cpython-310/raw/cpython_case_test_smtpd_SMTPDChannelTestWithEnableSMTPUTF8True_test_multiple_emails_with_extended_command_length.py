# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTestWithEnableSMTPUTF8True_test_multiple_emails_with_extended_command_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'ehlo example')
    fill_len = 512 + 26 + 10 - len('mail from:<@example>')
    for char in [b'a', b'b', b'c']:
        self.write_line(b'MAIL from:<' + char * fill_len + b'a@example>')
        self.assertEqual(self.channel.socket.last[0:3], b'500')
        self.write_line(b'MAIL from:<' + char * fill_len + b'@example>')
        self.assertEqual(self.channel.socket.last[0:3], b'250')
        self.write_line(b'rcpt to:<hans@example.com>')
        self.assertEqual(self.channel.socket.last[0:3], b'250')
        self.write_line(b'data')
        self.assertEqual(self.channel.socket.last[0:3], b'354')
        self.write_line(b'test\r\n.')
        self.assertEqual(self.channel.socket.last[0:3], b'250')
