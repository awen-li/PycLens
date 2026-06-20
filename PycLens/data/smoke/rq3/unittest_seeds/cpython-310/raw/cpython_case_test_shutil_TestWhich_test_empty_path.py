# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_empty_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base_dir = os.path.dirname(self.dir)
    with os_helper.change_cwd(path=self.dir), os_helper.EnvironmentVarGuard() as env:
        env['PATH'] = self.env_path
        rv = shutil.which(self.file, path='')
        self.assertIsNone(rv)
