# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_9

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def wrap():
        return bar

    async def bar():
        return 42

    async def foo():
        db = {'b': lambda : wrap}

        class DB:
            b = wrap
        return await bar() + await wrap()() + await db['b']()()() + await bar() * 1000 + await DB.b()()

    async def foo2():
        return -await bar()
    self.assertEqual(run_async(foo()), ([], 42168))
    self.assertEqual(run_async(foo2()), ([], -42))
