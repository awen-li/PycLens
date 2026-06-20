# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_faulthandler.py
# case: FaultHandlerTests_test_cancel_later_without_dump_traceback_later

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = dedent('\n            import faulthandler\n            faulthandler.cancel_dump_traceback_later()\n        ')
    (output, exitcode) = self.get_output(code)
    self.assertEqual(output, [])
    self.assertEqual(exitcode, 0)
