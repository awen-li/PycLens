# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestSFbugs_test_matching_blocks_cache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = difflib.SequenceMatcher(None, 'abxcd', 'abcd')
    first = s.get_matching_blocks()
    second = s.get_matching_blocks()
    self.assertEqual(second[0].size, 2)
    self.assertEqual(second[1].size, 2)
    self.assertEqual(second[2].size, 0)
