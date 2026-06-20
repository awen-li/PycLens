# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_VRFY

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'VRFY eggs@example')
    self.assertEqual(self.channel.socket.last, b'252 Cannot VRFY user, but will accept message and attempt ' + b'delivery\r\n')
