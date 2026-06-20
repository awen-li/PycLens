# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AsyncContextManagerTestCase_test_contextmanager_except_stopiter

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @asynccontextmanager
    async def woohoo():
        yield

    class StopIterationSubclass(StopIteration):
        pass

    class StopAsyncIterationSubclass(StopAsyncIteration):
        pass
    for stop_exc in (StopIteration('spam'), StopAsyncIteration('ham'), StopIterationSubclass('spam'), StopAsyncIterationSubclass('spam')):
        with self.subTest(type=type(stop_exc)):
            try:
                async with woohoo():
                    raise stop_exc
            except Exception as ex:
                self.assertIs(ex, stop_exc)
            else:
                self.fail(f'{stop_exc} was suppressed')
