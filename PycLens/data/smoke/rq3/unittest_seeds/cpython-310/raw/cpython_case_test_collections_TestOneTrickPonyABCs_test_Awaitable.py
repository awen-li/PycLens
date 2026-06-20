# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Awaitable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        yield

    @types.coroutine
    def coro():
        yield

    async def new_coro():
        pass

    class Bar:

        def __await__(self):
            yield

    class MinimalCoro(Coroutine):

        def send(self, value):
            return value

        def throw(self, typ, val=None, tb=None):
            super().throw(typ, val, tb)

        def __await__(self):
            yield
    self.validate_abstract_methods(Awaitable, '__await__')
    non_samples = [None, int(), gen(), object()]
    for x in non_samples:
        self.assertNotIsInstance(x, Awaitable)
        self.assertFalse(issubclass(type(x), Awaitable), repr(type(x)))
    samples = [Bar(), MinimalCoro()]
    for x in samples:
        self.assertIsInstance(x, Awaitable)
        self.assertTrue(issubclass(type(x), Awaitable))
    c = coro()
    self.assertNotIsInstance(c, Awaitable)
    c = new_coro()
    self.assertIsInstance(c, Awaitable)
    c.close()

    class CoroLike:
        pass
    Coroutine.register(CoroLike)
    self.assertTrue(isinstance(CoroLike(), Awaitable))
    self.assertTrue(issubclass(CoroLike, Awaitable))
    CoroLike = None
    support.gc_collect()
