# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_read_string_containing_null

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as ck:
            self.assertNotEqual(ck.handle, 0)
            test_val = 'A string\x00 with a null'
            SetValueEx(ck, 'test_name', 0, REG_SZ, test_val)
            (ret_val, ret_type) = QueryValueEx(ck, 'test_name')
            self.assertEqual(ret_type, REG_SZ)
            self.assertEqual(ret_val, 'A string')
    finally:
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
