# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_temp_dir__existing_dir__quiet_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def call_temp_dir(path):
        with os_helper.temp_dir(path) as temp_path:
            raise Exception('should not get here')
    path = tempfile.mkdtemp()
    path = os.path.realpath(path)
    try:
        self.assertTrue(os.path.isdir(path))
        self.assertRaises(FileExistsError, call_temp_dir, path)
        self.assertTrue(os.path.isdir(path))
    finally:
        shutil.rmtree(path)
