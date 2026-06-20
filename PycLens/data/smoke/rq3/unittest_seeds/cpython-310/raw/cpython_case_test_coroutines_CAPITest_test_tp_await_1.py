# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CAPITest_test_tp_await_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import awaitType as at

    async def foo():
        future = at(iter([1]))
        return await future
    self.assertEqual(foo().send(None), 1)
