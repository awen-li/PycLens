# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        raise StopIteration
    coro = foo()
    check = lambda : self.assertRaisesRegex(TypeError, "'coroutine' object is not iterable")
    with check():
        list(coro)
    with check():
        tuple(coro)
    with check():
        sum(coro)
    with check():
        iter(coro)
    with check():
        for i in coro:
            pass
    with check():
        [i for i in coro]
    coro.close()
