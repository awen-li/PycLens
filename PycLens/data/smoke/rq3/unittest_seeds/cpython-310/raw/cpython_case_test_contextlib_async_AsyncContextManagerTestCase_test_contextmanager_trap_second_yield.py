# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_contextmanager_trap_second_yield

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @asynccontextmanager
    async def whoo():
        yield
        yield
    ctx = whoo()
    await ctx.__aenter__()
    with self.assertRaises(RuntimeError):
        await ctx.__aexit__(None, None, None)
