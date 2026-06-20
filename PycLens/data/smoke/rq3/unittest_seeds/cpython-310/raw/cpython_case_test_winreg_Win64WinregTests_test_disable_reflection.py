# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: Win64WinregTests_test_disable_reflection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKeyEx(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_ALL_ACCESS | KEY_WOW64_32KEY) as created_key:
            disabled = QueryReflectionKey(created_key)
            self.assertEqual(type(disabled), bool)
            self.assertFalse(disabled)
            DisableReflectionKey(created_key)
            self.assertTrue(QueryReflectionKey(created_key))
        open_fail = lambda : OpenKeyEx(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_READ | KEY_WOW64_64KEY)
        self.assertRaises(OSError, open_fail)
        with OpenKeyEx(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_READ | KEY_WOW64_32KEY) as key:
            self.assertNotEqual(key.handle, 0)
    finally:
        DeleteKeyEx(HKEY_CURRENT_USER, test_reflect_key_name, KEY_WOW64_32KEY, 0)
