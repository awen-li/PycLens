# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_anext_stopiteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        try:
            yield StopIteration(1)
        except ZeroDivisionError:
            yield StopIteration(3)

    async def run():
        it = foo().__aiter__()
        v = await it.__anext__()
        self.assertIsInstance(v, StopIteration)
        self.assertEqual(v.value, 1)
        with self.assertRaises(StopIteration) as cm:
            it.__anext__().throw(ZeroDivisionError)
        v = cm.exception.args[0]
        self.assertIsInstance(v, StopIteration)
        self.assertEqual(v.value, 3)
        with self.assertRaises(StopAsyncIteration):
            await it.__anext__()
    self.loop.run_until_complete(run())
