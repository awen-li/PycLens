# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSetOfSets_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    inner = frozenset([1])
    outer = set([inner])
    element = outer.pop()
    self.assertEqual(type(element), frozenset)
    outer.add(inner)
    outer.remove(inner)
    self.assertEqual(outer, set())
    outer.discard(inner)
