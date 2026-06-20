# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: Win64WinregTests_test_reflection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKeyEx(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_ALL_ACCESS | KEY_WOW64_32KEY) as created_key:
            self.assertNotEqual(created_key.handle, 0)
            with OpenKey(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_ALL_ACCESS | KEY_WOW64_32KEY) as key:
                self.assertNotEqual(key.handle, 0)
            SetValueEx(created_key, '', 0, REG_SZ, '32KEY')
            open_fail = lambda : OpenKey(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_READ | KEY_WOW64_64KEY)
            self.assertRaises(OSError, open_fail)
        with OpenKey(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_ALL_ACCESS | KEY_WOW64_64KEY) as key:
            self.assertNotEqual(key.handle, 0)
            self.assertEqual('32KEY', QueryValue(key, ''))
            SetValueEx(key, '', 0, REG_SZ, '64KEY')
        with OpenKey(HKEY_CURRENT_USER, test_reflect_key_name, 0, KEY_READ | KEY_WOW64_32KEY) as key:
            self.assertEqual('64KEY', QueryValue(key, ''))
    finally:
        DeleteKeyEx(HKEY_CURRENT_USER, test_reflect_key_name, KEY_WOW64_32KEY, 0)
