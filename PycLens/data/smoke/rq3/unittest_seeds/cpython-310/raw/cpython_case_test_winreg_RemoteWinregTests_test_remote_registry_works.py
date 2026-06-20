# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: RemoteWinregTests_test_remote_registry_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    remote_key = ConnectRegistry(REMOTE_NAME, HKEY_CURRENT_USER)
    self._test_all(remote_key)
