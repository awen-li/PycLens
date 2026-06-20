# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_relative_cmd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (base_dir, tail_dir) = os.path.split(self.dir)
    relpath = os.path.join(tail_dir, self.file)
    with os_helper.change_cwd(path=base_dir):
        rv = shutil.which(relpath, path=self.temp_dir)
        self.assertEqual(rv, relpath)
    with os_helper.change_cwd(path=self.dir):
        rv = shutil.which(relpath, path=base_dir)
        self.assertIsNone(rv)
