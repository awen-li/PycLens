# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_setvalueex_value_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as ck:
            self.assertNotEqual(ck.handle, 0)
            SetValueEx(ck, 'test_name', None, REG_DWORD, 2147483648)
    finally:
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
