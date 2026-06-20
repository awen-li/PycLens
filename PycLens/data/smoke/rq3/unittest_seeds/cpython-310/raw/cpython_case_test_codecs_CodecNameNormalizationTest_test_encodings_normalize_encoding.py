# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecNameNormalizationTest_test_encodings_normalize_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    normalize = encodings.normalize_encoding
    self.assertEqual(normalize('utf_8'), 'utf_8')
    self.assertEqual(normalize('utfé€\U0010ffff-8'), 'utf_8')
    self.assertEqual(normalize('utf   8'), 'utf_8')
    self.assertEqual(normalize('UTF 8'), 'UTF_8')
    self.assertEqual(normalize('utf.8'), 'utf.8')
    self.assertEqual(normalize('utf...8'), 'utf...8')
