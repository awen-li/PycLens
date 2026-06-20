# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_with_8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    CNT = 0

    class CM:

        async def __aenter__(self):
            return self

        def __aexit__(self, *e):
            return 456

    async def foo():
        nonlocal CNT
        async with CM():
            CNT += 1
    with self.assertRaisesRegex(TypeError, "'async with' received an object from __aexit__ that does not implement __await__: int"):
        run_async(foo())
    self.assertEqual(CNT, 1)

    async def foo():
        nonlocal CNT
        for i in range(2):
            async with CM():
                CNT += 1
                break
    with self.assertRaisesRegex(TypeError, "'async with' received an object from __aexit__ that does not implement __await__: int"):
        run_async(foo())
    self.assertEqual(CNT, 2)

    async def foo():
        nonlocal CNT
        for i in range(2):
            async with CM():
                CNT += 1
                continue
    with self.assertRaisesRegex(TypeError, "'async with' received an object from __aexit__ that does not implement __await__: int"):
        run_async(foo())
    self.assertEqual(CNT, 3)

    async def foo():
        nonlocal CNT
        async with CM():
            CNT += 1
            return
    with self.assertRaisesRegex(TypeError, "'async with' received an object from __aexit__ that does not implement __await__: int"):
        run_async(foo())
    self.assertEqual(CNT, 4)
