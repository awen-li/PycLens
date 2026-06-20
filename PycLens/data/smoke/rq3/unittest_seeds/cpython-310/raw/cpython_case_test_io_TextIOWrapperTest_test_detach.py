# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_detach

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.BytesIO()
    b = self.BufferedWriter(r)
    t = self.TextIOWrapper(b, encoding='ascii')
    self.assertIs(t.detach(), b)
    t = self.TextIOWrapper(b, encoding='ascii')
    t.write('howdy')
    self.assertFalse(r.getvalue())
    t.detach()
    self.assertEqual(r.getvalue(), b'howdy')
    self.assertRaises(ValueError, t.detach)
    repr(t)
    self.assertEqual(t.encoding, 'ascii')
    self.assertEqual(t.errors, 'strict')
    self.assertFalse(t.line_buffering)
    self.assertFalse(t.write_through)
