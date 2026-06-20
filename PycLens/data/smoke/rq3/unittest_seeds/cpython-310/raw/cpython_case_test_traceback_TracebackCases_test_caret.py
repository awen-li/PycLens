# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TracebackCases_test_caret

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    err = self.get_exception_format(self.syntax_error_with_caret, SyntaxError)
    self.assertEqual(len(err), 4)
    self.assertTrue(err[1].strip() == 'return x!')
    self.assertIn('^', err[2])
    self.assertEqual(err[1].find('!'), err[2].find('^'))
    self.assertEqual(err[2].count('^'), 1)
    err = self.get_exception_format(self.syntax_error_with_caret_2, SyntaxError)
    self.assertIn('^', err[2])
    self.assertEqual(err[2].count('\n'), 1)
    self.assertEqual(err[1].find('+') + 1, err[2].find('^'))
    self.assertEqual(err[2].count('^'), 1)
    err = self.get_exception_format(self.syntax_error_with_caret_non_ascii, SyntaxError)
    self.assertIn('^', err[2])
    self.assertEqual(err[2].count('\n'), 1)
    self.assertEqual(err[1].find('+') + 1, err[2].find('^'))
    self.assertEqual(err[2].count('^'), 1)
    err = self.get_exception_format(self.syntax_error_with_caret_range, SyntaxError)
    self.assertIn('^', err[2])
    self.assertEqual(err[2].count('\n'), 1)
    self.assertEqual(err[1].find('y'), err[2].find('^'))
    self.assertEqual(err[2].count('^'), len('y for y in range(30)'))
    err = self.get_exception_format(self.tokenizer_error_with_caret_range, SyntaxError)
    self.assertIn('^', err[2])
    self.assertEqual(err[2].count('\n'), 1)
    self.assertEqual(err[1].find('('), err[2].find('^'))
    self.assertEqual(err[2].count('^'), 1)
