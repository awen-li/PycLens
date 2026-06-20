# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_slice.py
# case: SliceTest_test_indices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(slice(None).indices(10), (0, 10, 1))
    self.assertEqual(slice(None, None, 2).indices(10), (0, 10, 2))
    self.assertEqual(slice(1, None, 2).indices(10), (1, 10, 2))
    self.assertEqual(slice(None, None, -1).indices(10), (9, -1, -1))
    self.assertEqual(slice(None, None, -2).indices(10), (9, -1, -2))
    self.assertEqual(slice(3, None, -2).indices(10), (3, -1, -2))
    self.assertEqual(slice(None, -9).indices(10), (0, 1, 1))
    self.assertEqual(slice(None, -10).indices(10), (0, 0, 1))
    self.assertEqual(slice(None, -11).indices(10), (0, 0, 1))
    self.assertEqual(slice(None, -10, -1).indices(10), (9, 0, -1))
    self.assertEqual(slice(None, -11, -1).indices(10), (9, -1, -1))
    self.assertEqual(slice(None, -12, -1).indices(10), (9, -1, -1))
    self.assertEqual(slice(None, 9).indices(10), (0, 9, 1))
    self.assertEqual(slice(None, 10).indices(10), (0, 10, 1))
    self.assertEqual(slice(None, 11).indices(10), (0, 10, 1))
    self.assertEqual(slice(None, 8, -1).indices(10), (9, 8, -1))
    self.assertEqual(slice(None, 9, -1).indices(10), (9, 9, -1))
    self.assertEqual(slice(None, 10, -1).indices(10), (9, 9, -1))
    self.assertEqual(slice(-100, 100).indices(10), slice(None).indices(10))
    self.assertEqual(slice(100, -100, -1).indices(10), slice(None, None, -1).indices(10))
    self.assertEqual(slice(-100, 100, 2).indices(10), (0, 10, 2))
    self.assertEqual(list(range(10))[::sys.maxsize - 1], [0])
    vals = [None, -2 ** 100, -2 ** 30, -53, -7, -1, 0, 1, 7, 53, 2 ** 30, 2 ** 100]
    lengths = [0, 1, 7, 53, 2 ** 30, 2 ** 100]
    for slice_args in itertools.product(vals, repeat=3):
        s = slice(*slice_args)
        for length in lengths:
            self.check_indices(s, length)
    self.check_indices(slice(0, 10, 1), -3)
    with self.assertRaises(ValueError):
        slice(None).indices(-1)
    with self.assertRaises(ValueError):
        slice(0, 10, 0).indices(5)
    with self.assertRaises(TypeError):
        slice(0.0, 10, 1).indices(5)
    with self.assertRaises(TypeError):
        slice(0, 10.0, 1).indices(5)
    with self.assertRaises(TypeError):
        slice(0, 10, 1.0).indices(5)
    with self.assertRaises(TypeError):
        slice(0, 10, 1).indices(5.0)
    self.assertEqual(slice(0, 10, 1).indices(5), (0, 5, 1))
    self.assertEqual(slice(MyIndexable(0), 10, 1).indices(5), (0, 5, 1))
    self.assertEqual(slice(0, MyIndexable(10), 1).indices(5), (0, 5, 1))
    self.assertEqual(slice(0, 10, MyIndexable(1)).indices(5), (0, 5, 1))
    self.assertEqual(slice(0, 10, 1).indices(MyIndexable(5)), (0, 5, 1))
