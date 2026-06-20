# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cprofile.py
# case: CProfileTest_test_bad_counter_during_dealloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _lsprof
    with support.catch_unraisable_exception() as cm:
        obj = _lsprof.Profiler(lambda : int)
        obj.enable()
        obj = _lsprof.Profiler(1)
        obj.disable()
        obj.clear()
        self.assertEqual(cm.unraisable.exc_type, TypeError)
