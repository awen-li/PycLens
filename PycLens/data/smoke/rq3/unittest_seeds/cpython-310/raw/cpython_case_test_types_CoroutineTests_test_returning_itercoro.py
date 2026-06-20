# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_returning_itercoro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def gen():
        yield
    gencoro = gen()

    @types.coroutine
    def foo():
        return gencoro
    self.assertIs(foo(), gencoro)
    foo = types.coroutine(foo)
    self.assertIs(foo(), gencoro)
