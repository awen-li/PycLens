# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_count_with_stride

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(lzip('abc', count(2, 3)), [('a', 2), ('b', 5), ('c', 8)])
    self.assertEqual(lzip('abc', count(start=2, step=3)), [('a', 2), ('b', 5), ('c', 8)])
    self.assertEqual(lzip('abc', count(step=-1)), [('a', 0), ('b', -1), ('c', -2)])
    self.assertRaises(TypeError, count, 'a', 'b')
    self.assertEqual(lzip('abc', count(2, 0)), [('a', 2), ('b', 2), ('c', 2)])
    self.assertEqual(lzip('abc', count(2, 1)), [('a', 2), ('b', 3), ('c', 4)])
    self.assertEqual(lzip('abc', count(2, 3)), [('a', 2), ('b', 5), ('c', 8)])
    self.assertEqual(take(20, count(maxsize - 15, 3)), take(20, range(maxsize - 15, maxsize + 100, 3)))
    self.assertEqual(take(20, count(-maxsize - 15, 3)), take(20, range(-maxsize - 15, -maxsize + 100, 3)))
    self.assertEqual(take(3, count(10, maxsize + 5)), list(range(10, 10 + 3 * (maxsize + 5), maxsize + 5)))
    self.assertEqual(take(3, count(2, 1.25)), [2, 3.25, 4.5])
    self.assertEqual(take(3, count(2, 3.25 - 4j)), [2, 5.25 - 4j, 8.5 - 8j])
    self.assertEqual(take(3, count(Decimal('1.1'), Decimal('.1'))), [Decimal('1.1'), Decimal('1.2'), Decimal('1.3')])
    self.assertEqual(take(3, count(Fraction(2, 3), Fraction(1, 7))), [Fraction(2, 3), Fraction(17, 21), Fraction(20, 21)])
    BIGINT = 1 << 1000
    self.assertEqual(take(3, count(step=BIGINT)), [0, BIGINT, 2 * BIGINT])
    self.assertEqual(repr(take(3, count(10, 2.5))), repr([10, 12.5, 15.0]))
    c = count(3, 5)
    self.assertEqual(repr(c), 'count(3, 5)')
    next(c)
    self.assertEqual(repr(c), 'count(8, 5)')
    c = count(-9, 0)
    self.assertEqual(repr(c), 'count(-9, 0)')
    next(c)
    self.assertEqual(repr(c), 'count(-9, 0)')
    c = count(-9, -3)
    self.assertEqual(repr(c), 'count(-9, -3)')
    next(c)
    self.assertEqual(repr(c), 'count(-12, -3)')
    self.assertEqual(repr(c), 'count(-12, -3)')
    self.assertEqual(repr(count(10.5, 1.25)), 'count(10.5, 1.25)')
    self.assertEqual(repr(count(10.5, 1)), 'count(10.5)')
    self.assertEqual(repr(count(10.5, 1.0)), 'count(10.5, 1.0)')
    self.assertEqual(repr(count(10, 1.0)), 'count(10, 1.0)')
    c = count(10, 1.0)
    self.assertEqual(type(next(c)), int)
    self.assertEqual(type(next(c)), float)
    for i in (-sys.maxsize - 5, -sys.maxsize + 5, -10, -1, 0, 10, sys.maxsize - 5, sys.maxsize + 5):
        for j in (-sys.maxsize - 5, -sys.maxsize + 5, -10, -1, 0, 1, 10, sys.maxsize - 5, sys.maxsize + 5):
            r1 = repr(count(i, j))
            if j == 1:
                r2 = 'count(%r)' % i
            else:
                r2 = 'count(%r, %r)' % (i, j)
            self.assertEqual(r1, r2)
            for proto in range(pickle.HIGHEST_PROTOCOL + 1):
                self.pickletest(proto, count(i, j))
