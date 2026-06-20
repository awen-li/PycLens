# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_MAIL_command_rejects_SMTPUTF8_by_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    self.write_line(b'MAIL from: <naive@example.com> BODY=8BITMIME SMTPUTF8')
    self.assertEqual(self.channel.socket.last[0:1], b'5')
