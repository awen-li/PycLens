# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: ImportlibMigrationTests_test_get_loader_handles_spec_attribute_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'spam'
    mod = type(sys)(name)
    mod.__spec__ = None
    with CleanImport(name):
        sys.modules[name] = mod
        loader = pkgutil.get_loader(name)
    self.assertIsNone(loader)
