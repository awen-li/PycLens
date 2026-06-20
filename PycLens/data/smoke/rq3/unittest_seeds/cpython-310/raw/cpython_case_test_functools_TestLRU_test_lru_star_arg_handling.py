# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_lru_star_arg_handling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.lru_cache()
    def f(*args):
        return args
    self.assertEqual(f(1, 2), (1, 2))
    self.assertEqual(f((1, 2)), ((1, 2),))
