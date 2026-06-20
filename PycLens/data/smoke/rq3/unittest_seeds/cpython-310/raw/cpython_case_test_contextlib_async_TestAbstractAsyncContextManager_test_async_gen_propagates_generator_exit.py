# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAbstractAsyncContextManager_test_async_gen_propagates_generator_exit

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @asynccontextmanager
    async def ctx():
        yield

    async def gen():
        async with ctx():
            yield 11
    ret = []
    exc = ValueError(22)
    with self.assertRaises(ValueError):
        async with ctx():
            async for val in gen():
                ret.append(val)
                raise exc
    self.assertEqual(ret, [11])
