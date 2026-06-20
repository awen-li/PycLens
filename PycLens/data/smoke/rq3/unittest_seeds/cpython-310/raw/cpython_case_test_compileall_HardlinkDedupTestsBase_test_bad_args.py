# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: HardlinkDedupTestsBase_test_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.temporary_directory():
        self.make_script('pass')
        with self.assertRaises(ValueError):
            compileall.compile_dir(self.path, quiet=True, optimize=0, hardlink_dupes=True)
        with self.assertRaises(ValueError):
            compileall.compile_dir(self.path, quiet=True, optimize=[0, 0], hardlink_dupes=True)
