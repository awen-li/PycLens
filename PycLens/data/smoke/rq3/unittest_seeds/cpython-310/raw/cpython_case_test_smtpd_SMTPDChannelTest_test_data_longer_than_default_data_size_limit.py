# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_data_longer_than_default_data_size_limit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.channel.data_size_limit = 1048
    self.write_line(b'HELO example')
    self.write_line(b'MAIL From:eggs@example')
    self.write_line(b'RCPT To:spam@example')
    self.write_line(b'DATA')
    self.write_line(b'A' * self.channel.data_size_limit + b'A\r\n.')
    self.assertEqual(self.channel.socket.last, b'552 Error: Too much mail data\r\n')
