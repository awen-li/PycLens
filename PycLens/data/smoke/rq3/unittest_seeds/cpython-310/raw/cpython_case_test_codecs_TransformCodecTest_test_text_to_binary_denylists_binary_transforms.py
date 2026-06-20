# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_text_to_binary_denylists_binary_transforms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bad_input = 'bad input type'
    for encoding in bytes_transform_encodings:
        with self.subTest(encoding=encoding):
            fmt = '{!r} is not a text encoding; use codecs.encode\\(\\) to handle arbitrary codecs'
            msg = fmt.format(encoding)
            with self.assertRaisesRegex(LookupError, msg) as failure:
                bad_input.encode(encoding)
            self.assertIsNone(failure.exception.__cause__)
