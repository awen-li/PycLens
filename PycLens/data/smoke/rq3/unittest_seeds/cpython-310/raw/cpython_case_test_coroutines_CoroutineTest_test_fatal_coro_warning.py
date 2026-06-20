# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: CoroutineTest_test_fatal_coro_warning

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def func():
        pass
    with warnings.catch_warnings(), support.catch_unraisable_exception() as cm:
        warnings.filterwarnings('error')
        coro = func()
        coro_repr = repr(coro)
        coro = None
        support.gc_collect()
        self.assertIn('was never awaited', str(cm.unraisable.exc_value))
        self.assertEqual(repr(cm.unraisable.object), coro_repr)
