# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_dropwhile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])), [6, 4, 1])
