# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF8SigTest_test_partial

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_partial('\ufeff\x00ÿ߿ࠀ\uffff𐀀', ['', '', '', '', '', '\ufeff', '\ufeff\x00', '\ufeff\x00', '\ufeff\x00ÿ', '\ufeff\x00ÿ', '\ufeff\x00ÿ߿', '\ufeff\x00ÿ߿', '\ufeff\x00ÿ߿', '\ufeff\x00ÿ߿ࠀ', '\ufeff\x00ÿ߿ࠀ', '\ufeff\x00ÿ߿ࠀ', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff', '\ufeff\x00ÿ߿ࠀ\uffff𐀀'])
