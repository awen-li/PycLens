# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_profile.py
# case: ProfileTest_test_runctx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with silent():
        self.profilermodule.runctx('testfunc()', globals(), locals())
    self.profilermodule.runctx('testfunc()', globals(), locals(), filename=TESTFN)
    self.assertTrue(os.path.exists(TESTFN))
