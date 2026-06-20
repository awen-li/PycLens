# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelWithDecodeDataTrue_test_utf8_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_line(b'HELO example')
    self.write_line(b'MAIL From:eggs@example')
    self.write_line(b'RCPT To:spam@example')
    self.write_line(b'DATA')
    self.write_line(b'utf8 enriched text: \xc5\xbc\xc5\xba\xc4\x87')
    self.write_line(b'and some plain ascii')
    self.write_line(b'.')
    self.assertEqual(self.channel.received_data, 'utf8 enriched text: żźć\nand some plain ascii')
