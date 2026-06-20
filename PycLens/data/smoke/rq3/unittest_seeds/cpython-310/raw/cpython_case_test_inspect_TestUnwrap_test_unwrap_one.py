# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestUnwrap_test_unwrap_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(a, b):
        return a + b
    wrapper = functools.lru_cache(maxsize=20)(func)
    self.assertIs(inspect.unwrap(wrapper), func)
