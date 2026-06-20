# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_athrow_stopiteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        try:
            yield 1
        except ZeroDivisionError:
            yield StopIteration(2)

    async def run():
        g = gen()
        v = await g.asend(None)
        self.assertEqual(v, 1)
        v = await g.athrow(ZeroDivisionError)
        self.assertIsInstance(v, StopIteration)
        self.assertEqual(v.value, 2)
        with self.assertRaises(StopAsyncIteration):
            await g.asend(None)
    self.loop.run_until_complete(run())
