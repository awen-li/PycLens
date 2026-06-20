# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_async_def

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        pass
    foo_code = foo.__code__
    foo_flags = foo.__code__.co_flags
    decorated_foo = types.coroutine(foo)
    self.assertIs(foo, decorated_foo)
    self.assertEqual(foo.__code__.co_flags, foo_flags)
    self.assertIs(decorated_foo.__code__, foo_code)
    foo_coro = foo()

    def bar():
        return foo_coro
    for _ in range(2):
        bar = types.coroutine(bar)
        coro = bar()
        self.assertIs(foo_coro, coro)
        self.assertEqual(coro.cr_code.co_flags, foo_flags)
        coro.close()
