# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_accumulate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(accumulate(range(10))), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])
    self.assertEqual(list(accumulate(iterable=range(10))), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])
    for typ in (int, complex, Decimal, Fraction):
        self.assertEqual(list(accumulate(map(typ, range(10)))), list(map(typ, [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])))
    self.assertEqual(list(accumulate('abc')), ['a', 'ab', 'abc'])
    self.assertEqual(list(accumulate([])), [])
    self.assertEqual(list(accumulate([7])), [7])
    self.assertRaises(TypeError, accumulate, range(10), 5, 6)
    self.assertRaises(TypeError, accumulate)
    self.assertRaises(TypeError, accumulate, x=range(10))
    self.assertRaises(TypeError, list, accumulate([1, []]))
    s = [2, 8, 9, 5, 7, 0, 3, 4, 1, 6]
    self.assertEqual(list(accumulate(s, min)), [2, 2, 2, 2, 2, 0, 0, 0, 0, 0])
    self.assertEqual(list(accumulate(s, max)), [2, 8, 9, 9, 9, 9, 9, 9, 9, 9])
    self.assertEqual(list(accumulate(s, operator.mul)), [2, 16, 144, 720, 5040, 0, 0, 0, 0, 0])
    with self.assertRaises(TypeError):
        list(accumulate(s, chr))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, accumulate(range(10)))
        self.pickletest(proto, accumulate(range(10), initial=7))
    self.assertEqual(list(accumulate([10, 5, 1], initial=None)), [10, 15, 16])
    self.assertEqual(list(accumulate([10, 5, 1], initial=100)), [100, 110, 115, 116])
    self.assertEqual(list(accumulate([], initial=100)), [100])
    with self.assertRaises(TypeError):
        list(accumulate([10, 20], 100))
