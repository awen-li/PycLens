# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestFrozenSet_test_hash_effectiveness

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 13
    hashvalues = set()
    addhashvalue = hashvalues.add
    elemmasks = [(i + 1, 1 << i) for i in range(n)]
    for i in range(2 ** n):
        addhashvalue(hash(frozenset([e for (e, m) in elemmasks if m & i])))
    self.assertEqual(len(hashvalues), 2 ** n)

    def zf_range(n):
        nums = [frozenset()]
        for i in range(n - 1):
            num = frozenset(nums)
            nums.append(num)
        return nums[:n]

    def powerset(s):
        for i in range(len(s) + 1):
            yield from map(frozenset, itertools.combinations(s, i))
    for n in range(18):
        t = 2 ** n
        mask = t - 1
        for nums in (range, zf_range):
            u = len({h & mask for h in map(hash, powerset(nums(n)))})
            self.assertGreater(4 * u, t)
