# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tup = (1, 2, 3)
    refs_before = sys.getrefcount(tup)

    async def foo():
        async for i in tup:
            print('never going to happen')
    with self.assertRaisesRegex(TypeError, "async for' requires an object.*__aiter__.*tuple"):
        run_async(foo())
    self.assertEqual(sys.getrefcount(tup), refs_before)
