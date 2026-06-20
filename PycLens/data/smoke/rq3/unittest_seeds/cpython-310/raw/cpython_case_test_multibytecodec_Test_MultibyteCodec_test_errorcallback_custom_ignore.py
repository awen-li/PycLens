# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_MultibyteCodec_test_errorcallback_custom_ignore

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 100 * '\udc00'
    codecs.register_error('test.ignore', codecs.ignore_errors)
    for enc in ALL_CJKENCODINGS:
        self.assertEqual(data.encode(enc, 'test.ignore'), b'')
