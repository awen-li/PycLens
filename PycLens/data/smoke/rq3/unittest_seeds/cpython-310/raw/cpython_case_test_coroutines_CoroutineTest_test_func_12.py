# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def g():
        i = me.send(None)
        await foo
    me = g()
    with self.assertRaisesRegex(ValueError, 'coroutine already executing'):
        me.send(None)
