# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(filter(isEven, range(6))), [0, 2, 4])
    self.assertEqual(list(filter(None, [0, 1, 0, 2, 0])), [1, 2])
    self.assertEqual(list(filter(bool, [0, 1, 0, 2, 0])), [1, 2])
    self.assertEqual(take(4, filter(isEven, count())), [0, 2, 4, 6])
    self.assertRaises(TypeError, filter)
    self.assertRaises(TypeError, filter, lambda x: x)
    self.assertRaises(TypeError, filter, lambda x: x, range(6), 7)
    self.assertRaises(TypeError, filter, isEven, 3)
    self.assertRaises(TypeError, next, filter(range(6), range(6)))
    ans = [0, 2, 4]
    c = filter(isEven, range(6))
    self.assertEqual(list(copy.copy(c)), ans)
    c = filter(isEven, range(6))
    self.assertEqual(list(copy.deepcopy(c)), ans)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        c = filter(isEven, range(6))
        self.assertEqual(list(pickle.loads(pickle.dumps(c, proto))), ans)
        next(c)
        self.assertEqual(list(pickle.loads(pickle.dumps(c, proto))), ans[1:])
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        c = filter(isEven, range(6))
        self.pickletest(proto, c)
