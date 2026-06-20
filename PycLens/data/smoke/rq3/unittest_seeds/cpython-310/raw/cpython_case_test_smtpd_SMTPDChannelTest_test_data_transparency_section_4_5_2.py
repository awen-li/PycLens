# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_data_transparency_section_4_5_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'HELO example')
    self.write_line(b'MAIL From:eggs@example')
    self.write_line(b'RCPT To:spam@example')
    self.write_line(b'DATA')
    self.write_line(b'..\r\n.\r\n')
    self.assertEqual(self.channel.received_data, '.')
