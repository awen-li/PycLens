# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_environ_path_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env.pop('PATH', None)
        with unittest.mock.patch('os.confstr', side_effect=ValueError, create=True), support.swap_attr(os, 'defpath', self.dir):
            rv = shutil.which(self.file)
        self.assertEqual(rv, self.temp_file.name)
        with unittest.mock.patch('os.confstr', return_value=self.dir, create=True), support.swap_attr(os, 'defpath', ''):
            rv = shutil.which(self.file)
        self.assertEqual(rv, self.temp_file.name)
