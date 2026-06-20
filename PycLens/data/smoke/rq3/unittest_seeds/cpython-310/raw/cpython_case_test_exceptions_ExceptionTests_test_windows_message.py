# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_windows_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctypes = import_module('ctypes')
    code = 3765269347
    with self.assertRaisesRegex(OSError, 'Windows Error 0x%x' % code):
        ctypes.pythonapi.PyErr_SetFromWindowsErr(code)
