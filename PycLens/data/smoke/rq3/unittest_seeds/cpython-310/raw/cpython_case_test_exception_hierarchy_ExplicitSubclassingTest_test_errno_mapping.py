# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: ExplicitSubclassingTest_test_errno_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = SubOSError(EEXIST, 'Bad file descriptor')
    self.assertIs(type(e), SubOSError)
