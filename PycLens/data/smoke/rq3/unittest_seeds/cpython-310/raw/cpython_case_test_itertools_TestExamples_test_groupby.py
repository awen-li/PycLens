# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_groupby

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual([k for (k, g) in groupby('AAAABBBCCDAABBB')], list('ABCDAB'))
    self.assertEqual([list(g) for (k, g) in groupby('AAAABBBCCD')], [list('AAAA'), list('BBB'), list('CC'), list('D')])
