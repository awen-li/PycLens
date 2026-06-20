# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_HELP

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'HELP')
    self.assertEqual(self.channel.socket.last, b'250 Supported commands: EHLO HELO MAIL RCPT ' + b'DATA RSET NOOP QUIT VRFY\r\n')
