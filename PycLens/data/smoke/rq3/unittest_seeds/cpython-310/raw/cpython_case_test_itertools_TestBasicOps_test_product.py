# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_product

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (args, result) in [([], [()]), (['ab'], [('a',), ('b',)]), ([range(2), range(3)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]), ([range(0), range(2), range(3)], []), ([range(2), range(0), range(3)], []), ([range(2), range(3), range(0)], [])]:
        self.assertEqual(list(product(*args)), result)
        for r in range(4):
            self.assertEqual(list(product(*args * r)), list(product(*args, **dict(repeat=r))))
    self.assertEqual(len(list(product(*[range(7)] * 6))), 7 ** 6)
    self.assertRaises(TypeError, product, range(6), None)

    def product1(*args, **kwds):
        pools = list(map(tuple, args)) * kwds.get('repeat', 1)
        n = len(pools)
        if n == 0:
            yield ()
            return
        if any((len(pool) == 0 for pool in pools)):
            return
        indices = [0] * n
        yield tuple((pool[i] for (pool, i) in zip(pools, indices)))
        while 1:
            for i in reversed(range(n)):
                if indices[i] == len(pools[i]) - 1:
                    continue
                indices[i] += 1
                for j in range(i + 1, n):
                    indices[j] = 0
                yield tuple((pool[i] for (pool, i) in zip(pools, indices)))
                break
            else:
                return

    def product2(*args, **kwds):
        """Pure python version used in docs"""
        pools = list(map(tuple, args)) * kwds.get('repeat', 1)
        result = [[]]
        for pool in pools:
            result = [x + [y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)
    argtypes = ['', 'abc', '', range(0), range(4), dict(a=1, b=2, c=3), set('abcdefg'), range(11), tuple(range(13))]
    for i in range(100):
        args = [random.choice(argtypes) for j in range(random.randrange(5))]
        expected_len = prod(map(len, args))
        self.assertEqual(len(list(product(*args))), expected_len)
        self.assertEqual(list(product(*args)), list(product1(*args)))
        self.assertEqual(list(product(*args)), list(product2(*args)))
        args = map(iter, args)
        self.assertEqual(len(list(product(*args))), expected_len)
