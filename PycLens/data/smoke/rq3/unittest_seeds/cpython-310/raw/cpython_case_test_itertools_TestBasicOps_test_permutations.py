# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_permutations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, permutations)
    self.assertRaises(TypeError, permutations, 'abc', 2, 1)
    self.assertRaises(TypeError, permutations, None)
    self.assertRaises(ValueError, permutations, 'abc', -2)
    self.assertEqual(list(permutations('abc', 32)), [])
    self.assertRaises(TypeError, permutations, 'abc', 's')
    self.assertEqual(list(permutations(range(3), 2)), [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)])

    def permutations1(iterable, r=None):
        """Pure python version shown in the docs"""
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n - r + 1, n + 1))[::-1]
        yield tuple((pool[i] for i in indices[:r]))
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i + 1:] + indices[i:i + 1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    (indices[i], indices[-j]) = (indices[-j], indices[i])
                    yield tuple((pool[i] for i in indices[:r]))
                    break
            else:
                return

    def permutations2(iterable, r=None):
        """Pure python version shown in the docs"""
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        for indices in product(range(n), repeat=r):
            if len(set(indices)) == r:
                yield tuple((pool[i] for i in indices))
    for n in range(7):
        values = [5 * x - 12 for x in range(n)]
        for r in range(n + 2):
            result = list(permutations(values, r))
            self.assertEqual(len(result), 0 if r > n else fact(n) / fact(n - r))
            self.assertEqual(len(result), len(set(result)))
            self.assertEqual(result, sorted(result))
            for p in result:
                self.assertEqual(len(p), r)
                self.assertEqual(len(set(p)), r)
                self.assertTrue(all((e in values for e in p)))
            self.assertEqual(result, list(permutations1(values, r)))
            self.assertEqual(result, list(permutations2(values, r)))
            if r == n:
                self.assertEqual(result, list(permutations(values, None)))
                self.assertEqual(result, list(permutations(values)))
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                self.pickletest(proto, permutations(values, r))
