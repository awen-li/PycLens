# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CAPITest_test_tp_await_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import awaitType as at

    async def foo():
        future = at(1)
        return await future
    with self.assertRaisesRegex(TypeError, "__await__.*returned non-iterator of type 'int'"):
        self.assertEqual(foo().send(None), 1)
