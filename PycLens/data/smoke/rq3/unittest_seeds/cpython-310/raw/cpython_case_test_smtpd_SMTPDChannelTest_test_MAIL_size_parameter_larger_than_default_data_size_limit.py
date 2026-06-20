# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_MAIL_size_parameter_larger_than_default_data_size_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.channel.data_size_limit = 1048
    self.write_line(b'EHLO example')
    self.write_line(b'MAIL FROM:<eggs@example> SIZE=2096')
    self.assertEqual(self.channel.socket.last, b'552 Error: message size exceeds fixed maximum message size\r\n')
