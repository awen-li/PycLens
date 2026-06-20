# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_environ_path_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_cwd = os.path.basename(self.temp_file.name)
    if sys.platform == 'win32':
        curdir = os.curdir
        if isinstance(expected_cwd, bytes):
            curdir = os.fsencode(curdir)
        expected_cwd = os.path.join(curdir, expected_cwd)
    with os_helper.EnvironmentVarGuard() as env:
        env['PATH'] = os.pathsep
        with unittest.mock.patch('os.confstr', return_value=self.dir, create=True), support.swap_attr(os, 'defpath', self.dir):
            rv = shutil.which(self.file)
            self.assertIsNone(rv)
            with os_helper.change_cwd(self.dir):
                rv = shutil.which(self.file)
                self.assertEqual(rv, expected_cwd)
