# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contains.py
# case: TestContains_test_nonreflexive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = (float('nan'), 1, None, 'abc', NEVER_EQ)
    constructors = (list, tuple, dict.fromkeys, set, frozenset, deque)
    for constructor in constructors:
        container = constructor(values)
        for elem in container:
            self.assertIn(elem, container)
        self.assertTrue(container == constructor(values))
        self.assertTrue(container == container)
