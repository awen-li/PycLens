# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CNT = 0

    class AI:

        def __aiter__(self):
            1 / 0

    async def foo():
        nonlocal CNT
        async for i in AI():
            CNT += 1
        CNT += 10
    with self.assertRaises(ZeroDivisionError):
        run_async(foo())
    self.assertEqual(CNT, 0)
