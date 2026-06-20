# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_11

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def ident(val):
        return val

    async def bar():
        return 'spam'

    async def foo():
        return ident(val=await bar())

    async def foo2():
        return (await bar(), 'ham')
    self.assertEqual(run_async(foo2()), ([], ('spam', 'ham')))
