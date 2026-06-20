# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_expression_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def wrap(n):
        await asyncio.sleep(0.01)
        return n

    def make_arange(n):
        return (i * 2 for i in range(n) if await wrap(i))

    async def run():
        return [i async for i in make_arange(10)]
    res = self.loop.run_until_complete(run())
    self.assertEqual(res, [i * 2 for i in range(1, 10)])
