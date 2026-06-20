# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_unicodeencodeerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'gürk', 1, 2, 'ouch'], "'ascii' codec can't encode character '\\xfc' in position 1: ouch")
    self.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'gürk', 1, 4, 'ouch'], "'ascii' codec can't encode characters in position 1-3: ouch")
    self.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'üx', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\xfc' in position 0: ouch")
    self.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', 'Āx', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\u0100' in position 0: ouch")
    self.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', '\uffffx', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\uffff' in position 0: ouch")
    self.check_exceptionobjectargs(UnicodeEncodeError, ['ascii', '𐀀x', 0, 1, 'ouch'], "'ascii' codec can't encode character '\\U00010000' in position 0: ouch")
