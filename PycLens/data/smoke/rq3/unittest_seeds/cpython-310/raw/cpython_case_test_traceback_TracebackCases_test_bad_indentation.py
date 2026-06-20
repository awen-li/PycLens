# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_bad_indentation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    err = self.get_exception_format(self.syntax_error_bad_indentation, IndentationError)
    self.assertEqual(len(err), 4)
    self.assertEqual(err[1].strip(), 'print(2)')
    self.assertIn('^', err[2])
    self.assertEqual(err[1].find(')') + 1, err[2].find('^'))
    err = self.get_exception_format(self.syntax_error_bad_indentation2, IndentationError)
    self.assertEqual(len(err), 3)
    self.assertEqual(err[1].strip(), 'print(2)')
