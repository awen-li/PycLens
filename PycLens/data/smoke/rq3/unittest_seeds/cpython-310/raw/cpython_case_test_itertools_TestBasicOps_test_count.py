# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(lzip('abc', count()), [('a', 0), ('b', 1), ('c', 2)])
    self.assertEqual(lzip('abc', count(3)), [('a', 3), ('b', 4), ('c', 5)])
    self.assertEqual(take(2, lzip('abc', count(3))), [('a', 3), ('b', 4)])
    self.assertEqual(take(2, zip('abc', count(-1))), [('a', -1), ('b', 0)])
    self.assertEqual(take(2, zip('abc', count(-3))), [('a', -3), ('b', -2)])
    self.assertRaises(TypeError, count, 2, 3, 4)
    self.assertRaises(TypeError, count, 'a')
    self.assertEqual(take(10, count(maxsize - 5)), list(range(maxsize - 5, maxsize + 5)))
    self.assertEqual(take(10, count(-maxsize - 5)), list(range(-maxsize - 5, -maxsize + 5)))
    self.assertEqual(take(3, count(3.25)), [3.25, 4.25, 5.25])
    self.assertEqual(take(3, count(3.25 - 4j)), [3.25 - 4j, 4.25 - 4j, 5.25 - 4j])
    self.assertEqual(take(3, count(Decimal('1.1'))), [Decimal('1.1'), Decimal('2.1'), Decimal('3.1')])
    self.assertEqual(take(3, count(Fraction(2, 3))), [Fraction(2, 3), Fraction(5, 3), Fraction(8, 3)])
    BIGINT = 1 << 1000
    self.assertEqual(take(3, count(BIGINT)), [BIGINT, BIGINT + 1, BIGINT + 2])
    c = count(3)
    self.assertEqual(repr(c), 'count(3)')
    next(c)
    self.assertEqual(repr(c), 'count(4)')
    c = count(-9)
    self.assertEqual(repr(c), 'count(-9)')
    next(c)
    self.assertEqual(next(c), -8)
    self.assertEqual(repr(count(10.25)), 'count(10.25)')
    self.assertEqual(repr(count(10.0)), 'count(10.0)')
    self.assertEqual(type(next(count(10.0))), float)
    for i in (-sys.maxsize - 5, -sys.maxsize + 5, -10, -1, 0, 10, sys.maxsize - 5, sys.maxsize + 5):
        r1 = repr(count(i))
        r2 = 'count(%r)'.__mod__(i)
        self.assertEqual(r1, r2)
    for value in (-3, 3, maxsize - 5, maxsize + 5):
        c = count(value)
        self.assertEqual(next(copy.copy(c)), value)
        self.assertEqual(next(copy.deepcopy(c)), value)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            self.pickletest(proto, count(value))
    count(1, maxsize + 5)
    sys.exc_info()
