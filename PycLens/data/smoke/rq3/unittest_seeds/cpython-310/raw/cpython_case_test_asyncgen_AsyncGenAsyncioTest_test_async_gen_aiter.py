# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_aiter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1
        yield 2
    g = gen()

    async def consume():
        return [i async for i in aiter(g)]
    res = self.loop.run_until_complete(consume())
    self.assertEqual(res, [1, 2])
