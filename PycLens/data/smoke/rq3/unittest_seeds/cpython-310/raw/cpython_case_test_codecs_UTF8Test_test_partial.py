# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8Test_test_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_partial('\x00ÿ߿ࠀ\uffff𐀀', ['\x00', '\x00', '\x00ÿ', '\x00ÿ', '\x00ÿ߿', '\x00ÿ߿', '\x00ÿ߿', '\x00ÿ߿ࠀ', '\x00ÿ߿ࠀ', '\x00ÿ߿ࠀ', '\x00ÿ߿ࠀ\uffff', '\x00ÿ߿ࠀ\uffff', '\x00ÿ߿ࠀ\uffff', '\x00ÿ߿ࠀ\uffff', '\x00ÿ߿ࠀ\uffff𐀀'])
