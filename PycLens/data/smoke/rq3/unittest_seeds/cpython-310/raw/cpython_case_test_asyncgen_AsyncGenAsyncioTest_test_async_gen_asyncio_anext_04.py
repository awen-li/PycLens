# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_async_gen_asyncio_anext_04

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        yield 1
        await asyncio.sleep(0.01)
        try:
            yield 2
            yield 3
        except ZeroDivisionError:
            yield 1000
        await asyncio.sleep(0.01)
        yield 4

    async def run1():
        it = foo().__aiter__()
        self.assertEqual(await it.__anext__(), 1)
        self.assertEqual(await it.__anext__(), 2)
        self.assertEqual(await it.__anext__(), 3)
        self.assertEqual(await it.__anext__(), 4)
        with self.assertRaises(StopAsyncIteration):
            await it.__anext__()
        with self.assertRaises(StopAsyncIteration):
            await it.__anext__()

    async def run2():
        it = foo().__aiter__()
        self.assertEqual(await it.__anext__(), 1)
        self.assertEqual(await it.__anext__(), 2)
        try:
            it.__anext__().throw(ZeroDivisionError)
        except StopIteration as ex:
            self.assertEqual(ex.args[0], 1000)
        else:
            self.fail('StopIteration was not raised')
        self.assertEqual(await it.__anext__(), 4)
        with self.assertRaises(StopAsyncIteration):
            await it.__anext__()
    self.loop.run_until_complete(run1())
    self.loop.run_until_complete(run2())
