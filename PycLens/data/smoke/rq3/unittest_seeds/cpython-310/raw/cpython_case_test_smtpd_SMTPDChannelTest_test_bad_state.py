# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_bad_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.channel.smtp_state = 'BAD STATE'
    self.write_line(b'HELO example')
    self.assertEqual(self.channel.socket.last, b'451 Internal confusion\r\n')
