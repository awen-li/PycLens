# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cprofile.py
# case: CProfileTest_test_profile_enable_disable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prof = self.profilerclass()
    self.addCleanup(prof.disable)
    prof.enable()
    self.assertIs(sys.getprofile(), prof)
    prof.disable()
    self.assertIs(sys.getprofile(), None)
