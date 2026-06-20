# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iterlen.py
# case: TestInvariantWithoutMutations_test_invariant

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = self.it
    for i in reversed(range(1, n + 1)):
        self.assertEqual(length_hint(it), i)
        next(it)
    self.assertEqual(length_hint(it), 0)
    self.assertRaises(StopIteration, next, it)
    self.assertEqual(length_hint(it), 0)
