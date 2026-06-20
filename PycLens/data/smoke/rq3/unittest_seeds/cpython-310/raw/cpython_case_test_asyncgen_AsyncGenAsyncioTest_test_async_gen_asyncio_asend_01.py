# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_asend_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    def sgen():
        v = (yield 1)
        yield (v * 2)
    sg = sgen()
    v = sg.send(None)
    self.assertEqual(v, 1)
    v = sg.send(100)
    self.assertEqual(v, 200)

    async def gen():
        nonlocal DONE
        try:
            await asyncio.sleep(0.01)
            v = (yield 1)
            await asyncio.sleep(0.01)
            yield (v * 2)
            await asyncio.sleep(0.01)
            return
        finally:
            await asyncio.sleep(0.01)
            await asyncio.sleep(0.01)
            DONE = 1

    async def run():
        g = gen()
        v = await g.asend(None)
        self.assertEqual(v, 1)
        v = await g.asend(100)
        self.assertEqual(v, 200)
        with self.assertRaises(StopAsyncIteration):
            await g.asend(None)
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
