# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.BytesIO(b'\xc3\xa9\n\n')
    b = self.BufferedReader(r, 1000)
    t = self.TextIOWrapper(b, encoding='utf-8')
    t.__init__(b, encoding='latin-1', newline='\r\n')
    self.assertEqual(t.encoding, 'latin-1')
    self.assertEqual(t.line_buffering, False)
    t.__init__(b, encoding='utf-8', line_buffering=True)
    self.assertEqual(t.encoding, 'utf-8')
    self.assertEqual(t.line_buffering, True)
    self.assertEqual('é\n', t.readline())
    self.assertRaises(TypeError, t.__init__, b, encoding='utf-8', newline=42)
    self.assertRaises(ValueError, t.__init__, b, encoding='utf-8', newline='xyzzy')
