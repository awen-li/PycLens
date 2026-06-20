# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_athrow_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    class FooEr(Exception):
        pass

    def sgen():
        try:
            v = (yield 1)
        except FooEr:
            v = 1000
        yield (v * 2)
    sg = sgen()
    v = sg.send(None)
    self.assertEqual(v, 1)
    v = sg.throw(FooEr)
    self.assertEqual(v, 2000)
    with self.assertRaises(StopIteration):
        sg.send(None)

    async def gen():
        nonlocal DONE
        try:
            await asyncio.sleep(0.01)
            try:
                v = (yield 1)
            except FooEr:
                v = 1000
                await asyncio.sleep(0.01)
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
        v = await g.athrow(FooEr)
        self.assertEqual(v, 2000)
        with self.assertRaises(StopAsyncIteration):
            await g.asend(None)
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 1)
