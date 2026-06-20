# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCmpToKey_test_cmp_to_key_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cmp1(x, y):
        return (x > y) - (x < y)
    key = self.cmp_to_key(mycmp=cmp1)
    self.assertEqual(key(obj=3), key(obj=3))
    self.assertGreater(key(obj=3), key(obj=1))
    with self.assertRaises((TypeError, AttributeError)):
        key(3) > 1
    with self.assertRaises((TypeError, AttributeError)):
        1 < key(3)
    with self.assertRaises(TypeError):
        key = self.cmp_to_key()
    with self.assertRaises(TypeError):
        key = self.cmp_to_key(cmp1, None)
    key = self.cmp_to_key(cmp1)
    with self.assertRaises(TypeError):
        key()
    with self.assertRaises(TypeError):
        key(None, None)
