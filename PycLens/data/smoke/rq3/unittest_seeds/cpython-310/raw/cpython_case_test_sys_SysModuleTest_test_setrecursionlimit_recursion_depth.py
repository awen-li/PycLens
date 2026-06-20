# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_setrecursionlimit_recursion_depth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testinternalcapi import get_recursion_depth

    def set_recursion_limit_at_depth(depth, limit):
        recursion_depth = get_recursion_depth()
        if recursion_depth >= depth:
            with self.assertRaises(RecursionError) as cm:
                sys.setrecursionlimit(limit)
            self.assertRegex(str(cm.exception), 'cannot set the recursion limit to [0-9]+ at the recursion depth [0-9]+: the limit is too low')
        else:
            set_recursion_limit_at_depth(depth, limit)
    oldlimit = sys.getrecursionlimit()
    try:
        sys.setrecursionlimit(1000)
        for limit in (10, 25, 50, 75, 100, 150, 200):
            set_recursion_limit_at_depth(limit, limit)
    finally:
        sys.setrecursionlimit(oldlimit)
