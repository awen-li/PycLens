# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_switchinterval

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, sys.setswitchinterval)
    self.assertRaises(TypeError, sys.setswitchinterval, 'a')
    self.assertRaises(ValueError, sys.setswitchinterval, -1.0)
    self.assertRaises(ValueError, sys.setswitchinterval, 0.0)
    orig = sys.getswitchinterval()
    self.assertTrue(orig < 0.5, orig)
    try:
        for n in (1e-05, 0.05, 3.0, orig):
            sys.setswitchinterval(n)
            self.assertAlmostEqual(sys.getswitchinterval(), n)
    finally:
        sys.setswitchinterval(orig)
