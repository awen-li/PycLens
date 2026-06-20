# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_choices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    choices = self.gen.choices
    data = ['red', 'green', 'blue', 'yellow']
    str_data = 'abcd'
    range_data = range(4)
    set_data = set(range(4))
    for sample in [choices(data, k=5), choices(data, range(4), k=5), choices(k=5, population=data, weights=range(4)), choices(k=5, population=data, cum_weights=range(4))]:
        self.assertEqual(len(sample), 5)
        self.assertEqual(type(sample), list)
        self.assertTrue(set(sample) <= set(data))
    with self.assertRaises(TypeError):
        choices(2)
    self.assertEqual(choices(data, k=0), [])
    self.assertEqual(choices(data, k=-1), [])
    with self.assertRaises(TypeError):
        choices(data, k=2.5)
    self.assertTrue(set(choices(str_data, k=5)) <= set(str_data))
    self.assertTrue(set(choices(range_data, k=5)) <= set(range_data))
    with self.assertRaises(TypeError):
        choices(set_data, k=2)
    self.assertTrue(set(choices(data, None, k=5)) <= set(data))
    self.assertTrue(set(choices(data, weights=None, k=5)) <= set(data))
    with self.assertRaises(ValueError):
        choices(data, [1, 2], k=5)
    with self.assertRaises(TypeError):
        choices(data, 10, k=5)
    with self.assertRaises(TypeError):
        choices(data, [None] * 4, k=5)
    for weights in [[15, 10, 25, 30], [15.1, 10.2, 25.2, 30.3], [Fraction(1, 3), Fraction(2, 6), Fraction(3, 6), Fraction(4, 6)], [True, False, True, False]]:
        self.assertTrue(set(choices(data, weights, k=5)) <= set(data))
    with self.assertRaises(ValueError):
        choices(data, cum_weights=[1, 2], k=5)
    with self.assertRaises(TypeError):
        choices(data, cum_weights=10, k=5)
    with self.assertRaises(TypeError):
        choices(data, cum_weights=[None] * 4, k=5)
    with self.assertRaises(TypeError):
        choices(data, range(4), cum_weights=range(4), k=5)
    for weights in [[15, 10, 25, 30], [15.1, 10.2, 25.2, 30.3], [Fraction(1, 3), Fraction(2, 6), Fraction(3, 6), Fraction(4, 6)]]:
        self.assertTrue(set(choices(data, cum_weights=weights, k=5)) <= set(data))
    self.assertEqual(choices('abcd', [1, 0, 0, 0]), ['a'])
    self.assertEqual(choices('abcd', [0, 1, 0, 0]), ['b'])
    self.assertEqual(choices('abcd', [0, 0, 1, 0]), ['c'])
    self.assertEqual(choices('abcd', [0, 0, 0, 1]), ['d'])
    with self.assertRaises(IndexError):
        choices([], k=1)
    with self.assertRaises(IndexError):
        choices([], weights=[], k=1)
    with self.assertRaises(IndexError):
        choices([], cum_weights=[], k=5)
