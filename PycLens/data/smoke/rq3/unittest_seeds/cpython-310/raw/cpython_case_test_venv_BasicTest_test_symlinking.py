# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_venv.py
# case: BasicTest_test_symlinking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for usl in (False, True):
        builder = venv.EnvBuilder(clear=True, symlinks=usl)
        builder.create(self.env_dir)
        fn = self.get_env_file(self.bindir, self.exe)
        if usl:
            if self.cannot_link_exe:
                self.assertFalse(os.path.islink(fn))
            else:
                self.assertTrue(os.path.islink(fn))
