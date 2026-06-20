# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_contextmanager_finally

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = []

    @asynccontextmanager
    async def woohoo():
        state.append(1)
        try:
            yield 42
        finally:
            state.append(999)
    with self.assertRaises(ZeroDivisionError):
        async with woohoo() as x:
            self.assertEqual(state, [1])
            self.assertEqual(x, 42)
            state.append(x)
            raise ZeroDivisionError()
    self.assertEqual(state, [1, 42, 999])
