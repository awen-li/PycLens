# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_islice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(islice('ABCDEFG', 2)), list('AB'))
    self.assertEqual(list(islice('ABCDEFG', 2, 4)), list('CD'))
    self.assertEqual(list(islice('ABCDEFG', 2, None)), list('CDEFG'))
    self.assertEqual(list(islice('ABCDEFG', 0, None, 2)), list('ACEG'))
