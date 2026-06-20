# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestGetCandidateNames_test_retval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = tempfile._get_candidate_names()
    self.assertIsInstance(obj, tempfile._RandomNameSequence)
