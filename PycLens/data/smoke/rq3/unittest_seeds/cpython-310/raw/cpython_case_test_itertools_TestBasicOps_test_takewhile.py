# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_takewhile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [1, 3, 5, 20, 2, 4, 6, 8]
    self.assertEqual(list(takewhile(underten, data)), [1, 3, 5])
    self.assertEqual(list(takewhile(underten, [])), [])
    self.assertRaises(TypeError, takewhile)
    self.assertRaises(TypeError, takewhile, operator.pow)
    self.assertRaises(TypeError, takewhile, operator.pow, [(4, 5)], 'extra')
    self.assertRaises(TypeError, next, takewhile(10, [(4, 5)]))
    self.assertRaises(ValueError, next, takewhile(errfunc, [(4, 5)]))
    t = takewhile(bool, [1, 1, 1, 0, 0, 0])
    self.assertEqual(list(t), [1, 1, 1])
    self.assertRaises(StopIteration, next, t)
    self.assertEqual(list(copy.copy(takewhile(underten, data))), [1, 3, 5])
    self.assertEqual(list(copy.deepcopy(takewhile(underten, data))), [1, 3, 5])
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, takewhile(underten, data))
