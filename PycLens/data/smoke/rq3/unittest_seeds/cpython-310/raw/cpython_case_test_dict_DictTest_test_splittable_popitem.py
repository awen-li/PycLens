# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_splittable_popitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = self.make_shared_key_dict(2)
    orig_size = sys.getsizeof(a)
    item = a.popitem()
    self.assertEqual(item, ('z', 3))
    with self.assertRaises(KeyError):
        del a['z']
    self.assertGreater(sys.getsizeof(a), orig_size)
    self.assertEqual(list(a), ['x', 'y'])
    self.assertEqual(list(b), ['x', 'y', 'z'])
