# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_signatures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(inspect.signature(traceback.print_exception)), '(exc, /, value=<implicit>, tb=<implicit>, limit=None, file=None, chain=True)')
    self.assertEqual(str(inspect.signature(traceback.format_exception)), '(exc, /, value=<implicit>, tb=<implicit>, limit=None, chain=True)')
    self.assertEqual(str(inspect.signature(traceback.format_exception_only)), '(exc, /, value=<implicit>)')
