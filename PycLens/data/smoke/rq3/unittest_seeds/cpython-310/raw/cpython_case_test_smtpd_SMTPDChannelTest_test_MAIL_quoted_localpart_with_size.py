# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_MAIL_quoted_localpart_with_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    self.write_line(b'MAIL from: <"Fred Blogs"@example.com> SIZE=1000')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
    self.assertEqual(self.channel.mailfrom, '"Fred Blogs"@example.com')
