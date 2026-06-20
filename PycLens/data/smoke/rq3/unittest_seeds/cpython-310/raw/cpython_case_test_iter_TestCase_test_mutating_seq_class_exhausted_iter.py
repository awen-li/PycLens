# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_mutating_seq_class_exhausted_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = SequenceClass(5)
    exhit = iter(a)
    empit = iter(a)
    for x in exhit:
        next(empit)
    a.n = 7
    self.assertEqual(list(exhit), [])
    self.assertEqual(list(empit), [5, 6])
    self.assertEqual(list(a), [0, 1, 2, 3, 4, 5, 6])
