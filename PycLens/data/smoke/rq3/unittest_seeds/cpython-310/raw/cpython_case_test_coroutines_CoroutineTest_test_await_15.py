# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_15

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def nop():
        yield

    async def coroutine():
        await nop()

    async def waiter(coro):
        await coro
    coro = coroutine()
    coro.send(None)
    with self.assertRaisesRegex(RuntimeError, 'coroutine is being awaited already'):
        waiter(coro).send(None)
