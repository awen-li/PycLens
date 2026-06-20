# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for encoding in bytes_transform_encodings:
        with self.subTest(encoding=encoding):
            sin = codecs.encode(b'\x80', encoding)
            reader = codecs.getreader(encoding)(io.BytesIO(sin))
            sout = reader.read()
            self.assertEqual(sout, b'\x80')
