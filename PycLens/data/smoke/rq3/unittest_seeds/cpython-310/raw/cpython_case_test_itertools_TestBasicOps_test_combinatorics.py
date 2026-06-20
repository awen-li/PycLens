# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_combinatorics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in range(6):
        s = 'ABCDEFG'[:n]
        for r in range(8):
            prod = list(product(s, repeat=r))
            cwr = list(combinations_with_replacement(s, r))
            perm = list(permutations(s, r))
            comb = list(combinations(s, r))
            self.assertEqual(len(prod), n ** r)
            self.assertEqual(len(cwr), fact(n + r - 1) / fact(r) / fact(n - 1) if n else not r)
            self.assertEqual(len(perm), 0 if r > n else fact(n) / fact(n - r))
            self.assertEqual(len(comb), 0 if r > n else fact(n) / fact(r) / fact(n - r))
            self.assertEqual(prod, sorted(set(prod)))
            self.assertEqual(cwr, sorted(set(cwr)))
            self.assertEqual(perm, sorted(set(perm)))
            self.assertEqual(comb, sorted(set(comb)))
            self.assertEqual(cwr, [t for t in prod if sorted(t) == list(t)])
            self.assertEqual(perm, [t for t in prod if len(set(t)) == r])
            self.assertEqual(comb, [t for t in perm if sorted(t) == list(t)])
            self.assertEqual(comb, [t for t in cwr if len(set(t)) == r])
            self.assertEqual(comb, list(filter(set(cwr).__contains__, perm)))
            self.assertEqual(comb, list(filter(set(perm).__contains__, cwr)))
            self.assertEqual(comb, sorted(set(cwr) & set(perm)))
