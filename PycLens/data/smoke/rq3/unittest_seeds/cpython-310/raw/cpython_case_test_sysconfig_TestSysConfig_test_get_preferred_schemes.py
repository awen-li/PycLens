# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sysconfig.py
# case: TestSysConfig_test_get_preferred_schemes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_schemes = {'prefix', 'home', 'user'}
    os.name = 'nt'
    schemes = _get_preferred_schemes()
    self.assertIsInstance(schemes, dict)
    self.assertEqual(set(schemes), expected_schemes)
    os.name = 'posix'
    schemes = _get_preferred_schemes()
    self.assertIsInstance(schemes, dict)
    self.assertEqual(set(schemes), expected_schemes)
    os.name = 'posix'
    sys.platform = 'darwin'
    sys._framework = True
    self.assertIsInstance(schemes, dict)
    self.assertEqual(set(schemes), expected_schemes)
