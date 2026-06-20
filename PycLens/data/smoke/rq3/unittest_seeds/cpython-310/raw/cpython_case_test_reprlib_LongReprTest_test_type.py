# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: LongReprTest_test_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_path_limitations('foo')
    eq = self.assertEqual
    write_file(os.path.join(self.subpkgname, 'foo.py'), 'class foo(object):\n    pass\n')
    importlib.invalidate_caches()
    from areallylongpackageandmodulenametotestreprtruncation.areallylongpackageandmodulenametotestreprtruncation import foo
    eq(repr(foo.foo), "<class '%s.foo'>" % foo.__name__)
