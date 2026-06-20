# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class I:

        def __aiter__(self):
            return self

        def __anext__(self):
            return ()
    aiter = I()
    refs_before = sys.getrefcount(aiter)

    async def foo():
        async for i in aiter:
            print('never going to happen')
    with self.assertRaisesRegex(TypeError, "async for' received an invalid object.*__anext__.*tuple"):
        run_async(foo())
    self.assertEqual(sys.getrefcount(aiter), refs_before)
