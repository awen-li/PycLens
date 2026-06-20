# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: HardlinkDedupTestsBase_test_only_two_levels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for opts in ((0, 1), (1, 2), (0, 2)):
        with self.subTest(opts=opts):
            with self.temporary_directory():
                script = self.make_script(self.create_code())
                self.compile_dir(optimize=opts)
                pyc1 = get_pyc(script, opts[0])
                pyc2 = get_pyc(script, opts[1])
                self.assertTrue(is_hardlink(pyc1, pyc2))
