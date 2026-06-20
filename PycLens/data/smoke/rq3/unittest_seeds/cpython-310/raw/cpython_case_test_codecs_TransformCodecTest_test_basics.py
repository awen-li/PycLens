# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: TransformCodecTest_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    binput = bytes(range(256))
    for encoding in bytes_transform_encodings:
        with self.subTest(encoding=encoding):
            (o, size) = codecs.getencoder(encoding)(binput)
            self.assertEqual(size, len(binput))
            (i, size) = codecs.getdecoder(encoding)(o)
            self.assertEqual(size, len(o))
            self.assertEqual(i, binput)
