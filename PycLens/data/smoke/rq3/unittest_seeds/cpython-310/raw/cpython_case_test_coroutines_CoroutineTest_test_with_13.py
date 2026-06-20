# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_13

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CNT = 0

    class CM:

        async def __aenter__(self):
            1 / 0

        async def __aexit__(self, *e):
            return True

    async def foo():
        nonlocal CNT
        CNT += 1
        async with CM():
            CNT += 1000
        CNT += 10000
    with self.assertRaises(ZeroDivisionError):
        run_async(foo())
    self.assertEqual(CNT, 1)
