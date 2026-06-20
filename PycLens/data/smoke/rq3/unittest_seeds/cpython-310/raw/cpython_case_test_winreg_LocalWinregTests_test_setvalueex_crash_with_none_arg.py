# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_setvalueex_crash_with_none_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as ck:
            self.assertNotEqual(ck.handle, 0)
            test_val = None
            SetValueEx(ck, 'test_name', 0, REG_BINARY, test_val)
            (ret_val, ret_type) = QueryValueEx(ck, 'test_name')
            self.assertEqual(ret_type, REG_BINARY)
            self.assertEqual(ret_val, test_val)
    finally:
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
