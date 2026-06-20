# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_product_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (args, result) in [([], [()]), (['ab'], [('a',), ('b',)]), ([range(2), range(3)], [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]), ([range(0), range(2), range(3)], []), ([range(2), range(0), range(3)], []), ([range(2), range(3), range(0)], [])]:
        self.assertEqual(list(copy.copy(product(*args))), result)
        self.assertEqual(list(copy.deepcopy(product(*args))), result)
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            self.pickletest(proto, product(*args))
