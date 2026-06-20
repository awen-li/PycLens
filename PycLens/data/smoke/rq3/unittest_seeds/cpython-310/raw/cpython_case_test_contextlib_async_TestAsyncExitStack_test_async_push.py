# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAsyncExitStack_test_async_push

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc_raised = ZeroDivisionError

    async def _expect_exc(exc_type, exc, exc_tb):
        self.assertIs(exc_type, exc_raised)

    async def _suppress_exc(*exc_details):
        return True

    async def _expect_ok(exc_type, exc, exc_tb):
        self.assertIsNone(exc_type)
        self.assertIsNone(exc)
        self.assertIsNone(exc_tb)

    class ExitCM(object):

        def __init__(self, check_exc):
            self.check_exc = check_exc

        async def __aenter__(self):
            self.fail('Should not be called!')

        async def __aexit__(self, *exc_details):
            await self.check_exc(*exc_details)
    async with self.exit_stack() as stack:
        stack.push_async_exit(_expect_ok)
        self.assertIs(stack._exit_callbacks[-1][1], _expect_ok)
        cm = ExitCM(_expect_ok)
        stack.push_async_exit(cm)
        self.assertIs(stack._exit_callbacks[-1][1].__self__, cm)
        stack.push_async_exit(_suppress_exc)
        self.assertIs(stack._exit_callbacks[-1][1], _suppress_exc)
        cm = ExitCM(_expect_exc)
        stack.push_async_exit(cm)
        self.assertIs(stack._exit_callbacks[-1][1].__self__, cm)
        stack.push_async_exit(_expect_exc)
        self.assertIs(stack._exit_callbacks[-1][1], _expect_exc)
        stack.push_async_exit(_expect_exc)
        self.assertIs(stack._exit_callbacks[-1][1], _expect_exc)
        1 / 0
