# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_duplicate_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    namespace = {'False': None, 'assert': None, 'try': lambda : None, 'memoryview': None, 'Ellipsis': lambda : None}
    completer = rlcompleter.Completer(namespace)
    self.assertEqual(completer.complete('False', 0), 'False')
    self.assertIsNone(completer.complete('False', 1))
    self.assertEqual(completer.complete('assert', 0), 'assert ')
    self.assertIsNone(completer.complete('assert', 1))
    self.assertEqual(completer.complete('try', 0), 'try:')
    self.assertIsNone(completer.complete('try', 1))
    self.assertEqual(completer.complete('memoryview', 0), 'memoryview')
    self.assertIsNone(completer.complete('memoryview', 1))
    self.assertEqual(completer.complete('Ellipsis', 0), 'Ellipsis()')
    self.assertIsNone(completer.complete('Ellipsis', 1))
