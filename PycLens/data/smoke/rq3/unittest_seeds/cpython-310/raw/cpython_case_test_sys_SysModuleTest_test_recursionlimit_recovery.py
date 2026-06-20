# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_recursionlimit_recovery

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if hasattr(sys, 'gettrace') and sys.gettrace():
        self.skipTest('fatal error if run with a trace function')
    oldlimit = sys.getrecursionlimit()

    def f():
        f()
    try:
        for depth in (50, 75, 100, 250, 1000):
            try:
                sys.setrecursionlimit(depth)
            except RecursionError:
                continue
            with self.assertRaises(RecursionError):
                f()
            with self.assertRaises(RecursionError):
                f()
    finally:
        sys.setrecursionlimit(oldlimit)
