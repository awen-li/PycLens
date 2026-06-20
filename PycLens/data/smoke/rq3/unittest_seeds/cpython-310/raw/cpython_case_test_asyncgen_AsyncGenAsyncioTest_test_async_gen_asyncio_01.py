# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1
        await asyncio.sleep(0.01)
        yield 2
        await asyncio.sleep(0.01)
        return
        yield 3
    res = self.loop.run_until_complete(self.to_list(gen()))
    self.assertEqual(res, [1, 2])
