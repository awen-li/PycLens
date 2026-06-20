# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_encoding_errors_reading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.BytesIO(b'abc\n\xff\n')
    t = self.TextIOWrapper(b, encoding='ascii')
    self.assertRaises(UnicodeError, t.read)
    b = self.BytesIO(b'abc\n\xff\n')
    t = self.TextIOWrapper(b, encoding='ascii', errors='strict')
    self.assertRaises(UnicodeError, t.read)
    b = self.BytesIO(b'abc\n\xff\n')
    t = self.TextIOWrapper(b, encoding='ascii', errors='ignore')
    self.assertEqual(t.read(), 'abc\n\n')
    b = self.BytesIO(b'abc\n\xff\n')
    t = self.TextIOWrapper(b, encoding='ascii', errors='replace')
    self.assertEqual(t.read(), 'abc\n�\n')
