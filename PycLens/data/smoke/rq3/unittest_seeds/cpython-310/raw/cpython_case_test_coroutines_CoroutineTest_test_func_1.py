# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_func_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def foo():
        return 10
    f = foo()
    self.assertIsInstance(f, types.CoroutineType)
    self.assertTrue(bool(foo.__code__.co_flags & inspect.CO_COROUTINE))
    self.assertFalse(bool(foo.__code__.co_flags & inspect.CO_GENERATOR))
    self.assertTrue(bool(f.cr_code.co_flags & inspect.CO_COROUTINE))
    self.assertFalse(bool(f.cr_code.co_flags & inspect.CO_GENERATOR))
    self.assertEqual(run_async(f), ([], 10))
    self.assertEqual(run_async__await__(foo()), ([], 10))

    def bar():
        pass
    self.assertFalse(bool(bar.__code__.co_flags & inspect.CO_COROUTINE))
