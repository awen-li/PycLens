# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_gc_aclose_09

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    async def gen():
        nonlocal DONE
        try:
            while True:
                yield 1
        finally:
            await asyncio.sleep(0.01)
            await asyncio.sleep(0.01)
            DONE = 1

    async def run():
        g = gen()
        await g.__anext__()
        await g.__anext__()
        del g
        gc_collect()
        await asyncio.sleep(0.1)
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
