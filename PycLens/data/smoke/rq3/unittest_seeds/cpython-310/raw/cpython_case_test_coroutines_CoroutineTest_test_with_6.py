# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CM:

        def __aenter__(self):
            return 123

        def __aexit__(self, *e):
            return 456

    async def foo():
        async with CM():
            pass
    with self.assertRaisesRegex(TypeError, "'async with' received an object from __aenter__ that does not implement __await__: int"):
        run_async(foo())
