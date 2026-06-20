# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(repeat(object='a', times=3)), ['a', 'a', 'a'])
    self.assertEqual(lzip(range(3), repeat('a')), [(0, 'a'), (1, 'a'), (2, 'a')])
    self.assertEqual(list(repeat('a', 3)), ['a', 'a', 'a'])
    self.assertEqual(take(3, repeat('a')), ['a', 'a', 'a'])
    self.assertEqual(list(repeat('a', 0)), [])
    self.assertEqual(list(repeat('a', -3)), [])
    self.assertRaises(TypeError, repeat)
    self.assertRaises(TypeError, repeat, None, 3, 4)
    self.assertRaises(TypeError, repeat, None, 'a')
    r = repeat(1 + 0j)
    self.assertEqual(repr(r), 'repeat((1+0j))')
    r = repeat(1 + 0j, 5)
    self.assertEqual(repr(r), 'repeat((1+0j), 5)')
    list(r)
    self.assertEqual(repr(r), 'repeat((1+0j), 0)')
    c = repeat(object='a', times=10)
    self.assertEqual(next(c), 'a')
    self.assertEqual(take(2, copy.copy(c)), list('a' * 2))
    self.assertEqual(take(2, copy.deepcopy(c)), list('a' * 2))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, repeat(object='a', times=10))
