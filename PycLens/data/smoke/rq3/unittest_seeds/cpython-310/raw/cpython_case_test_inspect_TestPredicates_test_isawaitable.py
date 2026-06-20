# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestPredicates_test_isawaitable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        yield
    self.assertFalse(inspect.isawaitable(gen()))
    coro = coroutine_function_example(1)
    gen_coro = gen_coroutine_function_example(1)
    self.assertTrue(inspect.isawaitable(coro))
    self.assertTrue(inspect.isawaitable(gen_coro))

    class Future:

        def __await__():
            pass
    self.assertTrue(inspect.isawaitable(Future()))
    self.assertFalse(inspect.isawaitable(Future))

    class NotFuture:
        pass
    not_fut = NotFuture()
    not_fut.__await__ = lambda : None
    self.assertFalse(inspect.isawaitable(not_fut))
    coro.close()
    gen_coro.close()
