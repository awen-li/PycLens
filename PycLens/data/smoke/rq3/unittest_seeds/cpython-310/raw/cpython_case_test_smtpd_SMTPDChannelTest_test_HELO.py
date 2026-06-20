# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_HELO

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = smtpd.socket.getfqdn()
    self.write_line(b'HELO example')
    self.assertEqual(self.channel.socket.last, '250 {}\r\n'.format(name).encode('ascii'))
