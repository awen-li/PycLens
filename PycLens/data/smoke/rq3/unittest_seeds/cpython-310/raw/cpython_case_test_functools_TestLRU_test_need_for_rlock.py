# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_need_for_rlock

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @self.module.lru_cache(maxsize=10)
    def test_func(x):
        """Used to demonstrate a reentrant lru_cache call within a single thread"""
        return x

    class DoubleEq:
        """Demonstrate a reentrant lru_cache call within a single thread"""

        def __init__(self, x):
            self.x = x

        def __hash__(self):
            return self.x

        def __eq__(self, other):
            if self.x == 2:
                test_func(DoubleEq(1))
            return self.x == other.x
    test_func(DoubleEq(1))
    test_func(DoubleEq(2))
    self.assertEqual(test_func(DoubleEq(2)), DoubleEq(2))
