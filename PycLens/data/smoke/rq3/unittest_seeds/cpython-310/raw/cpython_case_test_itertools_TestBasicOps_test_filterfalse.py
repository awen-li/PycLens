# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_filterfalse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(filterfalse(isEven, range(6))), [1, 3, 5])
    self.assertEqual(list(filterfalse(None, [0, 1, 0, 2, 0])), [0, 0, 0])
    self.assertEqual(list(filterfalse(bool, [0, 1, 0, 2, 0])), [0, 0, 0])
    self.assertEqual(take(4, filterfalse(isEven, count())), [1, 3, 5, 7])
    self.assertRaises(TypeError, filterfalse)
    self.assertRaises(TypeError, filterfalse, lambda x: x)
    self.assertRaises(TypeError, filterfalse, lambda x: x, range(6), 7)
    self.assertRaises(TypeError, filterfalse, isEven, 3)
    self.assertRaises(TypeError, next, filterfalse(range(6), range(6)))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, filterfalse(isEven, range(6)))
