# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: LongReprTest_test_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.maxDiff = None
    self._check_path_limitations(self.pkgname)
    create_empty_file(os.path.join(self.subpkgname, self.pkgname + '.py'))
    importlib.invalidate_caches()
    from areallylongpackageandmodulenametotestreprtruncation.areallylongpackageandmodulenametotestreprtruncation import areallylongpackageandmodulenametotestreprtruncation
    module = areallylongpackageandmodulenametotestreprtruncation
    self.assertEqual(repr(module), '<module %r from %r>' % (module.__name__, module.__file__))
    self.assertEqual(repr(sys), "<module 'sys' (built-in)>")
