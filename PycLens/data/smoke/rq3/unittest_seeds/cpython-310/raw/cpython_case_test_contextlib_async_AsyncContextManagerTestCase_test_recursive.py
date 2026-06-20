# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_recursive

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    depth = 0
    ncols = 0

    @asynccontextmanager
    async def woohoo():
        nonlocal ncols
        ncols += 1
        nonlocal depth
        before = depth
        depth += 1
        yield
        depth -= 1
        self.assertEqual(depth, before)

    @woohoo()
    async def recursive():
        if depth < 10:
            await recursive()
    await recursive()
    self.assertEqual(ncols, 10)
    self.assertEqual(depth, 0)
