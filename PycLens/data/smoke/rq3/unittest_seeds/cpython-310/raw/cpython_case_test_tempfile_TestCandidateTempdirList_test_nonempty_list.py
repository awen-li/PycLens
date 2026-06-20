# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestCandidateTempdirList_test_nonempty_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cand = tempfile._candidate_tempdir_list()
    self.assertFalse(len(cand) == 0)
    for c in cand:
        self.assertIsInstance(c, str)
