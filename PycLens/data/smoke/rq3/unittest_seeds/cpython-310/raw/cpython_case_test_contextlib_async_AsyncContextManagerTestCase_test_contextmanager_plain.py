# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_contextmanager_plain

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = []

    @asynccontextmanager
    async def woohoo():
        state.append(1)
        yield 42
        state.append(999)
    async with woohoo() as x:
        self.assertEqual(state, [1])
        self.assertEqual(x, 42)
        state.append(x)
    self.assertEqual(state, [1, 42, 999])
