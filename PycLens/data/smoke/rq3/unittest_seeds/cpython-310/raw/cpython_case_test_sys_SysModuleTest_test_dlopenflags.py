# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_dlopenflags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(hasattr(sys, 'getdlopenflags'))
    self.assertRaises(TypeError, sys.getdlopenflags, 42)
    oldflags = sys.getdlopenflags()
    self.assertRaises(TypeError, sys.setdlopenflags)
    sys.setdlopenflags(oldflags + 1)
    self.assertEqual(sys.getdlopenflags(), oldflags + 1)
    sys.setdlopenflags(oldflags)
