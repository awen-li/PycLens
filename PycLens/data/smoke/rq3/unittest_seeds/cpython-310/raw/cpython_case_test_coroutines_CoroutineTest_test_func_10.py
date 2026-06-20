# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_10

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 0

    @types.coroutine
    def gen():
        nonlocal N
        try:
            a = (yield)
            yield (a ** 2)
        except ZeroDivisionError:
            N += 100
            raise
        finally:
            N += 1

    async def foo():
        await gen()
    coro = foo()
    aw = coro.__await__()
    self.assertIs(aw, iter(aw))
    next(aw)
    self.assertEqual(aw.send(10), 100)
    self.assertEqual(N, 0)
    aw.close()
    self.assertEqual(N, 1)
    coro = foo()
    aw = coro.__await__()
    next(aw)
    with self.assertRaises(ZeroDivisionError):
        aw.throw(ZeroDivisionError, None, None)
    self.assertEqual(N, 102)
