# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetCandidateNames_test_same_thing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = tempfile._get_candidate_names()
    b = tempfile._get_candidate_names()
    self.assertTrue(a is b)
