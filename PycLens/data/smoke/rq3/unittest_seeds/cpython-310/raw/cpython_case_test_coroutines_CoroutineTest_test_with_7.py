# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_7

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CM:

        async def __aenter__(self):
            return self

        def __aexit__(self, *e):
            return 444

    async def foo():
        async with CM():
            1 / 0
    try:
        run_async(foo())
    except TypeError as exc:
        self.assertRegex(exc.args[0], "'async with' received an object from __aexit__ that does not implement __await__: int")
        self.assertTrue(exc.__context__ is not None)
        self.assertTrue(isinstance(exc.__context__, ZeroDivisionError))
    else:
        self.fail('invalid asynchronous context manager did not fail')
