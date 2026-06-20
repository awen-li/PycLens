# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_setvalueex_negative_one_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as ck:
            with self.assertRaises(OverflowError):
                SetValueEx(ck, 'test_name_dword', None, REG_DWORD, -1)
                SetValueEx(ck, 'test_name_qword', None, REG_QWORD, -1)
            self.assertRaises(FileNotFoundError, QueryValueEx, ck, 'test_name_dword')
            self.assertRaises(FileNotFoundError, QueryValueEx, ck, 'test_name_qword')
    finally:
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
