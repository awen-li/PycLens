# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_line_buffering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.BytesIO()
    b = self.BufferedWriter(r, 1000)
    t = self.TextIOWrapper(b, encoding='utf-8', newline='\n', line_buffering=False)
    t.write('AB\nC')
    self.assertEqual(r.getvalue(), b'')
    t.reconfigure(line_buffering=True)
    self.assertEqual(r.getvalue(), b'AB\nC')
    t.write('DEF\nG')
    self.assertEqual(r.getvalue(), b'AB\nCDEF\nG')
    t.write('H')
    self.assertEqual(r.getvalue(), b'AB\nCDEF\nG')
    t.reconfigure(line_buffering=False)
    self.assertEqual(r.getvalue(), b'AB\nCDEF\nGH')
    t.write('IJ')
    self.assertEqual(r.getvalue(), b'AB\nCDEF\nGH')
    t.reconfigure()
    t.reconfigure(line_buffering=None)
    self.assertEqual(t.line_buffering, False)
    t.reconfigure(line_buffering=True)
    t.reconfigure()
    t.reconfigure(line_buffering=None)
    self.assertEqual(t.line_buffering, True)
