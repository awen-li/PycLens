# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_combinations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, combinations, 'abc')
    self.assertRaises(TypeError, combinations, 'abc', 2, 1)
    self.assertRaises(TypeError, combinations, None)
    self.assertRaises(ValueError, combinations, 'abc', -2)
    for op in [lambda a: a] + picklecopiers:
        self.assertEqual(list(op(combinations('abc', 32))), [])
        self.assertEqual(list(op(combinations('ABCD', 2))), [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')])
        testIntermediate = combinations('ABCD', 2)
        next(testIntermediate)
        self.assertEqual(list(op(testIntermediate)), [('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')])
        self.assertEqual(list(op(combinations(range(4), 3))), [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)])
        testIntermediate = combinations(range(4), 3)
        next(testIntermediate)
        self.assertEqual(list(op(testIntermediate)), [(0, 1, 3), (0, 2, 3), (1, 2, 3)])

    def combinations1(iterable, r):
        """Pure python version shown in the docs"""
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple((pool[i] for i in indices))
        while 1:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple((pool[i] for i in indices))

    def combinations2(iterable, r):
        """Pure python version shown in the docs"""
        pool = tuple(iterable)
        n = len(pool)
        for indices in permutations(range(n), r):
            if sorted(indices) == list(indices):
                yield tuple((pool[i] for i in indices))

    def combinations3(iterable, r):
        """Pure python version from cwr()"""
        pool = tuple(iterable)
        n = len(pool)
        for indices in combinations_with_replacement(range(n), r):
            if len(set(indices)) == r:
                yield tuple((pool[i] for i in indices))
    for n in range(7):
        values = [5 * x - 12 for x in range(n)]
        for r in range(n + 2):
            result = list(combinations(values, r))
            self.assertEqual(len(result), 0 if r > n else fact(n) / fact(r) / fact(n - r))
            self.assertEqual(len(result), len(set(result)))
            self.assertEqual(result, sorted(result))
            for c in result:
                self.assertEqual(len(c), r)
                self.assertEqual(len(set(c)), r)
                self.assertEqual(list(c), sorted(c))
                self.assertTrue(all((e in values for e in c)))
                self.assertEqual(list(c), [e for e in values if e in c])
            self.assertEqual(result, list(combinations1(values, r)))
            self.assertEqual(result, list(combinations2(values, r)))
            self.assertEqual(result, list(combinations3(values, r)))
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                self.pickletest(proto, combinations(values, r))
