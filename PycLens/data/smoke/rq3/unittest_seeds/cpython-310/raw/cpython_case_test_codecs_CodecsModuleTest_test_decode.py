# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: CodecsModuleTest_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(codecs.decode(b'\xe4\xf6\xfc', 'latin-1'), 'äöü')
    self.assertRaises(TypeError, codecs.decode)
    self.assertEqual(codecs.decode(b'abc'), 'abc')
    self.assertRaises(UnicodeDecodeError, codecs.decode, b'\xff', 'ascii')
    self.assertEqual(codecs.decode(obj=b'\xe4\xf6\xfc', encoding='latin-1'), 'äöü')
    self.assertEqual(codecs.decode(b'[\xff]', 'ascii', errors='ignore'), '[]')
