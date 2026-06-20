# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 1
        await asyncio.sleep(0.01)
        yield 2
        1 / 0
        yield 3
    with self.assertRaises(ZeroDivisionError):
        self.loop.run_until_complete(self.to_list(gen()))
