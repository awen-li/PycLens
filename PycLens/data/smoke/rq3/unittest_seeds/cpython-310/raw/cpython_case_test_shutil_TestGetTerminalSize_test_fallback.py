# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestGetTerminalSize_test_fallback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        del env['LINES']
        del env['COLUMNS']
        with support.swap_attr(sys, '__stdout__', None):
            size = shutil.get_terminal_size(fallback=(10, 20))
        self.assertEqual(size.columns, 10)
        self.assertEqual(size.lines, 20)
        with open(os.devnull, 'w', encoding='utf-8') as f, support.swap_attr(sys, '__stdout__', f):
            size = shutil.get_terminal_size(fallback=(30, 40))
        self.assertEqual(size.columns, 30)
        self.assertEqual(size.lines, 40)
