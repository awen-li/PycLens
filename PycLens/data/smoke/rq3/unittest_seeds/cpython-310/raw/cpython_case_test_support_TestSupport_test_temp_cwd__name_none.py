# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_temp_cwd__name_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_cwd = os.getcwd()
    with os_helper.temp_cwd(name=None) as new_cwd:
        self.assertNotEqual(new_cwd, original_cwd)
        self.assertTrue(os.path.isdir(new_cwd))
        self.assertEqual(os.getcwd(), new_cwd)
    self.assertEqual(os.getcwd(), original_cwd)
