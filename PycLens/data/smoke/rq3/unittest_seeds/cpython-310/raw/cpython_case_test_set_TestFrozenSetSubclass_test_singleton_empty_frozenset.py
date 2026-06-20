# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestFrozenSetSubclass_test_singleton_empty_frozenset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Frozenset = self.thetype
    f = frozenset()
    F = Frozenset()
    efs = [Frozenset(), Frozenset([]), Frozenset(()), Frozenset(''), Frozenset(), Frozenset([]), Frozenset(()), Frozenset(''), Frozenset(range(0)), Frozenset(Frozenset()), Frozenset(frozenset()), f, F, Frozenset(f), Frozenset(F)]
    self.assertEqual(len(set(map(id, efs))), len(efs))
