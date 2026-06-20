# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: HardlinkDedupTestsBase_test_hardlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (code, docstring, assertion) in self.iter_codes():
        with self.subTest(docstring=docstring, assertion=assertion):
            with self.temporary_directory():
                script = self.make_script(code)
                self.compile_dir()
                self.check_hardlinks(script, docstring, assertion)
