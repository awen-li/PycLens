# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_get_loader_None_in_sys_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'totally bogus'
    sys.modules[name] = None
    try:
        loader = pkgutil.get_loader(name)
    finally:
        del sys.modules[name]
    self.assertIsNone(loader)
