# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8Test_test_decoder_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = '\x00\x7f\x80ÿĀ߿ࠀ\uffff\U0010ffff'
    self.check_state_handling_decode(self.encoding, u, u.encode(self.encoding))
