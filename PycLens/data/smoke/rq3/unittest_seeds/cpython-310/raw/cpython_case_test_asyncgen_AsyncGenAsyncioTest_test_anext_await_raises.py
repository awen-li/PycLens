# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_anext_await_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class RaisingAwaitable:

        def __await__(self):
            raise ZeroDivisionError()
            yield

    class WithRaisingAwaitableAnext:

        def __aiter__(self):
            return self

        def __anext__(self):
            return RaisingAwaitable()

    async def do_test():
        awaitable = anext(WithRaisingAwaitableAnext())
        with self.assertRaises(ZeroDivisionError):
            await awaitable
        awaitable = anext(WithRaisingAwaitableAnext(), 'default')
        with self.assertRaises(ZeroDivisionError):
            await awaitable
        return 'completed'
    result = self.loop.run_until_complete(do_test())
    self.assertEqual(result, 'completed')
