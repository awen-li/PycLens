# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_anext_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        try:
            yield (1,)
        except ZeroDivisionError:
            yield (2,)

    async def run():
        it = foo().__aiter__()
        self.assertEqual(await it.__anext__(), (1,))
        with self.assertRaises(StopIteration) as cm:
            it.__anext__().throw(ZeroDivisionError)
        self.assertEqual(cm.exception.args[0], (2,))
        with self.assertRaises(StopAsyncIteration):
            await it.__anext__()
    self.loop.run_until_complete(run())
