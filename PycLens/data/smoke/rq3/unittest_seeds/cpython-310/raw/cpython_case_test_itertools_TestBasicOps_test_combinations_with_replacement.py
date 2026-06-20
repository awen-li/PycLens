# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_combinations_with_replacement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cwr = combinations_with_replacement
    self.assertRaises(TypeError, cwr, 'abc')
    self.assertRaises(TypeError, cwr, 'abc', 2, 1)
    self.assertRaises(TypeError, cwr, None)
    self.assertRaises(ValueError, cwr, 'abc', -2)
    for op in [lambda a: a] + picklecopiers:
        self.assertEqual(list(op(cwr('ABC', 2))), [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')])
        testIntermediate = cwr('ABC', 2)
        next(testIntermediate)
        self.assertEqual(list(op(testIntermediate)), [('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')])

    def cwr1(iterable, r):
        """Pure python version shown in the docs"""
        pool = tuple(iterable)
        n = len(pool)
        if not n and r:
            return
        indices = [0] * r
        yield tuple((pool[i] for i in indices))
        while 1:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple((pool[i] for i in indices))

    def cwr2(iterable, r):
        """Pure python version shown in the docs"""
        pool = tuple(iterable)
        n = len(pool)
        for indices in product(range(n), repeat=r):
            if sorted(indices) == list(indices):
                yield tuple((pool[i] for i in indices))

    def numcombs(n, r):
        if not n:
            return 0 if r else 1
        return fact(n + r - 1) / fact(r) / fact(n - 1)
    for n in range(7):
        values = [5 * x - 12 for x in range(n)]
        for r in range(n + 2):
            result = list(cwr(values, r))
            self.assertEqual(len(result), numcombs(n, r))
            self.assertEqual(len(result), len(set(result)))
            self.assertEqual(result, sorted(result))
            regular_combs = list(combinations(values, r))
            if n == 0 or r <= 1:
                self.assertEqual(result, regular_combs)
            else:
                self.assertTrue(set(result) >= set(regular_combs))
            for c in result:
                self.assertEqual(len(c), r)
                noruns = [k for (k, v) in groupby(c)]
                self.assertEqual(len(noruns), len(set(noruns)))
                self.assertEqual(list(c), sorted(c))
                self.assertTrue(all((e in values for e in c)))
                self.assertEqual(noruns, [e for e in values if e in c])
            self.assertEqual(result, list(cwr1(values, r)))
            self.assertEqual(result, list(cwr2(values, r)))
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                self.pickletest(proto, cwr(values, r))
