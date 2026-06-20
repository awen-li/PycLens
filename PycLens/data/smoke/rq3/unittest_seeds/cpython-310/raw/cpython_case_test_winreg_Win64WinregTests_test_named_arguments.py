# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: Win64WinregTests_test_named_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_named_args(HKEY_CURRENT_USER, test_key_name)
    DeleteKeyEx(key=HKEY_CURRENT_USER, sub_key=test_key_name, access=KEY_ALL_ACCESS, reserved=0)
