# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_asend_03

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    async def sleep_n_crash(delay):
        fut = asyncio.ensure_future(asyncio.sleep(delay), loop=self.loop)
        self.loop.call_later(delay / 2, lambda : fut.cancel())
        return await fut

    async def gen():
        nonlocal DONE
        try:
            await asyncio.sleep(0.01)
            v = (yield 1)
            await sleep_n_crash(0.01)
            DONE += 1000
            yield (v * 2)
        finally:
            await asyncio.sleep(0.01)
            await asyncio.sleep(0.01)
            DONE = 1

    async def run():
        g = gen()
        v = await g.asend(None)
        self.assertEqual(v, 1)
        await g.asend(100)
    with self.assertRaises(asyncio.CancelledError):
        self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
