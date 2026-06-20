# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_unoverwritable_fails

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for paths in self.ENV_SUBDIRS[:3]:
        fn = os.path.join(self.env_dir, *paths)
        with open(fn, 'wb') as f:
            f.write(b'')
        self.assertRaises((ValueError, OSError), venv.create, self.env_dir)
        self.clear_directory(self.env_dir)
