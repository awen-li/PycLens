# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_complete

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    completer = rlcompleter.Completer()
    self.assertEqual(completer.complete('', 0), '\t')
    self.assertEqual(completer.complete('a', 0), 'and ')
    self.assertEqual(completer.complete('a', 1), 'as ')
    self.assertEqual(completer.complete('as', 2), 'assert ')
    self.assertEqual(completer.complete('an', 0), 'and ')
    self.assertEqual(completer.complete('pa', 0), 'pass')
    self.assertEqual(completer.complete('Fa', 0), 'False')
    self.assertEqual(completer.complete('el', 0), 'elif ')
    self.assertEqual(completer.complete('el', 1), 'else')
    self.assertEqual(completer.complete('tr', 0), 'try:')
