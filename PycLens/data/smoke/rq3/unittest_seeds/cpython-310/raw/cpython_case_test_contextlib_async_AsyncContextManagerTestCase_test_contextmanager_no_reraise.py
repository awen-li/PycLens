# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_contextmanager_no_reraise

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @asynccontextmanager
    async def whee():
        yield
    ctx = whee()
    await ctx.__aenter__()
    self.assertFalse(await ctx.__aexit__(TypeError, TypeError('foo'), None))
