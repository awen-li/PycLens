# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_neg_setstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = iter(UnlimitedSequenceClass())
    it.__setstate__(-42)
    self.assertEqual(next(it), 0)
    self.assertEqual(next(it), 1)
