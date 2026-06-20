# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.encode('äöü', 'latin-1'), b'\xe4\xf6\xfc')
    self.assertRaises(TypeError, codecs.encode)
    self.assertRaises(LookupError, codecs.encode, 'foo', '__spam__')
    self.assertEqual(codecs.encode('abc'), b'abc')
    self.assertRaises(UnicodeEncodeError, codecs.encode, 'ÿff', 'ascii')
    self.assertEqual(codecs.encode(obj='äöü', encoding='latin-1'), b'\xe4\xf6\xfc')
    self.assertEqual(codecs.encode('[ÿ]', 'ascii', errors='ignore'), b'[]')
