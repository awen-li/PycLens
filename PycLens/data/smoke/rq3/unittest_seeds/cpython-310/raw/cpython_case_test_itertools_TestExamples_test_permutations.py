# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_permutations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(permutations('ABCD', 2)), list(map(tuple, 'AB AC AD BA BC BD CA CB CD DA DB DC'.split())))
    self.assertEqual(list(permutations(range(3))), [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)])
