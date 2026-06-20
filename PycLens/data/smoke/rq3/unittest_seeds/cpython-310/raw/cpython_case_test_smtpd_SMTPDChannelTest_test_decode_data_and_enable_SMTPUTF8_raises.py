# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtpd.py
# case: SMTPDChannelTest_test_decode_data_and_enable_SMTPUTF8_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(ValueError, smtpd.SMTPChannel, self.server, self.channel.conn, self.channel.addr, enable_SMTPUTF8=True, decode_data=True)
