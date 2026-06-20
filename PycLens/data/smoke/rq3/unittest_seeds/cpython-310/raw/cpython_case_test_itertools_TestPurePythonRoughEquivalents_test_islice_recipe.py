# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestPurePythonRoughEquivalents_test_islice_recipe

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(self.islice('ABCDEFG', 2)), list('AB'))
    self.assertEqual(list(self.islice('ABCDEFG', 2, 4)), list('CD'))
    self.assertEqual(list(self.islice('ABCDEFG', 2, None)), list('CDEFG'))
    self.assertEqual(list(self.islice('ABCDEFG', 0, None, 2)), list('ACEG'))
    it = iter(range(10))
    self.assertEqual(list(self.islice(it, 3)), list(range(3)))
    self.assertEqual(list(it), list(range(3, 10)))
    it = iter(range(10))
    self.assertEqual(list(self.islice(it, 3, 3)), [])
    self.assertEqual(list(it), list(range(3, 10)))
    c = count()
    self.assertEqual(list(self.islice(c, 1, 3, 50)), [1])
    self.assertEqual(next(c), 3)
