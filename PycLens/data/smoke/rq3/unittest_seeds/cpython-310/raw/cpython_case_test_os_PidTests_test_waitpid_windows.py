# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: PidTests_test_waitpid_windows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    STATUS_CONTROL_C_EXIT = 3221225786
    code = f'import _winapi; _winapi.ExitProcess({STATUS_CONTROL_C_EXIT})'
    self.check_waitpid(code, exitcode=STATUS_CONTROL_C_EXIT)
