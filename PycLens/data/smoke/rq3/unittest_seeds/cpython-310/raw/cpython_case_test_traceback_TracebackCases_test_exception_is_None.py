# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_exception_is_None

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NONE_EXC_STRING = 'NoneType: None\n'
    excfile = StringIO()
    traceback.print_exception(None, file=excfile)
    self.assertEqual(excfile.getvalue(), NONE_EXC_STRING)
    excfile = StringIO()
    traceback.print_exception(None, None, None, file=excfile)
    self.assertEqual(excfile.getvalue(), NONE_EXC_STRING)
    excfile = StringIO()
    traceback.print_exc(None, file=excfile)
    self.assertEqual(excfile.getvalue(), NONE_EXC_STRING)
    self.assertEqual(traceback.format_exc(None), NONE_EXC_STRING)
    self.assertEqual(traceback.format_exception(None), [NONE_EXC_STRING])
    self.assertEqual(traceback.format_exception(None, None, None), [NONE_EXC_STRING])
    self.assertEqual(traceback.format_exception_only(None), [NONE_EXC_STRING])
    self.assertEqual(traceback.format_exception_only(None, None), [NONE_EXC_STRING])
