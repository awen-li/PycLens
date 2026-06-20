# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: EnvironTests_test_putenv_unsetenv_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in ('', '=name', 'na=me', 'name=', 'name\x00', 'na\x00me'):
        self.assertRaises((OSError, ValueError), os.putenv, name, 'value')
        self.assertRaises((OSError, ValueError), os.unsetenv, name)
    if sys.platform == 'win32':
        longstr = 'x' * 32768
        self.assertRaises(ValueError, os.putenv, longstr, '1')
        self.assertRaises(ValueError, os.putenv, 'X', longstr)
        self.assertRaises(ValueError, os.unsetenv, longstr)
