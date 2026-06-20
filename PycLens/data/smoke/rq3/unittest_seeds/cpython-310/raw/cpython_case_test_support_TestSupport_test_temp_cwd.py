# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_temp_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    here = os.getcwd()
    with os_helper.temp_cwd(name=TESTFN):
        self.assertEqual(os.path.basename(os.getcwd()), TESTFN)
    self.assertFalse(os.path.exists(TESTFN))
    self.assertEqual(os.getcwd(), here)
