# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_nonexistent_remote_registry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    connect = lambda : ConnectRegistry('abcdefghijkl', HKEY_CURRENT_USER)
    self.assertRaises(OSError, connect)
