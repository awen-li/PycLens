# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_athrow_03

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    DONE = 0

    def foo():
        try:
            yield
        except:
            pass
    g = foo()
    g.send(None)
    with self.assertRaises(StopIteration):
        g.throw(ValueError)

    async def gen():
        nonlocal DONE
        try:
            yield
        except:
            pass
        DONE = 1

    async def run():
        nonlocal DONE
        g = gen()
        await g.asend(None)
        with self.assertRaises(StopAsyncIteration):
            await g.athrow(ValueError)
        DONE += 10
    self.loop.run_until_complete(run())
    self.assertEqual(DONE, 11)
