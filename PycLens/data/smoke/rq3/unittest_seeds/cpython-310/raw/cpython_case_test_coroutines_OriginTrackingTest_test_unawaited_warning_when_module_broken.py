# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: OriginTrackingTest_test_unawaited_warning_when_module_broken

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def corofn():
        pass
    orig_wuc = warnings._warn_unawaited_coroutine
    try:
        warnings._warn_unawaited_coroutine = lambda coro: 1 / 0
        with support.catch_unraisable_exception() as cm, warnings_helper.check_warnings(('coroutine .* was never awaited', RuntimeWarning)):
            coro = corofn()
            coro_repr = repr(coro)
            del coro
            support.gc_collect()
            self.assertEqual(repr(cm.unraisable.object), coro_repr)
            self.assertEqual(cm.unraisable.exc_type, ZeroDivisionError)
        del warnings._warn_unawaited_coroutine
        with warnings_helper.check_warnings(('coroutine .* was never awaited', RuntimeWarning)):
            corofn()
            support.gc_collect()
    finally:
        warnings._warn_unawaited_coroutine = orig_wuc
