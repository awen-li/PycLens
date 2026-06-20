# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_import_encoded_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (modname, encoding, teststr) in self.test_strings:
        mod = importlib.import_module('test.encoded_modules.module_' + modname)
        self.assertEqual(teststr, mod.test)
