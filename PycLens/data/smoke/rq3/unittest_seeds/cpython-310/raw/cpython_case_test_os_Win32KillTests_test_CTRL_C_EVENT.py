# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32KillTests_test_CTRL_C_EVENT

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from ctypes import wintypes
    import ctypes
    NULL = ctypes.POINTER(ctypes.c_int)()
    SetConsoleCtrlHandler = ctypes.windll.kernel32.SetConsoleCtrlHandler
    SetConsoleCtrlHandler.argtypes = (ctypes.POINTER(ctypes.c_int), wintypes.BOOL)
    SetConsoleCtrlHandler.restype = wintypes.BOOL
    SetConsoleCtrlHandler(NULL, 0)
    self._kill_with_event(signal.CTRL_C_EVENT, 'CTRL_C_EVENT')
