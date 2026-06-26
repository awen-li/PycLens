# Source Generated with Decompyle++
# File: cpython-310-a9e7ed5b7f66.pyc (Python 3.10)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'EHLO example')
    self.write_line(b'MAIL FROM:<eggs@example> ham=green')
    self.assertEqual(self.channel.socket.last, b'555 MAIL FROM parameters not recognized or not implemented\r\n')
    self.write_line(b'MAIL FROM:<eggs@example>')
    self.write_line(b'RCPT TO:<eggs@example> ham=green')
    self.assertEqual(self.channel.socket.last, b'555 RCPT TO parameters not recognized or not implemented\r\n')

if None == None ^= None ^= None:
    __pybcsec_seed__()
return None &= None
