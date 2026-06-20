# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(map(operator.pow, range(3), range(1, 7))), [0 ** 1, 1 ** 2, 2 ** 3])
    self.assertEqual(list(map(tupleize, 'abc', range(5))), [('a', 0), ('b', 1), ('c', 2)])
    self.assertEqual(list(map(tupleize, 'abc', count())), [('a', 0), ('b', 1), ('c', 2)])
    self.assertEqual(take(2, map(tupleize, 'abc', count())), [('a', 0), ('b', 1)])
    self.assertEqual(list(map(operator.pow, [])), [])
    self.assertRaises(TypeError, map)
    self.assertRaises(TypeError, list, map(None, range(3), range(3)))
    self.assertRaises(TypeError, map, operator.neg)
    self.assertRaises(TypeError, next, map(10, range(5)))
    self.assertRaises(ValueError, next, map(errfunc, [4], [5]))
    self.assertRaises(TypeError, next, map(onearg, [4], [5]))
    ans = [('a', 0), ('b', 1), ('c', 2)]
    c = map(tupleize, 'abc', count())
    self.assertEqual(list(copy.copy(c)), ans)
    c = map(tupleize, 'abc', count())
    self.assertEqual(list(copy.deepcopy(c)), ans)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        c = map(tupleize, 'abc', count())
        self.pickletest(proto, c)
