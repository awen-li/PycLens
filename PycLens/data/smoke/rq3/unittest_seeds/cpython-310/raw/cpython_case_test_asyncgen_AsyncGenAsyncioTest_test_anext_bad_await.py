# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest_test_anext_bad_await

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def bad_awaitable():

        class BadAwaitable:

            def __await__(self):
                return 42

        class MyAsyncIter:

            def __aiter__(self):
                return self

            def __anext__(self):
                return BadAwaitable()
        regex = '__await__.*iterator'
        awaitable = anext(MyAsyncIter(), 'default')
        with self.assertRaisesRegex(TypeError, regex):
            await awaitable
        awaitable = anext(MyAsyncIter())
        with self.assertRaisesRegex(TypeError, regex):
            await awaitable
        return 'completed'
    result = self.loop.run_until_complete(bad_awaitable())
    self.assertEqual(result, 'completed')
