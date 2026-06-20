# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFbugs_test_added_tab_hint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    diff = list(difflib.Differ().compare(['\tI am a buggy'], ['\t\tI am a bug']))
    self.assertEqual('- \tI am a buggy', diff[0])
    self.assertEqual('? \t          --\n', diff[1])
    self.assertEqual('+ \t\tI am a bug', diff[2])
    self.assertEqual('? +\n', diff[3])
