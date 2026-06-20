# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTestWithEnableSMTPUTF8True_test_MAIL_command_accepts_SMTPUTF8_when_announced

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    self.write_line('MAIL from: <naïve@example.com> BODY=8BITMIME SMTPUTF8'.encode('utf-8'))
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
