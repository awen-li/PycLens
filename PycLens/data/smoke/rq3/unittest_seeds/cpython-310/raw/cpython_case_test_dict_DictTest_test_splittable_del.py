# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_splittable_del

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = self.make_shared_key_dict(2)
    orig_size = sys.getsizeof(a)
    del a['y']
    with self.assertRaises(KeyError):
        del a['y']
    self.assertGreater(sys.getsizeof(a), orig_size)
    self.assertEqual(list(a), ['x', 'z'])
    self.assertEqual(list(b), ['x', 'y', 'z'])
    a['y'] = 42
    self.assertEqual(list(a), ['x', 'z', 'y'])
    self.assertEqual(list(b), ['x', 'y', 'z'])
