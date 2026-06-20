# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_uname_asdict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = platform.uname()._asdict()
    self.assertEqual(len(res), 6)
    self.assertIn('processor', res)
