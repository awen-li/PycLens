# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_HELO_parameter_rejected_when_extensions_not_enabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.extended_smtp = False
    self.write_line(b'HELO example')
    self.write_line(b'MAIL from:<foo@example.com> SIZE=1234')
    self.assertEqual(self.channel.socket.last, b'501 Syntax: MAIL FROM: <address>\r\n')
