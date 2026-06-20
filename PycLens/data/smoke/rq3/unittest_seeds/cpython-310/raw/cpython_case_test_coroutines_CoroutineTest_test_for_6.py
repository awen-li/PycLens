# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    I = 0

    class Manager:

        async def __aenter__(self):
            nonlocal I
            I += 10000

        async def __aexit__(self, *args):
            nonlocal I
            I += 100000

    class Iterable:

        def __init__(self):
            self.i = 0

        def __aiter__(self):
            return self

        async def __anext__(self):
            if self.i > 10:
                raise StopAsyncIteration
            self.i += 1
            return self.i
    manager = Manager()
    iterable = Iterable()
    mrefs_before = sys.getrefcount(manager)
    irefs_before = sys.getrefcount(iterable)

    async def main():
        nonlocal I
        async with manager:
            async for i in iterable:
                I += 1
        I += 1000
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        run_async(main())
    self.assertEqual(I, 111011)
    self.assertEqual(sys.getrefcount(manager), mrefs_before)
    self.assertEqual(sys.getrefcount(iterable), irefs_before)

    async def main():
        nonlocal I
        async with Manager():
            async for i in Iterable():
                I += 1
        I += 1000
        async with Manager():
            async for i in Iterable():
                I += 1
        I += 1000
    run_async(main())
    self.assertEqual(I, 333033)

    async def main():
        nonlocal I
        async with Manager():
            I += 100
            async for i in Iterable():
                I += 1
            else:
                I += 10000000
        I += 1000
        async with Manager():
            I += 100
            async for i in Iterable():
                I += 1
            else:
                I += 10000000
        I += 1000
    run_async(main())
    self.assertEqual(I, 20555255)
