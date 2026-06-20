# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_is_enabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig_stderr = sys.stderr
    try:
        sys.stderr = sys.__stderr__
        was_enabled = faulthandler.is_enabled()
        try:
            faulthandler.enable()
            self.assertTrue(faulthandler.is_enabled())
            faulthandler.disable()
            self.assertFalse(faulthandler.is_enabled())
        finally:
            if was_enabled:
                faulthandler.enable()
            else:
                faulthandler.disable()
    finally:
        sys.stderr = orig_stderr
