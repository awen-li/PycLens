# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_aclose_12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    async def target():
        await asyncio.sleep(0.01)
        1 / 0

    async def foo():
        nonlocal DONE
        task = asyncio.create_task(target())
        try:
            yield 1
        finally:
            try:
                await task
            except ZeroDivisionError:
                DONE = 1

    async def run():
        gen = foo()
        it = gen.__aiter__()
        await it.__anext__()
        await gen.aclose()
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
