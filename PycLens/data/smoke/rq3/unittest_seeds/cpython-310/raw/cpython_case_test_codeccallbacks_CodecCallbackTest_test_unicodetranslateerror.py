# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_unicodetranslateerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_exceptionobjectargs(UnicodeTranslateError, ['gürk', 1, 2, 'ouch'], "can't translate character '\\xfc' in position 1: ouch")
    self.check_exceptionobjectargs(UnicodeTranslateError, ['gĀrk', 1, 2, 'ouch'], "can't translate character '\\u0100' in position 1: ouch")
    self.check_exceptionobjectargs(UnicodeTranslateError, ['g\uffffrk', 1, 2, 'ouch'], "can't translate character '\\uffff' in position 1: ouch")
    self.check_exceptionobjectargs(UnicodeTranslateError, ['g𐀀rk', 1, 2, 'ouch'], "can't translate character '\\U00010000' in position 1: ouch")
    self.check_exceptionobjectargs(UnicodeTranslateError, ['gürk', 1, 3, 'ouch'], "can't translate characters in position 1-2: ouch")
