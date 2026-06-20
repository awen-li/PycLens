# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_extended_MAIL_allows_space_after_colon

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    self.write_line(b'MAIL from:   <foo@example.com> size=20')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
