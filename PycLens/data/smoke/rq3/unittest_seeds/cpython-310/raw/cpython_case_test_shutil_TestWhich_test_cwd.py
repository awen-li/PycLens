# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_cwd

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base_dir = os.path.dirname(self.dir)
    with os_helper.change_cwd(path=self.dir):
        rv = shutil.which(self.file, path=base_dir)
        if sys.platform == 'win32':
            self.assertEqual(rv, os.path.join(self.curdir, self.file))
        else:
            self.assertIsNone(rv)
