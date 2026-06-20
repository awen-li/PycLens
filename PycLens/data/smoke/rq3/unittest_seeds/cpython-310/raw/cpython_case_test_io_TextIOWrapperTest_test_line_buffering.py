# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_line_buffering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.BytesIO()
    b = self.BufferedWriter(r, 1000)
    t = self.TextIOWrapper(b, encoding='utf-8', newline='\n', line_buffering=True)
    t.write('X')
    self.assertEqual(r.getvalue(), b'')
    t.write('Y\nZ')
    self.assertEqual(r.getvalue(), b'XY\nZ')
    t.write('A\rB')
    self.assertEqual(r.getvalue(), b'XY\nZA\rB')
