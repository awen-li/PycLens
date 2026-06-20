# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeccallbacks.py
# case: CodecCallbackTest_test_unicodedecodeerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_exceptionobjectargs(UnicodeDecodeError, ['ascii', bytearray(b'g\xfcrk'), 1, 2, 'ouch'], "'ascii' codec can't decode byte 0xfc in position 1: ouch")
    self.check_exceptionobjectargs(UnicodeDecodeError, ['ascii', bytearray(b'g\xfcrk'), 1, 3, 'ouch'], "'ascii' codec can't decode bytes in position 1-2: ouch")
