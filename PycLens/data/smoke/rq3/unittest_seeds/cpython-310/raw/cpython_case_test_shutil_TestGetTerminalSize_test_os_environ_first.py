# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestGetTerminalSize_test_os_environ_first

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env['COLUMNS'] = '777'
        del env['LINES']
        size = shutil.get_terminal_size()
    self.assertEqual(size.columns, 777)
    with os_helper.EnvironmentVarGuard() as env:
        del env['COLUMNS']
        env['LINES'] = '888'
        size = shutil.get_terminal_size()
    self.assertEqual(size.lines, 888)
