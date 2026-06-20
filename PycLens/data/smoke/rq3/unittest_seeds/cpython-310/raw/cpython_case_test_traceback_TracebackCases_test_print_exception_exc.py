# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_print_exception_exc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output = StringIO()
    traceback.print_exception(Exception('projector'), file=output)
    self.assertEqual(output.getvalue(), 'Exception: projector\n')
