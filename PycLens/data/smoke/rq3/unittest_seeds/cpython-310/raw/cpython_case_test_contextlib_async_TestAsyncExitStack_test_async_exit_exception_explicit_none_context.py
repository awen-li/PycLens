# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAsyncExitStack_test_async_exit_exception_explicit_none_context

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyException(Exception):
        pass

    @asynccontextmanager
    async def my_cm():
        try:
            yield
        except BaseException:
            exc = MyException()
            try:
                raise exc
            finally:
                exc.__context__ = None

    @asynccontextmanager
    async def my_cm_with_exit_stack():
        async with self.exit_stack() as stack:
            await stack.enter_async_context(my_cm())
            yield stack
    for cm in (my_cm, my_cm_with_exit_stack):
        with self.subTest():
            try:
                async with cm():
                    raise IndexError()
            except MyException as exc:
                self.assertIsNone(exc.__context__)
            else:
                self.fail('Expected IndexError, but no exception was raised')
