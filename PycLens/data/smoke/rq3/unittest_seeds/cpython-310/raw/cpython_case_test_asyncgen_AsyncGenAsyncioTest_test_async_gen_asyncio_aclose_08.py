# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_aclose_08

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0
    fut = asyncio.Future(loop=self.loop)

    async def foo():
        nonlocal DONE
        try:
            yield 1
            await fut
            DONE += 1000
            yield 2
        finally:
            await asyncio.sleep(0.01)
            await asyncio.sleep(0.01)
            DONE += 1
        DONE += 1000

    async def run():
        gen = foo()
        it = gen.__aiter__()
        self.assertEqual(await it.__anext__(), 1)
        await gen.aclose()
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
    fut.cancel()
    self.loop.run_until_complete(asyncio.sleep(0.01))
