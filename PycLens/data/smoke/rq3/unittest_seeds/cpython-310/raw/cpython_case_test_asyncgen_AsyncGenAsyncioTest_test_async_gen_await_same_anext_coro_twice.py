# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_await_same_anext_coro_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def async_iterate():
        yield 1
        yield 2

    async def run():
        it = async_iterate()
        nxt = it.__anext__()
        await nxt
        with self.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited __anext__\\(\\)/asend\\(\\)'):
            await nxt
        await it.aclose()
    self.loop.run_until_complete(run())
