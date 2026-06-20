# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFbugs_test_comparing_empty_lists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    group_gen = difflib.SequenceMatcher(None, [], []).get_grouped_opcodes()
    self.assertRaises(StopIteration, next, group_gen)
    diff_gen = difflib.unified_diff([], [])
    self.assertRaises(StopIteration, next, diff_gen)
