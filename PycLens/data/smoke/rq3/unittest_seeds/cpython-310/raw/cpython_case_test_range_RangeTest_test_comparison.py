# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_ranges = [range(0), range(0, -1), range(1, 1, 3), range(1), range(5, 6), range(5, 6, 2), range(5, 7, 2), range(2), range(0, 4, 2), range(0, 5, 2), range(0, 6, 2)]
    test_tuples = list(map(tuple, test_ranges))
    ranges_eq = [a == b for a in test_ranges for b in test_ranges]
    tuples_eq = [a == b for a in test_tuples for b in test_tuples]
    self.assertEqual(ranges_eq, tuples_eq)
    ranges_ne = [a != b for a in test_ranges for b in test_ranges]
    self.assertEqual(ranges_ne, [not x for x in ranges_eq])
    for a in test_ranges:
        for b in test_ranges:
            if a == b:
                self.assertEqual(hash(a), hash(b))
    self.assertIs(range(0) == (), False)
    self.assertIs(() == range(0), False)
    self.assertIs(range(2) == [0, 1], False)
    self.assertEqual(range(0, 2 ** 100 - 1, 2), range(0, 2 ** 100, 2))
    self.assertEqual(hash(range(0, 2 ** 100 - 1, 2)), hash(range(0, 2 ** 100, 2)))
    self.assertNotEqual(range(0, 2 ** 100, 2), range(0, 2 ** 100 + 1, 2))
    self.assertEqual(range(2 ** 200, 2 ** 201 - 2 ** 99, 2 ** 100), range(2 ** 200, 2 ** 201, 2 ** 100))
    self.assertEqual(hash(range(2 ** 200, 2 ** 201 - 2 ** 99, 2 ** 100)), hash(range(2 ** 200, 2 ** 201, 2 ** 100)))
    self.assertNotEqual(range(2 ** 200, 2 ** 201, 2 ** 100), range(2 ** 200, 2 ** 201 + 1, 2 ** 100))
    with self.assertRaises(TypeError):
        range(0) < range(0)
    with self.assertRaises(TypeError):
        range(0) > range(0)
    with self.assertRaises(TypeError):
        range(0) <= range(0)
    with self.assertRaises(TypeError):
        range(0) >= range(0)
