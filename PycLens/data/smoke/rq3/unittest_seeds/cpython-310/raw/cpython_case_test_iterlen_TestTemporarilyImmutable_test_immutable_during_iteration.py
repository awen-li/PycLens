# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iterlen.py
# case: TestTemporarilyImmutable_test_immutable_during_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = self.it
    self.assertEqual(length_hint(it), n)
    next(it)
    self.assertEqual(length_hint(it), n - 1)
    self.mutate()
    self.assertRaises(RuntimeError, next, it)
    self.assertEqual(length_hint(it), 0)
