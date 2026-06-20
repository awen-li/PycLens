# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_data_dialog

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
    self.write_line(b'data\r\nmore\r\n.')
    self.assertEqual(self.channel.socket.last, b'250 OK\r\n')
    self.assertEqual(self.server.messages, [(('peer-address', 'peer-port'), 'eggs@example', ['spam@example'], 'data\nmore')])
