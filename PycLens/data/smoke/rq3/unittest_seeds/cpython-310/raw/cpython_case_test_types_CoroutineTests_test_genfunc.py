# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_genfunc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        yield
    self.assertIs(types.coroutine(gen), gen)
    self.assertIs(types.coroutine(types.coroutine(gen)), gen)
    self.assertTrue(gen.__code__.co_flags & inspect.CO_ITERABLE_COROUTINE)
    self.assertFalse(gen.__code__.co_flags & inspect.CO_COROUTINE)
    g = gen()
    self.assertTrue(g.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)
    self.assertFalse(g.gi_code.co_flags & inspect.CO_COROUTINE)
    self.assertIs(types.coroutine(gen), gen)
