# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: WeakMethodTestCase_test_hashing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = Object(1)
    y = Object(1)
    a = weakref.WeakMethod(x.some_method)
    b = weakref.WeakMethod(y.some_method)
    c = weakref.WeakMethod(y.other_method)
    self.assertEqual(hash(a), hash(b))
    ha = hash(a)
    del x, y
    gc.collect()
    self.assertEqual(hash(a), ha)
    self.assertEqual(hash(b), ha)
    self.assertRaises(TypeError, hash, c)
