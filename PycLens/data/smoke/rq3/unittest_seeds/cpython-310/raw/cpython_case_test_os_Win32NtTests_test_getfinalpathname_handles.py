# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: Win32NtTests_test_getfinalpathname_handles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nt = import_helper.import_module('nt')
    ctypes = import_helper.import_module('ctypes')
    import ctypes.wintypes
    kernel = ctypes.WinDLL('Kernel32.dll', use_last_error=True)
    kernel.GetCurrentProcess.restype = ctypes.wintypes.HANDLE
    kernel.GetProcessHandleCount.restype = ctypes.wintypes.BOOL
    kernel.GetProcessHandleCount.argtypes = (ctypes.wintypes.HANDLE, ctypes.wintypes.LPDWORD)
    hproc = kernel.GetCurrentProcess()
    handle_count = ctypes.wintypes.DWORD()
    ok = kernel.GetProcessHandleCount(hproc, ctypes.byref(handle_count))
    self.assertEqual(1, ok)
    before_count = handle_count.value
    filenames = ['\\\\?\\C:', '\\\\?\\NUL', '\\\\?\\CONIN', __file__]
    for _ in range(10):
        for name in filenames:
            try:
                nt._getfinalpathname(name)
            except Exception:
                pass
            try:
                os.stat(name)
            except Exception:
                pass
    ok = kernel.GetProcessHandleCount(hproc, ctypes.byref(handle_count))
    self.assertEqual(1, ok)
    handle_delta = handle_count.value - before_count
    self.assertEqual(0, handle_delta)
