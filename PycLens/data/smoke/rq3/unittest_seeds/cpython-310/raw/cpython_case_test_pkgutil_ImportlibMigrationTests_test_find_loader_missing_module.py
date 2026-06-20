# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_find_loader_missing_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'totally bogus'
    loader = pkgutil.find_loader(name)
    self.assertIsNone(loader)
