# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_splittable_setdefault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = self.make_shared_key_dict(2)
    a['a'] = 1
    size_a = sys.getsizeof(a)
    a['b'] = 2
    b.setdefault('b', 2)
    size_b = sys.getsizeof(b)
    b['a'] = 1
    self.assertGreater(size_b, size_a)
    self.assertEqual(list(a), ['x', 'y', 'z', 'a', 'b'])
    self.assertEqual(list(b), ['x', 'y', 'z', 'b', 'a'])
