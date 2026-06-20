# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_reflection_unsupported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as ck:
            self.assertNotEqual(ck.handle, 0)
        key = OpenKey(HKEY_CURRENT_USER, test_key_name)
        self.assertNotEqual(key.handle, 0)
        with self.assertRaises(NotImplementedError):
            DisableReflectionKey(key)
        with self.assertRaises(NotImplementedError):
            EnableReflectionKey(key)
        with self.assertRaises(NotImplementedError):
            QueryReflectionKey(key)
        with self.assertRaises(NotImplementedError):
            DeleteKeyEx(HKEY_CURRENT_USER, test_key_name)
    finally:
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
