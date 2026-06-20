# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_read_linenum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = csv.reader(['line,1', 'line,2', 'line,3'])
    self.assertEqual(r.line_num, 0)
    next(r)
    self.assertEqual(r.line_num, 1)
    next(r)
    self.assertEqual(r.line_num, 2)
    next(r)
    self.assertEqual(r.line_num, 3)
    self.assertRaises(StopIteration, next, r)
    self.assertEqual(r.line_num, 3)
