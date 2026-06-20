# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestOneTrickPonyABCs_test_Coroutine

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
    self.validate_abstract_methods(Coroutine, '__await__', 'send', 'throw')
    non_samples = [None, int(), gen(), object(), Bar()]
    for x in non_samples:
        self.assertNotIsInstance(x, Coroutine)
        self.assertFalse(issubclass(type(x), Coroutine), repr(type(x)))
    samples = [MinimalCoro()]
    for x in samples:
        self.assertIsInstance(x, Awaitable)
        self.assertTrue(issubclass(type(x), Awaitable))
    c = coro()
    self.assertNotIsInstance(c, Coroutine)
    c = new_coro()
    self.assertIsInstance(c, Coroutine)
    c.close()

    class CoroLike:

        def send(self, value):
            pass

        def throw(self, typ, val=None, tb=None):
            pass

        def close(self):
            pass

        def __await__(self):
            pass
    self.assertTrue(isinstance(CoroLike(), Coroutine))
    self.assertTrue(issubclass(CoroLike, Coroutine))

    class CoroLike:

        def send(self, value):
            pass

        def close(self):
            pass

        def __await__(self):
            pass
    self.assertFalse(isinstance(CoroLike(), Coroutine))
    self.assertFalse(issubclass(CoroLike, Coroutine))
