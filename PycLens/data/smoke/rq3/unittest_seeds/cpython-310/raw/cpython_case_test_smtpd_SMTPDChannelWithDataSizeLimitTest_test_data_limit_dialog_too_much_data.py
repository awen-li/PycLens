# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelWithDataSizeLimitTest_test_data_limit_dialog_too_much_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'HELO example')
    self.write_line(b'MAIL From:eggs@example')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
    self.write_line(b'RCPT To:spam@example')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
    self.write_line(b'DATA')
    self.assertEqual(self.channel.socket.last, b'354 End data with <CR><LF>.<CR><LF>\r\n')
    self.write_line(b'This message is longer than 32 bytes\r\n.')
    self.assertEqual(self.channel.socket.last, b'552 Error: Too much mail data\r\n')
