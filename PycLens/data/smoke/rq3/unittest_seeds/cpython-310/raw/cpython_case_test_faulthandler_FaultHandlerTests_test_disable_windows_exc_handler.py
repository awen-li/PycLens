# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_disable_windows_exc_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = dedent('\n            import faulthandler\n            faulthandler.enable()\n            faulthandler.disable()\n            code = faulthandler._EXCEPTION_ACCESS_VIOLATION\n            faulthandler._raise_exception(code)\n        ')
    (output, exitcode) = self.get_output(code)
    self.assertEqual(output, [])
    self.assertEqual(exitcode, 3221225477)
