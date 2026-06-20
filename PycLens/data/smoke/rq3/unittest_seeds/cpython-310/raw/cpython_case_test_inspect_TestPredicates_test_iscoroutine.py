# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_iscoroutine

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    async_gen_coro = async_generator_function_example(1)
    gen_coro = gen_coroutine_function_example(1)
    coro = coroutine_function_example(1)
    self.assertFalse(inspect.iscoroutinefunction(gen_coroutine_function_example))
    self.assertFalse(inspect.iscoroutinefunction(functools.partial(functools.partial(gen_coroutine_function_example))))
    self.assertFalse(inspect.iscoroutine(gen_coro))
    self.assertTrue(inspect.isgeneratorfunction(gen_coroutine_function_example))
    self.assertTrue(inspect.isgeneratorfunction(functools.partial(functools.partial(gen_coroutine_function_example))))
    self.assertTrue(inspect.isgenerator(gen_coro))
    self.assertFalse(inspect.iscoroutinefunction(unittest.mock.Mock()))
    self.assertTrue(inspect.iscoroutinefunction(unittest.mock.AsyncMock()))
    self.assertTrue(inspect.iscoroutinefunction(coroutine_function_example))
    self.assertTrue(inspect.iscoroutinefunction(functools.partial(functools.partial(coroutine_function_example))))
    self.assertTrue(inspect.iscoroutine(coro))
    self.assertFalse(inspect.isgeneratorfunction(unittest.mock.Mock()))
    self.assertFalse(inspect.isgeneratorfunction(unittest.mock.AsyncMock()))
    self.assertFalse(inspect.isgeneratorfunction(coroutine_function_example))
    self.assertFalse(inspect.isgeneratorfunction(functools.partial(functools.partial(coroutine_function_example))))
    self.assertFalse(inspect.isgenerator(coro))
    self.assertFalse(inspect.isasyncgenfunction(unittest.mock.Mock()))
    self.assertFalse(inspect.isasyncgenfunction(unittest.mock.AsyncMock()))
    self.assertFalse(inspect.isasyncgenfunction(coroutine_function_example))
    self.assertTrue(inspect.isasyncgenfunction(async_generator_function_example))
    self.assertTrue(inspect.isasyncgenfunction(functools.partial(functools.partial(async_generator_function_example))))
    self.assertTrue(inspect.isasyncgen(async_gen_coro))
    coro.close()
    gen_coro.close()
