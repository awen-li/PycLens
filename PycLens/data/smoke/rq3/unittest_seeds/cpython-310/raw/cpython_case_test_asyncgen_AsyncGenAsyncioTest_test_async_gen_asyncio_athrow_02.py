# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_athrow_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    class FooEr(Exception):
        pass

    async def sleep_n_crash(delay):
        fut = asyncio.ensure_future(asyncio.sleep(delay), loop=self.loop)
        self.loop.call_later(delay / 2, lambda : fut.cancel())
        return await fut

    async def gen():
        nonlocal DONE
        try:
            await asyncio.sleep(0.01)
            try:
                v = (yield 1)
            except FooEr:
                await sleep_n_crash(0.01)
            yield (v * 2)
            await asyncio.sleep(0.01)
        finally:
            await asyncio.sleep(0.01)
            await asyncio.sleep(0.01)
            DONE = 1

    async def run():
        g = gen()
        v = await g.asend(None)
        self.assertEqual(v, 1)
        try:
            await g.athrow(FooEr)
        except asyncio.CancelledError:
            self.assertEqual(DONE, 1)
            raise
        else:
            self.fail('CancelledError was not raised')
    with self.assertRaises(asyncio.CancelledError):
        self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
