# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_03

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    loop = self.loop

    class Gen:

        async def __aiter__(self):
            yield 1
            await asyncio.sleep(0.01)
            yield 2
    res = loop.run_until_complete(self.to_list(Gen()))
    self.assertEqual(res, [1, 2])
