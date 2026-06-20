# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFbugs_test_hint_indented_properly_with_tabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    diff = list(difflib.Differ().compare(['\t \t \t^'], ['\t \t \t^\n']))
    self.assertEqual('- \t \t \t^', diff[0])
    self.assertEqual('+ \t \t \t^\n', diff[1])
    self.assertEqual('? \t \t \t +\n', diff[2])
