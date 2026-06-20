# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_refcount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global n
    self.assertRaises(TypeError, sys.getrefcount)
    c = sys.getrefcount(None)
    n = None
    self.assertEqual(sys.getrefcount(None), c + 1)
    del n
    self.assertEqual(sys.getrefcount(None), c)
    if hasattr(sys, 'gettotalrefcount'):
        self.assertIsInstance(sys.gettotalrefcount(), int)
