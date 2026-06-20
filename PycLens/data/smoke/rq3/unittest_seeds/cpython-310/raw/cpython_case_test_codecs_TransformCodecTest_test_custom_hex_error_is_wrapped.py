# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_custom_hex_error_is_wrapped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = "^decoding with 'hex_codec' codec failed"
    with self.assertRaisesRegex(Exception, msg) as failure:
        codecs.decode(b'hello', 'hex_codec')
    self.assertIsInstance(failure.exception.__cause__, type(failure.exception))
