# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_stack_in_coroutine_throw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def a():
        return await b()

    async def b():
        return await c()

    @types.coroutine
    def c():
        try:
            yield len(traceback.extract_stack())
        except ZeroDivisionError:
            yield len(traceback.extract_stack())
    coro = a()
    len_send = coro.send(None)
    len_throw = coro.throw(ZeroDivisionError)
    self.assertEqual(len_send, len_throw)
