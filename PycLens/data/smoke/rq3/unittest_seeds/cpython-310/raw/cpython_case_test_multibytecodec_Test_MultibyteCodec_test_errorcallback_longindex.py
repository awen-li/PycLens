# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_MultibyteCodec_test_errorcallback_longindex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dec = codecs.getdecoder('euc-kr')
    myreplace = lambda exc: ('', sys.maxsize + 1)
    codecs.register_error('test.cjktest', myreplace)
    self.assertRaises(IndexError, dec, b'apple\x92ham\x93spam', 'test.cjktest')
