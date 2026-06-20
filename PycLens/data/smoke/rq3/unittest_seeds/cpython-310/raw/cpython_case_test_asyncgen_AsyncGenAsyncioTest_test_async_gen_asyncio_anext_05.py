# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_anext_05

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        v = (yield 1)
        v = (yield v)
        yield (v * 100)

    async def run():
        it = foo().__aiter__()
        try:
            it.__anext__().send(None)
        except StopIteration as ex:
            self.assertEqual(ex.args[0], 1)
        else:
            self.fail('StopIteration was not raised')
        try:
            it.__anext__().send(10)
        except StopIteration as ex:
            self.assertEqual(ex.args[0], 10)
        else:
            self.fail('StopIteration was not raised')
        try:
            it.__anext__().send(12)
        except StopIteration as ex:
            self.assertEqual(ex.args[0], 1200)
        else:
            self.fail('StopIteration was not raised')
        with self.assertRaises(StopAsyncIteration):
            await it.__anext__()
    self.loop.run_until_complete(run())
