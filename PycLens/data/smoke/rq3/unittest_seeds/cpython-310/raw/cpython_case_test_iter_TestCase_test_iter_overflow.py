# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_iter_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = iter(UnlimitedSequenceClass())
    it.__setstate__(sys.maxsize - 2)
    self.assertEqual(next(it), sys.maxsize - 2)
    self.assertEqual(next(it), sys.maxsize - 1)
    with self.assertRaises(OverflowError):
        next(it)
    with self.assertRaises(OverflowError):
        next(it)
