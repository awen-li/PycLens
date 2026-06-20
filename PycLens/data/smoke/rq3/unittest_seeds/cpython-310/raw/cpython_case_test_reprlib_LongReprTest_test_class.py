# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: LongReprTest_test_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_path_limitations('bar')
    write_file(os.path.join(self.subpkgname, 'bar.py'), 'class bar:\n    pass\n')
    importlib.invalidate_caches()
    from areallylongpackageandmodulenametotestreprtruncation.areallylongpackageandmodulenametotestreprtruncation import bar
    self.assertEqual(repr(bar.bar), "<class '%s.bar'>" % bar.__name__)
