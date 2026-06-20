# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_recursionlimit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, sys.getrecursionlimit, 42)
    oldlimit = sys.getrecursionlimit()
    self.assertRaises(TypeError, sys.setrecursionlimit)
    self.assertRaises(ValueError, sys.setrecursionlimit, -42)
    sys.setrecursionlimit(10000)
    self.assertEqual(sys.getrecursionlimit(), 10000)
    sys.setrecursionlimit(oldlimit)
