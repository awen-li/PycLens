# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_long_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'x' * 256
    try:
        with CreateKey(HKEY_CURRENT_USER, test_key_name) as key:
            SetValue(key, name, REG_SZ, 'x')
            (num_subkeys, num_values, t) = QueryInfoKey(key)
            EnumKey(key, 0)
    finally:
        DeleteKey(HKEY_CURRENT_USER, '\\'.join((test_key_name, name)))
        DeleteKey(HKEY_CURRENT_USER, test_key_name)
