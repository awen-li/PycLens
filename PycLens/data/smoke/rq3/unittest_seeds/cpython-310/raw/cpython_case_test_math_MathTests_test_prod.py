# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_prod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prod = math.prod
    self.assertEqual(prod([]), 1)
    self.assertEqual(prod([], start=5), 5)
    self.assertEqual(prod(list(range(2, 8))), 5040)
    self.assertEqual(prod(iter(list(range(2, 8)))), 5040)
    self.assertEqual(prod(range(1, 10), start=10), 3628800)
    self.assertEqual(prod([1, 2, 3, 4, 5]), 120)
    self.assertEqual(prod([1.0, 2.0, 3.0, 4.0, 5.0]), 120.0)
    self.assertEqual(prod([1, 2, 3, 4.0, 5.0]), 120.0)
    self.assertEqual(prod([1.0, 2.0, 3.0, 4, 5]), 120.0)
    self.assertEqual(prod([1, 1, 2 ** 32, 1, 1]), 2 ** 32)
    self.assertEqual(prod([1.0, 1.0, 2 ** 32, 1, 1]), float(2 ** 32))
    self.assertRaises(TypeError, prod)
    self.assertRaises(TypeError, prod, 42)
    self.assertRaises(TypeError, prod, ['a', 'b', 'c'])
    self.assertRaises(TypeError, prod, ['a', 'b', 'c'], start='')
    self.assertRaises(TypeError, prod, [b'a', b'c'], start=b'')
    values = [bytearray(b'a'), bytearray(b'b')]
    self.assertRaises(TypeError, prod, values, start=bytearray(b''))
    self.assertRaises(TypeError, prod, [[1], [2], [3]])
    self.assertRaises(TypeError, prod, [{2: 3}])
    self.assertRaises(TypeError, prod, [{2: 3}] * 2, start={2: 3})
    self.assertRaises(TypeError, prod, [[1], [2], [3]], start=[])
    self.assertEqual(prod([2, 3], start='ab'), 'abababababab')
    self.assertEqual(prod([2, 3], start=[1, 2]), [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2])
    self.assertEqual(prod([], start={2: 3}), {2: 3})
    with self.assertRaises(TypeError):
        prod([10, 20], 1)
    self.assertEqual(prod([0, 1, 2, 3]), 0)
    self.assertEqual(prod([1, 0, 2, 3]), 0)
    self.assertEqual(prod([1, 2, 3, 0]), 0)

    def _naive_prod(iterable, start=1):
        for elem in iterable:
            start *= elem
        return start
    iterable = range(1, 10000)
    self.assertEqual(prod(iterable), _naive_prod(iterable))
    iterable = range(-10000, -1)
    self.assertEqual(prod(iterable), _naive_prod(iterable))
    iterable = range(-1000, 1000)
    self.assertEqual(prod(iterable), 0)
    iterable = [float(x) for x in range(1, 1000)]
    self.assertEqual(prod(iterable), _naive_prod(iterable))
    iterable = [float(x) for x in range(-1000, -1)]
    self.assertEqual(prod(iterable), _naive_prod(iterable))
    iterable = [float(x) for x in range(-1000, 1000)]
    self.assertIsNaN(prod(iterable))
    self.assertIsNaN(prod([1, 2, 3, float('nan'), 2, 3]))
    self.assertIsNaN(prod([1, 0, float('nan'), 2, 3]))
    self.assertIsNaN(prod([1, float('nan'), 0, 3]))
    self.assertIsNaN(prod([1, float('inf'), float('nan'), 3]))
    self.assertIsNaN(prod([1, float('-inf'), float('nan'), 3]))
    self.assertIsNaN(prod([1, float('nan'), float('inf'), 3]))
    self.assertIsNaN(prod([1, float('nan'), float('-inf'), 3]))
    self.assertEqual(prod([1, 2, 3, float('inf'), -3, 4]), float('-inf'))
    self.assertEqual(prod([1, 2, 3, float('-inf'), -3, 4]), float('inf'))
    self.assertIsNaN(prod([1, 2, 0, float('inf'), -3, 4]))
    self.assertIsNaN(prod([1, 2, 0, float('-inf'), -3, 4]))
    self.assertIsNaN(prod([1, 2, 3, float('inf'), -3, 0, 3]))
    self.assertIsNaN(prod([1, 2, 3, float('-inf'), -3, 0, 2]))
    self.assertEqual(type(prod([1, 2, 3, 4, 5, 6])), int)
    self.assertEqual(type(prod([1, 2.0, 3, 4, 5, 6])), float)
    self.assertEqual(type(prod(range(1, 10000))), int)
    self.assertEqual(type(prod(range(1, 10000), start=1.0)), float)
    self.assertEqual(type(prod([1, decimal.Decimal(2.0), 3, 4, 5, 6])), decimal.Decimal)
