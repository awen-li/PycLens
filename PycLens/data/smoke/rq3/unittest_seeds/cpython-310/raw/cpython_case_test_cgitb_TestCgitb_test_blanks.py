# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgitb.py
# case: TestCgitb_test_blanks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(cgitb.small(''), '')
    self.assertEqual(cgitb.strong(''), '')
    self.assertEqual(cgitb.grey(''), '')
