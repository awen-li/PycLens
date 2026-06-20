# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_encoding_errors_writing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.BytesIO()
    t = self.TextIOWrapper(b, encoding='ascii')
    self.assertRaises(UnicodeError, t.write, 'ÿ')
    b = self.BytesIO()
    t = self.TextIOWrapper(b, encoding='ascii', errors='strict')
    self.assertRaises(UnicodeError, t.write, 'ÿ')
    b = self.BytesIO()
    t = self.TextIOWrapper(b, encoding='ascii', errors='ignore', newline='\n')
    t.write('abcÿdef\n')
    t.flush()
    self.assertEqual(b.getvalue(), b'abcdef\n')
    b = self.BytesIO()
    t = self.TextIOWrapper(b, encoding='ascii', errors='replace', newline='\n')
    t.write('abcÿdef\n')
    t.flush()
    self.assertEqual(b.getvalue(), b'abc?def\n')
