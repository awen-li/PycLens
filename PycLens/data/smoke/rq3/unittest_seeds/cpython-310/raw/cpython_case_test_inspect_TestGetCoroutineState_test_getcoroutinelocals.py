# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetCoroutineState_test_getcoroutinelocals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def gencoro():
        yield
    gencoro = gencoro()

    async def func(a=None):
        b = 'spam'
        await gencoro
    coro = func()
    self.assertEqual(inspect.getcoroutinelocals(coro), {'a': None, 'gencoro': gencoro})
    coro.send(None)
    self.assertEqual(inspect.getcoroutinelocals(coro), {'a': None, 'gencoro': gencoro, 'b': 'spam'})
