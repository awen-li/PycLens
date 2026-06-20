# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_reentrancy_with_len

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_len = builtins.len
    try:
        builtins.len = self.module.lru_cache(4)(len)
        for i in [0, 0, 1, 2, 3, 3, 4, 5, 6, 1, 7, 2, 1]:
            self.assertEqual(len('abcdefghijklmn'[:i]), i)
    finally:
        builtins.len = old_len
