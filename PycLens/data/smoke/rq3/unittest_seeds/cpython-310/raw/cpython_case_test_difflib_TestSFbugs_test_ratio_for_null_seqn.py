# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFbugs_test_ratio_for_null_seqn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = difflib.SequenceMatcher(None, [], [])
    self.assertEqual(s.ratio(), 1)
    self.assertEqual(s.quick_ratio(), 1)
    self.assertEqual(s.real_quick_ratio(), 1)
