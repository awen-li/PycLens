# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_islice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for args in [(10, 20, 3), (10, 3, 20), (10, 20), (10, 10), (10, 3), (20,)]:
        self.assertEqual(list(islice(range(100), *args)), list(range(*args)))
    for (args, tgtargs) in [((10, 110, 3), (10, 100, 3)), ((10, 110), (10, 100)), ((110,), (100,))]:
        self.assertEqual(list(islice(range(100), *args)), list(range(*tgtargs)))
    self.assertEqual(list(islice(range(10), None)), list(range(10)))
    self.assertEqual(list(islice(range(10), None, None)), list(range(10)))
    self.assertEqual(list(islice(range(10), None, None, None)), list(range(10)))
    self.assertEqual(list(islice(range(10), 2, None)), list(range(2, 10)))
    self.assertEqual(list(islice(range(10), 1, None, 2)), list(range(1, 10, 2)))
    it = iter(range(10))
    self.assertEqual(list(islice(it, 3)), list(range(3)))
    self.assertEqual(list(it), list(range(3, 10)))
    it = iter(range(10))
    self.assertEqual(list(islice(it, 3, 3)), [])
    self.assertEqual(list(it), list(range(3, 10)))
    ra = range(10)
    self.assertRaises(TypeError, islice, ra)
    self.assertRaises(TypeError, islice, ra, 1, 2, 3, 4)
    self.assertRaises(ValueError, islice, ra, -5, 10, 1)
    self.assertRaises(ValueError, islice, ra, 1, -5, -1)
    self.assertRaises(ValueError, islice, ra, 1, 10, -1)
    self.assertRaises(ValueError, islice, ra, 1, 10, 0)
    self.assertRaises(ValueError, islice, ra, 'a')
    self.assertRaises(ValueError, islice, ra, 'a', 1)
    self.assertRaises(ValueError, islice, ra, 1, 'a')
    self.assertRaises(ValueError, islice, ra, 'a', 1, 1)
    self.assertRaises(ValueError, islice, ra, 1, 'a', 1)
    self.assertEqual(len(list(islice(count(), 1, 10, maxsize))), 1)
    c = count()
    self.assertEqual(list(islice(c, 1, 3, 50)), [1])
    self.assertEqual(next(c), 3)
    for args in [(10, 20, 3), (10, 3, 20), (10, 20), (10, 3), (20,)]:
        self.assertEqual(list(copy.copy(islice(range(100), *args))), list(range(*args)))
        self.assertEqual(list(copy.deepcopy(islice(range(100), *args))), list(range(*args)))
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            self.pickletest(proto, islice(range(100), *args))
    it = (x for x in (1, 2))
    wr = weakref.ref(it)
    it = islice(it, 1)
    self.assertIsNotNone(wr())
    list(it)
    support.gc_collect()
    self.assertIsNone(wr())

    class IntLike(object):

        def __init__(self, val):
            self.val = val

        def __index__(self):
            return self.val
    self.assertEqual(list(islice(range(100), IntLike(10))), list(range(10)))
    self.assertEqual(list(islice(range(100), IntLike(10), IntLike(50))), list(range(10, 50)))
    self.assertEqual(list(islice(range(100), IntLike(10), IntLike(50), IntLike(5))), list(range(10, 50, 5)))
