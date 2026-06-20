# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_change_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_cwd = os.getcwd()
    with os_helper.temp_dir() as temp_path:
        with os_helper.change_cwd(temp_path) as new_cwd:
            self.assertEqual(new_cwd, temp_path)
            self.assertEqual(os.getcwd(), new_cwd)
    self.assertEqual(os.getcwd(), original_cwd)
