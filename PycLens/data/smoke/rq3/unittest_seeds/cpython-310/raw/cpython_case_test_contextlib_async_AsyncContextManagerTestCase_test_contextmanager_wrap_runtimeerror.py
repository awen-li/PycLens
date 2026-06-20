# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_contextmanager_wrap_runtimeerror

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @asynccontextmanager
    async def woohoo():
        try:
            yield
        except Exception as exc:
            raise RuntimeError(f'caught {exc}') from exc
    with self.assertRaises(RuntimeError):
        async with woohoo():
            1 / 0
    with self.assertRaises(StopAsyncIteration):
        async with woohoo():
            raise StopAsyncIteration
