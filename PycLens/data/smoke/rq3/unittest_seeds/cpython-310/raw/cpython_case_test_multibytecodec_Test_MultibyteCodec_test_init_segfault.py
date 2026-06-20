# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_MultibyteCodec_test_init_segfault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(AttributeError, _multibytecodec.MultibyteStreamReader, None)
    self.assertRaises(AttributeError, _multibytecodec.MultibyteStreamWriter, None)
