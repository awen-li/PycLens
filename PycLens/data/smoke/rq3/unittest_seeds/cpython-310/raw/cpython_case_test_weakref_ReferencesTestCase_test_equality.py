# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = Object(1)
    y = Object(1)
    z = Object(2)
    a = weakref.ref(x)
    b = weakref.ref(y)
    c = weakref.ref(z)
    d = weakref.ref(x)
    self.assertTrue(a == b)
    self.assertFalse(a != b)
    self.assertFalse(a == c)
    self.assertTrue(a != c)
    self.assertTrue(a == d)
    self.assertFalse(a != d)
    self.assertFalse(a == x)
    self.assertTrue(a != x)
    self.assertTrue(a == ALWAYS_EQ)
    self.assertFalse(a != ALWAYS_EQ)
    del x, y, z
    gc.collect()
    for r in (a, b, c):
        self.assertIs(r(), None)
    self.assertFalse(a == b)
    self.assertTrue(a != b)
    self.assertFalse(a == c)
    self.assertTrue(a != c)
    self.assertEqual(a == d, a is d)
    self.assertEqual(a != d, a is not d)
