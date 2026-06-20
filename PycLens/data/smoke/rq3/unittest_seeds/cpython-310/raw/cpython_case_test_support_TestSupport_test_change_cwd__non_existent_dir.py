# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_change_cwd__non_existent_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original_cwd = os.getcwd()

    def call_change_cwd(path):
        with os_helper.change_cwd(path) as new_cwd:
            raise Exception('should not get here')
    with os_helper.temp_dir() as parent_dir:
        non_existent_dir = os.path.join(parent_dir, 'does_not_exist')
        self.assertRaises(FileNotFoundError, call_change_cwd, non_existent_dir)
    self.assertEqual(os.getcwd(), original_cwd)
