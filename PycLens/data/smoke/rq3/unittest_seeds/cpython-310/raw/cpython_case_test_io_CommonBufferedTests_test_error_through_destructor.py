# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_error_through_destructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.CloseFailureIO()
    with support.catch_unraisable_exception() as cm:
        with self.assertRaises(AttributeError):
            self.tp(rawio).xyzzy
        if not IOBASE_EMITS_UNRAISABLE:
            self.assertIsNone(cm.unraisable)
        elif cm.unraisable is not None:
            self.assertEqual(cm.unraisable.exc_type, OSError)
