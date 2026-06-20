# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestGetTerminalSize_test_stty_match

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        size = subprocess.check_output(['stty', 'size']).decode().split()
    except (FileNotFoundError, PermissionError, subprocess.CalledProcessError):
        self.skipTest('stty invocation failed')
    expected = (int(size[1]), int(size[0]))
    with os_helper.EnvironmentVarGuard() as env:
        del env['LINES']
        del env['COLUMNS']
        actual = shutil.get_terminal_size()
    self.assertEqual(expected, actual)
