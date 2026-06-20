# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_multiset_operations_equivalent_to_set_operations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = list(product(('a', 'b', 'c'), range(2)))
    powerset = chain.from_iterable((combinations(s, r) for r in range(len(s) + 1)))
    counters = [Counter(dict(groups)) for groups in powerset]
    for (cp, cq) in product(counters, repeat=2):
        sp = set(cp.elements())
        sq = set(cq.elements())
        self.assertEqual(set(cp + cq), sp | sq)
        self.assertEqual(set(cp - cq), sp - sq)
        self.assertEqual(set(cp | cq), sp | sq)
        self.assertEqual(set(cp & cq), sp & sq)
        self.assertEqual(cp == cq, sp == sq)
        self.assertEqual(cp != cq, sp != sq)
        self.assertEqual(cp <= cq, sp <= sq)
        self.assertEqual(cp >= cq, sp >= sq)
        self.assertEqual(cp < cq, sp < sq)
        self.assertEqual(cp > cq, sp > sq)
