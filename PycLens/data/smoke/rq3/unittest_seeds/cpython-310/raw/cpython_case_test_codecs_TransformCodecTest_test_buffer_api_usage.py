# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_buffer_api_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original = b'12345\x80'
    for encoding in bytes_transform_encodings:
        with self.subTest(encoding=encoding):
            data = original
            view = memoryview(data)
            data = codecs.encode(data, encoding)
            view_encoded = codecs.encode(view, encoding)
            self.assertEqual(view_encoded, data)
            view = memoryview(data)
            data = codecs.decode(data, encoding)
            self.assertEqual(data, original)
            view_decoded = codecs.decode(view, encoding)
            self.assertEqual(view_decoded, data)
