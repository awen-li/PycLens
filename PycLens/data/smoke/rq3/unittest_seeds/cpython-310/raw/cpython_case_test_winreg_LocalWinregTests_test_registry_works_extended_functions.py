# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_registry_works_extended_functions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cke = lambda key, sub_key: CreateKeyEx(key, sub_key, 0, KEY_ALL_ACCESS)
    self._write_test_data(HKEY_CURRENT_USER, CreateKey=cke)
    oke = lambda key, sub_key: OpenKeyEx(key, sub_key, 0, KEY_READ)
    self._read_test_data(HKEY_CURRENT_USER, OpenKey=oke)
    self._delete_test_data(HKEY_CURRENT_USER)
