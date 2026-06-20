# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_temp_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parent_dir = tempfile.mkdtemp()
    parent_dir = os.path.realpath(parent_dir)
    try:
        path = os.path.join(parent_dir, 'temp')
        self.assertFalse(os.path.isdir(path))
        with os_helper.temp_dir(path) as temp_path:
            self.assertEqual(temp_path, path)
            self.assertTrue(os.path.isdir(path))
        self.assertFalse(os.path.isdir(path))
    finally:
        os_helper.rmtree(parent_dir)
