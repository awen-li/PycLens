# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_reprlib.py
# case: LongReprTest_test_instance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_path_limitations('baz')
    write_file(os.path.join(self.subpkgname, 'baz.py'), 'class baz:\n    pass\n')
    importlib.invalidate_caches()
    from areallylongpackageandmodulenametotestreprtruncation.areallylongpackageandmodulenametotestreprtruncation import baz
    ibaz = baz.baz()
    self.assertTrue(repr(ibaz).startswith('<%s.baz object at 0x' % baz.__name__))
