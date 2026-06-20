# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: Win64WinregTests_test_reflection_functions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with OpenKey(HKEY_LOCAL_MACHINE, 'Software') as key:
        self.assertTrue(QueryReflectionKey(key))
        self.assertIsNone(EnableReflectionKey(key))
        self.assertIsNone(DisableReflectionKey(key))
        self.assertTrue(QueryReflectionKey(key))
