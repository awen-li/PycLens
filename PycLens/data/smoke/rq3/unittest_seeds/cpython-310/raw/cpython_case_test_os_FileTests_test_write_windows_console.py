# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: FileTests_test_write_windows_console

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "print('x' * 100000)"
    self.write_windows_console(sys.executable, '-c', code)
    self.write_windows_console(sys.executable, '-u', '-c', code)
