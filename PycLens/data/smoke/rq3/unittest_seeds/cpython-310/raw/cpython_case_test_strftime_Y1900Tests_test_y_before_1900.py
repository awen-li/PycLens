# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strftime.py
# case: Y1900Tests_test_y_before_1900

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = (1899, 1, 1, 0, 0, 0, 0, 0, 0)
    if sys.platform == 'win32' or sys.platform.startswith(('aix', 'sunos', 'solaris')):
        with self.assertRaises(ValueError):
            time.strftime('%y', t)
    else:
        self.assertEqual(time.strftime('%y', t), '99')
