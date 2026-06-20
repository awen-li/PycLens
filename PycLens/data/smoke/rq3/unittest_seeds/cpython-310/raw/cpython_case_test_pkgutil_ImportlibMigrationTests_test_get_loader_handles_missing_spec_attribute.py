# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_get_loader_handles_missing_spec_attribute

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'spam'
    mod = type(sys)(name)
    del mod.__spec__
    with CleanImport(name):
        sys.modules[name] = mod
        loader = pkgutil.get_loader(name)
    self.assertIsNone(loader)
