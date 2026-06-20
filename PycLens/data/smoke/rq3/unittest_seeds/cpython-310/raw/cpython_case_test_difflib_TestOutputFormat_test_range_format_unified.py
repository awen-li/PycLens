# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestOutputFormat_test_range_format_unified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    spec = '           Each <range> field shall be of the form:\n             %1d", <beginning line number>  if the range contains exactly one line,\n           and:\n            "%1d,%1d", <beginning line number>, <number of lines> otherwise.\n           If a range is empty, its beginning line number shall be the number of\n           the line just before the range, or 0 if the empty range starts the file.\n        '
    fmt = difflib._format_range_unified
    self.assertEqual(fmt(3, 3), '3,0')
    self.assertEqual(fmt(3, 4), '4')
    self.assertEqual(fmt(3, 5), '4,2')
    self.assertEqual(fmt(3, 6), '4,3')
    self.assertEqual(fmt(0, 0), '0,0')
