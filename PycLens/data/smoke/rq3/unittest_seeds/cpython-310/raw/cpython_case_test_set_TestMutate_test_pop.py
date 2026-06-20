# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestMutate_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    popped = {}
    while self.set:
        popped[self.set.pop()] = None
    self.assertEqual(len(popped), len(self.values))
    for v in self.values:
        self.assertIn(v, popped)
