# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestGetTerminalSize_test_does_not_crash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    size = shutil.get_terminal_size()
    self.assertGreaterEqual(size.columns, 0)
    self.assertGreaterEqual(size.lines, 0)
