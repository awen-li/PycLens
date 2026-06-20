# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_load_module_extension_file_is_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = '_testimportmultiple'
    found = imp.find_module(name)
    if found[0] is not None:
        found[0].close()
    if found[2][2] != imp.C_EXTENSION:
        self.skipTest("found module doesn't appear to be a C extension")
    imp.load_module(name, None, *found[1:])
