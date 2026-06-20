# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_581080

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    iter = re.finditer('\\s', 'a b')
    self.assertEqual(next(iter).span(), (1, 2))
    self.assertRaises(StopIteration, next, iter)
    scanner = re.compile('\\s').scanner('a b')
    self.assertEqual(scanner.search().span(), (1, 2))
    self.assertIsNone(scanner.search())
