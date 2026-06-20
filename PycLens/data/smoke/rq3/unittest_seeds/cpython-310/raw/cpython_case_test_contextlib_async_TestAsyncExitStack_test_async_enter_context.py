# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: TestAsyncExitStack_test_async_enter_context

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestCM(object):

        async def __aenter__(self):
            result.append(1)

        async def __aexit__(self, *exc_details):
            result.append(3)
    result = []
    cm = TestCM()
    async with AsyncExitStack() as stack:

        @stack.push_async_callback
        async def _exit():
            result.append(4)
        self.assertIsNotNone(_exit)
        await stack.enter_async_context(cm)
        self.assertIs(stack._exit_callbacks[-1][1].__self__, cm)
        result.append(2)
    self.assertEqual(result, [1, 2, 3, 4])
