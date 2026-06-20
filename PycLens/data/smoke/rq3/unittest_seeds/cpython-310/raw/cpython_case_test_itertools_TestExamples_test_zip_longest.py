# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_zip_longest

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(zip_longest('ABCD', 'xy', fillvalue='-')), [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')])
