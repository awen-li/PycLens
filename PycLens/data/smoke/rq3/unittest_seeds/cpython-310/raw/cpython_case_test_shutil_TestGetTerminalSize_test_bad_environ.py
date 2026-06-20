# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestGetTerminalSize_test_bad_environ

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env['COLUMNS'] = 'xxx'
        env['LINES'] = 'yyy'
        size = shutil.get_terminal_size()
    self.assertGreaterEqual(size.columns, 0)
    self.assertGreaterEqual(size.lines, 0)
