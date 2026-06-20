# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_coro_wrapper_send_stop_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        return StopIteration(10)
    result = run_async__await__(foo())
    self.assertIsInstance(result[1], StopIteration)
    self.assertEqual(result[1].value, 10)
