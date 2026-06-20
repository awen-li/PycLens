# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: LocaleCodecTest_test_decode_unsupported_error_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError) as cm:
        self.decode(b'', 'backslashreplace')
    self.assertEqual(str(cm.exception), 'unsupported error handler')
