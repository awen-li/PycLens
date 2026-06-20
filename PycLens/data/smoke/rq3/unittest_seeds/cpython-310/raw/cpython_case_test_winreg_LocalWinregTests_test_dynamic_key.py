# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winreg.py
# case: LocalWinregTests_test_dynamic_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        EnumValue(HKEY_PERFORMANCE_DATA, 0)
    except OSError as e:
        if e.errno in (errno.EPERM, errno.EACCES):
            self.skipTest('access denied to registry key (are you running in a non-interactive session?)')
        raise
    QueryValueEx(HKEY_PERFORMANCE_DATA, '')
