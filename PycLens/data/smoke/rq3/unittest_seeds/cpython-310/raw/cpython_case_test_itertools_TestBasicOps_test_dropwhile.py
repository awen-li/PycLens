# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_dropwhile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = [1, 3, 5, 20, 2, 4, 6, 8]
    self.assertEqual(list(dropwhile(underten, data)), [20, 2, 4, 6, 8])
    self.assertEqual(list(dropwhile(underten, [])), [])
    self.assertRaises(TypeError, dropwhile)
    self.assertRaises(TypeError, dropwhile, operator.pow)
    self.assertRaises(TypeError, dropwhile, operator.pow, [(4, 5)], 'extra')
    self.assertRaises(TypeError, next, dropwhile(10, [(4, 5)]))
    self.assertRaises(ValueError, next, dropwhile(errfunc, [(4, 5)]))
    self.assertEqual(list(copy.copy(dropwhile(underten, data))), [20, 2, 4, 6, 8])
    self.assertEqual(list(copy.deepcopy(dropwhile(underten, data))), [20, 2, 4, 6, 8])
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, dropwhile(underten, data))
