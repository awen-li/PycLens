# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def bar():
        yield 1

    async def foo():
        await bar()
    check = lambda : self.assertRaisesRegex(TypeError, "'coroutine' object is not iterable")
    coro = foo()
    with check():
        for el in coro:
            pass
    coro.close()
    for el in bar():
        self.assertEqual(el, 1)
    self.assertEqual([el for el in bar()], [1])
    self.assertEqual(tuple(bar()), (1,))
    self.assertEqual(next(iter(bar())), 1)
