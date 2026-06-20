# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_keywords

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @asynccontextmanager
    async def woohoo(self, func, args, kwds):
        yield (self, func, args, kwds)
    async with woohoo(self=11, func=22, args=33, kwds=44) as target:
        self.assertEqual(target, (11, 22, 33, 44))
