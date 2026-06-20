# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_binary_to_text_denylists_binary_transforms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'encode first to ensure we meet any format restrictions'
    for encoding in bytes_transform_encodings:
        with self.subTest(encoding=encoding):
            encoded_data = codecs.encode(data, encoding)
            fmt = '{!r} is not a text encoding; use codecs.decode\\(\\) to handle arbitrary codecs'
            msg = fmt.format(encoding)
            with self.assertRaisesRegex(LookupError, msg):
                encoded_data.decode(encoding)
            with self.assertRaisesRegex(LookupError, msg):
                bytearray(encoded_data).decode(encoding)
