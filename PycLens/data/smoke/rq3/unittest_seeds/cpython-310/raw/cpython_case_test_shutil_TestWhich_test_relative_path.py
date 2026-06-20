# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestWhich_test_relative_path

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (base_dir, tail_dir) = os.path.split(self.dir)
    with os_helper.change_cwd(path=base_dir):
        rv = shutil.which(self.file, path=tail_dir)
        self.assertEqual(rv, os.path.join(tail_dir, self.file))
