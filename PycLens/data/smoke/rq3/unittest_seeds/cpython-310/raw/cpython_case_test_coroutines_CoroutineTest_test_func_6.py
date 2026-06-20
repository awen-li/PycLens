# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def bar():
        yield 1
        yield 2

    async def foo():
        await bar()
    f = foo()
    self.assertEqual(f.send(None), 1)
    self.assertEqual(f.send(None), 2)
    with self.assertRaises(StopIteration):
        f.send(None)
