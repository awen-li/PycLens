# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_starmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(starmap(operator.pow, zip(range(3), range(1, 7)))), [0 ** 1, 1 ** 2, 2 ** 3])
    self.assertEqual(take(3, starmap(operator.pow, zip(count(), count(1)))), [0 ** 1, 1 ** 2, 2 ** 3])
    self.assertEqual(list(starmap(operator.pow, [])), [])
    self.assertEqual(list(starmap(operator.pow, [iter([4, 5])])), [4 ** 5])
    self.assertRaises(TypeError, list, starmap(operator.pow, [None]))
    self.assertRaises(TypeError, starmap)
    self.assertRaises(TypeError, starmap, operator.pow, [(4, 5)], 'extra')
    self.assertRaises(TypeError, next, starmap(10, [(4, 5)]))
    self.assertRaises(ValueError, next, starmap(errfunc, [(4, 5)]))
    self.assertRaises(TypeError, next, starmap(onearg, [(4, 5)]))
    ans = [0 ** 1, 1 ** 2, 2 ** 3]
    c = starmap(operator.pow, zip(range(3), range(1, 7)))
    self.assertEqual(list(copy.copy(c)), ans)
    c = starmap(operator.pow, zip(range(3), range(1, 7)))
    self.assertEqual(list(copy.deepcopy(c)), ans)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        c = starmap(operator.pow, zip(range(3), range(1, 7)))
        self.pickletest(proto, c)
