# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_for_tuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Done(Exception):
        pass

    class AIter(tuple):
        i = 0

        def __aiter__(self):
            return self

        async def __anext__(self):
            if self.i >= len(self):
                raise StopAsyncIteration
            self.i += 1
            return self[self.i - 1]
    result = []

    async def foo():
        async for i in AIter([42]):
            result.append(i)
        raise Done
    with self.assertRaises(Done):
        foo().send(None)
    self.assertEqual(result, [42])
