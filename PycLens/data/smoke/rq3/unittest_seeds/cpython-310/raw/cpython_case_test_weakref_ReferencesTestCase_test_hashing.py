# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_hashing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = Object(42)
    y = Object(42)
    a = weakref.ref(x)
    b = weakref.ref(y)
    self.assertEqual(hash(a), hash(42))
    del x, y
    gc.collect()
    self.assertEqual(hash(a), hash(42))
    self.assertRaises(TypeError, hash, b)
