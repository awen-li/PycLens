# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestDocExample_test_grades

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = self.module.bisect(breakpoints, score)
        return grades[i]
    result = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    self.assertEqual(result, ['F', 'A', 'C', 'C', 'B', 'A', 'A'])
