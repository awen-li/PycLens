# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_binary_to_text_denylists_text_transforms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for bad_input in (b'immutable', bytearray(b'mutable')):
        with self.subTest(bad_input=bad_input):
            msg = "^'rot_13' is not a text encoding; use codecs.decode\\(\\) to handle arbitrary codecs"
            with self.assertRaisesRegex(LookupError, msg) as failure:
                bad_input.decode('rot_13')
            self.assertIsNone(failure.exception.__cause__)
