# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_11

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class F:

        def __aiter__(self):
            return self

        def __anext__(self):
            return self

        def __await__(self):
            1 / 0

    async def main():
        async for _ in F():
            pass
    with self.assertRaisesRegex(TypeError, 'an invalid object from __anext__') as c:
        main().send(None)
    err = c.exception
    self.assertIsInstance(err.__cause__, ZeroDivisionError)
