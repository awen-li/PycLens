# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_await_14

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Wrapper:

        def __init__(self, coro):
            assert coro.__class__ is types.CoroutineType
            self.coro = coro

        def __await__(self):
            return self.coro.__await__()

    class FutureLike:

        def __await__(self):
            return (yield)

    class Marker(Exception):
        pass

    async def coro1():
        try:
            return await FutureLike()
        except ZeroDivisionError:
            raise Marker

    async def coro2():
        return await Wrapper(coro1())
    c = coro2()
    c.send(None)
    with self.assertRaisesRegex(StopIteration, 'spam'):
        c.send('spam')
    c = coro2()
    c.send(None)
    with self.assertRaises(Marker):
        c.throw(ZeroDivisionError)
