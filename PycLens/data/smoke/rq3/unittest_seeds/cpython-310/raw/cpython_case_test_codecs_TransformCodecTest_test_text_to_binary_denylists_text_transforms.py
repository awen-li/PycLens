# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_text_to_binary_denylists_text_transforms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = "^'rot_13' is not a text encoding; use codecs.encode\\(\\) to handle arbitrary codecs"
    with self.assertRaisesRegex(LookupError, msg):
        'just an example message'.encode('rot_13')
