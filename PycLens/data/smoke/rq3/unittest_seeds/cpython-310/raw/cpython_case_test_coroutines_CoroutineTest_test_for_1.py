# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    aiter_calls = 0

    class AsyncIter:

        def __init__(self):
            self.i = 0

        def __aiter__(self):
            nonlocal aiter_calls
            aiter_calls += 1
            return self

        async def __anext__(self):
            self.i += 1
            if not self.i % 10:
                await AsyncYield(self.i * 10)
            if self.i > 100:
                raise StopAsyncIteration
            return (self.i, self.i)
    buffer = []

    async def test1():
        async for (i1, i2) in AsyncIter():
            buffer.append(i1 + i2)
    (yielded, _) = run_async(test1())
    self.assertEqual(aiter_calls, 1)
    self.assertEqual(yielded, [i * 100 for i in range(1, 11)])
    self.assertEqual(buffer, [i * 2 for i in range(1, 101)])
    buffer = []

    async def test2():
        nonlocal buffer
        async for i in AsyncIter():
            buffer.append(i[0])
            if i[0] == 20:
                break
        else:
            buffer.append('what?')
        buffer.append('end')
    (yielded, _) = run_async(test2())
    self.assertEqual(aiter_calls, 2)
    self.assertEqual(yielded, [100, 200])
    self.assertEqual(buffer, [i for i in range(1, 21)] + ['end'])
    buffer = []

    async def test3():
        nonlocal buffer
        async for i in AsyncIter():
            if i[0] > 20:
                continue
            buffer.append(i[0])
        else:
            buffer.append('what?')
        buffer.append('end')
    (yielded, _) = run_async(test3())
    self.assertEqual(aiter_calls, 3)
    self.assertEqual(yielded, [i * 100 for i in range(1, 11)])
    self.assertEqual(buffer, [i for i in range(1, 21)] + ['what?', 'end'])
